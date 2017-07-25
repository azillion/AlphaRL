#!/usr/bin/env python3
__version_singleton = None


class Version(object):
    """Imports models. Contains a comparison to check if it's the correct version of models.
    Change version in this __init__ to the new version number."""

    def __init__(self):
        self.__version__ = 1
        self.Index = None
        self.imports()

    def __eq__(self, other):
        if other is None:
            return False
        if self.__version__ == other:
            return True
        else:
            return False

    def __repr__(self):
        return "<Replay Models Version Object: v{}".format(str(self.__version__))

    def __str__(self):
        return "v{}".format(str(self.__version__))

    def __dict__(self):
        return {
            "index": self.Index,
        }

    def __instancecheck__(self, instance):
        if type(instance) == Version:
            if self.__version__ == instance.__version__:
                return True
        return False

    def imports(self):
        """Imports all the models"""
        from .indexModel import Index as temp_i
        self.Index = temp_i


def get_models():
    """Returns the Version object"""
    global __version_singleton
    if __version_singleton == None:
        __version_singleton = Version()
    return __version_singleton
