import os
import sys

if os.path.isfile('config-local.ini'):
    os.rename('config.ini', 'config-remoto.ini')
    os.rename('config-local.ini', 'config.ini')
    print('Utilizando configuração local')
    os.system("pause")
    sys.exit()
elif os.path.isfile('config-remoto.ini'):
    os.rename('config.ini', 'config-local.ini')
    os.rename('config-remoto.ini', 'config.ini')
    print('Utilizando configuração remota')
    os.system("pause")
    sys.exit()
else:
    print('Arquivo nao localizado')