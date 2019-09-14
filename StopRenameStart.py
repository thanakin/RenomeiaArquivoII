import os
import sys

os.system("net stop Spooler") 
'''requer elevação/executar como Administrador''' #Parando serviço
if os.path.isdir('vazia'): #Renomeando pastas I
    os.rename('teste', 'dados') #
    os.rename('vazia', 'teste') #
    print('Utilizando Base de VIDEOS / vazia')  
elif os.path.isdir('dados'): #Renomeando pastas II
    os.rename('teste', 'vazia') #
    os.rename('dados', 'teste') #
    print('Utilizando Base de TESTES / com dados')
else: #Caso algo de errado...
    print('Arquivo nao localizado') 
os.system("net stop Spooler") 
'''requer elevação/executar como Administrador''' #Re-iniciando serviço
os.system("pause") #Aguardando interação final do usuario
sys.exit() #Encerrando script