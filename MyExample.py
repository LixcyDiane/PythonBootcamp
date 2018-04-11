print('Hello')
print('Hello Again')

a = 5
b = 10
print(a + b) 

print(type(a)) #Checks variable data type
print(len('burrito')) #prints string length 

#variables can be switched from type to type without new declaration 
variable = 1
print(variable)
variable = "concentracion" 
print(variable)

#variable indexing 
print(variable[2]) #shows character in index 2
print(variable[4:]) #shows all characters starting from index 4
print(variable[:6]) #shows all characters from index 0 to index 5
print(variable[-1]) #shows last character 
print(variable[:-1]) #show all characters except last one
print(variable[::3]) #shows everything going in steps of 3
print(variable[::-1]) #shows everything backwards

#variable slicing 
print(variable[0:5:1]) #from index 0 to index 4 in steps of 1
print(variable[0:8:2]) #from index 0 to index 7 in steps of 2

#repetition
letter = 'k'
print(letter * 5)

