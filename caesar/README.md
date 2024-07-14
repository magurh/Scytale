# Caesar

Despite its name, Caesar is an app that uses any type of substitution cyphers (not only Caesar cyphers) for encryption. The app is built in python using the `cryptography` module.

Caesar also has an option to decrypt messages without a key. This uses letter and N-gram frequency analysis, together with a Monte Carlo Markov Chain type algorithm. Note that this only works on substitution cyphers.


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