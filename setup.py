
import os, sys
try:
    import pip
except:
    os.system("sudo apt-get install python-pip -y")
    import pip

try: 
    from crontab import CronTab
except:
    pip.main(['install', 'crontab'])
    from crontab import CronTab

def main(path):


    os.system("mkdir /opt/EBS/")
    print("making directory...")
    os.system("adduser EBS")
    print("creating user and group...")
    os.system("groupadd EBS")
    os.system("usermod -aG EBS EBS")
    os.system("chown -R EBS:EBS /opt/EBS")
    print("setting file permissions"...)
    os.system("cp ./EBS.conf /opt/EBS/")
    print("adding path to conf...")
    if path != "":

        os.system("echo \"path=" + path + "\" >> ./EBS.conf")

    os.system("cp ./EBS.py /opt/EBS/")
    print("cp ./EBS.py /opt/EBS/")
    print("copying files...")
    os.system("touch /opt/EBS/ebs-cron.sh")
    print("assembling shell script...")
    os.system("echo \"sudo python /opt/EBS/EBS.py\" >> /opt/EBS/ebs-cron.sh")
    print("making cron job"...)
    makeCron()
    print("jobs done!")

def makeCron():

    cron = CronTab(user="EBS")

    job = cron.new(command="/opt/EBS/ebs-cron.sh", comment="EBS Spam Ownage Monitor")
    job.hour.every(1)
    job.enable()


if __name__ == "__main__":

    path = input("Enter the path to your spam filter log file [leave blank to configure in EBS.conf]")

    
    try:

        import pip

    except:

        os.system("sudo apt-get install python-pip -y")
        import pip

    try:

        from crontab import CronTab

    except:

        pip.main(['install', 'crontab'])
        from crontab import CronTab

    main(path)






