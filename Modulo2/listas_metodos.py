lista = [8,90,1,5,44,132,600,3,4]
lista.sort() #menor a mayor
lista.sort(reverse = True) #mayor a menor 
print(lista)

#encontrar numero mayor o menor
print("Numero mayor es: ",lista[0])
print("Numero menor es: ",lista[-1])
lista = [8,90,1,5,44,132,600,3,4]
print(lista)
print("Numero menor es: ",min(lista))
print("Numero mayor es: ",max(lista))

#Buscar elemento
lista = [8,90,1,5,44,132,600,3,4]
print(100 in lista)
print(9 not in lista)

