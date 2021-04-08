arr=[8,1,5,9,7,0,6,4,2,3]

def selection_sort(lista):
    
    control=0

    for i in range(len(lista)):

        temp =lista[control]
        valor_menor = lista[lista.index(min(lista[control:]))]
        indice_menor = lista.index(min(lista[control:]))

        lista[control]=valor_menor
        lista[indice_menor]=temp       
        control+=1    
    
    return lista

print(selection_sort(arr))
