#!/bin/python3
from subprocess import Popen, PIPE, run
import json
import pprint
import os,os.path
import pathlib

Path = pathlib.Path

base_path = "/home/jake_w71753/SecureSoftwareProgramming/project3/logs/"

def getUserAuthTimes(userid):
    """
    Returns a list of the dates of login for user userid from log/auth.log
    """
    with Popen(["grep", userid, base_path + "auth.log"], stdout=PIPE) as proc:
        # Pipe the output of subprocess.Popen() to stdout
        dtl = []
        for line in proc.stdout.readlines():
            bits = line.decode("utf-8").split()
            dt = " ".join(bits[:3])
            dtl.append(dt)
    return list(set(dtl))

#get all user ids that are failed logins with invalid user names. Return a dictionary mapping the userid to the number of invalid attempts
def getInvalidLogins():
    """
    Returns a dictionary mapping invalid user ids to # of failed logins on log/auth.log
    """
    #extractLogFiles("auth", logdir="/home/jake_w71753/logs")
    with Popen(["grep", "invalid", base_path + "auth.log"], stdout=PIPE) as proc:
        # Pipe the output of subprocess.Popen() to stdout
        invals = {}
        for line in proc.stdout.readlines():
            bits = line.decode("utf-8")
            user = bits.split()[8]
            if user in invals.keys():
                invals[user] += 1;
            else:
                invals[user] = 1
    return invals

#extract all gzipped files for a specified file. put them in a combined file
def extractLogFiles(logfile,logdir = "/home/twmoore/log"):
    new_content = ""
    path = Path(logdir)
    for p in list(path.glob(logfile + "*.gz")):
        run(["gunzip", p])
    for p in list(path.glob(logfile + "*")):
        if '.all' in p.as_posix():
            continue
        with Popen(["cat", p], stdout=PIPE) as proc:
            for line in proc.stdout.readlines():
                new_content += line.decode("utf-8")
    
    f = open(logdir + logfile + ".all", "w")
    
    f.write(new_content)
    f.close()
    
    return new_content

    
#find all IP addresses for invalid logins, then see which IPs are also used for scanning
def compareInvalidIPs():
    extractLogFiles("auth", logdir=base_path)
    with Popen(["grep", "Invalid", f"{base_path}auth.all"], stdout=PIPE) as proc:
        # Pipe the output of subprocess.Popen() to stdout
        invals = []
        for line in proc.stdout.readlines():
            bits = line.decode("utf-8")
            if(len(bits.split()) > 9):
                user = bits.split()[9]
            else: 
                user = bits.split()[8]
            if user not in invals:
                invals.append(user)
        
    extractLogFiles("ufw", logdir=base_path)
    fw_ips = []
    i = 1
    with Popen(["grep", "BLOCK", f"{base_path}ufw.all"], stdout=PIPE) as proc:
        lines = proc.stdout.readlines();
        for line in lines:
            ip = [ip for ip in line.decode("utf-8").split(" ") if "SRC=" in ip][0].replace("SRC=", "")
            if ip not in fw_ips:
                fw_ips.append(ip)
            
            i=i+1
    
    same_ips = []
    for ip in fw_ips:
        if ip in invals:            
            same_ips.append(ip)

    return same_ips


if __name__=="__main__":
    print(getUserAuthTimes("tmoore"))
    print(getInvalidLogins())
    print(compareInvalidIPs())
