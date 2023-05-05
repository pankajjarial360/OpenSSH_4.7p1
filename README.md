# OpenSSH_4.7p1 CVE-2008-5161.
OpenSSH 4.7p1 Debian 8ubuntu1 (protocol 2.0) exploit 

# Exploit description 

This is a Python script for exploiting an SSH server running OpenSSH version 4.7p1 on a remote target. The script uses the Metasploit Framework to launch a brute-force attack against the target's SSH service and attempts to log in using a list of usernames and passwords from a wordlist file.

The script starts by connecting to the target's SSH service and checking the version number to confirm that it is vulnerable to the exploit. If the version number is correct, the script proceeds to run the Metasploit Framework console and sets up the necessary parameters for the brute-force attack. The script then launches the exploit and waits for it to complete.

Once the exploit is completed, the script retrieves and displays any active sessions that have been created. It then enters an interactive mode that allows the user to interact with any active session.

To use this script, the user must have the Metasploit Framework installed and configured on their system. The script can be run from the command line and requires the IP address of the target SSH server to be specified as a command-line argument.

## Requirement to run  this Exploit
Step up your lab which have a vesion OpenSSH_4.7p1

### In my case I am running Metasploitable2 
![image](https://user-images.githubusercontent.com/87800233/236505619-3c582808-7779-46b7-a53d-f29a63252599.png)
### Check your Target IP 
![image](https://user-images.githubusercontent.com/87800233/236505969-071ffac6-b657-4608-98a6-5c68493e5abc.png)
### In my case Its:-> 192.168.1.5
![image](https://user-images.githubusercontent.com/87800233/236506215-38dd8485-2a15-48b0-8e4b-e7370ca50373.png)
### Install pwntools ( because code use pwn library)
![image](https://user-images.githubusercontent.com/87800233/236504633-62627c10-88c5-4ef3-8ed4-d2746e12daf6.png)

## Download or Clone the Repository in your local machine 
![image](https://user-images.githubusercontent.com/87800233/236511955-b5b4b1c6-2325-47b0-8a23-b16e6e43c129.png)

## Move to exploit Directory and gave the execute permission to exploit 
![image](https://user-images.githubusercontent.com/87800233/236512436-0b172f2d-c45e-40bc-a2e3-b20c0e9bc18a.png)

### After all the setup, Now run the Exploit by gaving the Target IP

https://user-images.githubusercontent.com/87800233/236513807-b97fb778-aef0-4872-8878-e33b705c4b7b.mp4

### And here We Are In ( For The Win) and  get The InterActive shell.
