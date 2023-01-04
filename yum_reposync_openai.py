import subprocess

repos = ["base", "extras"]
local_directory = "/var/www/html/repos/"

def reposync(repo, local_directory):
    print("Synchronizing repository: {}".format(repo))
    result = subprocess.run(["reposync", "-g", "-l", "-d", "-m", "--download_path={}".format(local_directory), "-r", repo], stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    if result.stderr:
        print("Error synchronizing repository {}: {}".format(repo, result.stderr.decode("utf-8")))

if __name__ == "__main__":
    for repo in repos:
        reposync(repo, local_directory)
