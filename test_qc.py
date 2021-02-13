from dataclasses import dataclass
import math
import numpy as np

@dataclass
class Qubit:
    zero_coefficient: int
    one_coefficient: int

    @staticmethod
    def from_array(array: np.ndarray):
        """Create a Qubit from a two by one array"""
        if array.shape != (2, 1):
            raise ValueError(f"Array must be 2 by 1 to create Qubit. Value passed {array}")
        return Qubit(array[0][0], array[1][0])

    def probability_measure_zero(self):
        return self.zero_coefficient ** 2 / (self.zero_coefficient ** 2 + self.one_coefficient ** 2)


    def probability_measure_one(self):
        return self.one_coefficient ** 2 / (self.zero_coefficient ** 2 + self.one_coefficient ** 2)

    def hadamard(self):
        """Apply the hadamard gate to this Qubit"""
        return QCGates.hadamard(self)

    def qc_not(self):
        """Apply the quantum computing not gate to this Qubit
        In the Brilliant course this is gate "X"
        """
        return QCGates.qc_not(self)

    def as_array(self) -> np.ndarray:
        return np.array(
            [
                [self.zero_coefficient],
                [self.one_coefficient]
            ]
        )

    def identity(self):
        return QCGates.identity(self)

    def change_phase(self):
        return QCGates.change_phase(self)


Qubit.ZERO_KET = Qubit(1, 0)
Qubit.ONE_KET = Qubit(0, 1)
_ONE_OVER_ROOT_2 = 1 / math.sqrt(2)
Qubit.POSITIVE_HADAMARD = Qubit(_ONE_OVER_ROOT_2, _ONE_OVER_ROOT_2)
Qubit.NEGATIVE_HADAMARD = Qubit(_ONE_OVER_ROOT_2, -_ONE_OVER_ROOT_2)


class QCGates:
    HADAMARD_MATRIX = 1/np.sqrt(2) * np.array(
        [
            [1, 1],
            [1, -1]
        ])

    @staticmethod
    def matmul(qubit: Qubit, matrix: np.ndarray) -> Qubit:
        q_array = qubit.as_array()
        result = np.matmul(matrix, q_array)
        return Qubit.from_array(result)

    @staticmethod
    def hadamard(qubit: Qubit) -> Qubit:
        return QCGates.matmul(qubit, QCGates.HADAMARD_MATRIX)

    @staticmethod
    def qc_not(qubit: Qubit) -> Qubit:
        return Qubit.ZERO_KET if qubit == Qubit.ONE_KET else Qubit.ONE_KET

    @staticmethod
    def identity(qubit: Qubit) -> Qubit:
        return qubit

    Z_MATRIX = np.array(
        [
            [1, 0],
            [0, -1]
        ]
    )

    @staticmethod
    def change_phase(qubit: Qubit) -> Qubit:
        return QCGates.matmul(qubit, QCGates.Z_MATRIX)

def test_computational_states():
    zero = Qubit.ZERO_KET # |0>
    assert zero.probability_measure_zero() == 1
    assert zero.probability_measure_one() == 0

    second_zero = Qubit.ZERO_KET
    assert second_zero == zero
    
    one = Qubit.ONE_KET # |1>
    assert one != zero
    
    assert one.probability_measure_zero() == 0
    assert one.probability_measure_one() == 1


def test_hadamard_states():
    positive_one_over_root_2 = 1 / math.sqrt(2)
    assert Qubit.POSITIVE_HADAMARD.zero_coefficient == positive_one_over_root_2
    assert Qubit.POSITIVE_HADAMARD.one_coefficient == positive_one_over_root_2

    assert Qubit.NEGATIVE_HADAMARD.zero_coefficient == positive_one_over_root_2
    assert Qubit.NEGATIVE_HADAMARD.one_coefficient == -positive_one_over_root_2

def test_hadamard_gates():
    assert Qubit.ZERO_KET.hadamard() == Qubit.POSITIVE_HADAMARD
    assert Qubit.ONE_KET.hadamard() == Qubit.NEGATIVE_HADAMARD
    assert Qubit.ZERO_KET.qc_not().hadamard() == Qubit.NEGATIVE_HADAMARD

def test_not_gates():
    assert Qubit.ZERO_KET.qc_not() == Qubit.ONE_KET
    assert Qubit.ONE_KET.qc_not() == Qubit.ZERO_KET

def test_identity_gate():
    assert Qubit.ZERO_KET.identity() == Qubit.ZERO_KET
    assert Qubit.ONE_KET.identity() == Qubit.ONE_KET
    assert Qubit.POSITIVE_HADAMARD.identity() == Qubit.POSITIVE_HADAMARD
    assert Qubit.NEGATIVE_HADAMARD.identity() == Qubit.NEGATIVE_HADAMARD
    

def test_phase_gate():
    assert Qubit.ZERO_KET.change_phase() == Qubit.ZERO_KET
    assert Qubit.ONE_KET.change_phase() == Qubit(0, -1)
    assert Qubit.POSITIVE_HADAMARD.change_phase() == Qubit.NEGATIVE_HADAMARD
    assert Qubit.NEGATIVE_HADAMARD.change_phase() == Qubit.POSITIVE_HADAMARD

def test_probability_changes():
    assert Qubit.ONE_KET.change_phase().probability_measure_zero() == Qubit.ONE_KET.probability_measure_zero()
    assert Qubit.ONE_KET.change_phase().probability_measure_one() == Qubit.ONE_KET.probability_measure_one()