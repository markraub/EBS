import re
import time


def init():

    path = ""

    email = ""

    outlog = ""

    for lines in file("/opt/EBS/EBS.conf"):

        line_array = lines.split()

        if "path" in line_array[0]:

            path = line_array[2]

        elif "out_log" in line_array[0]:

            outlog = line_array[2]

        elif "email" in line_array[0]:

            email = line_array[2]

    main(path, email, outlog)


def DictCompile():
    
    new_dict = {}

    for line in file("/opt/EBS/searchterms"):

        line_array = line.split()

        new_dict[line_array[0]] = line_array[1]

    return new_dict


def FindIPS(logfile, search_dict):

    IP_REGEX = "\\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\b"
    
    p = re.compile(IP_REGEX)
    
    for line in open(logfile):

        m = p.search(line)

        if m is not None:

            if m.group in search_dict:

                search_dict[m.group()] += 1

            elif m.group() not in search_dict:

                search_dict[m.group()] = 1

    return search_dict
    

def main(path, email, outlog):

    startTime = time.time()

    search_dict = DictCompile()

    for items in search_dict:

        p = re.compile(items)

        for line in open(path):

            m = p.search(line)

            if m is not None:

                if m.group() in spamDict:

                    spamDict[m.group()] += 1

                elif m.group() not in spamDict:

                    spamDict[m.group()] = 1

    search_dict = FindIPS(path, search_dict)

    for each in spamDict:

        if spamDict[each] != 0:

            print(str(each) + " was found " + str(spamDict[each]) + " times")

            if spamDict[each] >= Notify:

                Notify_Of_Brute(email)

                break

    print("Calculation time: " + str(time.time()-startTime))


def Notify_Of_Brute(email):

    print(email + " has been notified!")

if __name__ == "__main__":

    init()




