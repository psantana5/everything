import paramiko

def run_ssh_command(hostname, port, username, password, command):
    try:
        # Create an SSH client instance
        ssh = paramiko.SSHClient()

        # Automatically add the server's host key (this is insecure in production, use with caution)
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the remote server
        ssh.connect(hostname, port=port, username=username, password=password)

        # Execute the command on the remote server
        stdin, stdout, stderr = ssh.exec_command(command)

        # Read the output from the command
        output = stdout.read().decode().strip()

        # Read any error output, if available
        errors = stderr.read().decode().strip()

        # Print the output and errors (if any)
        if output:
            print(f"Output from {command}:")
            print(output)
        if errors:
            print(f"Errors from {command}:")
            print(errors)

        # Close the SSH connection
        ssh.close()

    except paramiko.AuthenticationException:
        print("Authentication failed. Please check your credentials.")
    except paramiko.SSHException as e:
        print(f"Unable to establish SSH connection: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Ask the user for the remote server details
hostname = input("Enter the remote server IP address or hostname: ")
port = 22  # Default SSH port is 22

# Ask the user for their SSH credentials
username = input("Enter your SSH username: ")
password = input("Enter your SSH password: ")

command_to_run = input("Enter the command to execute on the remote server: ")

# Run the SSH command and retrieve the output
run_ssh_command(hostname, port, username, password, command_to_run)
