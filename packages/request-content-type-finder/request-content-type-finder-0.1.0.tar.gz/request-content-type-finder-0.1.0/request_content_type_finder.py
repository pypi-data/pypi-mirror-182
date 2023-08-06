from src.finder import FileTypeFinder


def find(response):
    file_type_finder = FileTypeFinder()

    return file_type_finder.find_file_type(response)