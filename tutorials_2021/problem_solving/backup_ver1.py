#Sample program to make backup of files from source directory to target ditectory

import os
import time

source= ['/home/sky/working_dir/python3/tutorials/Basics']
target_dir ='/home/sky/working_dir/python3/tutorials/backup'


#The name of the zip archive is the current date and time .zip
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%s')+'.zip'

#create target directory if not present

if not os.path.exists(target_dir):
    os.mkdir(target_dir) #make directory

#We use the zip command to put the files in a zip archive

zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

#Run the backup
print('Zip command is:',zip_command)

print('Running:')

if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup Failed')


