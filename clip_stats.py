#!/usr/bin/python

import sys, os

'''
python clip_stat.py /clip_directory/
WAVs only
output : Found 3 files, 1.08 MB, 0.01 hours
'''

file_count = 0
total_size = 0
total_duration = 0

def runScript():
    global file_count, total_size, total_duration
    dir = sys.argv[-1]
    split_ext = os.path.splitext(dir)
    for root_dir, subdir_list, file_list in os.walk(dir):
        for file_name in file_list:
            #print(file_name)
            if os.path.splitext(file_name)[1].lower() == '.wav':
                full_path = os.path.join(root_dir, file_name)
                checkFile(full_path)
    # Print final total without carriage return
    print("Found {0} files, {1:.2f} MB, {2:.2f} hours".format(file_count, total_size, (total_duration / 60 / 60)))

def getDuration(file_path):

    file_size = os.path.getsize(file_path)
    return file_size / (2 * 16000)

def checkFile(file_path):
    global file_count, total_size, total_duration
    file_count += 1
    total_duration += getDuration(file_path)
    total_size += os.path.getsize(file_path) / 1024 / 1024

    print("Found {0} files, {1:.2f} MB, {2:.2f} hours".format(file_count, total_size, (total_duration / 60 / 60)),
          end="\r")
    #print("Found {0} files, {1:.2f} MB, {2:.2f} hours".format(file_count,total_size,(total_duration/60 /60)),end="\n")


runScript()



