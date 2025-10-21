🧪 Testing

This project uses pytest for automated testing of core modules such as ObserverCollapse, CognitiveField, TimePerception, MitochondrialInfluence, and RealityProjection.

🔧 Installation

To get started with testing, install the development dependencies:
pip install -r requirements-dev.txt

If you don’t have a requirements-dev.txt yet, you can create one with:
pytest
pytest-cov

Running Tests

From the project root, run:
pytest

To include coverage reporting:
pytest --cov=citeon --cov-report=term-missing

To test a specific module:
pytest tests/test_reality_projection.py 

📁 Test File Structure
/citeon/
    observer_collapse.py
    cognitive_field.py
    time_perception.py
    mitochondrial_influence.py
    reality_projection.py

/tests/
    test_observer_collapse.py
    test_cognitive_field.py
    test_time_perception.py
    test_mitochondrial_influence.py
    test_reality_projection.py

Each test file contains unit tests for its corresponding module. All tests follow pytest conventions and are compatible with CI/CD workflows.

Example Test Snippet
# tests/test_observer_collapse.py

from citeon.observer_collapse import ObserverCollapse

def test_entropy_collapse():
    oc = ObserverCollapse()
    result = oc.collapse_entropy(input_entropy=0.8, observer_focus=0.6)
    assert 0.0 <= result <= 1.0
