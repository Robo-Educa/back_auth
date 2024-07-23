# 🤖 Robô Educa 
### 🤓 Aprenda Programação e Inteligência Artificial construindo seu próprio robô.

<hr>

## Servidor Python
* Para testar a aplicação acesse : https://pyserver-xd3gd6y2aa-uw.a.run.app

### Tecnologias utilizadas

- ![Pyton](https://img.shields.io/badge/python-v3-green)
- ![HTML](https://img.shields.io/badge/HTML-5-orange)
- ![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow)

### Como Usar 

1. Clone o repositório.
```
$ git clone https://github.com/Robo-Educa/py_server.git 
```
2. Instale as dependências.
```
$ cd py_server
$ pip install -r requirements.txt
```
3. Crie um arquivo .ENV a partir do .ENV.EXAMPLE e preencha os valores das variáveis de ambiente conforme o seu projeto.

4. Execute o projeto.
```
$ python main.py
```
5. Teste no Navegador
```
http://localhost:5000
```

### Como realizar deploy no ambiente de nuvem da Google (Cloud Run)
* Crie um Projeto 
* Em um terminal do Google Cloud SDK Shell digite:
```
$ cd py_server
$ gcloud components update
$ gcloud init
$ gcloud run deploy --source .
```
* No console da Google Cloud Platform, selecione o projeto.
* FireBase-Firestore / Criar Banco de Dados.
* Baixar arquivo JSOn com credenciais de acesso :
    * IAM e Administrador / Contas de Serviço / Clicar na conta de Serviço
    * Chaves / Adicionar chave / Criar nova Chave / JSON / Criar
    * O arquivo JSON será baixado automaticamente
* Criar Bucket privado. Salvar no Bucket o arquivo JSON com a credencial de acesso ao banco de dados
* Cloud Run / Clicar no Aplicativo / Clicar em: Editar e implantar uma nova versão
* Volumes / Adicionar volume referente ao Bucket contendo a credencial do banco de dados
    * Tipo: Bucket do Cloud Storage
    * Acessar a Guia Containers / Montagem de Volumes / Montar Volume
    * Selecionar o nome do volume criado 
    * Caminho da Montagem : especificar um nome que servirá como path. Ex: /config
    * Concluir / Implantar
* Cloud Run / Clicar no Aplicativo / Clicar em: Editar e implantar uma nova versão    
* Variáveis e Secrets / Adicione as mesmas variáveis do arquivo .ENV
    * Atenção para PATH da credencial Firestore que deverá conter o path do volume recém criado. Ex: /config/credencial.json

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request.

## Licença

Este projeto está licenciado sob a [Apache 2.0 License](LICENSE). Observe também os Termos de Serviço.

