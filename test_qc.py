from dataclasses import dataclass
import math

@dataclass
class Qubit:
    zero_coefficient: int
    one_coefficient: int

    def probability_measure_zero(self):
        return self.zero_coefficient ** 2 / (self.zero_coefficient ** 2 + self.one_coefficient ** 2)


    def probability_measure_one(self):
        return self.one_coefficient ** 2 / (self.zero_coefficient ** 2 + self.one_coefficient ** 2)

Qubit.ZERO_KET = Qubit(1, 0)
Qubit.ONE_KET = Qubit(0, 1)
_ONE_OVER_ROOT_2 = 1 / math.sqrt(2)
Qubit.POSITIVE_HADAMARD = Qubit(_ONE_OVER_ROOT_2, _ONE_OVER_ROOT_2)
Qubit.NEGATIVE_HADAMARD = Qubit(_ONE_OVER_ROOT_2, -_ONE_OVER_ROOT_2)


class QCGates:
    @staticmethod
    def hadamard(qubit: Qubit) -> Qubit:
        return Qubit.POSITIVE_HADAMARD if qubit == qubit.ZERO_KET else Qubit.NEGATIVE_HADAMARD

    @staticmethod
    def qc_not(qubit: Qubit) -> Qubit:
        return Qubit.ZERO_KET if qubit == Qubit.ONE_KET else Qubit.ONE_KET

    
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
    assert QCGates.hadamard(Qubit.ZERO_KET) == Qubit.POSITIVE_HADAMARD
    assert QCGates.hadamard(Qubit.ONE_KET) == Qubit.NEGATIVE_HADAMARD

def test_not_gates():
    assert QCGates.qc_not(Qubit.ZERO_KET) == Qubit.ONE_KET
    assert QCGates.qc_not(Qubit.ONE_KET) == Qubit.ZERO_KET