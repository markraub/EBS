
import os, sys
    

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
    #print("adding path to conf...")
    #if path != "":

    #    os.system("echo \"path=" + path + "\" >> ./EBS.conf")

    os.system("cp ./EBS.py /opt/EBS/")
    print("cp ./EBS.py /opt/EBS/")
    print("copying files...")
    os.system("touch /opt/EBS/ebs-cron.sh")
    os.system("touch /opt/EBS/out.log")
    print("assembling shell script...")
    os.system("echo \"sudo python /opt/EBS/EBS.py\" >> /opt/EBS/ebs-cron.sh")
    print("making cron job...")
    makeCron()
    print("jobs done!")

def makeCron():

    cronjob = "00 * * * * /opt/EBS/ebs-cron.sh"
    try:
        os.system("crontab -l | { cat; echo \"" + cronjob + "\"; } | crontab -")
    except:
        os.system("crontab -e")
        os.system("crontab -l | { cat; echo \"" + cronjob + "\"; } | crontab -")

if __name__ == "__main__":


    
    try:

        import pip

    except:

        os.system("sudo apt-get install python-pip -y")
        import pip

    try:

        import crontab as ct

    except:

        pip.main(['install', 'crontab'])
        import crontab as ct




    main()






