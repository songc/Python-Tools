import argparse
from configparser import ConfigParser
import subprocess
parser = argparse.ArgumentParser()
parser.add_argument('jar', help="Spark jar file")
parser.add_argument('-t', '--table_name', help="hbase table name")
parser.add_argument('-m', '--mode', default="yarn")
parser.add_argument('-c', '--core_num')
parser.add_argument('-v', '--version')
args = parser.parse_args()
cfg = ConfigParser()

jar = args.jar
mode = args.mode
table_name = args.table_name
version = args.version
core_num = args.core_num
if mode == 'yarn':
    cfg.read('config/yarn.ini')
else:
    cfg.read('config/standalone.ini')

cmd_list = list()
cmd_list.append(cfg.get('base', 'spark-submit'))
for options in cfg.items('common'):
    cmd_list.append('--{0}'.format(options[0]))
    cmd_list.append(options[1])

for options in cfg.items('conf'):
    cmd_list.append('--conf')
    cmd_list.append('{0}={1}'.format(*options))

app_name = '{}-{}-{}'.format(table_name, version, core_num)
cmd_list.append(jar)
cmd_list.append(app_name)
cmd_list.append(table_name)
cmd_list.append(app_name)
print(cmd_list)
subprocess.check_call(cmd_list)