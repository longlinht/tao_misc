# coding=utf-8

import os
import sys

def main():
   filepath = sys.argv[1]
   bookName = sys.argv[2]

   if not os.path.isfile(filepath):
       print("File path {} does not exist. Exiting...".format(filepath))
       sys.exit()

   DELIMITER = "=========="
   TIME_MAKR = "- 您在"
   lineNum = 0
   books = {}
  
   bag_of_words = {}
   with open(filepath) as fp:
       encounter = False
       delimiterCount = 0
       curBookName = ""
       for line in fp:
           if lineNum == 0:
               books[line] = []
               curBookName = line
               delimiterCount += 1
           else:
               if line.startswith(DELIMITER):
                   delimiterCount += 1
                   encounter = True
               else:
                   if encounter == True:
                       if line in books:
                           curBookName = line
                       else:
                           books[line] = []
                       encounter = False
                       curBookName = line
                   else:
                       books[curBookName].append(line)
           lineNum += 1
           #print(line)

       fp.close()            

   outFile = open("ClippingOutput.txt", "w")
   for k in books:
       if k.startswith(bookName) :
           outFile.writelines(k)
           lines = books[k]
           for l in lines:
               if l.startswith(TIME_MAKR):
                   continue
               if l.startswith(bookName):
                   continue
               outFile.writelines(l)
   outFile.close()

if __name__ == '__main__':
    main()
