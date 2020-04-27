# coding: utf-8

import abc


class ITaskRunner(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def run_add(self, first: int, second: int) -> None:
        pass

    @abc.abstractmethod
    def run_add_and_wait(self, first: int, second: int) -> int:
        pass
