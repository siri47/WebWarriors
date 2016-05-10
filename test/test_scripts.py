import sys
import urllib2
import time


def write_to_db(file_path, count):

    with open(file_path, "r") as file:
        lines = file.readlines()

    for row in lines:
        data = row.split(',')
        url = data[0] + "?count=" + str(count)
        platform = data[1].strip("\n")
        print "\n*********** stats for %s ***************\n" % platform
        start = time.time()
        conn = urllib2.urlopen(url)
        end = time.time()
        if conn.getcode() == 200:
            print "time taken to write %d values = %d seconds\n" % (count, end - start)
        else:
            print "server did not send 200 response!\n"


def read_from_db(file_path):

    with open(file_path, "r") as file:
        lines = file.readlines()

    for row in lines:
        data = row.split(',')
        url = data[0]
        platform = data[1].strip("\n")
        print "\n*********** stats for %s ***************\n" % platform
        start = time.time()
        conn = urllib2.urlopen(url)
        data = conn.read()
        end = time.time()
        if conn.getcode() == 200:
            print "time taken to read values = %d seconds\n" % (end - start)
        else:
            print "server did not send 200 response!\n"






if __name__ == "__main__":
    argc = len(sys.argv)
    if argc < 3 or argc > 4:
        print "usage: %s action(0/1) file_path [count - only for write]" % (sys.argv[0])
        exit(0)
    try:
        action = int(sys.argv[1])
        if argc == 4:
          count = int(sys.argv[3])
    except:
        print "integer expected for action [and count]!"
        exit(0)
    file_path = sys.argv[2]
    if action == 1:
        write_to_db(file_path, count)
    else:
        read_from_db(file_path)
