#find and replace
str = "It's thanksgiving day. It's my birthday,too!"
print str
print str.find("day")
str = str.replace("day", "month")
print str

#min and max
x = [2,54,-2,7,12,98]
print x
print min(x) #-2
print max(x) #98

#first and last
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0], x[7]

#new list
x = [19,2,54,-2,7,12,98,32,10,-3,6]
print x
x.sort()
print x
first_list = x[0:len(x)/2]
second_list = x[len(x)/2:len(x)]
print "first_list", first_list
print "second_list", second_list
second_list.insert(0,first_list)
print second_list
