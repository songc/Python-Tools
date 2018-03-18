import happybase
import os

hostname = 'hadoop-hbase'
table_name = 'spark-test'
path = 'F:\\Download\\software\\彩图'
connection = happybase.Connection(host=hostname)
connection.create_table(table_name, {'info': dict()})
table = connection.table(table_name)

for file in os.listdir(path):
    with open(file, 'rb') as f:
        table.put(f.name, {b'info:content': f.read()})