from dataclasses import dataclass

@dataclass
class Qubit:
    zero_coefficient: int
    one_coefficient: int

    def measure(self):
        return 0

Qubit.ZERO_KET = Qubit(1, 0)
Qubit.ONE_KET = Qubit(0, 1)

    
def test_computational_states():
    zero = Qubit.ZERO_KET # |0>
    assert zero.measure() == 0

    second_zero = Qubit.ZERO_KET
    assert second_zero == zero
    
    one = Qubit.ONE_KET # |1>
    assert one != zero
    # one measures to one