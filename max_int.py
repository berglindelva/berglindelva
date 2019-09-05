num_int=int(input('Input a number: '))
#I put the counter as 0 at first and then I go in a while loop
#When the while loop is bigger then zero it continous running and finds the biggest number
#when a number smaller then zero is the input it prints out the biggest number
max_int=0

while num_int>=0:
    if max_int<num_int:
        max_int=num_int
    num_int=int(input('Input a number: '))
print('The maximum is:', max_int)
