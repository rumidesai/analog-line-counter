"""
Python file for printing number of lines in a directory and it's subdirectories.
"""
import os
import argparse

class DataStore():
    """
    Data store for file paths and number of lines in each file encountered.
    """
    def __init__(self):
        self.file_paths = []
        self.num_lines = []

    def add_file_path(self, file_path):
        """
        Add file path to a list.

        Parameters
        ----------
        self
        file_path : str
            File path
        """
        self.file_paths.append(file_path)

    def add_line_count(self, num_line):
        """
        Add number of lines per file to a list.

        Parameters
        ----------
        self
        num_line : int
            Number of lines
        """
        self.num_lines.append(num_line)

    def get_num_file_paths(self):
        """
        Get total number of files.

        Parameters
        ----------
        self

        Returns
        -------
        Number of files
        """
        return len(self.file_paths)

    def get_total_num_lines(self):
        """
        Get total number of lines.

        Parameters
        ----------
        self

        Returns
        -------
        Total number of lines
        """
        return sum(self.num_lines)

    def print_details(self):
        """
        Print data store.

        Parameters
        ----------
        self
        """
        for file_path, num_line in zip(self.file_paths, self.num_lines):
            print(file_path + "\t" + str(num_line))
        print('=' * 20)

        print('Number of files found:\t' + str(len(self.file_paths)))
        print('Total number of lines:\t' + str(sum(self.num_lines)))
        if len(self.file_paths) != 0:
            avg_lines = sum(self.num_lines) / len(self.file_paths)
            print('Average lines per file:\t' + str((avg_lines)))


def count_lines(directory, extension):
    """
    Prints the number of lines in each file given the user directory and file extension.

    Parameters
    ----------
    directory : str
        Directory path
    extension : str
        Extension
    """

    data = DataStore()

    total_lines = 0
    total_files = 0

    for subdir, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(subdir, file)
            if not file_path.endswith(extension):
                continue
            with open(file_path) as file_pointer:
                num_lines = sum(1 for _ in file_pointer)
                total_lines += num_lines
                total_files += 1
                data.add_file_path(file_path)
                data.add_line_count(num_lines)

    return data


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('directory', type=str, help='Directory path')
    parser.add_argument('--extension', type=str, required=False, default='.txt', help='Extension')

    args = parser.parse_args()
    data_store = count_lines(directory=args.directory, extension=args.extension)
    data_store.print_details()
