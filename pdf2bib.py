import gscholar.gscholar as gs
import os
import fnmatch
import time
import random

def enterfile(pdf, bibfile):
    if os.path.exists(pdf):
        biblist = gs.pdflookup( pdf, all, gs.FORMAT_BIBTEX, None )
    else:
        return -1

    if len(biblist) < 1:
        print "no results found"
        return -2

    # move file and bib info
    d = gs.rename_file( pdf, biblist[0], False )
    # save bib info to file
    with open( bibfile, 'a') as bf:
        bf.write('\n'+d["bib"])

pdfs =[]
dir = '/home/ebert/Dropbox/PapersIn/'
bibfn = os.path.join(dir,'test.bib')
for root, dirnames, filenames in os.walk(dir):
    for filename in fnmatch.filter(filenames, '*.pdf'):
        pdfs.append(os.path.join(root,filename))

print len(pdfs)
for pdf in pdfs:
    print "\n============================="
    print pdf
    enterfile(pdf, bibfn)
    waittime = random.randint(10,20)
    print "time to wait % s..." % waittime
    time.sleep(waittime)
