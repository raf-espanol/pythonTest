import os

list=['dog','cat','frog','turtle','cat','frog','cat','dove']

def countwords(list):
  dict={}
  for i in range(len(list)):
    if list[i] in dict.keys():
      dict[list[i]]+=1
    else:
      dict[list[i]]=1

  for k,v in dict.items():
    print "%d,%s" % (v, k)


countwords(list)
