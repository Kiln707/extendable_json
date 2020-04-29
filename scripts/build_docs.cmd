CWD=%~dp0
cd ..
python -m setup.py sphinx
sphinx-build -M markdown ./docs build
echo F | xcopy /s /y build\markdown\index.md README.md
cd %CWD%
pause
