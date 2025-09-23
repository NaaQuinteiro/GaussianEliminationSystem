system_len = input("Informe o tamanho do seu sistema (i,j)")

line_len = int(system_len.split(",")[0])

column_len = int(system_len.split(",")[1])


lista = []
lista_linhas = []

for i in range(line_len):
    print(f"Linha {i}")
    for i in range(column_len):
        columns = int(input(f"Informe a {i} coluna:\n"))
        lista_linhas.append(columns)
    
    lista.append(lista_linhas)
    lista_linhas = []
    


print(lista)
# criar uma lista para cada linha e cada elemento é referente a uma coluna 
# lista = linha  coluna = coeficient