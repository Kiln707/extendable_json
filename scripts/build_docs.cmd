CWD=%~dp0
cd ..
python -m setup.py sphinx
cd %CWD%
pause
