#!/bin/zsh
python3.8 -m build

python3.8 -m pip install --upgrade twine

python3.8 -m twine upload --repository testpypi dist/*
