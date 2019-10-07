echo exectuting build...

python setup.py sdist bdist_wheel

echo --------------------------------------------

echo uploading to test.pypi.org ...
python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

echo --------------------------------------------



