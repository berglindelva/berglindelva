n = int(input("Enter the length of the sequence: ")) # Do not change this line
#I create 4 counters and one sum
#I go into a while loop to check when the counter is smaller then n
#then I sum the first three counters and print it
#I go into a if loop in the while loop to check if the first counter is bigger than or equal to 2
#then I give counter 2 the value of counter 3
#then counter 2 gets the value of counter 1 in the while loop
#And counter 1 gets the value of the sum
#The fourth counter is then always +1
num_one=1
num_two=0
num_three=0
counter=0
sum_int=0
while counter<n:
    sum_int=num_one+num_two+num_three
    print(sum_int)
    if num_one>=2:
        num_three=num_two
    num_two=num_one
    num_one=sum_int
    counter+=1
