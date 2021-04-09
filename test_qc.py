import math
import pytest
from qubit import ZERO_KET, ONE_KET
from qc_gates import hadamard

def test_computational_states():
    zero = ZERO_KET # |0>
    assert zero.probability_measure_zero() == 1
    assert zero.probability_measure_one() == 0

    second_zero = ZERO_KET
    assert second_zero == zero
    
    one = ONE_KET # |1>
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
    assert ZERO_KET.hadamard() == Qubit.POSITIVE_HADAMARD
    assert ONE_KET.hadamard() == Qubit.NEGATIVE_HADAMARD
    assert ZERO_KET.qc_not().hadamard() == Qubit.NEGATIVE_HADAMARD
    assert Qubit.POSITIVE_HADAMARD.hadamard() == pytest.approx(ZERO_KET)

def test_not_gates():
    assert ZERO_KET.qc_not() == ONE_KET
    assert ONE_KET.qc_not() == ZERO_KET

def test_identity_gate():
    assert ZERO_KET.identity() == ZERO_KET
    assert ONE_KET.identity() == ONE_KET
    assert Qubit.POSITIVE_HADAMARD.identity() == Qubit.POSITIVE_HADAMARD
    assert Qubit.NEGATIVE_HADAMARD.identity() == Qubit.NEGATIVE_HADAMARD
    

def test_phase_gate():
    assert ZERO_KET.change_phase() == ZERO_KET
    assert ONE_KET.change_phase() == Qubit(0, -1)
    assert Qubit.POSITIVE_HADAMARD.change_phase() == Qubit.NEGATIVE_HADAMARD
    assert Qubit.NEGATIVE_HADAMARD.change_phase() == Qubit.POSITIVE_HADAMARD

def test_probability_changes():
    assert ONE_KET.change_phase().probability_measure_zero() == ONE_KET.probability_measure_zero()
    assert ONE_KET.change_phase().probability_measure_one() == ONE_KET.probability_measure_one()

def test_multiple_gates():
    assert ZERO_KET.qc_not().change_phase().hadamard() == Qubit(-1/math.sqrt(2), 1/math.sqrt(2))

def test_approx_equal_testing_method():
    v1 = 1
    v2 = 1.0000001
    assert v1 == pytest.approx(v2)
    
    q1 = Qubit(v1, 0)
    q2 = Qubit(v2, 0)
    assert not(q1 == q2)
    assert astuple(q1) == (v1, 0)
    assert not(astuple(q1) == astuple(q2))
    assert astuple(q1) == pytest.approx(astuple(q2))
    assert q1 == pytest.approx(q2)

def test_single_letter_gates():
    # H gate is Haddamard
    assert H(ZERO_KET) == Qubit.POSITIVE_HADAMARD