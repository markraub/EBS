import re
import time
import sqlite3


class Result:

    c = sqlite3.connect("/opt/EBS/EBS_Results.db")
    conn = c.cursor()

    def __init__(self, term):

        self.term = term
        self.stamp = time.time()
    

    
    def writeToDB(self, table):    
        
        #print("writing to db: ")

        Result.conn.execute("INSERT INTO " + table + " values (?, ?)", (self.term, str(self.stamp)))

        Result.c.commit()

    def closeDB(self):

        #print("closing db")

        Result.c.commit()

        Result.c.close()

    def printDB(self):

        #print("printing db")

        tables = ["ipv4", "ipv6", "hostname", "phrase"]
        
        for each in tables:

            print(each)

            for row in Result.conn.execute("SELECT * FROM " + each + " ORDER BY stamp"):

                print(row)

    def getCount(self):

        #print("showing count")

        for row in Result.conn.execute("select term, count(term) from results group by term"):
        #    print("cest")
            print(row)


#parsing the configuration file for the necessary configuration
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

#compiles the searchterms file into a dictionary
def DictCompile():
    
    new_dict = []

    for line in open("/opt/EBS/searchterms"):

        line = line.strip()
        
        new_dict.append(line)

    return new_dict


#searches through the logs of your spam filter for IPv4 addresses
def FindIPv4(logfile):

    IP_REGEX = "^([0-9]{1,3}\.){3}[0-9]{1,3}(\/([0-9]|[1-2][0-9]|3[0-2]))?$"
    
    new_search_dict = []

    p = re.compile(IP_REGEX)
    
    for line in open(logfile):

        m = p.search(line)

        if m is not None:

            new_search_dict.append(m.group())    

    print("ipv4 results: " + str(new_search_dict))

    return new_search_dict

def FindPhrase(logfile, search_dict):

    new_search_dict = []

    for items in search_dict:

        p = re.compile(items)

        for line in open(logfile):

            m = p.search(line)

            if m is not None and m.group() is not "":

                new_search_dict.append(m.group())

    print("phrase results: " + str(new_search_dict))

    
    return new_search_dict

def FindHostname(logfile):

    #REGEX = "^(([a-zA-Z]|[a-zA-Z][a-zA-Z\-]*[a-zA-Z])\.)*([A-Za-z]|[A-Za-z][A-Za-z\-]*[A-Za-z])$"

    REGEX = "^(([a-zA-Z]|[a-zA-Z][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z]|[A-Za-z][A-Za-z0-9\-]*[A-Za-z0-9])$"

    new_search_dict = []

    p = re.compile(REGEX)

    for line in open(logfile):

        m = p.search(line)

        if m is not None and "." in m.group():

            new_search_dict.append(m.group())

    print("hostname results: " + str(new_search_dict))


    return new_search_dict

def FindIPv6(logfile):

    REGEX = "(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))"

    new_search_dict = []

    p = re.compile(REGEX)

    for line in open(logfile):

        m = p.search(line)

        if m is not None:

            new_search_dict.append(m.group())

    print("ipv6 results: " + str(new_search_dict))

    return new_search_dict

#does the initial search for all the searchterms in your dictionary
def main(path, email, outlog, tolerance):

    #print(path)

    startTime = time.time()

    master = Result(None)

    for each in FindPhrase(path, DictCompile()):

        new_entry = Result(each)
        new_entry.writeToDB("phrase")

    for each in FindIPv4(path):

        new_entry = Result(each)
        new_entry.writeToDB("ipv4")

    for each in FindHostname(path):

        new_entry = Result(each)
        new_entry.writeToDB("hostname")

    for each in FindIPv6(path):

        new_entry = Result(each)
        new_entry.writeToDB("ipv6")
    
    #master.printDB()

    #master.getCount()

    master.closeDB

    
    print("Calculation time: " + str(time.time()-startTime))

#sends an email to the given administrator email
def Notify_Of_Brute(email):

    print(email + " has been notified!")

if __name__ == "__main__":

    init()




