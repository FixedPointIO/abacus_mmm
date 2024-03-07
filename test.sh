#!/bin/bash



set -e

readonly VENV_DIR=/tmp/test_env
echo "Creating virtual environment under ${VENV_DIR}."
echo "You might want to remove this when you no longer need it."

# Install deps in a virtual env.
python -m venv "${VENV_DIR}"
source "${VENV_DIR}/bin/activate"
python --version

# Install JAX.
python -m pip install --upgrade pip setuptools
python -m pip install -r requirements/requirements.txt
python -c 'import jax; print(jax.__version__)'

# Run setup.py, this installs the python dependencies
python -m pip install .

# Python test dependencies.
python -m pip install -r requirements/requirements_tests.txt

# Run tests using pytest.
python -m pytest abacus_mmm