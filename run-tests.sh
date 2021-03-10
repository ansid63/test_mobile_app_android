#!/bin/bash
python3 -m venv venv
unzip tests.zip
pip install -r tests/requirements.txt
pytest -sv tests/test_authorization_bitbar.py