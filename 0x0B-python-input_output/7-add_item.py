#!/usr/bin/python3
"""script that adds all arguments to a Python list,
and then save them to a file
"""
import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


name_file = "/home/klich1984/holbeton/holbertonschool-higher_level_programming/0x0B-python-input_output/add_item.json"
try:
    open(name_file, 'r', encoding='utf-8')
    print("entre al try")
except:
    save_to_json_file(sys.argv[1:], name_file)
else:
    print("entre al else")
    arguments = len(sys.argv) - 1
    position = 1
    while (arguments >= position):
        print(position, end=" ")
        file_js = load_from_json_file(name_file)
        file_js += sys.argv[1:]
        print("file_js = ", file_js)
        save_to_json_file(file_js, name_file)
        position += position
    
    print("arguments = ", arguments)
print(sys.argv[1:])