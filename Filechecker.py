import os

# check file
def checkFile(File,mode='r'):
  try:
    if not File.endswith('.txt'):
      print("Support file txt only")
      sys.exit(1)
    return open(File,mode)
  except FileNotFoundError:
    print("Wrong file or file path")
    sys.exit(1)

# check directory path
def checkDir(Dir):
  word = ''
  if  os.path.exists(Dir):
    for f in os.listdir(Dir):
      if f.endswith(".txt"):
        File = open(os.path.join(Dir,f),'r').read()
        word += File
    return word
  else :
    print("Wrong directory path")
    sys.exit(1)