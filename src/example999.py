# example999.py

from typing import Generic, TypeVar

T_co = TypeVar('T_co', covariant=True)
T_contra = TypeVar('T_contra', contravariant=True)


class I_co(Generic[T_co]):
    t: T_co

    def __init__(self, t: T_co) -> None:
        super().__init__()
        self.t = t


class I_contra(Generic[T_contra]):
    t: T_contra

    def __init__(self, t: T_contra) -> None:
        super().__init__()
        self.t = t


class I_co_derived(I_co):

    def print(self) -> None:
        print(f'{self.t}')


class I_contra_derived(I_contra):

    def print(self) -> None:
        print(f'{self.t}')


class A:
    a: int = 0

    def __str__(self) -> str:
        return f'{self.a}'


class B(A):
    b: int = 0

    def __str__(self) -> str:
        return f'{self.a},{self.b}'


def print_co(i: I_co[A]) -> None:
    print(f'{i.t}')


def print_contra(i: I_contra[B]) -> None:
    print(f'{i.t}')


def example999(input: str):
    '''
    '''
    result = ''
    return result
