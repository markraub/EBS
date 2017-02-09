import re
import time

def init(config):

    spamDict = {}

    NumbOfSpams = 0

    AddFlag = False

    for line in open(config):

        if "ADD" in line:

            AddFlag = True

            continue

        elif "END" in line:

            AddFlag = False

        elif AddFlag:

            spamDict[line.strip()] = 0

        elif "NUMBER" in line:

            NumbOfSpams = line.split()[1]

        elif "LOGPATH" in line:

            LogPath = line.split()[1]

    return spamDict, NumbOfSpams, LogPath


def main():

    startTime = time.time()

    spamDict, Notify, LogPath = init("config.txt")

    print(spamDict)
    print(Notify)
    print(LogPath)

    for items in spamDict:

        p = re.compile(items)

        for line in open(LogPath + "*.txt"):

            m = p.search(line)

            if m is not None:

                if m.group() in spamDict:

                    spamDict[m.group()] += 1

                elif m.group() not in spamDict:

                    spamDict[m.group()] = 1

    for each in spamDict:

        if spamDict[each] != 0:

            print(str(each) + " was found " + str(spamDict[each]) + " times")

            if spamDict[each] >= Notify:

                Notify_Of_Brute()

                break

    print("End time: " + str(time.time()-startTime))


def Notify_Of_Brute():

    print("RTP has been notified!")

if __name__ == "__main__":

    main()