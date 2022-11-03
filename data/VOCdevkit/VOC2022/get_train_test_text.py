import os
from sklearn.model_selection import train_test_split


all_file_names = []
#a = open("train.txt", "w")
for path, subdirs, files in os.walk(r'JPEGImages'):
  for filename in files:
    #a.write(filename[:filename.rfind('.')] + os.linesep)
    all_file_names.append(filename[:filename.rfind('.')])
    #print(filename)
     #f = os.path.join(path, filename)
     #a.write(str(f) + os.linesep) 

train, test = train_test_split(all_file_names,test_size=0.2)

train_f = open("train.txt", "w")
for f in train:
  train_f.write(f + os.linesep)

test_f = open("test.txt", "w")
for f in test:
  test_f.write(f + os.linesep)



