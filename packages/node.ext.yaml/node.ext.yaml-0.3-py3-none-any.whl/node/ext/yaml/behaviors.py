from ._yaml import ordered_dump
from ._yaml import ordered_load
from .interfaces import IYamlMappingStorage
from .interfaces import IYamlMember
from .interfaces import IYamlRoot
from .interfaces import IYamlSequenceStorage
from node.behaviors import MappingStorage
from node.behaviors import SequenceStorage
from node.behaviors import WildcardFactory
from node.ext.fs import FSLocation
from node.ext.fs import join_fs_path
from node.interfaces import ICallable
from node.interfaces import IMappingNode
from node.interfaces import ISequenceNode
from node.utils import instance_property
from odict import odict
from plumber import Behavior
from plumber import default
from plumber import finalize
from plumber import override
from plumber import plumb
from zope.interface import implementer
import os


@implementer(IYamlMember)
class YamlMember(WildcardFactory):
    factories = default(dict())
    default_mapping_factory = default(None)
    default_sequence_factory = default(None)

    @override
    def __getitem__(self, name):
        value = self.storage[name]
        if isinstance(value, odict) or isinstance(value, list):
            factory = self.factory_for_pattern(str(name))
            if factory is None:
                factory = (
                    self.default_mapping_factory
                    if isinstance(value, odict)
                    else self.default_sequence_factory
                )
            if factory is not None:
                value = factory(name=name, parent=self)
        return value

    @override
    def __setitem__(self, name, value):
        if IYamlMember.providedBy(value):
            value = value.storage
        self.storage[name] = value


class YamlStorage(Behavior):

    @plumb
    def __init__(next_, self, **kw):
        next_(self, **kw)
        name = self.name
        parent = self.parent
        own_storage = None
        if parent:
            storage = parent.storage
            if IMappingNode.providedBy(parent) and name in storage:
                own_storage = storage[name]
            elif ISequenceNode.providedBy(parent) and int(name) < len(storage):
                own_storage = storage[int(name)]
        if own_storage is None:
            if IMappingNode.providedBy(self):
                own_storage = odict()
            elif ISequenceNode.providedBy(self):
                own_storage = list()
        self._storage = own_storage

    @finalize
    @property
    def storage(self):
        return self._storage


@implementer(IYamlMappingStorage)
class YamlMappingStorage(YamlStorage, YamlMember, MappingStorage):
    """"""


@implementer(IYamlSequenceStorage)
class YamlSequenceStorage(YamlStorage, YamlMember, SequenceStorage):

    @plumb
    def __getitem__(next_, self, index):
        if type(index) is slice:
            raise NotImplementedError(
                'YamlSequenceStorage not supports slicing'
            )
        return next_(self, index)

    @plumb
    def insert(next_, self, index, value):
        if IYamlMember.providedBy(value):
            value = value.storage
        next_(self, index, value)

    @override
    def __contains__(self, value):
        if IYamlMember.providedBy(value):
            value = value.storage
        for v in self.storage:
            if v is value:
                return True
        return False


@implementer(IYamlRoot, ICallable)
class YamlRootStorage(YamlMember, MappingStorage, FSLocation):

    @finalize
    @instance_property
    def storage(self):
        file_path = join_fs_path(self)
        if os.path.exists(file_path):
            with open(file_path) as f:
                return ordered_load(f.read())
        return odict()

    @finalize
    def __call__(self):
        data = ordered_dump(self.storage, sort_keys=False)
        file_path = join_fs_path(self)
        with open(file_path, 'w') as f:
            f.write(data)


@implementer(ICallable)
class YamlCallableMember(Behavior):

    @override
    def __call__(self):
        yaml_root = self.acquire(IYamlRoot)
        if yaml_root:
            yaml_root()
