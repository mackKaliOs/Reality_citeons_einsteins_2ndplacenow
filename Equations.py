"""
Equations Module
This module defines core mathematical models for the CITEON engine.
Each function models a key principle in reality calculation and projection.
"""

import math


def collapse_entropy(input_entropy, observer_bias):
    """Models entropy collapse based on observer's influence."""
    influence_factor = 1 - abs(observer_bias - 0.5) * 2
    collapsed_entropy = input_entropy * influence_factor
    return max(0.0, min(collapsed_entropy, 1.0))


def emotional_resonance(amplitude, frequency, coherence_index):
    """Calculates cognitive resonance score."""
    return amplitude * math.sin(2 * math.pi * frequency) * coherence_index


def relative_time_distortion(cognitive_load, temporal_emotion_scale):
    """Models time perception distortion."""
    return 1.0 / (1.0 + cognitive_load * temporal_emotion_scale)


def mitochondrial_coherence(membrane_potential, atp_output, noise_level):
    """Quantifies mitochondrial field strength under coherence influence."""
    base_signal = membrane_potential * atp_output
    signal_to_noise_ratio = base_signal / (1 + noise_level)
    return signal_to_noise_ratio


def reality_projection_field(observer_alignment, coherence_score, quantum_interference):
    """Projects a probability field based on mind-reality coherence."""
    wave_function = observer_alignment * coherence_score
    interference_mod = math.exp(-abs(quantum_interference))
    return wave_function * interference_mod
