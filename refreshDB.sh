#!/bin/bash

rm /opt/EBS/EBS_Results.db

touch /opt/EBS/EBS_Results.db

echo "import sqlite3
conn = sqlite3.connect(\"/opt/EBS/EBS_Results.db\") 
c = conn.cursor()
c.execute(\"create ipv4 results (term, stamp)\")
c.execute(\"create ipv6 results (term, stamp)\")
c.execute(\"create hostname results (term, stamp)\")
c.execute(\"create phrase results (term, stamp)\")
conn.commit()
conn.close()" | python



