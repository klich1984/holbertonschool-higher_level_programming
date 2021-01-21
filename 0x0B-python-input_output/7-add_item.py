#!/usr/bin/python3
"""script that adds all arguments to a Python list,
and then save them to a file
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


name_file = "add_item.json"
try:
    open(name_file, 'r', encoding='utf-8')
except:
    save_to_json_file(sys.argv[1:], name_file)
else:
    file_js = load_from_json_file(name_file)
    file_js += (sys.argv[1:])
    save_to_json_file(file_js, name_file)
