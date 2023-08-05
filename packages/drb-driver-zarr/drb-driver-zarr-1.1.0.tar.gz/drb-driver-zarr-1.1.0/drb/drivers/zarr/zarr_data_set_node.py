import enum
from abc import ABC
from typing import Any, List, Optional, Union, Dict, Tuple

import drb.topics.resolver as resolver
import zarr

from drb.core import DrbNode
from drb.nodes.abstract_node import AbstractNode
from drb.exceptions.core import DrbNotImplementationException, DrbException
from drb.core.path import ParsedPath


class DrbZarrAttributeNames(enum.Enum):
    """
    A Boolean that tell if the zarr is read only.
    """

    READ_ONLY = "read_only"


class DrbZarrDataSetNode(AbstractNode, ABC):
    """
    This node will be inherited by DrbZarrGroupNode and DrbZarrArrayNode.

    Parameters:
        parent (DrbNode): The parent of the node.
        name (str): The name of the node.
        data_set (Union[zarr.hierarchy.Group, zarr.core.Array]):
                 the dataset of the node
                 corresponding to a zarr group
                 otherwise a zarr array.
    """

    def __init__(
        self,
        parent: DrbNode,
        name: str,
        data_set: Union[zarr.hierarchy.Group, zarr.core.Array],
    ):
        super().__init__()

        self._data_set = data_set
        self._parent: DrbNode = parent
        self._name = name
        self._path = None
        self._attributes: Dict[Tuple[str, str], Any] = None

    @property
    def namespace_uri(self) -> Optional[str]:
        """
        Not use in this implementation

        Return:
            None
        """
        return None

    def close(self) -> None:
        """
        Not use in this implementation.
        Do nothing.
        """
        pass

    @property
    def path(self) -> ParsedPath:
        """
        Returns the path of the node.

        Returns:
            ParsedPath: The path of the node.
        """
        if self._path is None:
            self._path = self.parent.path / self.name
        return self._path

    @property
    def parent(self) -> Optional[DrbNode]:
        """
        Return the parent of this node if he has one otherwise None.

        Returns:
            DrbNode: The parent of this node or None.
        """
        return self._parent

    @property
    def name(self) -> str:
        """
        Return the name of the node.
        This name doesn't contain the path of the node.

        Returns:
            str: the node name
        """
        return self._name

    @property
    def attributes(self) -> Dict[Tuple[str, str], Any]:
        if self._attributes is None:
            self._attributes = {}
            for key in self._data_set.attrs.keys():
                self._attributes[key, None] = self._data_set.attrs[key]
            self._attributes[
                DrbZarrAttributeNames.READ_ONLY.value, None
            ] = self._data_set.read_only
        return self._attributes

    def get_attribute(self, name: str, namespace_uri: str = None) -> Any:
        key = (name, namespace_uri)
        if key in self.attributes.keys():
            return self.attributes[key]
        raise DrbException(
            f"Attribute not found name: {name}, " f"namespace: {namespace_uri}"
        )

    @property
    def value(self) -> Optional[Any]:
        """
        Not use in this implementation.

        Returns:
            None
        """
        return None

    def has_impl(self, impl: type) -> bool:
        return impl is self._data_set.__class__

    def get_impl(self, impl: type, **kwargs) -> Any:
        if self.has_impl(impl):
            return self._data_set
        raise DrbNotImplementationException(
            f"no {impl} " f"implementation found"
        )

    @staticmethod
    def create_node_from_data_set(parent, data_set):
        name = data_set.name
        if name and name[0] == "/":
            name = name[1:]
        if not name:
            name = "."
        if isinstance(data_set, zarr.hierarchy.Group):
            node = DrbZarrGroupNode(parent, name, data_set)
        else:
            node = DrbZarrArrayNode(parent, name, data_set)
        return node


class DrbZarrGroupNode(DrbZarrDataSetNode):
    """
    This node is used to organize the data in a zarr architecture,
    he contains a group of zarr array in his children
    or another DrbZarrGroupNode.

    Parameters:
        parent (DrbNode): The parent of the node.
        name (str): The name of the node.
        data_set (Union[zarr.hierarchy.Group, zarr.core.Array]):
                 the dataset of the node
                 corresponding to a zarr group
                 otherwise a zarr array.
    """

    def __init__(
        self,
        parent: DrbNode,
        name: str,
        data_set: Union[zarr.hierarchy.Group, zarr.core.Array],
    ):
        super().__init__(parent, name, data_set)
        self._children: List[DrbNode] = None

    @property
    @resolver.resolve_children
    def children(self) -> List[DrbNode]:
        if self._children is None:
            self._children = []
            self._data_set.visitvalues(self.add_data_set_children)
        return self._children

    def add_data_set_children(self, data_set):
        """
        Add the dataset given in argument to the List of children.

        Parameters:
            data_set : a data set to be added in the children List.
        """
        child = DrbZarrDataSetNode.create_node_from_data_set(self, data_set)
        self._children.append(child)

    def _get_named_child(
        self,
        name: str,
        namespace_uri: str = None,
        occurrence: Union[int, slice] = 0,
    ) -> Union[DrbNode, List[DrbNode]]:
        if self._children is None:
            if namespace_uri is None:
                data_set = self._data_set[name]
                return [self.create_node_from_data_set(self, data_set)][
                    occurrence
                ]

            raise DrbException(
                f"No child found having name: {name} and"
                f" namespace: {namespace_uri}"
            )
        else:
            return super()._get_named_child(name, namespace_uri, occurrence)


class DrbZarrArrayNode(DrbZarrDataSetNode):
    """
    This node is used to represent one or a set of values
    contained in a Zarr array.

    Parameters:
        parent (DrbNode): The parent of the node.
        name (str): The name of the node.
        data_set (Union[zarr.hierarchy.Group, zarr.core.Array]):
                 the dataset of the node
                 corresponding to a zarr group
                 otherwise a zarr array.
    """

    def __init__(
        self,
        parent: DrbNode,
        name: str,
        data_set: Union[zarr.hierarchy.Group, zarr.core.Array],
    ):
        super().__init__(parent, name, data_set)

    @property
    def children(self) -> List[DrbNode]:
        return []

    def has_child(self, name: str = None, namespace: str = None) -> bool:
        return False
