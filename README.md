<div align="center">
<img src="static/images/logo.png" alt="Logo">
</div>

### 🤓 Aprenda a programar construindo seu próprio robô.

<hr>

Robô-Educa  é uma plataforma inovadora que ensina programação para crianças de 6 a 14 anos, promovendo a inclusão 🤝 e a sustentabilidade ♻️. A jornada começa com uma história inspiradora sobre dois irmãos que constroem um robô 🤖 com a ajuda do professor 👨‍🏫 que incentiva às crianças a montarem seu próprio robô humanoide utilizando materiais reciclados, programação e nuvem ♻️💻☁️.

O web aplicativo Robô-Educa, acessível por smartphone 📱, se torna o "cérebro" 🧠 do robô, interagindo com a criança por mensagens de áudio 🗣️, tornando-o acessível inclusive para pessoas com deficiência visual 👀. A montagem do robô 🤖 e a interação com o aplicativo estimulam a coordenação motora 🖐️ e a criatividade ✨, expondo a criança a conceitos tecnológicos de forma lúdica e inclusiva.

A Gemini API, da Google, permite ao Robô-Educa entender e responder às perguntas da criança sobre robótica 🤖, explicar conceitos complexos 🤯 e realizar quizzes gamificados 🎉. Essa tecnologia, hospedada na plataforma Google, transforma o aprendizado em uma conversa natural e divertida 😄, abrindo novas perspectivas para o futuro das crianças 🚀.

<hr>

### Link para testar a aplicação:
* Acesse : https://robo-educa-gemini-server-xd3gd6y2aa-uw.a.run.app/
* Autorize o uso do Microfone 
* Clique em : ENTRAR COMO VISITANTE
* Ouça as perguntas e respomda corretamente para acumular pontos

<hr>

### Histórico:

<div align="center">
<img src="static/images/robopet.jpg" alt="Logo">
</div>

A Inteligência artificial está cada vez mais presente em nossas vidas, fazendo-se necessário estimular o maior número de pessoas a darem os primeiros passos no entendimento desta tecnologia permitindo assim que as mesmas se tornem não somente usuários mais principalmente protagonistas na criação dos novos recursos desta tecnologia no futuro.

Foi a partir deste pensamento que no ano de 2018 surgiu o projeto Robô Educa. Uma plataforma acessível para Ensino de Programação e Inteligência Artificial em que a criança dá os primeiros passos no universo destas tecnologias montando o seu próprio robô. Nesta época o robô era feito de garrafas pet e alguns componentes eletrônicos como Leds, resistores e baterias.
Mas somente no ano de 2024, com o uso da GEMINI API, que o robô passou a ter um "cérebro" capaz de responder de forma inteligente e rápida, tornando a iteração fluida e encantadora!

O idealizador deste projeto, [Carlos Sales](https://drive.google.com/file/d/1KPPJQhNn_YsWYK6qllP6muns6WlSRyM1/view?usp=sharing), é um homem negro de origem periférica graduado em Ciência de Dados e Desenvolvimento de Sistemas. O mesmo conta um pouco da sua história no documentário [C0d3rs Championship](https://www.primevideo.com/detail/0GS98CG03BVM7C224YK7KIWXOJ) disponível no Amazon Prime Video. 

Visite nossa [galeria de fotos](https://photos.app.goo.gl/yJiewdTTsNFtmF846) para conhecer mais sobre nossas oficinas de inclusão realizadas em comunidades carentes na cidade de Salvador, Bahia - Brasil.

<hr>

### Tecnologias utilizadas neste aplicativo

- ![Pyton](https://img.shields.io/badge/python-v3-green)
- ![HTML](https://img.shields.io/badge/HTML-5-orange)
- ![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow)
- ![Google Cloud](https://img.shields.io/badge/Google_Cloud-gray?style=for-the-badge&logo=google-cloud)
- ![Firestore](https://img.shields.io/badge/Firebase-Firestore-orange?style=for-the-badge&logo=firebase)

<div align="center">
<img src="static/images/gemini.png" alt="Logo Gemini API">
</div>

<hr>

### Como executar este aplicativo em seu PC Windows

1. Clone o repositório:
```
$ git clone https://github.com/Robo-Educa/robo-educa-gemini-server.git 
```
2. Instale as dependências:
```
$ cd robo-educa-gemini-server
$ pip install -r requirements.txt
```
3. Crie um arquivo .ENV a partir do .ENV.EXAMPLE e preencha os valores das variáveis de ambiente conforme o seu projeto.

4. Execute o projeto:
```
$ python main.py
```
5. Teste no Navegador:
```
http://localhost:5000
```

### Como realizar deploy no ambiente de nuvem da Google (Cloud Run)
* No console da Google Cloud Platform, crie um Projeto 
* Certifique-se de ter instalado em seu PC Windows a CLI gcloud (Google Cloud SDK Shell) disponível em : https://cloud.google.com/sdk/docs/install?hl=pt-br
* Em um terminal do Google Cloud SDK Shell, vá para a pasta em que se encontra o seu projeto e inicialize sua conexão informando o seu email, projeto e região default para hospedagem do seu App:
```
$ cd\[path do projeto]
$ gcloud init
```
* Faça o deploy do seu App:
```
$ gcloud run deploy --source .
```
* No console da Google Cloud Platform, selecione o seu projeto.
* No menu de navegação selecione: FireBase-Firestore 
* Crie um Banco de Dados do tipo Nativo
* Baixe um arquivo JSON contendo credenciais de acesso ao seu banco:
    * IAM e Administrador / Contas de Serviço / Clicar na conta de Serviço: Default compute service account
    * Chaves / Adicionar chave / Criar nova Chave / JSON / Criar
    * O arquivo JSON será baixado automaticamente
* No menu de navegação selecione: Google Cloud Storage
* Crie um Bucket privado. Salve neste Bucket o arquivo JSON contendo credencial de acesso ao banco de dados
* No menu de navegação selecione: Cloud Run 
* Clique no Aplicativo 
* Clique em: "Editar e implantar uma nova versão"
    * Clique em Volumes / Adicionar um Volume referente ao Bucket contendo a credencial do banco de dados
        * Tipo: Bucket do Cloud Storage
        * Acessar a Guia Containers / Montagem de Volumes / Montar Volume
        * Selecionar o nome do volume criado 
        * Caminho da Montagem : especificar um nome que servirá como path. Ex: /config
        * Concluir / Implantar
* Clique novamente em: Editar e implantar uma nova versão    
    * Variáveis e Secrets / Adicione as mesmas variáveis contidas n arquivo .ENV.example
        * Atenção para variável PATH_CREDENTIAL_FIRESTORE que deverá conter o path do volume recém criado. Ex: /config/credencial.json
        * Atenção para variável API_KEY que deverá conter uma chave válida que pode ser obtida em : https://aistudio.google.com
* Atenção: Cuidado com o arquivo JSON contendo a credencial de acesso ao banco de dados e também com sua API_KEY Gemini. Nunca os exponha publicamente, utilize secrets ou outros recusos de seguranças recomendados pela plataforma Google Cloud.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request.

## Licença

Este projeto está licenciado sob a [Apache 2.0 License](LICENSE). Observe também os Termos de Serviço.

