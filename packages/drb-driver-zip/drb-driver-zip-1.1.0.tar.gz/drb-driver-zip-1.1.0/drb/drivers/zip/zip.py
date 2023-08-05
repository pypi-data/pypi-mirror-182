import enum
import io
import zipfile
from typing import Any, List, Dict, Optional, Tuple
from zipfile import ZipExtFile, ZipInfo

from drb.core import DrbNode, ParsedPath, DrbFactory
from drb.exceptions.core import DrbException, DrbNotImplementationException
from drb.nodes.abstract_node import AbstractNode
from drb.topics.resolver import resolve_children

import drb
from drb.exceptions.zip import DrbZipNodeException


class DrbZipAttributeNames(enum.Enum):
    SIZE = 'size'
    """
    The size of the file in bytes.
    """
    DIRECTORY = 'directory'
    """
    A boolean that tell if the file is a directory.
    """
    RATIO = 'ratio'
    """
    the ratio between the size of the compressed file and the original file.
    """
    PACKED = 'packed'
    """
    The size of the compressed file in bytes.
    """


class DrbZipNode(AbstractNode):
    """
    This node is used to browse the content of a zip container.

    Parameters:
        parent (DrbNode): The zip container.
        zip_info (ZipInfo): Class with attributes describing
                            each file in the ZIP archive.

    """

    def __init__(self, parent: DrbNode, zip_info: ZipInfo):
        super().__init__()
        self._zip_info = zip_info
        self._attributes: Dict[Tuple[str, str], Any] = None
        self._name = None
        self._parent: DrbNode = parent
        self._children: List[DrbNode] = None
        self._path = None

    @property
    def parent(self) -> Optional[DrbNode]:
        return self._parent

    @property
    def path(self) -> ParsedPath:
        if self._path is None:
            self._path = self.parent.path / self.name
        return self._path

    @property
    def name(self) -> str:
        if self._name is None:
            if self._zip_info.filename.endswith('/'):
                self._name = self._zip_info.filename[:-1]
            else:
                self._name = self._zip_info.filename
            if '/' in self._name:
                self._name = self._name[self._name.rindex('/') + 1:]
        return self._name

    @property
    def namespace_uri(self) -> Optional[str]:
        return None

    @property
    def value(self) -> Optional[Any]:
        return None

    @property
    def attributes(self) -> Dict[Tuple[str, str], Any]:
        if self._attributes is None:
            self._attributes = {}
            name_attribute = DrbZipAttributeNames.DIRECTORY.value
            self._attributes[name_attribute, None] = self._zip_info.is_dir()

            name_attribute = DrbZipAttributeNames.SIZE.value
            self._attributes[name_attribute, None] = self._zip_info.file_size

            name_attribute = DrbZipAttributeNames.RATIO.value
            if self._zip_info.compress_size > 0:
                self._attributes[name_attribute, None] = \
                    self._zip_info.file_size / self._zip_info.compress_size
            else:
                self._attributes[name_attribute, None] = 0
            name_attribute = DrbZipAttributeNames.PACKED.value
            self._attributes[name_attribute, None] = \
                self._zip_info.compress_size
        return self._attributes

    def get_attribute(self, name: str, namespace_uri: str = None) -> Any:
        key = (name, namespace_uri)
        if key in self.attributes.keys():
            return self.attributes[key]
        raise DrbException(f'Attribute not found name: {name}, '
                           f'namespace: {namespace_uri}')

    def get_file_list(self):
        return self.parent.get_file_list()

    def _is_a_child(self, filename):
        if not filename.startswith(self._zip_info.filename):
            return False

        filename = filename[len(self._zip_info.filename):]

        if not filename:
            return False

        if not filename.startswith('/') and \
                not self._zip_info.filename.endswith('/'):
            return False

        # Either the name do not contains sep either only one a last position
        return '/' not in filename or filename.index('/') == (
                len(filename) - 1)

    @property
    @resolve_children
    def children(self) -> List[DrbNode]:
        if self._children is None:
            self._children = [DrbZipNode(self, entry) for entry in
                              self.get_file_list()
                              if self._is_a_child(entry.filename)]
            self._children = sorted(self._children,
                                    key=lambda entry_cmp: entry_cmp.name)

        return self._children

    def has_impl(self, impl: type) -> bool:
        if issubclass(ZipExtFile, impl):
            return not self.get_attribute(
                DrbZipAttributeNames.DIRECTORY.value, None)

    def get_impl(self, impl: type, **kwargs) -> Any:
        if self.has_impl(impl):
            return self.parent.open_entry(self._zip_info)
        raise DrbNotImplementationException(f'no {impl} '
                                            f'implementation found')

    def close(self):
        pass

    def open_entry(self, zip_info: ZipInfo):
        # open the entry on zip file to return ZipExtFile
        # we back to the first node_file to open is
        return self.parent.open_entry(zip_info)


