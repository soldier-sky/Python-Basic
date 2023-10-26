import subprocess
import os
# print list of files in / directory
# using subprocess.call

print('List of directory in / dir\n')
subprocess.call(['ls', '/', ' -la'])

cwd=os.getcwd()
print('List of directoy in cwd', cwd)
subprocess.call('ls -la' ,shell=True)



# Using subprocess.check_call() to get status of subprocess i.e. error code
err_code=subprocess.check_call('echo sunil', shell=True)
print('Error code of above command is', err_code)


# Using subprocess.check_output()
output= subprocess.check_output(['ls', '-la'])
print(output)
