import rarfile
import os
import argparse
import zipfile

parser = argparse.ArgumentParser()
parser.add_argument('dir', help="目标文件或目录")
parser.add_argument('-p', '--password',default=None)
args = parser.parse_args()
password = args.password
root_dir = args.dir
file_list = []
for rar in os.listdir(root_dir):
    file_list.append(os.path.join(root_dir,rar))
for file in file_list:
    dirname = os.path.dirname(file)
    if file.endswith('.rar'):
        uzip = rarfile.RarFile(file)
        uzip.extractall(path=dirname,pwd=password)
        uzip.close()
    if file.endswith('.zip'):
        uzip = zipfile.ZipFile(file)
        uzip.extractall(path="dirname",pwd=password)
        uzip.close()
