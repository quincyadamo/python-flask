#Create a function called draw_stars() that takes a list of numbers and prints out *.

y = [1,'quincy',2,'thomas',3,'samantha',4,'jose']
def draw_stars(my_list):
    for item in my_list:
        output = ''
        if type(item) is int:
            for i in range(item):
                output += '*'
        elif type(item) is str:
            f_letter = item[0].upper()
            for i in range(len(item)):
                output += f_letter
        print output

draw_stars(y)

#Modify the function above. Allow a list containing integers and strings to be passed to the draw_stars() function

x = [4,6,1,3,5,7,25]
def draw_stars(num_list):
    for num in num_list:
        output = ''
        for i in range(num):
            output += '*'
        print output

draw_stars(x)
