import os
import time
import datetime

# Config file path
CONFIG_PATH='config'
# Unset the config variable
START=''
CLOCK_FORMAT=''
END=''

# Checking clear screen method
if os.name == 'posix':
    CLEAR="os.system('clear')"
elif os.name in ('nt', "dos", "ce"):
    CLEAR="os.system('CLS')"
else:
    CLEAR="print('\n' * 100)"

# Reading config file
with open(CONFIG_PATH, 'r') as config_file:
    CONFIG=config_file.read()

# Running the config file
exec(CONFIG)

while True:
    try:
        exec(CLEAR)
        print(START)
        date = datetime.datetime.now()
        print(date.strftime(CLOCK_FORMAT))
        print(END)
        time.sleep(0.1)
    except KeyboardInterrupt:
        break

