<div align="center">
<img src="static/images/logo.png" alt="Logo">
</div>

![English](https://img.shields.io/badge/Language-English-blue)

## 🤓  Learn to Code by Building Your Own Robot.

**Robô Educa** is an innovative platform that teaches programming to children aged 6 to 14, promoting inclusion and sustainability ♻️. The journey begins with an inspiring story of two siblings, Suzy and Otávio, who wish to build a robot 🤖 and receive help from their teacher Carlos Sales 👨‍🏫. He encourages them to create their own humanoid robot using recycled materials, programming, and cloud technology ♻️💻☁️.

It is in this context that the Robô Educa Web App emerges. Accessible from any smartphone 📱, it becomes the "brain" of the robot 🧠, interacting with the child through audio messages 🗣️, making it accessible even to individuals with visual impairments. Assembling the robot and interacting with the app stimulate motor coordination 🖐️ and creativity ✨, teaching children technological concepts in a playful and inclusive way.

And all the magic performed by the app is made possible by the **Google GEMINI API** 🤖, which allows Robô Educa to understand and respond to children's questions, explain complex concepts 🤯, and conduct gamified quizzes 🎉. This technology available on Google's cloud transforms learning into a natural and fun conversation 😄, opening new perspectives for these children's future 🚀.

## 🤖 How to Test the App:

* Visit: https://robo-educa-gemini-server-xd3gd6y2aa-uw.a.run.app/
* Click on Start;
* Allow microphone access;
* Click on: ENTER AS GUEST;
* Listen to the questions and answer correctly to earn points.

## 📆 History

<div align="center">
<img src="static/images/robopet.jpg" alt="Logo">
</div>

Artificial intelligence is increasingly present in our lives, making it necessary to encourage as many people as possible to take their first steps in understanding this technology, allowing them to become not only users but also protagonists in creating new resources for this technology in the future.

It was with this thought that the Robô Educa project was launched in 2018. It is an inclusive platform for Programming Education where children take their first steps in this universe by building their own robot. At that time, the robot was made from PET bottles and some electronic components such as Arduino, LEDs, resistors, and batteries.

But it was only in 2024, with the advent of Generative AI and the Google GEMINI API, that the robot gained a "brain" capable of responding in an intelligent and rapid manner, making interaction with the child smooth and delightful 😄!

The creator of this project, [Carlos Sales](https://drive.google.com/file/d/1KPPJQhNn_YsWYK6qllP6muns6WlSRyM1/view?usp=sharing), is a Black man from a disadvantaged background, graduated in Data Science and Systems Development. He shares some of his story in the documentary [C0d3rs Championship](https://www.primevideo.com/detail/0GS98CG03BVM7C224YK7KIWXOJ) available on Amazon Prime Video.

<div style="display: flex;">
<img src="static/images/image1.jpg" alt="Imagem 1" style="width: 22%; margin-right: 8px;">
<img src="static/images/image2.jpg" alt="Imagem 2" style="width: 22%; margin-right: 8px;">
<img src="static/images/image3.jpg" alt="Imagem 3" style="width: 22%; margin-right: 8px;">
<img src="static/images/image4.jpg" alt="Imagem 4" style="width: 22%;">
</div>

## 💪 Impact

Using only a few LEDs, resistors, and batteries, we have impacted hundreds of children in various communities in our city.

With the use of generative artificial intelligence and cloud technology, new possibilities for expanding our robot's cognitive abilities arise. We hope to reach an even larger number of children, now **around the world!**

Visit our [photo gallery](https://photos.app.goo.gl/yJiewdTTsNFtmF846) to learn more about our inclusion workshops conducted in underserved communities in Salvador, Bahia - Brazil.

💪 And you? Did you like it? Then do your part and contribute to this initiative so we can expand our impact even further.

## 💻 Technologies Used in This App

<div align="center">
<img src="static/images/gemini.png" alt="Logo Gemini API">
</div>

- ![Pyton](https://img.shields.io/badge/python-v3-green)
- ![HTML](https://img.shields.io/badge/HTML-5-orange)
- ![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow)
- ![Firestore](https://img.shields.io/badge/Firebase-Firestore-orange?style=for-the-badge&logo=firebase)
- ![Google Cloud](https://img.shields.io/badge/Google_Cloud-gray?style=for-the-badge&logo=google-cloud)

## ✍️ How to Run This App on Your Windows PC

1. Clone the repository:
```
$ git clone https://github.com/Robo-Educa/robo-educa-gemini-server.git 
```
2. Install dependencies:
```
$ cd robo-educa-gemini-server
$ pip install -r requirements.txt
```
3. Create a .ENV file from .ENV.EXAMPLE and fill in the environment variable values according to your project.

4. Run the project:
```
$ python main.py
```
5. Test in the Browser:
```
http://localhost:5000
```

## ☁️ How to Deploy on Google Cloud (Cloud Run)

![Google Cloud](https://img.shields.io/badge/Google_Cloud-gray?style=for-the-badge&logo=google-cloud)

* In the Google Cloud Platform console, create a Project.
* Make sure you have the gcloud CLI (Google Cloud SDK Shell) installed on your Windows PC.
* In a Google Cloud SDK Shell terminal, navigate to the folder where your project is located and initialize your connection by providing your email, project, and default region for hosting your App:
```
$ cd\[path do projeto]
$ gcloud init
```
* Deploy your App:
```
$ gcloud run deploy --source .
```
* In the Google Cloud Platform console, select your project.
* In the navigation menu, select: FireBase-Firestore
* Create a Native Database
* Download a JSON file containing access credentials for your database:
    * IAM & Admin / Service Accounts / Click on the Service Account: Default compute service account
    * Keys / Add Key / Create New Key / JSON / Create
    * The JSON file will be automatically downloaded.
* In the navigation menu, select: Google Cloud Storage
* Create a private Bucket. Save the JSON file containing database access credentials in this Bucket.
* In the navigation menu, select: Cloud Run
* Click on the Application
* Click on: "Edit and deploy a new version"
    * Click on Volumes / Add a Volume referring to the Bucket containing the database credentials
    * Type: Cloud Storage Bucket
    * Go to the Containers tab / Volume Mounting / Mount Volume
    * Select the name of the created volume
    * Mount Path: specify a name that will serve as a path. E.g., /config
    * Finish / Deploy
* Click again on: Edit and deploy a new version
* Variables and Secrets / Add the same variables contained in the .ENV.example file
    * Note the variable PATH_CREDENTIAL_FIRESTORE should contain the path to the newly created volume. E.g., /config/credential.json
    * Note the variable API_KEY should contain a valid key that can be obtained from: https://aistudio.google.com
* Caution: Be careful with the JSON file containing the database access credentials and your Gemini API_KEY. Never expose them publicly; use secrets or other security measures recommended by Google Cloud.

## 📄 License

This project is licensed under the [Apache 2.0 License](LICENSE). Also, see the Terms of Service.

## 🤝 Contributions

Contributions are welcome! Feel free to open a pull request or contribute in any other way.

* Contacts/WhatsApp: +55 (71) 9.9341-6896
* E-mail: roboeduca.net@gmail.com

<div style="display: flex;">
<img src="static/images/ods1.jpg" alt="Ods 4" style="width: 30%; margin-right: 5px;">
<img src="static/images/ods2.jpg" alt="ODS ONU" style="width: 30%; margin-right: 5px;">
<img src="static/images/ods3.jpg" alt="Ods 10" style="width: 30%;">
</div>

<hr>

<div align="center">
<img src="static/images/logo.png" alt="Logo">
</div>

![Portuguese](https://img.shields.io/badge/Language-Portuguese-brightgreen)

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