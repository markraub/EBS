
import os, sys
try:
    import pip
except:
    os.system("sudo apt-get install python-pip")

try: 
    from crontab import CronTab
except:
    pip.main(['install', crontab])
    from crontab import CronTab

def main(verbosity, terms, level, path):

    if verbosity:

        os.system("mkdir /opt/EBS/")
        print("mkdir /opt/EBS/")
        os.system("cp ./EBS.py /opt/EBS/")
        print("cp ./EBS.py /opt/EBS/")
        os.system("touch /opt/EBS/ebs-cron.sh")
        print("touch /opt/EBS/ebs-cron.sh")
        os.system("touch /opt/EBS/spamDict.txt")
        print("touch /opt/EBS/spamDict.txt")
        for each in terms:

            os.system("echo \"" + str(each) + " \n\" >> /opt/EBS/spamDict.txt " )
            print("Added " + each + " to the spam dictionary")

        os.system("echo \"sudo python3 /opt/EBS/EBS.py " + str(level) + " " + str(path))
        print("echo \"sudo python3 /opt/EBS/EBS.py " + str(level) + " " + str(path))
        print("making cron job")
        makeCron()


    else:

        os.system("mkdir /opt/EBS/")
        os.system("cp ./EBS.py /opt/EBS/")
        os.system("touch /opt/EBS/ebs-cron.sh")
        os.system("touch /opt/EBS/spamDict.txt")
        for each in terms:
            os.system("echo \"" + str(each) + " \n\" >> /opt/EBS/spamDict.txt ")

        os.system("echo \"sudo python3 /opt/EBS/EBS.py " + str(level) + " " + str(path))

        makeCron()



def makeCron():

    cron = CronTab()

    job = cron.new(command="/opt/EBS/ebs-cron.sh", comment="EBS Spam Ownage Monitor")
    job.hour.every(1)
    job.enable()


def AddSearchTerms(index, args):

    term_lst = []

    for each in range(index, len(args)-1):

        if "[" in args[each]:

            term_lst.append(args[each][1:len(args[each])-2])

            for items in range(each + 1, len(args)-1):

                if "]" in args[items]:

                    term_lst.append(args[items][0:len(args[items])-2])

                    return term_lst

                elif "-" in args[items]:

                    sys.exit("search term error, make sure to enclose your search terms in brackets and use commas")

                term_lst.append(args[items])


if __name__ == "__main__":




    args = sys.argv

    verbosity = False

    terms = ["Blocked", "SPAM", "spam", "quarentine", "QUARENTINE", "BLOCKED", "Quarentined", "quarentined"]

    level = 15

    path = ""

    appendval = False

    if "-p" not in args or "--log-path" not in args:

        sys.exit("You need to enter a path")

    for each in range(1, len(args)-1):

        if args[each] == "-v" or args[each] == "--verbose":

            verbosity = True

        elif args[each] == "-a" or args [each] == "--append-terms":

            appendval = True

        elif args[each] == "-t" or "--search-terms":

            for stuff in args:

                if stuff == "-a" or "--append-terms":

                    appendval = True

            if appendval:

                templst = AddSearchTerms(each, args)

                for items in templst:

                    terms.append(items)

                each += len(templst)

            else:

                terms = AddSearchTerms(each, args)

                each += len(terms)

        elif args[each] == " -l" or args[each] == "--set-level":

            level = int(args[each+1])

        elif args[each] == "-p" or args[each] == "--log-path":

            path = args[each+1]

        else:

            sys.exit("Error, please check your arguments")





