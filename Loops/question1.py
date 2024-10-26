# Write a Python program that prints the numbers from 1 to 50 using a for loop. 
# For numbers that are divisible by 3, print "Fizz" instead of the number, 
# and for numbers divisible by 5, print "Buzz". For numbers divisible by both, print "FizzBuzz".


for i in range(1, 50):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3==0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
