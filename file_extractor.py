#!/usr/bin/python

import shutil
import argparse

def failed():
    print "Too few arguments"
    exit(1)

def copyFiles(srcPath, dstPath, fileList):
    for file in fileList:
        shutil.copy( ("%s/%s" % (srcPath, file)), dstPath )
    return 0

def getFileNames(filePath):
    with open(filePath) as fd:
        files = [line.rstrip('\n') for line in open(filePath)]
    return files

def main(args):

    if args.mnt:
        mountpath = args.mnt
    else:
        failed()
    if args.blobs:
        propFile = args.blobs
    else:
        failed()
    if args.vendor:
        vendorFile = args.vendor
    else:
        failed()
    if args.dest:
        destPath = args.dest
    else:
        destPath = "/tmp/"

    filesList = getFileNames(propFile)
    status = copyFiles(mountpath, destPath, filesList)

    if status != 0:
        print "Copy failed, please check for errors"
        exit(1)

def init():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mnt", help="Mount path for the factory image")
    parser.add_argument("-b", "--blobs", help="Path to proprietary-blobs.txt")
    parser.add_argument("-v", "--vendor", help="Path to vendor_owner_info.txt")
    parser.add_argument("-d", "--dest", help="Path to destination for files")
    args = parser.parse_args()
    main(args)

if __name__ =='__main__':
    init()
