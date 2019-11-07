import binascii

# get binary
binary = lambda b: format(b,'b')

# display based on differences in binary or not
def show(x,ln='',Bin=False,out=None):
  if out != None:
    if Bin :
      out.write(str(binary(x[0])+binary(int(binascii.hexlify(bytes(x[1],encoding='utf-8')),16)))) 
    else :
      out.write(str(x[0])+x[1]) 
  else:
    if Bin :
      print(binary(x[0])+binary(int(binascii.hexlify(bytes(x[1],encoding='utf-8')),16)), end=ln) 
    else :
      print(str(x[0])+x[1],end=ln) 
    