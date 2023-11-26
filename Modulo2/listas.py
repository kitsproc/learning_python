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
