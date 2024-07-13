# Enigma


### Setup

1. Set path for python, on windows:
```
set PYTHONPATH=..
```
while on MacOS or Linux:
```
export PYTHONPATH=..
```

2. Run app:

```
python app/gui.py
```

3. To build a standalone executable:

```
pyinstaller --onefile -w app/gui.py
```

For this, you may need to temporarily disable the antivirus.