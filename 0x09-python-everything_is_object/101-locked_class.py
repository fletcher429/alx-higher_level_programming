#!/usr/bin/python3
class LockedClass:
    __slots__ = ('first_name',)

    def __setattr__(self, name, value):
        if hasattr(self, name):
            super().__setattr__(name, value)
        elif name == 'first_name':
            super().__setattr__(name, value)
        else:
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(name))