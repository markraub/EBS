import re
import time

def init():

    path = ""

    email = ""

    outlog = ""

    tolerance = 15

    for lines in open("/opt/EBS/EBS.conf"):

        line_array = lines.split()

        if len(line_array) > 0:

            if "path" in line_array[0]:

                path = line_array[2]

            elif "out_log" in line_array[0]:

                outlog = line_array[2]

            elif "email" in line_array[0]:

                email = line_array[2]

            elif "tolerance" in line_array[0]:

                tolerance = int(line_array[2])

    main(path, email, outlog, tolerance)


def DictCompile():
    
    new_dict = {}

    for line in open("/opt/EBS/searchterms"):

        line_array = line.split()
        
        if len(line_array) > 0:
            new_dict[line_array[0]] = int(line_array[1])

    return new_dict

def DictOut(search_dict):

    new_search_dict = ""

    data_file = open("/etc/EBS/searchterms", "ra")

    for line in file:

        line_array = line.split()

        if line_array[0] in search_dict:

            int(line_array[1]) += search_dict[line_array[0]
            print(line_array)
            new_search_dict += (line_array[0] + " " + str(line_array[1]) + "\n")
    
    data_file.write(new_search_dict)
    data_file.close()
    print("wrote dictionary to file")


def FindIPS(logfile, search_dict):

    IP_REGEX = "\\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\b"
    
    new_search_dict = ""

    p = re.compile(IP_REGEX)

    data_file = open("/etc/EBS/searchterms", "ra")
    
    for line in open(logfile):

        m = p.search(line)

        if m is not None:

            if m.group in search_dict:

                search_dict[m.group()] += 1

            elif m.group() not in search_dict:

                search_dict[m.group()] = 1
                new_search_dict += m.group() + " " + str(1) + "\n"

    data_file.write(new_serch_dict)
    data_file.close()

    return search_dict
    

def main(path, email, outlog, tolerance):

    print(path)

    startTime = time.time()

    search_dict = DictCompile()

    for items in search_dict:

        p = re.compile(items)

        for line in open(path):

            m = p.search(line)

            if m is not None:

                if m.group() in search_dict:

                    search_dict[m.group()] += 1

                elif m.group() not in search_dict:

                    search_dict[m.group()] = 1

    search_dict = FindIPS(path, search_dict)

    for each in search_dict:

        if search_dict[each] != 0:

            print(str(each) + " was found " + str(search_dict[each]) + " times")

            if search_dict[each] >= tolerance:

                Notify_Of_Brute(email)

                break

    print("Calculation time: " + str(time.time()-startTime))


def Notify_Of_Brute(email):

    print(email + " has been notified!")

if __name__ == "__main__":

    init()




