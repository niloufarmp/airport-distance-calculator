import os
import re


class FileManager:
    def __init__(self, file_name, file_location, has_header=True):
        self.file_path = os.path.join(file_location, file_name)
        self.has_header = has_header

    def load_column(self, delimiter, column):
        file = open(self.file_path, 'r')
        result_column = [row.split(delimiter)[column] for row in file.readlines()]
        file.close()
        if self.has_header:
            return result_column[1:]
        else:
            return result_column

    def search_for_row(self, keyword):
        file = open(self.file_path, 'r')
        matched_lines = re.search(keyword, file.read(), flags=re.MULTILINE | re.I)
        file.close()
        if matched_lines:
            return matched_lines.group(0)
