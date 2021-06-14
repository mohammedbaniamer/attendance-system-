import os
import shutil
import csv

yaml = 'all data/Trained data.yaml'
if os.path.isfile(yaml):
    os.remove(yaml)
file = open(yaml, 'w+')

stImages = 'all data/StudentImages'
print(os.path.exists(stImages))
if os.path.exists(stImages):
    shutil.rmtree(stImages)
os.mkdir(stImages)

csvv = 'all data/RegisteredStudents.csv'
if os.path.isfile(csvv):
    os.remove(csvv)
with open(csvv, 'a+') as csvF:
    writer = csv.writer(csvF)
    writer.writerow(['Row', 'ID', 'NAME'])