@ECHO OFF

if NOT EXIST "env" (
echo --------------------
echo Creating venv
echo --------------------
python -m venv env
)
env/Scripts/activate
REM Despues de activar el ambiente ya no se corren las instrucciones
REM pip install virtualenv
REM pip install -r requirements.txt