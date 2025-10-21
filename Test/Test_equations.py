# tests/test_equations.py

import pytest
from citeon.equations import (
    collapse_entropy,
    emotional_resonance,
    relative_time_distortion,
    mitochondrial_coherence,
    reality_projection_field,
)

def test_collapse_entropy_within_bounds():
    result = collapse_entropy(0.8, 0.5)
    assert 0.0 <= result <= 1.0
    assert result == pytest.approx(0.8)

def test_collapse_entropy_bias_extreme():
    result = collapse_entropy(0.9, 0.0)
    assert result < 0.9
    assert 0.0 <= result <= 1.0

def test_emotional_resonance_wave_pattern():
    res = emotional_resonance(1.0, 1.0, 1.0)
    assert -1.0 <= res <= 1.0

def test_emotional_resonance_zero_coherence():
    res = emotional_resonance(5.0, 2.0, 0.0)
    assert res == 0.0

def test_relative_time_distortion_low_load():
    res = relative_time_distortion(0.1, 0.1)
    assert res > 0.9

def test_relative_time_distortion_high_load():
    res = relative_time_distortion(10, 2)
    assert 0 < res < 0.1

def test_mitochondrial_coherence_positive_values():
    res = mitochondrial_coherence(150.0, 3.2, 2.5)
    assert res > 0.0

def test_mitochondrial_coherence_increasing_noise():
    base = mitochondrial_coherence(100, 3, 1)
    noisy = mitochondrial_coherence(100, 3, 10)
    assert noisy < base

def test_reality_projection_field_alignment_effect():
    aligned = reality_projection_field(1.0, 1.0, 0.0)
    misaligned = reality_projection_field(0.5, 1.0, 0.0)
    assert aligned > misaligned

def test_reality_projection_field_interference_effect():
    low_interference = reality_projection_field(1.0, 1.0, 0.1)
    high_interference = reality_projection_field(1.0, 1.0, 5.0)
    assert high_interference < low_interference
