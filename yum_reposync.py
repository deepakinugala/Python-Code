import os
import subprocess
updates = "reposync -g -l -d -m --repoid=updates --download-metadata --download_path=/var/www/html/repos/"
base = "reposync -g -l -d -m --repoid=base --download-metadata --download_path=/var/www/html/repos/"
epel = "reposync -g -l -d -m --repoid=epel --download-metadata --download_path=/var/www/html/repos/"
extras = "reposync -g -l -d -m --repoid=extras --download-metadata --download_path=/var/www/html/repos/"
centosplus = "reposync -g -l -d -m --repoid=centosplus --download-metadata --download_path=/var/www/html/repos/"
dockerstable = "reposync -g -l -d -m --repoid=docker-ce-stable --download-metadata --download_path=/var/www/html/repos/"

base_execute = subprocess.Popen(base, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
base_execute.wait()

if base_execute.returncode == 0:
    print("base: success")
else:
    print("base: failed")

updates_execute = subprocess.Popen(updates, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
updates_execute.wait()


if updates_execute.returncode == 0:
    print("updates: success")
else:
    print("updates: failed")