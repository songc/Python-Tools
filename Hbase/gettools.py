import happybase

host_name = 'hadoop-hbase'
table_name = 'spark-test'
connect = happybase.Connection(host_name)
table = connect.table(table_name)

for row_key, row_data in table.scan(limit=100, filter=b'KeyOnlyFilter()'):
    print(str(row_key, 'utf-8'))
