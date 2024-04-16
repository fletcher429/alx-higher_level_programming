#!/usr/bin/python3
"""import os"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = \
    __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file
try:
    my_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    my_list = []
for i in sys.argv[1:]:
    my_list.append(i)
save_to_json_file(my_list, "add_item.json")
