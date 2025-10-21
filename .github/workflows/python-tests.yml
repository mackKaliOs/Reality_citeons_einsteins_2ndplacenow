name: 🧪 CI | Pytest with Coverage

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - name: 📥 Checkout Repository
      uses: actions/checkout@v3

    - name: 🐍 Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: 📦 Install Dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install pytest pytest-cov

    - name: 🧪 Run Tests with Coverage
      run: |
        pytest --cov=citeon --cov-report=term-missing

    - name: 📤 Upload HTML Coverage Report (artifact)
      if: always()
      uses: actions/upload-artifact@v3
      with:
        name: htmlcov
        path: htmlcov
