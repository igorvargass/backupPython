import os
import shutil
from datetime import datetime

def backup(dir_origem, dir_destino):
    #Verifica se os diretórios existem
    if not os.path.exists(dir_origem):
        print(f'O diretório de origem "{dir_origem}" não existe.')
        return
    if not os.path.exists(dir_destino):
        print(f'O diretório de destino "{dir_destino}" não existe. Criando diretório...')
        os.makedirs(dir_destino)

    #Salva hora atual na variável
    data_hora_atual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    #Renomeia o diretorio de backup com a data e hora atual
    dir_backup = os.path.join(dir_destino, f'backup_{data_hora_atual}')

    #Copia os arquivos do diretório de origem para o diretório de backup
    try:
        shutil.copytree(dir_origem, dir_backup)
        print(f'Backup realizado com sucesso em: "{dir_backup}".')
    except Exception as e:
        print(f'Erro ao realizar backup: {str(e)}')

#Exemplo
if __name__ == "__main__":
    dir_origem = input('Digite o diretorio de origem: ')
    dir_destino = input('Digite o diretorio de destino (Se não existir, não se preocupe, eu crio): ')

    #Chama a função 'backup'
    backup(dir_origem, dir_destino)
