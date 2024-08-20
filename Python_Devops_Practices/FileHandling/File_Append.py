file = open('Source_file.txt', 'a')
file.write ("\n I am the best programmer in the devops \n")


file = open("Source_file.txt", 'r')
print(file.read())
file.close()