
#Print a new list of all the strings containing that char character
new_list = []
word_list = ['hello','world','my','name','is','Quincy']
char = 'o'
for word in word_list:

    if word.find(char) != -1: # if -1 that means that char is not in word
        new_list.append(word)
    # if char is in word then add word to new_list array
    # 1. how to determine if a given string (char) is a sub string of another string (word)
    # 2. how to add word into the exiting array new_list

print new_list
