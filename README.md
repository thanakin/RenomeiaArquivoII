# RenomeiaArquivoII
### Melhorando o RenomeiaArquivo.

**Necessidade:**
* Parar o serviço do MySQL e alternar entre copias de uma mesma base de dados: uma com muitos dados e outra vazia.
* Ambas tem o mesmo nome, pois a aplicação que faz uso dela assim exige.
* Em uma delas (com dados) faço testes diariamente.
* Na outra (vazia) utilizo na gravação de video-aulas para os utilizadores da aplicação, por isso "precisa estar sem dados".

## Obs.:
Como este script precisa parar um seviço do S.O., é necessario executa-lo com privilegios de administrador:
```
runas.exe /user:administrator "StopRenameStart.py"
```

**Referências:**
[Parando serviços Windows via prompt](https://www.itprotoday.com/windows-78/how-can-i-stop-service-command-line)
[Documentação da biblioteca os.path](https://docs.python.org/3/library/os.path.html)