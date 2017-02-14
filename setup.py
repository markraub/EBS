
import os, sys
    
#main() will create the directories, users, groups, and move the files that EBS requires to function
def main():

    
    os.system("mkdir /opt/EBS/")
    print("making directory...")
    os.system("groupadd EBS")
    print("creating user and group...")
    password = str(hash(os.urandom(256))) + str(hash(os.urandom(32)))
    os.system("useradd -u 3434 -g EBS -p " + password + " EBS")
    os.system("chown -R EBS:EBS /opt/EBS")
    print("setting file permissions...")
    os.system("cp ./EBS.conf /opt/EBS/")
    os.system("cp ./EBS.py /opt/EBS/")
    print("cp ./EBS.py /opt/EBS/")
    print("copying files...")
    os.system("touch /opt/EBS/ebs-cron.sh")
    os.system("touch /opt/EBS/out.log")
    os.system("cp ./searchterms /opt/EBS/")
    print("assembling shell script...")
    os.system("echo \"sudo python /opt/EBS/EBS.py\" >> /opt/EBS/ebs-cron.sh")
    print("making cron job...")
    makeCron()
    print("jobs done!")

#creates the crontjob for the EBS user
def makeCron():

    ebs_cron = CrontTab(user="EBS")
    job = ebs_cron.new(command="python /opt/EBS/EBS.py")
    job.minute.every(15)
    job.enable()	
	

#when run from cli, this will install the necessary libs
if __name__ == "__main__":

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






