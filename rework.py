#! /usr/bin/python3
"""Reads in compile_commands.json and rewrites such that docker can use it."""
import os
from pathlib import Path

def main():
    compile_commands = open('compile_commands.json', 'r')
    lines = compile_commands.readlines()
    compile_commands.close()

    # recursively find all cpp files in the current directory and subdirectories
    cpp_files = Path('.').rglob('*.cpp')
    cpp_files = [str(file) for file in cpp_files]

    for i in range(len(lines)):
        for file in cpp_files:
            cpp_file = os.path.basename(file)
            if lines[i].find(cpp_file) != -1:
                j = lines[i].find(cpp_file)
                k = lines[i].find(cpp_file) + len(cpp_file)
                while lines[i][j] != ' ' and lines[i][j] != '"':
                    j -= 1
                full_path_in_compile_commands = lines[i][j+1:k]
                lines[i] = lines[i].replace(full_path_in_compile_commands, file)
                print(lines[i])

    compile_commands = open('compile_commands.json', 'w')
    compile_commands.writelines(lines)
    compile_commands.close()

if __name__ == '__main__':
    main()
