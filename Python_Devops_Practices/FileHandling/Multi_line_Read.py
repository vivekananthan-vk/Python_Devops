file= open('Source_file.txt', 'r')
lines = file.readlines() #---> It will provide the multiple lines in list
print ("Multiple line result:", lines)
file.close()