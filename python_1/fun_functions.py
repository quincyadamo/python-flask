#Create a function called odd_even that counts from 1 to 2000 and prints "odd" and "even"

for num in range (1,2001):
    if num % 2 == 0:
        print "This number is " + str(num) + " This is an even number"
    else:
        print "This number is " + str(num) + " This is an odd number"

#Create a function called 'multiply' + return a list where each value has been multiplied by 5.

def multiply(arr, num):
    for x in range(0, len(arr)):
        arr[x] *= num
    return arr

numbers_array = [2, 4, 10, 16,]

print multiply(numbers_array, 5)

#Write a function that takes the multiply function call as an argument

def layered_multiples(arr):
    print arr
    new_array = []
    for x in arr:
        val_arr = []
        for i in range(0,x):
            val_arr.append(1)
        new_array.append(val_arr)
    return new_array

x = layered_multiples(multiply([2,4,5],3))
print x
