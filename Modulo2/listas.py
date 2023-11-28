#Listas
lista = ["Hola", 2, 5.7, True, 3, 7]
print(lista)

lista_cursos = ['Python','Django','Ruby','2',3,5]

primer_curso  = lista_cursos[0]
segundo_curso = lista_cursos[1]
tercero_curso = lista_cursos[2]

print(primer_curso)
print(segundo_curso)
print(tercero_curso)


#Modificando la lista
lista_cursos[0] = 'Rust'
lista_cursos[2] = 'Flask'
print(lista_cursos)

#Sublistas
sub_lista = lista_cursos[0:2]
print(sub_lista)

sub_lista = lista_cursos[1:2]
print(sub_lista)

#Modificar listas
lista_cursos.append('Ruby2')
lista_cursos.append(3)
lista_cursos.append(4)
lista_cursos.append('C')
print("Tamaño de lista es: ",len(lista_cursos))
print(lista_cursos)

#Añadir elemento a alista desde un indice

lista_cursos.insert(1,'C++')
print(lista_cursos)

print("Tamaño de lista es: ",len(lista_cursos))
print(lista_cursos)

lista_cursos.insert(0,'C++')
print(lista_cursos)
print("Tamaño de lista es: ",len(lista_cursos))
print(lista_cursos)

#Ampliar lista con extend
lista_a_anexar=[100,101,102]
lista_cursos.extend(lista_a_anexar)
print("Tamaño de lista es: ",len(lista_cursos))
print(lista_cursos)

#Eliminar elementos de la lista, con remove
print(lista_cursos)
lista_cursos.remove(100)
print("Tamaño de lista es: ",len(lista_cursos))
print(lista_cursos)

#Eliminar con indices, con del
print(lista_cursos)
del lista_cursos[0]
print("Tamaño de lista es: ",len(lista_cursos))
print(lista_cursos)

#Eliminar todos los elementos de la lista
print("Tamaño de lista es: ",len(lista_cursos))
print(lista_cursos)
lista_cursos.clear()
print("Tamaño de lista es: ",len(lista_cursos))
print(lista_cursos)