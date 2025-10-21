🧪 Testing

This project uses `pytest` for automated testing of core modules.

🔧 Installation

To get started with testing, install the development dependencies:
pip install -r requirements-dev.txt

If you don’t have a `requirements-dev.txt` yet:
pytest
pytest-cov

📈 Running Tests

Run all tests:
pytest

With coverage reporting:
pytest –cov=citeon –cov-report=term-missing

Test a specific module:
pytest tests/test_reality_projection.py

📁 File Structure:
- `/citeon/` → core logic
- `/tests/` → each test file mirrors its corresponding module

📄 Example Test Snippet
```python
from citeon.observer_collapse import ObserverCollapse

def test_entropy_collapse():
    oc = ObserverCollapse()
    result = oc.collapse_entropy(input_entropy=0.8, observer_bias=0.5)
    assert 0.0 <= result <= 1.0
