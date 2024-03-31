# Análise de Linguagem no Language Studio

1. Acesse a página inicial da azure no link: https://portal.azure.com, e clique em "Criar um recurso".
![Página Inicial da Azure](images/img-1.jpg)

<br>

2. No menu de opções na lateral esquerda, clique em "IA + Machine Learning".
![Menu lateral da Azure](images/img-2.jpg)

<br>

3. Na opção "Análise de Texto" clique em "Criar".
![Serviços Cognitivos da Azure](images/img-3.jpg)

<br>

4. Na tela "Select additional features" clique em "Continue to create your resourse"
![Detalhes do projeto](images/img-4.jpg)

<br>

5. Em "Detalhes do projeto", não altere a opção de assinatura. Em "Grupo de recursos" escolha um já criado ou crie um novo no botão abaixo "Criar novo".
![Detalhes do projeto](images/img-5.jpg)

<br>

6. Descendo a tela, temos os detalhes da instância, é recomendado não utilizar servidores da região do Brasil, por questões de instabilidade, aqui utilize a já indicada pela Azure ou "East US". Em "Nome" coloque um nome de sua preferência. Em "Tipo de preço" escolha a opção "Free F0". E confirme a checkbox abaixo sobre os termos de uso.
![Detalhes da instância](images/img-6.jpg)

<br>

7. Revise tudo e clique no botão "Examinar + criar" na lateral inferior esquerda
![Botão Examinar + Criar](images/img-7.jpg)

<br>

8. Você será redirecionado a outra página com os termos, clique em "Criar" na lateral inferior esquerda
![Tela Examinar + Criar](images/img-8.jpg)

<br>

9. Após ser redirecionado, deve aparecer um card de exito. Acesse: https://language.cognitive.azure.com. (Talvez seja necessário refazer o login de sua conta)
![Tela de implantação concluida](images/img-9.jpg)

<br>

10. Ao acessar o Language Studio, deve aparecer um formulário para a identificação do recurso. Mantenha o diretório que ele já identificou, selecione sua assinatura padrão e mantenha a opção "Language". Em "Resource Name" escolha o recurso criado.
![Formulário do Language Studio](images/img-10.jpg)

<br>

11. Na tela inicial do Language Studio, vá até a seção "Classify text". 
![Tela Inicial do Language Studio](images/img-11.jpg)

<br>

12. Clique no card "Analyze sentiment and mine opinions"
![Detect faces in image](images/img-12.jpg)

<br>

13. Selecione a linguagem do texto que irá colocar e mantenha o recurso da linguagem selecionado.
![Teste de imagens](images/img-13.jpg)

<br>

14. É possível colocar um texto na caixa maior de escrita, subir um arquivo de texto, ou escolher entre alguns dos templates já pré selecionados pela Azure.
![Teste de imagens](images/img-14.jpg)

<br>

15. Coloque o texto que deseja testar, marque a chckbox de utilização de recursos e clique em "Run".
![Teste de imagens](images/img-15.jpg)

<br>

16. Abaixo ele gera o resultado da análise na seção "Result", e separa uma análise individual para cada uma das sentenças identificadas.
![Teste de imagens](images/img-16.jpg)

<br>

17. Na seção "JSON" ele coloca o código da análise em JSON.
![Teste de imagens](images/img-17.jpg)

<br>