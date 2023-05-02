import os

def compare_files(file1, file2):
    with open(file1) as f1:
        with open(file2) as f2:
            with open('output.txt', 'w') as output_file:
                for line in f1:
                    if line not in f2:
                        output_file.write(line)

compare_files('1.txt', 'Xbrowser_1.txt')
