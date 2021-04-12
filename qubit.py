from dataclasses import astuple, dataclass
import math
import numpy as np


@dataclass
class Qubit:
    # TODO: Make into module with propper imports
    # TODO: Get type hinting working
    zero_coefficient: int
    one_coefficient: int

    @staticmethod
    def from_array(array: np.ndarray):
        """Create a Qubit from a two by one array"""
        if array.shape != (2, 1):
            raise ValueError(
                f"Array must be 2 by 1 to create Qubit. Value passed {array}"
            )
        return Qubit(array[0][0], array[1][0])

    def __iter__(self):
        # Needed to support pytest.approx
        return iter(astuple(self))

    def __len__(self):
        # Needed to support pytest.approx
        return len(astuple(self))

    def probability_measure_zero(self):
        return self.zero_coefficient ** 2 / (
            self.zero_coefficient ** 2 + self.one_coefficient ** 2
        )

    def probability_measure_one(self):
        return self.one_coefficient ** 2 / (
            self.zero_coefficient ** 2 + self.one_coefficient ** 2
        )

    def qc_not(self):
        """Apply the quantum computing not gate to this Qubit
        In the Brilliant course this is gate "X"
        """
        return QCGates.qc_not(self)

    def as_array(self) -> np.ndarray:
        return np.array([[self.zero_coefficient], [self.one_coefficient]])

    def identity(self):
        return QCGates.identity(self)

    def change_phase(self):
        return QCGates.change_phase(self)


ZERO_KET = Qubit(1, 0)
ONE_KET = Qubit(0, 1)
_ONE_OVER_ROOT_2 = 1 / math.sqrt(2)
POSITIVE_HADAMARD = Qubit(_ONE_OVER_ROOT_2, _ONE_OVER_ROOT_2)
NEGATIVE_HADAMARD = Qubit(_ONE_OVER_ROOT_2, -_ONE_OVER_ROOT_2)
