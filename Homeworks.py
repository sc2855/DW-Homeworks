import os

file_name = "eurofxref-hist-90d.xml"
file_path = os.path.abspath(file_name)

if os.path.exists(file_path):
    print(f"File found: {file_path}")
else:
    print(f"File not found! Expected location: {file_path}")
