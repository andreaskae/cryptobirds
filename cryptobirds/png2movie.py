# CryptoBirds "A Birds Eye View of Crypto Currencies"
# part5 - movie generator - png2movie.py
#
# v08 (c) 2014, 2015 by Andreas

"""
# start manually with 
python -u ./png2movie.py > ./png2movie.log 2>&1 &
sleep 1
tail -f -n 15 ./png2movie.log 
# Ctrl-C to stop logfile viewing
"""

import os, fnmatch
from moviepy.editor import ImageSequenceClip
# pip install moviepy
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
    
    videofilename = "video__" + filenames[0] + "_TO_" + filenames[-1] + "__.mp4"
    if debug: print videofilename 
    
    return filenames, videofilename  


def makeMovie(fromDirectory=".", filenamepattern = FILENAMEPATTERN, 
              fps=2, debug = True, **args):
      
    filenames, videofilename = getFilenames(fromDirectory, filenamepattern, debug)
    
    if debug: print "generating movie, may take a while, patience!"    
    try:
        cl = ImageSequenceClip(filenames, fps=fps)
        cl.write_videofile(videofilename, **args)   
    except Exception as e:
        print "Video NOT generated. Exception: %s" % e


def printIdea():
    print
    print "What about this:"
    print "Part 1: get the coinmarketcap data"
    print "Part 2: store it into db for later analysis"
    print "part 3: Generate PNG image, available on server 1"
    print "part 4: download PNG (to machine 2), every 5 minutes"
    print "part 5: make movie from all PNG in folder"
    print "part 6: varieties: ... all PNG of the past 24 hours only; generate one every 1 (6) hours?"
    print "part 7: youtube uploader, insert newest youtube URL into webpage on server 1"
    print "part 8: Not to forget: donation button, or subscription service. Easy. "
    print "parts 1,3,4,5 are ready!\n"

if __name__ == "__main__":
    printIdea()
    makeMovie(fps=2, write_logfile=True)
    printIdea()
    