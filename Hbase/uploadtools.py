import happybase
import os

hostname = 'hadoop-hbase'
table_name = 'spark-test'
path = 'F:\\Download\\software\\彩图'
connection = happybase.Connection(host=hostname)
try:
    connection.create_table(table_name, {'info': dict()})
except Exception:
    print(table_name, "already Exists")
table = connection.table(table_name)

for file in os.listdir(path):
    with open(os.path.join(path, file), 'rb') as f:
        table.put(f.name, {b'info:content': f.read()})
else:
    print('All File have been Upload Success')
