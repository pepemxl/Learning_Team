@ECHO OFF
ECHO "pytest library needed"
ECHO "pytest example_01"
pytest tests/example_01
ECHO "pytest -v example_01"
pytest -v tests/example_01
ECHO "pytest -v example_02"
ECHO "Note: only files with prefix or sufix test will be tested"
pytest -v tests/example_02
ECHO "pytest -v example_03 unittest"
pytest -v tests/example_03
