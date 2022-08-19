# Task 5 - Create the python package


Unique symbols package


Description:

Unique symbols package helps to find out a quantity to the unique symbols in your file or from the string directly through the command line.


How to use a package?

1. Install a package using a <a link='https://packaging.python.org/en/latest/tutorials/installing-packages/'>pip</a> by following the next command:

python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps unique_symbols_vlad

2. Now you are ready to use a package directly from your command line. If you'd like to count the symbols from the string, use following command:

python3 unique_symbols_vlad.py --string 'HERE SHOULD BE YOUR STRING'

Please, note that in this example we've put "unique_symbols_vlad.py" as we've been in the folder with the file.

Also, you can use the following command to count unique symbols from your file:

python3 unique_symbols.py --file here/should/be/your/path/to/file

Be informed if you passed two parameters, the parameter '--file' will have higher priority. That means the string will be ignored.
