# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/00_callbacks.ipynb (unless otherwise specified).

__all__ = ['Callback', 'console', 'CallbackHandler', 'ReporterCallback']

# Cell
from contextlib import ContextDecorator
from rich.console import Console
from fastcore.imports import *
from fastcore.foundation import *
from fastcore.basics import *
from fastcore.meta import *

# Cell
_events = L.split('after_enter before_exit')

# Cell
mk_class('event', **_events.map_dict(),
         doc="All possible events as attributes to get tab-completion and typo-proofing")

# Cell
@funcs_kwargs(as_method=True)
class Callback(Stateful,GetAttr):
    "Basic class handling tweaks of the runner"
    _methods = _events

    def __init__(self, **kwargs): assert not kwargs, f'Passed unknown events: {kwargs}'
    def __repr__(self): return type(self).__name__

    def __call__(self, event_name):
        "Call `self.{event_name}` if it's defined"
        res = getattr(self, event_name, noop)()
        return res

    def __setattr__(self, name, value):
        super().__setattr__(name, value)

    @property
    def name(self):
        "Name of the `Callback`, camel-cased and with '*Callback*' removed"
        return class2attr(self, 'Callback')

# Cell
console = Console()

# Cell
class CallbackHandler:
    "Basic handler to assign the callback events to their respective flows"
    def __init__(self,cbs=None): self.cbs = cbs if cbs else []

    def after_enter(self, o):
        res = True
        for cb in self.cbs: res = res and cb.after_enter(o)
        return res

    def before_exit(self, o):
        res = True
        for cb in self.cbs: res = res and cb.before_exit(o)
        return res

# Cell
class ReporterCallback(Callback):
    def after_enter(self): console.print(self.desc, style="green")
    def before_exit(self): console.print(self.desc, style="green")