import filecmp

def compare_files(file1_path, file2_path):
    if filecmp.cmp(file1_path, file2_path):
        return 1  # Files are the same
    else:
        return 0  # Files have differences

file1_path = "/home/dinesh/mini_project/esc_command/esc_Bold.py"
file2_path = "/home/dinesh/mini_project/printer/esc_Bold.py"

result = compare_files(file1_path, file2_path)
print(result)

