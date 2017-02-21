
import os, sys, sqlite3
    
#main() will create the directories, users, groups, and move the files that EBS requires to function
def main():

    
    
    os.system("mkdir /opt/EBS/")
    print("making directory...")
    os.system("cp ./EBS.conf /opt/EBS/")
    os.system("cp ./EBS.py /opt/EBS/")
    print("cp ./EBS.py /opt/EBS/")
    print("creating database...")
    os.system("touch /opt/EBS/EBS_Results.db")
    conn = sqlite3.connect("/opt/EBS/EBS_Results.db")
    c = conn.cursor()
    c.execute("create table results (term, stamp)")
    conn.commit()
    conn.close()
    print("copying files...")
    os.system("touch /opt/EBS/ebs-cron.sh")
    os.system("touch /opt/EBS/out.log")
    os.system("cp ./searchterms /opt/EBS/")
    print("making cron job...")
    makeCron()
    print("jobs done!")

#creates the crontjob for the EBS user
def makeCron():

    ebs_cron = CrontTab(user="root")
    job = ebs_cron.new(command="python /opt/EBS/EBS.py")
    job.minute.every(15)
    job.enable()	
	

#when run from cli, this will install the necessary libs
if __name__ == "__main__":
    
    os.system("sudo add-apt-repositort universe -y")
    os.system("sudo apt-get update -y")
    os.system("sudo apt-get install python-pip -y")

    try:

        import pip

    except:

        os.system("sudo apt-get install python-pip -y")
        import pip

    try:

        from crontab import CronTab

    except:

        pip.main(['install', 'python-crontab'])
        from crontab import CronTab




    main()






