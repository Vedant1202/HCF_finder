


## FOR TWO INTEGERS
## x = ENTER A NUMBER
x=24
divisors=()
for i in range(1,x+1):
    if x%i == 0:
     divisors=divisors+(i,)
     ##FOR DEBUGGING OR PRINTING THE DIVISORS THE FOLLOWING STEP IS WRITTEN ( DENOTED BY '//')
    ##// print( 'Divisors of',x,'are',divisors)

## a = ENTER A NUMBER
a=12
divisorss=()
for j in range(1,a+1):
    if a%j == 0:
     divisorss=divisorss+(j,)
     ##//print ( 'Divisors of',a,'are', divisorss)
def common_elements(list1, list2):
    result = []
    for element in list1:
        if element in list2:
            result.append(element)
    return result
g=()
g=g+(common_elements(divisors, divisorss),)
##commonfactors=()
##commonfactors=commonfactors+(g)
h=max(g)
print('THE COMMON FACTORS ARE',(h))
o=max(h)
print( 'THE HCF OF',a,'AND',x,'ARE',o,'.')


##FOR THREE OR MORE NUMBER OF INTEGERS
## x = ENTER A NUMBER
divisors=()
for i in range(1,x+1):
    if x%i == 0:
     divisors=divisors+(i,)
    ## //print( 'Divisors of',x,'are',divisors)
## a = ENTER A NUMBER
divisorss=()
for j in range(1,a+1):
    if a%j == 0:
     divisorss=divisorss+(j,)
     ##// print ( 'Divisors of',a,'are', divisorss)
## b = ENTER A NUMBER
divisorsss=()
for k in range(1,b+1):
    if b%k == 0:
     divisorsss=divisorsss+(k,)
     ##// print ( 'Divisors of',b,'are', divisorsss)
##FOR 4TH INTEGER COPY ABOVE CODE AND CHANGE THE VARIABLES
def common_elements(list1, list2, list3):
    ##FOR 4TH LIST ADD ANOTHER LIST EG. LIST4
    result = []
    for element in list1:
        if element in list2:
            if element in list3:
                ##FOR 4TH INTERGER ADD ANOTHER IF STATEMENT
             result.append(element)
    return result

g=()
g=g+(common_elements(divisors, divisorss, divisorsss),)## ADD THE 4TH LIST HERE AS WELL
##commonfactors=()
##commonfactors=commonfactors+(g)
h=max(g)
##// print('THE COMMON FACTORS ARE',(h))
o=max(h)
print( 'THE HCF OF',a,'AND',x, 'AND',b,'ARE',o,'.')## ADD THE 4TH LIST HERE AS WELL
