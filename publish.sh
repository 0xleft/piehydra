set -e

export PATH=~/.local/bin:$PATH

python3 setup.py sdist bdist_wheel
twine upload dist/*
rm -rf build dist *.egg-info