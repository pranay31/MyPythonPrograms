from __future__ import absolute_import, division, print_function
import six
import warnings
import os
import sys
import abc

def overrides(interface_class): #superclass
    def overrider(method):
        try:
            assert method in dir(interface_class)
            return method
        except AssertionError:
    return overrider

def suppress_warnings(func):
    def suppressor(*args, **kwargs):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            return func(*args, **kwargs)
    return suppressor

class BaseCapIterator(six.withclass(abc.ABCMeta)):
    def __init__(self, n):
        if n < 0:
            raise ValueError("n value is less than zero")
        else:
            self.n = n


    def foo(self):
        warnings.warn(self.__class__.__name__,warnings.catch_warnings)

    @suppress_warnings
    def foo_safe(self):
        self.foo()

    def __iter__(self):
        for iter_number in range(self.n):
            yield iter_number

    @abc.abstractmethod
    def to_list(self):
        return [property for property in self]

class OddCapOneIterator(BaseCapIterator):
    def __init__(self, n):
        super(OddCapOneIterator, self).__init__(n)

    @overrides(BaseCapIterator)
    def _iter(self):
        for number_in_loop in self:
            if number_in_loop > 0 and number_in_loop % 2 == 1:
                yield number_in_loop


class EvenCapOneIterator(BaseCapIterator):
    def __init__(self, n):
        super(super(OddCapOneIterator, self).__init__(n), self).__init__(n)

    @overrides(BaseCapIterator)
    def _iter(self):
        for number_in_loop in self:
            if number_in_loop % 2 == 0:
                yield number_in_loop




