"""
Test `line_counter.py`.
"""
from line_counter import count_lines

def test_count_lines_dir_subdir_true():
    """
    Count number of lines in directory and subdirectory.
    """
    directory = 'test1'
    extension = 'txt'
    data_store = count_lines(directory=directory, extension=extension)
    assert data_store.get_num_file_paths() == 4
    assert data_store.get_total_num_lines() == 16

def test_count_lines_false():
    """
    Count number of lines with no files with given extension.
    """
    directory = 'test1'
    extension = 'dir'
    data_store = count_lines(directory=directory, extension=extension)
    assert not data_store.get_num_file_paths() == 4
    assert not data_store.get_total_num_lines() == 16
    assert data_store.get_num_file_paths() == 0
    assert data_store.get_total_num_lines() == 0

def test_count_lines_dir_only_true():
    """
    Count number of lines in directory with no subdirectories.
    """
    directory = 'test2'
    extension = 'txt'
    data_store = count_lines(directory=directory, extension=extension)
    assert data_store.get_num_file_paths() == 2
    assert data_store.get_total_num_lines() == 3
