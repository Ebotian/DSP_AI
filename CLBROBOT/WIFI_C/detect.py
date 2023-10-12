# import a library to detect encodings
import chardet
import glob

# for every text file, print the file name & a gues of its file encoding
print("File".ljust(45), "Encoding")
#for filename in glob.glob('*.txt'):
filename='/home/ebotian/Downloads/robo/CLBROBOT/WIFI_C/视频开启指令.txt'
with open(filename, 'rb') as rawdata:
  result = chardet.detect(rawdata.read())
print(filename.ljust(45), result['encoding'])