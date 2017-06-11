import os, sqlite3


os.system("rm /opt/EBS/EBS_Results.db")

os.system("touch /opt/EBS/EBS_Results.db")

import sqlite3
conn = sqlite3.connect("/opt/EBS/EBS_Results.db") 
c = conn.cursor()
c.execute("create table ipv4 (term, stamp)")
c.execute("create table ipv6 (term, stamp)")
c.execute("create table hostname (term, stamp)")
c.execute("create table phrase (term, stamp)")
conn.commit()
conn.close()
