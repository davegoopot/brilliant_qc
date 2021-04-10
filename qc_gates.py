import numpy as np
from qubit import Qubit, ONE_KET, ZERO_KET

HADAMARD_MATRIX = 1/np.sqrt(2) * np.array(
        [
            [1, 1],
            [1, -1]
        ])

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


def identity(qubit: Qubit) -> Qubit:
    return qubit

Z_MATRIX = np.array(
    [
        [1, 0],
        [0, -1]
    ]
)


def change_phase(qubit: Qubit) -> Qubit:
    return matmul(qubit, Z_MATRIX)