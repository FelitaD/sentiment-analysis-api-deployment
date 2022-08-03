#!/bin/bash

echo "Running status test."
python3 test_status.py
echo "Running login test."
python3 test_login.py
echo "Running permissions test."
python3 test_permissions.py
echo "Running analyzer v1 test."
python3 test_analyzer_1.py
echo "Running analyzer v2 test."
python3 test_analyzer_2.py