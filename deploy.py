#! /usr/bin/python

import os
import sys

if __name__ == "__main__":
    SERVER_IP, PORT, PASSWORD = sys.argv[1:4]

    os.system("cp init_scripts/sslocal /etc/init.d/sslocal")
    os.system("cp init_scripts/ssserver /etc/init.d/ssserver")

    for file in ["local.json", "server.json"]:
        with open("configs/{0}".format(file), "r") as f:
            content = f.read()
        with open("/etc/{0}".format(file), "w") as f:
            f.write(content.replace("{{SERVER_IP}}", SERVER_IP).replace("{{PORT}}", PORT).replace("{{PASSWORD}}", PASSWORD))
    print("Success!")
