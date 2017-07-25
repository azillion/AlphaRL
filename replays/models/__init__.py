from models.v1 import get_models as v1

_models_singleton = None
__used_version__ = None


def version_compare(*args):
    global _models_singleton
    for arg in args:
        model_version = arg()
        if _models_singleton is None:
            if model_version == __used_version__:
                _models_singleton = model_version
    if _models_singleton is not None:
        yield _models_singleton
    else:
        yield None


def get_version(version: int = 1):
    global __used_version__
    if __used_version__ is None:
        __used_version__ = version

    for v_object in version_compare(v1):
        if v_object is not None:
            return v_object