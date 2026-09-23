name: Run API Tests

on:
  push:
    branches: [ main, master ]
  pull_request:
    branches: [ main, master ]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - name: Descargar el código
      uses: actions/checkout@v4

    - name: Configurar Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'

    - name: Instalar dependencias
      run: |
        python -m pip install --upgrade pip
        pip install pytest requests

    - name: Ejecutar pruebas
      run: |
        pytest create_user_test.py