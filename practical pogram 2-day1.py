l=[2,5,7,3,4,8,9,1,3,5]
def sumsquare():
      odd=0
      even=0
      for i in l:
            if i%2==0:
                  even+=i**2
            else:
                  odd+=i**2
      a=[odd,even]
      return a
print(sumsquare())
