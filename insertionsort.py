#This is my python program.
pos=-1
def search(list,n):
    i=0
    while i<=len(list):
          if list[i]==n:
             globals()['pos']=i
             return True
          i=i+1
    return False
    
    
list=[2,4,5,7,12,16,18,23,56]
n=16

if search(list,n):
   print('found at',pos)
else:
   print('not found')
