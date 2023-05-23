import csv
import os

# Caminho do arquivo de origem
arquivo_origem = "C:\\Users\\augus\\Downloads\\TesteCopiar.csv"

# Caminho do arquivo de destino
arquivo_destino = "C:\\Users\\augus\\Downloads\\TesteColar.csv"

# Ler o arquivo de origem
with open(arquivo_origem, "r") as arquivo_csv_origem:
    leitor_csv = csv.reader(arquivo_csv_origem)
    
    # Ler as linhas do arquivo de origem
    linhas_origem = list(leitor_csv)

# Escrever o arquivo de destino com as informações do arquivo de origem
with open(arquivo_destino, "w", newline="") as arquivo_csv_destino:
    escritor_csv = csv.writer(arquivo_csv_destino)
    
    # Escrever as linhas do arquivo de origem no arquivo de destino
    for linha in linhas_origem:
        escritor_csv.writerow(linha)

print("Arquivo CSV copiado com sucesso.")

file = 'TesteCopiar.csv'  
location = "C:\\Users\\augus\\Downloads"
path = os.path.join(location, file)  
os.remove(path)

print("O arquivo foi removido")



