set -e
pandoc --from=markdown --to=rst --output=README.rst README.md
python3 setup.py sdist bdist_wheel
twine upload dist/*
