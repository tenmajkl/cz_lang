install:
	python3 -m venv .
	bin/pip3 install -r requirements.txt
	bin/pyinstaller src/cz.py
