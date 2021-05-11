## Usage

import subprocess
import time
import os
# will delete all files in folder before cloning to prevent errors
print('Removing Directory to update')
os.system('RMDIR /S /Q Crypto_Data_File')
time.sleep(10)
print('\n gathering new data from github \n')
#Will download a copy of the current crypto data to folder Crypto_Data
subprocess.call(['git', 'clone', '--branch','main',
    'https://github.com/Mackenzie1215/Crypto','Crypto_Data_File'])