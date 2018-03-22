import happybase
import os

hostname = 'spark-test-0'
table_name = 'test-1.16G'
path = 'F:\\Data\\茎杆烧伤刺激6'
connection = happybase.Connection(host=hostname)
try:
    connection.create_table(table_name, {'info': dict()})
    print(table_name, "Create Success")
except Exception:
    print(table_name, "already Exists")
table = connection.table(table_name)

with table.batch(batch_size=20) as batch:
    for index, file in enumerate(os.listdir(path)):
        rowKey = '{:0=4d}'.format(index)[::-1] + file
        with open(os.path.join(path, file), 'rb') as f:
            batch.put(rowKey, {b'info:content': f.read()})
            print(file, "upload success")
    else:
        print('All File have been Upload Success')
