# Reconhecimento Facial e transformação de imagens em Dados no Azure ML

1. Acessar a página inicial da azure no link: https://portal.azure.com, e clicar em "Criar um recurso".
![Página Inicial da Azure](images/img-1.jpg)

<br>

2. No menu de opções na lateral esquerda, clicar em "IA + Machine Learning".
![Menu lateral da Azure](images/img-2.jpg)

<br>

3. Na opção "Serviços Cognitivos" clicar em "Criar".
![Serviços Cognitivos da Azure](images/img-3.jpg)

<br>

4. Em "Detalhes do projeto", não alterar a opção de assinatura. Em "Grupo de recursos" escolha um já criado ou crie um novo no botão abaixo "Criar novo".
![Detalhes do projeto](images/img-4.jpg)

<br>

5. Descendo a tela, temos os detalhes da instância, é recomendado não utilizar servidores da região do Brasil, por questões de instabilidade, aqui utilize a já indicada pela Azure ou "East US". Em "Nome" coloque um nome de sua preferência. Em "Tipo de preço" escolha a opção padrão. E confirme a checkbox sobre os preços abaixo.  
![Detalhes da instância](images/img-5.jpg)

<br>

6. Revise tudo e clique no botão "Examinar + criar" na lateral inferior esquerda
![Botão Examinar + Criar](images/img-6.jpg)

<br>

7. Você será redirecionado a outra página com os termos, clique em "Criar" na lateral inferior esquerda
![Tela Examinar + Criar](images/img-7.jpg)

<br>

8. Após ser redirecionado, deve aparecer um card de exito. Após isso acesse: https://portal.vision.cognitive.azure.com. (Talvez seja necessário refazer o login de sua conta)
![Tela de implantação concluida](images/img-8.jpg)

<br>

9. Na tela inicial do Vision Studio, clique em "View all resources".
![Tela inicial do Vision Studio](images/img-9.jpg)

<br>

10. Selecione o recurso criado na checkbox a esquerda do nome dele. E aperte em "Select as default resource". Ele não vai indicar nenhum feedback, então pode fechar a tela no botão na lateral superior direita.
![Recurso como default](images/img-10.jpg)

<br>

11. Ao retornar a tela inicial, clique na seção "Face".
![Seção Face](images/img-11.jpg)

<br>

12. Clique no card "Detect faces in image"
![Detect faces in image](images/img-12.jpg)

<br>

13. Clique no checkbox para reconhecer o uso de recursos.
![Reconhecer uso de recurso](images/img-13.jpg)

<br>

14. É possível utilizar o recurso colocando uma imagem própria, clicando em "Browse for a file", onde ele pedirá uma foto do seu computador, em "Take a photo", onde ele tirará uma foto na hora. Ou também é possível utilizar uma das fotos pré selecionadas ao lado.
![Teste de imagens](images/img-14.jpg)

<br>

15. Na opção "Detected attributes" ele indica a quantidade de rostos na imagem, em "JSON" ele mostra o código de identificação facial.
<p align="center">
 <img src="images/img-15.jpg" alt="Atributos Detectados" width="400"/>
 <img src="images/img-16.jpg" alt="JSON de Identificação Facial" width="400"/>
</p>
