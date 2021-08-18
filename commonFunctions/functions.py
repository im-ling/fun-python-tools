import os


def read_text_file_to_lines(file_path):
    file_obj = open(file_path, "r")
    lines = file_obj.readlines()
    file_obj.close()
    return lines


def write_lines_to_path(lines, path):
    with open(path, 'w') as filehandle:
        for line in lines:
            filehandle.write(line)


def all_files_in_folder(folder_path):
    result = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            result.append(file_path)
    return result


def find_all_file_endswith(suffix, local_path):
    result = []
    for root, dirs, files in os.walk(local_path):
        for file in files:
            if file.endswith(suffix):
                file_path = os.path.join(root, file)
                result.append(file_path)
    return result
