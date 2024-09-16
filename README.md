# Organizador de Arquivos por Extensão
Organizar arquivos em espalhados
Este script tem como objetivo organizar arquivos em um diretório, movendo-os para pastas separadas com base em suas extensões. Ele também limpa subpastas vazias após mover os arquivos.

Funcionalidades
Move arquivos de um diretório de origem para pastas organizadas por extensão em um diretório de destino.
Cria automaticamente pastas para cada extensão de arquivo.
Exibe o progresso do processo de movimentação, mostrando a porcentagem de arquivos movidos.
Remove subpastas vazias na origem após os arquivos serem movidos.
Tecnologias Utilizadas
Python: Linguagem de programação usada para implementar o script.
Bibliotecas padrão:
os: Utilizada para navegação nos diretórios e manipulação de arquivos.
shutil: Utilizada para mover arquivos entre diretórios.
time: Utilizada para medir o tempo de execução do processo.
Pré-requisitos
Python 3.x: Certifique-se de ter o Python instalado em sua máquina. Você pode baixar o Python aqui.
Permissões de escrita: O diretório de destino deve permitir a criação de pastas e movimentação de arquivos.
Como usar
1. Clonar o repositório ou copiar o script
Baixe o script ou clone o repositório no diretório onde deseja executar o script.
git clone <URL-do-repositório>
2. Definir diretórios de origem e destino
No código, você precisa ajustar as variáveis pasta_origem e pasta_destino para apontar para os diretórios corretos em seu sistema:
# Caminho para o diretório de origem onde os arquivos estão localizados
pasta_origem = 'E:\\Drive_GOOGLE'

# Caminho para o diretório de destino onde os arquivos serão organizados
pasta_destino = 'Z:\\'
3. Executar o script
Após configurar os caminhos, execute o script:
python organizar_arquivos.py
4. Acompanhar o progresso
O script exibirá a porcentagem de arquivos movidos e o tempo total de execução após finalizar a organização.

Detalhamento das Funções
mover_por_extensao(pasta_origem, pasta_destino)
Esta função percorre todos os arquivos no diretório de origem e os move para pastas no diretório de destino com base em suas extensões.

Parâmetros:
pasta_origem: Diretório onde os arquivos estão localizados.
pasta_destino: Diretório onde os arquivos organizados serão movidos.
contar_arquivos(pasta)
Função auxiliar para contar o número total de arquivos no diretório de origem.

limpar_subpastas_vazias(pasta)
Remove subpastas vazias no diretório de origem após todos os arquivos serem movidos.

Exemplo de uso
python organizar_arquivos.py

Ao executar o script, ele moverá todos os arquivos do diretório E:\\Drive_GOOGLE para o diretório Z:\\, criando subpastas baseadas nas extensões dos arquivos (por exemplo, .jpg, .txt, .pdf), e exibirá o progresso do processo.

Resultados Esperados
Arquivos movidos com sucesso para pastas organizadas por tipo de arquivo.
Subpastas vazias no diretório de origem serão removidas automaticamente.
Tempo total de execução exibido ao final.
Contribuições
Sinta-se à vontade para contribuir com melhorias, novas funcionalidades ou correções. Para isso, faça um fork do repositório, crie uma branch para sua alteração e envie um pull request.

