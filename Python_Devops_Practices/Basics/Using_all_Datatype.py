#Integer
i_var = 50
print("Integer variable:", i_var)

#Floating
f_var = 3.16
print("Floating varible:", f_var)

#String
s_var = 'Vivek_new_Devops_Path'
print("String Variable:", s_var)

#List
l_var = [1,2,3,4]
print("List Variable:", l_var)

#tuple
t_var = (100,200,300,400)
print("Tuple Variable:", t_var)

#Dictionary
d_var ={'name':'Vivek','age':'31','profession':'Devops_Engineer'}
print("Dictionary_Variable:", d_var)

#set 
se_var = {1, 2, 3, 4, 5}
print("Set Variable", se_var)

#Actions

#Adding Integer and Float Operations
result = i_var + f_var
print("Added Values: ", result)

#Merging the strings
new_strings = s_var + "Is_Set_On_Fire"
print("Modified Strings:", new_strings)

#List Modifications
l_var.append(2)
l_var.remove(2)
print("Modified List :", l_var)

#Dictionary_Alteration
d_var["profession"]="AWS_DEVEOPS_ENGINEER"
print(d_var)
del d_var ["age"]
print("Modified dicitionary:", d_var)

#Set_Modification
se_var.add(5)
se_var.remove(3)
print("Modified Set Values:", se_var)