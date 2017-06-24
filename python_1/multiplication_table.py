base_number_list = [1,2,3,4,5,6,7,8,9,10,11,12]

for count in range (0,13):

    if count == 0:
        print 'x ' + ' '.join(str(x) for x in base_number_list)
    else:
        multiplied_list = map((lambda x: x * count), base_number_list)
        #print multiplied_list
        rowOfText = ' '.join(str(x) for x in multiplied_list)
        print str(count) + ' ' + rowOfText
