import numpy as np
from qubit import Qubit, ONE_KET, ZERO_KET

# fmt: off
HADAMARD_MATRIX = 1/np.sqrt(2) * np.array(
        [
            [1, 1],
            [1, -1]
        ])
# fmt: off

def matmul(qubit: Qubit, matrix: np.ndarray) -> Qubit:
    q_array = qubit.as_array()
    result = np.matmul(matrix, q_array)
    return Qubit.from_array(result)


def hadamard(qubit: Qubit) -> Qubit:
    return matmul(qubit, HADAMARD_MATRIX)

def H(q: Qubit):
    return hadamard(q)


def qc_not(qubit: Qubit) -> Qubit:
    return ZERO_KET if qubit == ONE_KET else ONE_KET

def X(q: Qubit):
    return qc_not(q)


def identity(qubit: Qubit) -> Qubit:
    return qubit

def I(q: Qubit):
    return identity(q)

# fmt: off
Z_MATRIX = np.array(
    [
        [1, 0],
        [0, -1]
    ]
)
# fmt: on


def change_phase(qubit: Qubit) -> Qubit:
    return matmul(qubit, Z_MATRIX)


def Z(q: Qubit):
    return change_phase(q)


# fmt: off
S_MATRIX = np.array(
    [
        [1, 0],
        [0, 1j]
    ]
)
# fmt: on

def S(q: Qubit):
    return matmul(q, S_MATRIX)


