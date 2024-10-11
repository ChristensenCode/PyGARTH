#!/usr/bin/bash
pip uninstall pygarth -y
python -m build
pip install dist/pygarth-0.0.1-py3-none-any.whl
pygarth -h