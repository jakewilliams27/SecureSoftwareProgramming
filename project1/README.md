
# Assignment
## Task
**Your task in this assignment is to implement several functions whose behavior is specified in the starter code below:**

*p1starter.py*


1. Get all user ids that are failed logins with invalid user names. Return a dictionary mapping the userid to the number of invalid attempts. The objective of the getInvalidLogins() method is to get all user ids that are failed logins due to providing invalid user names. This information is stored in the log/auth.log files. The function should return a dictionary mapping the user id to the number of invalid attempts. 

       def getInvalidLogins():

           """

           Returns a dictionary mapping invalid user ids to # of failed logins on log/auth.log

           """

           return True


2. extract all gzipped files for a specified file. put them in a combined file. The extractLogFiles() method should extract all gzipped files that correspond to the logfile argument provided. For example, if logfile = "auth.log", the method should check for all files located in logdir that are specified: auth.log, auth.log.1, auth.log.x.gz where x is a number. Any that are .gz files should be decompressed. Once complete, all files should be combined to a single file ending in .all (for this example, auth.log.all).

       def extractLogFiles(logfile,logdir = "/home/twmoore/log"):

           return True


3. Find all IP addresses for invalid logins, then see which IPs are also used for scanning. The compareInvalidIPs() method should find all IP addresses that are used for both invalid logins AND are blocked by the firewall. To get the invalid logins, you should use the log/auth.log file. For compareInvalidIPs, you should first extract all gzipped versions of auth.log* (meaning auth.log, auth.log.0, auth.log.1, etc.) using the extractLogFiles() method that you implement. Similarly, you will extract all gzipped versions of ufw.log* using the extractLogFiles() method for firewall logs. You will then compare the IPs found in each version.

       def compareInvalidIPs():

           return True



## Solution
**Here is the output for my solution code when executing the if __name__=="__main__" code branch. Your output should be similar.**

    
<code>twmoore@cloudshell:~$ python3 p1sol.py</code>

<code>['Feb 21 13:29:56', 'Feb 21 13:36:38', 'Feb 21 13:33:56']</code>

