# CryptoBirds "A Birds Eye View of Crypto Currencies"
# part 6 - movie generator - png2movie.py
#
# v09 (c) 2014, 2015 by Andreas
#

"""
# start manually with 
python -u ./png2movie.py > ./png2movie.log 2>&1 &
sleep 1
tail -f -n 15 ./png2movie.log 
# Ctrl-C to stop logfile viewing
"""

VIDEOFILENAME = "video__%s_TO_%s__.mp4"
printIdea = True

import os, fnmatch
from moviepy.editor import ImageSequenceClip
# pip install moviepy   # https://pypi.python.org/pypi/moviepy

# first call will take long because stuff is downloaded 

from downloadRepeater import FILENAMETEMPLATE
FILENAMEPATTERN = FILENAMETEMPLATE % "*"

def getFilenames(fromDirectory=".", filenamepattern = FILENAMEPATTERN, debug=True):
    filenames = os.listdir(fromDirectory)
    filenames = [singlefile
                 for singlefile in filenames
                 if fnmatch.fnmatch(singlefile, filenamepattern) ]
    filenames.sort()
    if debug: print filenames
    
    videofilename = VIDEOFILENAME % (filenames[0], filenames[-1])
    if debug: print videofilename 
    
    return filenames, videofilename  


def makeMovie(fromDirectory=".", filenamepattern = FILENAMEPATTERN, 
              fps=2, debug = True, **args):
      
    filenames, videofilename = getFilenames(fromDirectory, filenamepattern, debug)
    
    if debug: print "generating movie, may take a while, patience!\n"    
    try:
        cl = ImageSequenceClip(filenames, fps=fps)
        cl.write_videofile(videofilename, **args)   
    except Exception as e:
        print "Video NOT generated. Exception: %s" % e


def printIdea():
    print "\nIdeas for the next steps:"
    print "Part 1: get the coinmarketcap data"
    print "Part 2: store it into DB for later analysis"
    print "part 3: generate PNG image"
    print "part 4: available for self-service (on server 1)"
    print "part 5: download PNG (to machine 2), every 5 minutes"
    print "part 6: make movie from all PNGs in folder"
    print "part 7: variation: ... all PNGs of the past 24 hours only;" 
    print "                   ... automatically generate video every 4 hours?"
    print "part 8: youtube uploader; newest youtube URL into www, on server 1"
    print "part 9: Not to forget: donation button, subscription service. Easy."
    print "parts 1,3,4,5,6 are ready!\n"

if __name__ == "__main__":
    if printIdea: printIdea()
    makeMovie(fps=5, write_logfile=True)
    if printIdea: printIdea()
    