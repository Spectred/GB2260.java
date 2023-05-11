import glob
import os

if __name__ == '__main__':
    dict = {}

    folder_path = '.'
    file_extension = '*.txt'
    file_paths = glob.glob(os.path.join(folder_path, file_extension))
    for file_path in file_paths:
        with open(file_path, 'r') as f:
            line = f.readline()
            while line:
                code, name = line.strip().split("\t")
                if str(code).isdigit():
                    dict.setdefault(code, name)
                line = f.readline()

    print(len(dict.items()))
    print(dict)
    sorted_list = sorted(dict.items(), key=lambda x: x[0])
    with open('2000-2022.txt', 'w') as f:
        for code, name in sorted_list:
            f.write(f'{code}\t{name}\n')