<code>{'mysql': 5, 'admin': 17, 'from': 2, 'user': 244, 'ad': 1, 'id': 1, 'tylermoore': 7, 'debian': 3, 'blake': 1, 'me': 1, 'marcela': 1, 'nikhil': 1, 'hb': 1, 'xxx': 1, 'nagios': 2, 'vishal': 1, 'wk': 1, 'jason': 1, 'pi': 13, 'carlos': 1, 'carson': 1, 'carter': 1, 'nathan': 1, 'guest': 3, 'a': 3, 'oracle2': 1, 'support': 5, 'julie': 1, 'new1': 1, 'diana': 1, 'mico': 1, 'konrad': 1, 'hex': 1, 'library': 1, 'jesse': 1, 'print': 1, 'test': 21, 'nick': 1, 'du': 1, 'eric': 1, 'noc': 1, 'student1': 1, 'ajay': 2, 'ajith': 2, 'alarm': 2, 'nikhita': 1, 'tammy': 1, 'noaccess': 1, 'cw': 1, 'py': 1, 'cashier': 2, 'centos': 3, 'central': 2, 'node': 1, 'gns3': 4, 'ossuser': 4, 'ansible': 8, 'ubuntu': 20, 'git': 8, 'www': 5, 'gpadmin': 4, 'db2admin': 2, 'system': 2, 'nova': 1, 'kafka': 3, 'zabbix': 3, 'server': 2, 'testuser': 8, 'postgres': 12, '02': 2, 'tomcat': 5, 'oracle': 21, 'ts3': 3, 'gbase': 2, 'nutanix': 2, 'uat': 1, 'msilva': 1, 'kim': 1, 'gloria': 1, 'nvidia': 20, 'off': 1, 'odoo': 5, 'jeus': 1, 'yf': 1, 'odroid': 1, 'asu': 1, 'office': 1, 'tsm': 1, 'csp': 1, 'cs': 1, 'css': 1, 'courtier': 1, 'oneadmin': 1, 'administrador': 1, 'rust': 1, 'gpu': 12, 'rtx': 4, 'gtx': 4, 'ttt': 1, 'onlime_r': 1, 'oozie': 1, 'sshvpn': 1, 'kathleen': 1, 'stu': 1, 'openadmin': 1, 'openhabian': 1, 'fk': 1, 'cd': 1, 'openproject': 1, 'wkiconsole': 1, 'openstack': 1, 'usuario': 1, 'gituser': 1, 'ec2-user': 2, 'ubnt': 1, 'demo': 2, 'spark': 1, 'jenkins': 6, 'ftpadmin': 1, 'webadmin': 1, 'svn': 2, 'openvpn': 1, 'student': 2, 'weblogic': 2, 'db2inst1': 3, 'fd': 1, 'ernest': 1, 'oper': 1, 'operator': 3, 'rise': 1, 'svnuser': 1, 'seconlab': 7, 'samy': 1, 'chef': 2, 'web': 4, 'sammy': 1, 'etherpad': 1, 'max': 1, 'vincent': 1, 'jaya': 1, 'jack': 1, 'cesar': 1, 'charles': 1, 'chase': 1, 'matlab': 1, 'qq': 1, 'helpdesk': 1, 'lc': 2, 'grid': 1, 'rafi': 1, 'harsh': 1, 'ali': 1, 'station': 1, 'am': 1, 'joe': 1, 'tuan': 1, 'lichen': 1, 'engin': 1, 'oscar': 1, 'test1': 1, 'chimistry': 1, 'osmc': 1, 'ospite': 1, 'temp': 2, 'ftpuser': 5, 'hanbo': 1, 'abc': 1, 'deploy': 3, 'chandra': 1, 'sompong': 1, 'cp': 1, 'carol': 1, 'user1': 5, 'cisco': 3, 'dev': 1, 'tracelab': 1, 'hadoop': 3, 'deployer': 1, 'uftp': 2, 'lenovo': 2, 'testa': 1, 'ljw': 1, 'vpn': 1, 'zsy': 1, 'lgh': 1, 'radio': 1, 'fuser': 1, 'public': 1, 'odoo12': 1, 'steam': 1, 'splunk': 1, 'musicbot': 1, 'jboss': 1, 'es': 2, 'docker': 1, 'chia': 1, 'kubeadm': 1, 'apache': 1, 'csgo': 2, 'csgoserver': 2, 'minecraft': 5, 'mc': 2, 'mcserver': 2, '1': 1, 'azureuser': 1, 'csserver': 1, 'cssserver': 1, 'ctrls': 2, 'lzt': 1, 'terminal': 1, 'info': 1, 'alex': 2, 'verdaccio': 1, 'sftpuser': 1, 'ddos': 1, 'theo': 1, 'joseph': 1, 'auger': 1, 'bitrix': 1, 'scan': 1, 'tr': 1, 'test6': 1, 'admin1': 1, 'christian': 1, 'christopher': 1, 'cmsuser': 1, 'aurora': 1, 'shop': 1, 'lmt': 1, 'sander': 1, 'init': 1, 'tam': 1, 'salim': 1, 'nfsnobod': 1, 'ftpdata': 1, 'pan': 1, 'walter': 1, 'gitlab-runner': 1, 'Cisco': 1, 'ckl': 1, 'jamil': 1, 'satis': 1, 'olga': 1, 'manager': 1, 'otrs': 1, 'roger': 1, 'pac': 1, 'pappajack': 1, 'paul': 1, 'pdv': 1, 'rookie': 1, 'wj': 1, 'pentaho': 1, 'rajesh': 1, 'thomas': 1, 'petar': 1, 'clfs': 1, 'client': 1, 'cliente1': 1, 'satish': 1, 'kt': 1, 'alexander': 1, 'alfresco': 1, 'alien': 1, 'sheller': 1, 'sometimes': 1, 'plex': 2, 'lu': 1, 'olivier': 1, 'chrome': 1, 'abuse': 1, 'dstserver': 1, 'kevin': 1, 'rancher': 1, 'katrina': 1, 'nano': 1, 'cubie': 1, 'cyrus': 1, 'upload': 1, 'avorion': 1, 'nmrsu': 1, 'ppp': 1, 'cliente': 1, 'cloud-user': 1, 'cms': 1, 'prakash': 1, 'admin3': 1, 'external': 1, 'credito': 1, 'felipe': 1, 'virtual': 1, 'press': 1, 'prios': 1, 'prod': 1, 'ma': 1, 'product': 1, 'damian': 1, 'pemp': 1, 'teacher': 1, 'user03': 1, 'toni': 1, 'william': 1, 'transfer': 1, 'ftpuser1': 1, 'downloader': 1, 'tomek': 1, 'dmdba': 1, 'andy': 1, 'venus': 1, 'jeffrey': 1, 'ds': 1, 'tutor': 1, 'ekp': 1, 'program': 1, 'yyy': 1, 'john': 1, 'gc': 1, 'hive': 1, 'user2': 2, 'testing': 1, 'jira': 1, 'prueba': 3, 'vyos': 1, 'sdbadmin': 1, 'michael': 1, 'tom': 1, 'tracerlab': 1, 'wpuser': 1, 'mos': 1, 'huawei': 1, 'minerstat': 1, 'cmsftp': 1, 'cod4server': 1, 'colton': 1, 'prueba1': 1}</code>

<code>{'64.62.197.32', '198.98.49.221', '65.49.20.69', '179.43.159.3', '64.62.197.122', '129.244.0.252', '45.125.65.126', '178.73.215.171', '45.9.20.25', '45.153.160.139', '141.98.10.206', '65.49.20.68', '141.98.10.81', '64.62.197.182', '164.90.156.240', '179.43.187.173', '164.90.227.119', '104.248.168.145', '95.111.235.212', '65.49.20.66', '139.135.229.24', '2.57.122.107', '64.62.197.2', '31.7.57.130', '64.62.197.62', '67.205.138.198', '81.17.24.154', '179.43.159.4', '179.43.170.170', '106.12.222.80', '141.98.10.179', '107.189.31.191', '165.22.85.106', '67.205.162.21', '141.98.11.23', '147.182.244.135', '65.49.20.67', '157.230.108.36', '43.154.1.155', '179.43.170.172', '206.81.30.225', '43.154.40.120', '179.43.139.10', '142.93.48.117', '167.71.79.19', '141.98.10.202', '141.98.11.22', '43.154.1.130', '45.9.20.73', '116.172.130.197', '64.62.197.212', '188.166.255.101', '128.199.13.112', '198.98.51.76'}{'141.98.11.23', '45.9.20.73', '64.62.197.182', '45.125.65.126', '64.62.197.62', '81.17.24.154', '116.172.130.197', '141.98.11.22', '179.43.187.173', '45.9.20.25', '141.98.10.81'}</code>


