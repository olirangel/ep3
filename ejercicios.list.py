

listanumeros = [] #lista vacia 
respuesta = "<"

while respuesta == "<":
    listanumeros.append int(input("ingresa el numero: ")) #agregar el num al final de la lista 
    print (listanumeros) #muestra la lista

    respuesta = input ("presiona < para agregar otro numero a la lista: ")


print(listanumeros)


#ejercicio69
country_tuple = ("France", "England", "Spanish","Germany", "Autralia")
print (country_tuple)
print()
country = input ("Please enter one of the countries from above: ")
print (country, "has index number",country_tuple.index(country))


#ejercicio70
