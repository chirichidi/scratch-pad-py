import os
import sys


src_path = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
src_path += "/scratch_pad_py"
sys.path.append(src_path)

dir_list = os.listdir(src_path)
for item in dir_list:
    path = src_path + "/" + item
    if not os.path.isdir(path):
        continue
    if item.startswith("."):
        continue
    if path in sys.path:
        continue
    sys.path.append(item)
