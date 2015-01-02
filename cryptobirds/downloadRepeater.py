# CryptoBirds "A Birds Eye View of Crypto Currencies"
# part 5 - image downloader - downloadRepeater.py
#
# v09 (c) 2014, 2015 by Andreas
#

"""
# run in background with
python -u ./downloadRepeater.py > ./downloadRepeater.log 2>&1 &
sleep 1
tail -f ./downloadRepeater.log
# Ctrl-C to stop logfile viewing
"""

URLPNG = "http://104.131.30.126/current.png"
PAUSEBETWEEN = 300
FILENAMETEMPLATE = "AndersBrun_%s.png"

import time, shutil
import wget
# pip install wget    # https://pypi.python.org/pypi/wget

def getEm(url = URLPNG, pauseBetween = PAUSEBETWEEN, debug = True):

    if debug: print "Querying %s every %d seconds:" % (url, pauseBetween)
    
    while True:
        timestamp = time.strftime("%Y%m%d_%H%M%S", time.gmtime())
        
        try:
            filename = wget.download(url)
            newName= FILENAMETEMPLATE % timestamp
            shutil.move(filename, newName)
            if debug: 
                print "downloaded image, and renamed to ",
                print "%s ... now waiting another %d seconds..." % (newName, pauseBetween)
        except Exception as e:
            if debug: print "exception (%s): %s" % (timestamp, e)
            
        time.sleep(pauseBetween )
        
    # N.B.: Will never stop, kill manually.
    
if __name__ == "__main__":
    getEm()
