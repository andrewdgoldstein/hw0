file = open('test.csv')
n=0
for x in file:
  if "single malt scotch" in x.lower():
    n+=1
print n 
