### TYPE HINTS ###
### Es to nos ayuda a validar el tipo de dato haciendo que asi fastApi lo pueda valorar
### Y mejorar la expoerencia de desarrollo y la legilibiulidad de código 


my_string_variable = "My String Variable"
print(my_string_variable)
print(type(my_string_variable))

my_string_variable = 5
print(my_string_variable)
print(type(my_string_variable))

#Tipado débil --> puedo poner int apesar de ser str
my_typed_variable: int = "My typed Variable"

print(my_typed_variable)
print(type(my_typed_variable))
