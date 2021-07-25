## Create a python virtualenv

```bash
python -m venv env
```

## Activate Enviroment

### windows
```bash
env/Scripts/activate
```

## To run the application
----------------------

### linux
```bash
./init.sh
export FLASK_APP=main.py
flask run
```

### windows
```bash
./init.bat
pip install -r requirements.txt
set FLASK_APP=main.py
flask run
```