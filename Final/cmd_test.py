import subprocess
#subprocess.check_output(['ls','-l']) #all that is technically needed...
subprocess.call(['ls'])

#To Run as administrator use:
#subprocess.call(['runas', '/user:Administrator', SERVER_TASK_SCHEDULE THING])

#Processes to run:
#* schtasks /Change /TN SERVER_TASK_NAME /DISABLE
#* schtasks /Change /TN SERVER_TASK_NAME /ENABLE
#* schtasks /Run /TN SERVER_TASK_NAME
