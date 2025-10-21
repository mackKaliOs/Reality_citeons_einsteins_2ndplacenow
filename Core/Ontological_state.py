# core/ontological_state.py

"""
Ontological State Tracker for CITEON

Tracks evolving ontological nodes, their weights, and overall system coherence.
"""

from collections import defaultdict

class OntologicalState:
    def __init__(self):
        self.state = defaultdict(float)  # Each node gets a float influence score
        self.history = []

    def apply_influence(self, concept_id, influence_value):
        """Apply influence to a node in the ontological field."""
        self.state[concept_id] += influence_value
        self.history.append((concept_id, influence_value))

    def collapse_state(self, threshold=1.0):
        """
        Collapse active nodes above threshold into 'expressed' reality.
        Returns list of expressed states.
        """
        expressed = [k for k, v in self.state.items() if v >= threshold]
        return expressed

    def reset(self):
        """Reset the ontological field to zero."""
        self.state.clear()
        self.history.clear()

    def snapshot(self):
        """Return a current snapshot of the state."""
        return dict(self.state)
