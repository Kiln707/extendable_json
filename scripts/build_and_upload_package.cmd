CWD=%~dp0
cd ..
python -m setup.py sphinx
sphinx-build -M markdown ./docs build
echo F | xcopy /s /y build\markdown\index.md README.md
python setup.py sdist bdist_wheel
twine upload extendable_json dist/*
git push --mirror https://github.com/Kiln707/extendable_json.git
cd %CWD%
pause
