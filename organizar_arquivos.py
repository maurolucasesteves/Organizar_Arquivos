import os
import shutil
import time

# Defina o caminho para o diretório de origem onde os arquivos descompactados estão localizados
pasta_origem = 'E:\\'

# Defina o caminho para o diretório de destino onde os arquivos organizados serão movidos
pasta_destino = 'Z:\\'

# Verifique se o diretório de destino existe, se não, crie-o
if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

# Função para mover arquivos para pastas baseadas em suas extensões
def mover_por_extensao(pasta_origem, pasta_destino):
    total_arquivos = contar_arquivos(pasta_origem)
    arquivos_movers = 0

    start_time = time.time()  # Iniciar temporizador

    for subdir, dirs, files in os.walk(pasta_origem):
        for file in files:
            # Obtenha a extensão do arquivo
            _, ext = os.path.splitext(file)
            ext = ext.lower()  # Use lowercase para evitar problemas com maiúsculas/minúsculas

            if ext:  # Verifique se a extensão não está vazia
                # Crie o caminho da nova pasta para a extensão dentro da pasta de destino
                pasta_extensao = os.path.join(pasta_destino, ext[1:])  # Remover o ponto da extensão para o nome da pasta

                # Crie a pasta se ela não existir
                if not os.path.exists(pasta_extensao):
                    os.makedirs(pasta_extensao)

                # Caminho completo do arquivo original
                caminho_arquivo = os.path.join(subdir, file)
                
                # Caminho de destino para mover o arquivo
                caminho_destino = os.path.join(pasta_extensao, file)
                
                # Mover o arquivo para a pasta correspondente
                shutil.move(caminho_arquivo, caminho_destino)

                arquivos_movers += 1
                # Exibir porcentagem concluída
                percentual_concluido = (arquivos_movers / total_arquivos) * 100
                print(f"Movendo arquivo {arquivos_movers}/{total_arquivos} ({percentual_concluido:.2f}%)")

    # Após mover todos os arquivos, limpar subpastas vazias
    limpar_subpastas_vazias(pasta_origem)

    end_time = time.time()  # Fim do temporizador
    tempo_decorrido = end_time - start_time
    print(f"Tempo total de execução: {tempo_decorrido:.2f} segundos")

# Função para contar todos os arquivos no diretório
def contar_arquivos(pasta):
    contador = 0
    for subdir, dirs, files in os.walk(pasta):
        contador += len(files)
    return contador

# Função para remover subpastas vazias
def limpar_subpastas_vazias(pasta):
    for subdir, dirs, files in os.walk(pasta, topdown=False):
        for d in dirs:
            caminho_dir = os.path.join(subdir, d)
            # Remover o diretório se ele estiver vazio
            if not os.listdir(caminho_dir):
                os.rmdir(caminho_dir)
                print(f"Pasta removida: {caminho_dir}")

# Chamada da função para mover arquivos por extensão
mover_por_extensao(pasta_origem, pasta_destino)

print("Arquivos movidos e pastas desnecessárias limpas com sucesso!")
