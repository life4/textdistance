pandoc --from=markdown --to=rst --output=README.rst README.md
python3 setup.py sdist
twine upload dist/*