class DrbBaseZipNode(DrbZipNode):
    """
    This node is used to open a zip container, and browse his content.

    Parameters:
        base_node (DrbNode): The base node.
    """

    def __init__(self, base_node: DrbNode):
        super().__init__(parent=base_node.parent, zip_info=None)
        self._file_list = None
        self._zip_file = None
        self._zip_file_source = None
        self.base_node = base_node

    @property
    def parent(self) -> Optional[DrbNode]:
        """
        Returns the parent of the base node.

        Returns:
            DrbNode: the parent of the node
        """
        return self.base_node.parent

    @property
    def path(self) -> ParsedPath:
        """
        Returns the path of the base node.

        Returns:
            ParsedPath: the full path of the base node
        """
        return self.base_node.path

    @property
    def name(self) -> str:
        """
        Return the name of the base node.
        This name doesn't contain the path.

        Returns:
            str: the base node name
        """
        return self.base_node.name

    @property
    def namespace_uri(self) -> Optional[str]:
        """
        Return the namespace uri of the base node.

        Returns:
            str: the base node namespace
        """
        return self.base_node.namespace_uri

    @property
    def value(self) -> Optional[Any]:
        """
        Return the value of the base node.

        Returns:
            Any: the value
        """
        return self.base_node.value

    @property
    def attributes(self) -> Dict[Tuple[str, str], Any]:
        """
        Return the attributes of the base node.

        Returns:
            Dict: Key(key_name, key_namespace): value(Any)
        """
        return self.base_node.attributes

    def get_attribute(self, name: str, namespace_uri: str = None) -> Any:
        """
        Return a specific attributes of the base node.

        Parameters:
            name (str): The name of the attribute.
            namespace_uri (str): The namespace_uri of the attribute
                                 (default: None).
        Returns:
            Any: the attribute
        """
        return self.base_node.get_attribute(name, namespace_uri)

    @property
    def zip_file(self) -> zipfile.ZipFile:
        if self._zip_file is None:
            try:
                if self.base_node.has_impl(io.BufferedIOBase):
                    self._zip_file_source = self.base_node \
                        .get_impl(io.BufferedIOBase)
                    self._zip_file = zipfile.ZipFile(self._zip_file_source)
                else:
                    raise DrbZipNodeException(f'Unsupported base_node '
                                              f'{type(self.base_node).name} '
                                              f'for DrbFileZipNode')
            except Exception as e:
                raise DrbZipNodeException(f'Unable to read zip file'
                                          f' {self.name} ') from e
        return self._zip_file

    def has_impl(self, impl: type) -> bool:
        return self.base_node.has_impl(impl)

    def get_impl(self, impl: type, **kwargs) -> Any:
        return self.base_node.get_impl(impl)

    def close(self):
        if self._zip_file_source is not None:
            self._zip_file_source.close()
        if self._zip_file is not None:
            self._zip_file.close()
        self.base_node.close()

    def __add_dir_for_path(self, file_info):
        self._file_list.append(file_info)

        if file_info.filename[:-1].find('/') > 0:
            index = file_info.filename[:-1].rindex('/')
            if index > 0:
                path_zip = file_info.filename[:index + 1]
                if path_zip not in self.zip_file.NameToInfo.keys() and \
                        not any(
                            x.filename == path_zip for x in self._file_list):
                    self.__add_dir_for_path(
                        zipfile.ZipInfo(path_zip, file_info.date_time))

    def get_file_list(self):
        if self._file_list is None:
            self._file_list = []
            for fileInfo in self.zip_file.filelist:
                self.__add_dir_for_path(fileInfo)

        return self._file_list

    def _is_a_child(self, filename):
        if '/' not in filename or filename.index('/') == (len(filename) - 1):
            return True
        return False

    def open_entry(self, zip_info: zipfile.ZipInfo):
        # open a entry of the zip en return an BufferedIOBase impl
        return self._zip_file.open(zip_info)


class DrbZipFactory(DrbFactory):

    def _create(self, node: DrbNode) -> DrbNode:
        if isinstance(node, DrbBaseZipNode) or \
                isinstance(node, DrbZipNode):
            return node
        return DrbBaseZipNode(base_node=node)
