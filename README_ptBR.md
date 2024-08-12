<div align="center">
<img src="static/images/logo.png" alt="Logo">
</div>

<hr>

[English Version](/README.md)

![Portuguese](https://img.shields.io/badge/Language-English-blue)
<hr>


## 🤓 Aprenda a programar construindo seu próprio robô.

Robô Educa  é uma plataforma inovadora que ensina programação para crianças de 6 a 14 anos, promovendo a inclusão e a sustentabilidade 🤝♻️. A jornada começa com uma história inspiradora de dois irmãos, Suzy e Otávio, que desejam construir um robô 🤖 e contam com a ajuda de seu professor Carlos Sales 👨‍🏫 que os incentiva a montar seu próprio robô humanoide utilizando materiais reciclados, programação e nuvem ♻️💻☁️.

É neste contexto que surge o Web Aplicativo Robô Educa que acessível a partir de qualquer smartphone 📱 se torna o "cérebro" do robô 🧠 interagindo com a criança através de  mensagens de áudio 🗣️ tornando-o acessível inclusive para pessoas com deficiência visual. A montagem do robô e a interação com o aplicativo estimulam a coordenação motora 🖐️ e a criatividade ✨ ensinando a criança conceitos tecnológicos de forma lúdica e inclusiva.

E toda a mágica realizado pelo aplicativo só é possível por conta do uso da **Google GEMINI API** 🤖 que permite ao Robô Educa entender e responder às perguntas da criança, explicar conceitos complexos 🤯 e realizar quizzes gamificados 🎉. Essa tecnologia disponível na nuvem da Google transforma o aprendizado em uma conversa natural e divertida 😄 abrindo novas perspectivas para o futuro destas crianças 🚀.

## 🤖 Como testar o aplicativo:
* Acesse : https://robo-educa-gemini-server-xd3gd6y2aa-uw.a.run.app/
* Clique em Iniciar;
* Autorize o uso do Microfone;
* Clique em: ENTRAR COMO VISITANTE;
* Ouça as perguntas e responda corretamente para acumular pontos.

## 📆 Histórico

<div align="center">
<img src="static/images/robopet.jpg" alt="Logo">
</div>

A Inteligência artificial está cada vez mais presente em nossas vidas, fazendo-se necessário estimular o maior número de pessoas a darem os primeiros passos no entendimento desta tecnologia permitindo assim que as mesmas se tornem não somente usuários mais principalmente protagonistas na criação dos novos recursos desta tecnologia no futuro.

Foi a partir deste pensamento que no ano de 2018 surgiu o projeto Robô Educa. Uma plataforma inclusiva para Ensino de Programação em que a criança dá os primeiros passos neste universo montando o seu próprio robô. Nesta época o robô era feito de garrafas PET e alguns componentes eletrônicos como Arduino, leds, resistores, e baterias.

Mas foi somente no ano de 2024 com o advento das IA Generativas e da **Google GEMINI API**, que o robô passou a ter um "cérebro" capaz de responder de forma **inteligente e rápida**, tornando a interação com a criança **flúida e encantadora** 😄!

O idealizador deste projeto, [Carlos Sales](https://drive.google.com/file/d/1KPPJQhNn_YsWYK6qllP6muns6WlSRyM1/view?usp=sharing), é um homem negro de origem periférica graduado em Ciência de Dados e Desenvolvedor de Sistemas. O mesmo conta um pouco da sua história no documentário [C0d3rs Championship](https://www.primevideo.com/detail/0GS98CG03BVM7C224YK7KIWXOJ) disponível no Amazon Prime Video. 

<div style="display: flex;">
<img src="static/images/image1.jpg" alt="Imagem 1" style="width: 22%; margin-right: 8px;">
<img src="static/images/image2.jpg" alt="Imagem 2" style="width: 22%; margin-right: 8px;">
<img src="static/images/image3.jpg" alt="Imagem 3" style="width: 22%; margin-right: 8px;">
<img src="static/images/image4.jpg" alt="Imagem 4" style="width: 22%;">
</div>

## 💪 Impacto

Utilizando apenas alguns poucos leds, resistores e baterias, conseguimos impactar centenas de crianças em diversas comunidades da nossa cidade. 

Já a partir do uso da inteligência artificial generativa e da nuvem, surgem novas possibilidades de expansão das habilidades cognitivas de nosso robô. Com a qual esperamos  alcançar um número ainda maior de crianças, agora **em todo o mundo**!

Visite nossa [galeria de fotos](https://photos.app.goo.gl/yJiewdTTsNFtmF846) para conhecer mais sobre nossas oficinas de inclusão realizadas em comunidades carentes na cidade de Salvador, Bahia - Brasil.

💪 E você? Gostou? Então faça sua parte e colabore com esta iniciativa para que possamos ampliar ainda mais o nosso impacto.

## 💻 Tecnologias utilizadas neste aplicativo

<div align="center">
<img src="static/images/gemini.png" alt="Logo Gemini API">
</div>

- ![Pyton](https://img.shields.io/badge/python-v3-green)
- ![HTML](https://img.shields.io/badge/HTML-5-orange)
- ![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow)
- ![Firestore](https://img.shields.io/badge/Firebase-Firestore-orange?style=for-the-badge&logo=firebase)
- ![Google Cloud](https://img.shields.io/badge/Google_Cloud-gray?style=for-the-badge&logo=google-cloud)

## Visão Geral da Plataforma Robô Educa

A plataforma **Robô Educa** oferece uma experiência prática e criativa para os alunos, orientando-os na montagem física de um robô humanoide. Este robô é feito com materiais recicláveis ou MDF e pode ser customizado com elementos como LEDs, baterias e outros componentes. Após a montagem física, os alunos dão vida ao robô usando o "cérebro" dele, que é o aplicativo descrito neste código.

O aplicativo permite que o robô humanoide desempenhe funções cognitivas: ouvir, pensar e falar. Essas capacidades são implementadas utilizando tecnologias de **Speech-to-Text** e **Text-to-Speech**, permitindo que o robô ouça mensagens faladas, as analise e responda com uma fala sintetizada.

### Pilha Tecnológica e Arquitetura

A aplicação é desenvolvida utilizando ferramentas open-source e hospedada na Google Cloud, aproveitando sua infraestrutura robusta. O backend é desenvolvido em Python usando o framework Flask, seguindo o padrão de design **Service/Repository**:

- **Camada de Serviço**: Lida com a lógica de negócio.
- **Camada de Repositório**: Gerencia a integração com o banco de dados.

Para armazenamento de dados, a plataforma utiliza um banco de dados NoSQL, o **Firebase/Firestore**, que oferece escalabilidade e flexibilidade para armazenar conversas e dados de usuários.

### Arquivos Principais e Funcionalidades

### Backend - `routes.py`
O arquivo `routes.py` gerencia todas as rotas disponíveis na aplicação. É aqui que diferentes endpoints são definidos para lidar com as interações dos usuários e o processamento de dados.

```python
# Dependências
from main import app
from flask import render_template, request, session, redirect, url_for, make_response, jsonify
# Serviços
import service.loginService as loginService
import service.talkService as talkService

# Página inicial/Index
@app.route('/')
def home():
    return render_template('index.html')
```

### Frontend - HTML, CSS e JavaScript
O frontend é implementado utilizando HTML, CSS e JavaScript, focando na simplicidade e facilidade de uso. Ele começa solicitando o acesso ao microfone, que é gerenciado pelo `mediadevices.js`.

**Acesso ao Microfone**:
Quando o aplicativo é iniciado, ele verifica as permissões para uso do microfone. Se for a primeira vez que o usuário acessa o app, ele será solicitado a conceder a permissão. Este processo é gerenciado pelo arquivo `mediadevices.js`.

```javascript
async function devices_micPrompt() {
    let permission;
    await navigator.mediaDevices
        .getUserMedia({
            audio: true
        })
        .then(function (stream) {
            permission = "granted"        
        })
        .catch(function (error) {
            if (error.message == "Requested device not found") {
                permission = "notFound";
            } else if (error.message == "Permission denied") {
                permission = "denied";
            } else {
                console.log(error.message)
                permission = 'error';
            }
        });
    return permission;
}
```

**Autenticação do Usuário**:
O processo de login é gerenciado pelo `login.js`, que envia uma requisição POST para o backend para validar o usuário. Se o usuário não tiver credenciais válidas, ele pode fazer login como convidado.

```javascript
async function login(usertype) {    

    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;    

    displayStartLogin();
    
    await fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username: username, password: password, usertype: usertype })
    })
    .then(response => response.json())
    .then(data => {

        displayStopLogin();
        
        switch (data.status) {
            case 'success':
                goToPage("interaction");
                break;
            case 'errorUser':
                alert("Usuário inexistente");
                document.getElementById("username").focus();
                break;
            case 'errorPwd':
                alert("Senha incorreta");
                document.getElementById("password").focus();
                break;
            case 'errorGuest':
                alert("Não foi possível criar usuário temporário. Tente novamente!");                
                break;                
            default:
                break;
        }        
    });
    
}
```

**Interação**:
Após o login bem-sucedido, a interação começa no frontend com o arquivo `interaction.html`. A interface visual, gerenciada pelo `display.js`, é simples, com elementos que simbolizam escuta, pensamento e fala.

**Escuta Contínua e Processamento de Fala**:
O robô começa com uma saudação e convida o usuário a participar de um quiz sobre programação. Após falar, o app ativa o microfone em modo contínuo, escutando o que o usuário fala. Essas tarefas são realizadas pelo `Talk.js`, que utiliza as APIs `Media Devices`, `SpeechRecognition()` e `SpeechSynthesisUtterance()`.

```javascript
// Este evento é acionado quando o reconhecimento de voz captura um resultado
recognition.onresult = event => {    
    const transcript = event.results[event.resultIndex][0].transcript;    
    talk(transcript);           // Envia transcrição do audio falado pelo usuário para o backend processar junto à Inteligência Artificial e dar uma respectiva resposta
};

// Verifica se usuário não estiver falando (reproduzindo audio). Após 1 minuto de inatividade, interrrompe reconhecimento e exibe botão de pausa
recognition.onend = () => {
    if (speakStatus == false) {     
        timestampAtual = Date.now();
        var diferenca = timestampAtual - timestampParam;
        var minutosPassados = diferenca / (1000 * 60);
        if (minutosPassados < 1) {
            recognition.start(); // Inicia o reconhecimento de voz
        } else {
            hideAllExceptClose();
            showElement("divPauseStart");
        }
    }        
};
```

### Processamento Cognitivo com a API Google Gemini

Quando uma frase completa é detectada, ela é enviada para o backend para processamento cognitivo. Isso é realizado utilizando a **API GEMINI**, que aproveita o modelo `gemini-1.5-flash` para respostas rápidas e precisas, garantindo conversas fluidas que tornam o robô mais envolvente e realista.

```python
import google.generativeai as genai

# Interação com a Google Gemini API
def talk(userMessage):
    # Obtem ID do usuário logado
    user_id = session["userId"]

    # Obtem histórico de mensagens do usuário
    message_history = messageHistory.getById(user_id)
    message_history_gemini_format = format_messages_for_gemini(message_history)   
    
    # Salva mensagem do usuário em banco de dados
    role = "user"                                       # role=user => mensagem enviada pelo usuário
    messageHistory.store(user_id, role, userMessage)    

    # Inicia interação com Gemini AI
    try:
        convo = model.start_chat(history = message_history_gemini_format) # Inicia chat, contextualizando a IA com o histórico da conversação
        convo.send_message(userMessage)                     # envia nova mensagem para ser processada pela IA
        bot_response = convo.last.text                      # Obtem resposta da IA
    except:
        bot_response = "error"

    # Salva resposta do Bot em banco de dados
    if bot_response != "error":
        role = "model"                                      # role=model => mensagem enviada pela IA
        messageHistory.store(user_id, role, bot_response)    
    else:
        bot_response = "Desculpe, não foi possível obter resposta da Inteligência Artificial."

    response = {"status": "success", "message": bot_response}
    return response
```

### Armazenamento de Dados e Personalização

A plataforma armazena a conversa de cada usuário no Firestore utilizando coleções NoSQL. Isso garante a segurança das crianças, além de permitir a moderação e personalização do conteúdo.

```python
import time
import repository.db_resource as dbr

# Instância de conexão com banco de dados NoSQL Google Firestore
db = dbr.firestore_resource()       

# Obtem histórico de mensagens a partir do ID do usuário
def getById(user_id):
    collection = f"message_history_{user_id}"
    messages_ref = db.collection(collection).order_by("timestamp")
    messages = messages_ref.stream()

    return messages

# Salva mensagem para recuperação de histórico de conversa na contextualização da resposta
def store(user_id, role, message):
    collection = f"message_history_{user_id}"
    try:
        doc_ref = db.collection(collection).document()
        doc_ref.set({
            "timestamp": int(time.time()),
            "role": role,
            "parts": [message]
        })    
    except Exception as e:
        print(f"Erro ao salvar mensagem no banco de dados. Detalhes: {e}")
        return False
```

### Conclusão

O Robô Educa combina criatividade física com inteligência artificial de ponta para criar uma experiência interativa e educacional para crianças. A arquitetura modular da plataforma e o uso de tecnologias web modernas a tornam escalável, segura e adaptável a diversos ambientes de aprendizado.

## ✍️ Como executar este aplicativo em seu PC Windows

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
## ☁️ Como realizar deploy no ambiente de nuvem da Google (Cloud Run)
![Google Cloud](https://img.shields.io/badge/Google_Cloud-gray?style=for-the-badge&logo=google-cloud)
* No console da Google Cloud Platform, crie um Projeto 
* Certifique-se de ter instalado em seu PC Windows a CLI gcloud (Google Cloud SDK Shell)
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
    * IAM e Administrador / Contas de Serviço / Clicar na conta de Serviço: **Default compute service account**
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

## 📄 Licença

Este projeto está licenciado sob a [Apache 2.0 License](LICENSE). Observe também os Termos de Serviço.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request ou colaborar de qualquer outra forma.

* Contatos/WhatsApp: +55 (71) 9.9341-6896 
* E-mail: roboeduca.net@gmail.com

<div style="display: flex;">
<img src="static/images/ods1.jpg" alt="Ods 4" style="width: 30%; margin-right: 5px;">
<img src="static/images/ods2.jpg" alt="ODS ONU" style="width: 30%; margin-right: 5px;">
<img src="static/images/ods3.jpg" alt="Ods 10" style="width: 30%;">
</div>