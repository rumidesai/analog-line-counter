## Line counter - Rumi Desai

### Overview
Line counter is an application for counting the number of lines in a file when the user is specifying which directory to test in and with an optional argument of a file extension. The default file extension is '.txt'.

### Setup
- `pip install pytest`

### Steps to run
- For help - `python line_counter.py -h`
- Default file extension - `python line_counter.py test1`
- Specified file extension - `python line_counter.py test1 --extension .txt`
- To run the test - `python3 -m pytest tests/`

### Steps to check pylint
- For checking pylint - `pylint line_counter.py`
- For checking test pylint - `pylint tests/test_line_counter.py`

### Note
The pylint test for `test_line_counter.py` will throw an error for `Unable to import 'line_counter'` but that is due to pytest error and can be ignored.