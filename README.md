# Scytale


### Setup

1. Close the repository:

"""
git clone https://github.com/magurh/Scytale.git
cd Scytale
"""

2. Create and Activate Virtual Environment

On Windows:
"""
python -m venv venv
venv\Scripts\activate
"""

On MacOS/Linux:
"""
python3 -m venv venv
source venv/bin/activate
"""

3. Install dependencies

"""
pip install -r requirements.txt
"""

4. Run app

"""
python -m app/gui.py
"""

5. Build executable

To build a standalone executable:

"""
pyinstaller --onefile -w app/gui.py
"""