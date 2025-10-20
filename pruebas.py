

nombres = ['cristian', 'luli', 'juan']
apellidos = ['romano', 'ortiz', 'vallejos']
nuevaLista = []
for x in nombres:
    if 'a' in x:
        nuevaLista.append(x)
    elif 'a' not in x:
        print('no hay nombres con esa letra')
print('Fin de programa')

print(nuevaLista)