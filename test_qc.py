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