import requests
import os
import time
import sys

baseurl = str("http://" + "localhost" + ":" + "5000" + "/" )
delay = 30 # time in seconds between each loop
max_fails = 5 # maximum amount of failures before aborting

current_fails = 0

def main_loop():
    print "Connecting to " + baseurl
    while 1:
        keepalive(baseurl)
        print "Retrying in " + str(delay) + " seconds..."
        time.sleep(delay)

def keepalive(url):
    try:
        alive = requests.get(url)
        if alive.status_code == 200:
            print "Web service connection looks good"
        else:
            print "Received status code " + str(alive.status_code) + "when connecting to" + url
    except requests.exceptions.RequestException:
        print "Failed to establish connection!"
        global current_fails
        current_fails += 1
        if current_fails >= max_fails:
            print "Reached maximum number of failures! Aborting"
            sys.exit(1)



if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print >> sys.stderr, '\nExiting by user request.\n'
        sys.exit(0)
