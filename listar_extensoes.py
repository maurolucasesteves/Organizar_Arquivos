import os
from collections import Counter

# Defina o caminho para o diretório que você deseja analisar
diretorio = 'Z:\\'

# Defina o caminho para o arquivo de saída
arquivo_saida = 'Z:\\resultado_extensoes.txt'

# Crie uma lista para armazenar as extensões encontradas
extensoes_encontradas = []

# Percorra todos os arquivos no diretório e subdiretórios
for subdir, dirs, files in os.walk(diretorio):
    for file in files:
        # Obtenha a extensão do arquivo
        _, ext = os.path.splitext(file)
        if ext:  # Verifique se o arquivo tem uma extensão
            extensoes_encontradas.append(ext.lower())

# Conte as ocorrências de cada extensão
contagem_extensoes = Counter(extensoes_encontradas)

# Exiba o resultado no console e salve em um arquivo txt
with open(arquivo_saida, 'w') as f:
    for ext, count in contagem_extensoes.items():
        resultado = f'Extensão: {ext}, Quantidade: {count}'
        print(resultado)
        f.write(resultado + '\n')

print(f"Os resultados foram salvos no arquivo: {arquivo_saida}")
