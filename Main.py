import os
import subprocess
from datetime import datetime

script_path = os.path.abspath('./TestExecution.py')
report_path = os.path.abspath(f'./Reports/report{datetime.now().strftime("%Y%m%d%H%M%S")}.html')
command = f'pytest {script_path} --html={report_path}'
subprocess.run(command, check=True, shell=True)