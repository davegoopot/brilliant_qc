import math
import pytest
from qubit import ZERO_KET, ONE_KET, POSITIVE_HADAMARD, NEGATIVE_HADAMARD, Qubit
from qc_gates import hadamard, H, qc_not, identity, I, change_phase
from dataclasses import astuple

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
    assert POSITIVE_HADAMARD.zero_coefficient == positive_one_over_root_2
    assert POSITIVE_HADAMARD.one_coefficient == positive_one_over_root_2

    assert NEGATIVE_HADAMARD.zero_coefficient == positive_one_over_root_2
    assert NEGATIVE_HADAMARD.one_coefficient == -positive_one_over_root_2

def test_hadamard_gates():
    assert hadamard(ZERO_KET) == POSITIVE_HADAMARD
    assert hadamard(ONE_KET) == NEGATIVE_HADAMARD
    assert hadamard(qc_not(ZERO_KET)) == NEGATIVE_HADAMARD
    assert hadamard(POSITIVE_HADAMARD) == pytest.approx(ZERO_KET)

def test_not_gates():
    assert qc_not(ZERO_KET) == ONE_KET
    assert qc_not(ONE_KET) == ZERO_KET

def test_identity_gate():
    assert identity(ZERO_KET) == ZERO_KET
    assert identity(ONE_KET) == ONE_KET
    assert identity(POSITIVE_HADAMARD) == POSITIVE_HADAMARD
    assert identity(NEGATIVE_HADAMARD) == NEGATIVE_HADAMARD
    

def test_phase_gate():
    assert change_phase(ZERO_KET) == ZERO_KET
    assert change_phase(ONE_KET) == Qubit(0, -1)
    assert change_phase(POSITIVE_HADAMARD) == NEGATIVE_HADAMARD
    assert change_phase(NEGATIVE_HADAMARD) == POSITIVE_HADAMARD

def test_probability_changes():
    assert change_phase(ONE_KET).probability_measure_zero() == ONE_KET.probability_measure_zero()
    assert change_phase(ONE_KET).probability_measure_one() == ONE_KET.probability_measure_one()

def test_multiple_gates():
    assert hadamard(change_phase(qc_not(ZERO_KET))) == Qubit(-1/math.sqrt(2), 1/math.sqrt(2))

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
    assert H(ZERO_KET) == POSITIVE_HADAMARD
    # I gate is identity
    assert I(ZERO_KET) == ZERO_KET