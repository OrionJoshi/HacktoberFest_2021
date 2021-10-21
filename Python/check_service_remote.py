'''
This script can be used to check if a service is running on a remote Linux
server with hostname, username, password, service name
'''

import paramiko  # pip install paramiko
import re


def commandExec(hostname, username, password, service):

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    command = f"systemctl status {service}"

    try:
        client.connect(hostname=hostname, port=22,
                       username=username, password=password)
        stdin, stdout, stderr = client.exec_command(command)

        output = stdout.read().decode()

        pattern = r"running"
        match = re.search(pattern, output)

        if match:
            print("\nThe service is running!")
        else:
            print("\nWhoops! The service is not running.")

    except:
        print("Could not connect to the Server!")
