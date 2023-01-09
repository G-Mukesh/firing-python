def  isIso(x,y):
      if len(x)!=len(y):
            return False
      for i in range(len(x)):
            if x.count(x[i])!=y.count(y[i]):
                  return False
      return True
print(isIso('fool','poor'))

            
      
