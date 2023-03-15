import os
import sys
from importlib import import_module
from types import ModuleType

import sniffio


class _DynamicBackend(ModuleType):
    def __getattr__(self, item):
        asynclib_name = sniffio.current_async_library()
        modulename = "dynmod._backends._" + asynclib_name
        try:
            mod = sys.modules[modulename]
        except KeyError:
            mod = import_module(modulename)
        return getattr(mod, item)


def _prepare_backend_module(name: str = None):
    if name is None:  # use dynamic proxy-object
        backend = _DynamicBackend("dynmod.backend")
        backend.__file__ = "<file>"  # n/a, not imported
    elif name not in ("asyncio", "trio"):
        raise RuntimeError("Unknown backend: %s" % (name,))
    else:  # static mirror module to backend
        if name == "asyncio":
            import dynmod._backends._asyncio as _b
        else:
            import dynmod._backends._trio as _b
        backend = ModuleType("dynmod.backend")
        backend.__file__ = _b.__file__
        backend.__dict__.update((k, v) for k, v in _b.__dict__.items() if not (k.startswith("__") and k.endswith("__")))
    sys.modules[backend.__name__] = backend


# .backend pseudo-module
_prepare_backend_module(os.environ.get("DYNMOD_BACKEND"))
