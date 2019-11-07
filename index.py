import argparse
import Filechecker as File 
import Output as put

# argument documentary
arg = argparse.ArgumentParser()
arg.add_argument("-b","--binary",action="store_true", help = "Convert to binary")
option = arg.add_mutually_exclusive_group()
option.add_argument("-f","--file", help = "Read file txt")
option.add_argument("-d","--directory", help = "Read all file txt in directory")
arg.add_argument("-o","--outputFile", help = "output result to file txt")
args = vars(arg.parse_args())

#check user want to put on file or not
out = File.checkFile(args['outputFile'],'w') if args['outputFile'] != None else None

# check user input file or directory or not
if args["file"] != None :
  word = File.checkFile(args['file']).read()
elif args["directory"] != None:
  word = File.checkDir(args['directory'])
else :
  word = str(input("Word : "))
    
freq = 0
previous=''

# Run-length encoding process
for i in word:
  if i != previous :
    if freq != 0 :
      put.show([freq,previous],Bin=args['binary'],out=out)
    previous = i
    freq = 1 
  elif i == previous :
    freq += 1
else:
  put.show([freq,previous],ln='\n',Bin=args['binary'],out=out)

