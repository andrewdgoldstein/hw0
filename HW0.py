file = open('iowa-liquor-sample.csv')
n=0
for x in file:
  if x.lower()=="single malt scotch":
    n+=1
print n 
