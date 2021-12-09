import os
  
# environment variable
db_hostname = 'HOSTNAME'
db_name = 'DATABASE'
db_port = 'PORT'
db_user = 'USER'
jenkins_build_number = 'BUILD_NUMBER'
jenkins_job_name = 'JOB_NAME'
print('Database hostname: ' + os.getenv(db_hostname))
print('Database port: ' + os.getenv(db_port))
print('Database name: ' + os.getenv(db_name))
print('Database user: ' + os.getenv(db_user))
print('Jenkins BUILD_NUMBER: ' + os.getenv(jenkins_build_number))
print('Jenkins JOB_NAME: ' + os.getenv(jenkins_job_name))

