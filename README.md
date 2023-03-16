# Accenture - Gama Academy - Mulheres em Tech - Data Engineer/Azure - Pandas

Este é o repositório da versão do projeto em Pandas.

Para retornar ao repositório geral, clique [aqui](https://github.com/SheAnalyzes/readme-repository)!

## Índice

- [Apresentação do problema](#apresentação-do-problema)
- [Objetivo](#objetivo)
- [Analisando o problema](#analisando-o-problema)
- [Modelagem dos dados enviados ao Banco SQL](#modelagem-dos-dados-enviados-ao-banco-sql)
- [Fluxograma dos csvs manipulados com pandas](#fluxograma-dos-csvs-manipulados-com-pandas)
- [Tecnologias utilizadas](#tecnologias-utilizadas)
- [Passo a passo para rodar o projeto](#passo-a-passo-para-rodar-o-projeto)
- [Passo a passo da criação do projeto](#passo-a-passo-da-criação-do-projeto)
- [Grupo - SheAnalyses](#grupo---sheanalyses)

### Apresentação do problema

Desenvolver uma aplicação em Python para carga de arquivos em um banco de dados SQL e gerar relatórios estatísticos visando a descoberta de fraudes em conta correntede cartão de crédito.
<br>
Link do desafio: https://docs.google.com/document/d/10fBZm7Sxm60FEIyNk4rqUE-pJLhXRxDi1grAATF7hVw/edit

### Objetivo

Seu objetivo inicial é analisar estes arquivos criando uma base de dados relacional para fazer a carga e depois analisá-la. O cartão fraudado, será aquele que tiver movimentações abaixo de 2 minutos de espaçamento entre as transações.

### Analisando o problema

<ul>
    <li>Brainstorm: https://whimsical.com/projeto-final-5zim4iYZrkWQ2Dbpy2knML</li>
    <li>Atribuição das atividades: https://trello.com/b/4JhJb0Iz/project-data-azure-desafio-final</li>
</ul>

### Modelagem dos dados enviados ao Banco SQL
![image](https://user-images.githubusercontent.com/70452464/225104839-128e92fd-3fd5-45ab-a5e3-4a361d39d98c.png)

### Fluxograma dos csvs manipulados com pandas
![image](https://user-images.githubusercontent.com/70452464/225104278-53620e29-1e7b-486a-870a-6ded04cb18e4.png)

### Tecnologias utilizadas

<ul>
    <li>Python</li>
    <li>Git</li>
    <li>SQL</li>
    <li>Trello</li>
    <li>Banco de Dados - Azure</li>
</ul>

### Passo a passo para rodar o projeto

<ol>
    <li>Faça um clone do repositorio na sua maquina</li>
    <li>Instale a venv na pasta do projeto: python -m venv venv  e ative com o comando: venv\Scripts\activate.</li>
    <li>Instale as bibliotecas do requirements.txt. Principalmente o pandas, podbc.</li>
    <li>Coloque as configurações do seu banco de Dados na pasta connectionDB.</li>
    <li>Na pasta do projeto rode o comando pelo terminal: python main.py para iniciar o projeto.</li>
    <li>Pronto! Pelo terminal, digite alguma das opções apresentadas no menu.</li>
</ol>

### Passo a passo da criação do projeto
#### 1 - Criando um ambiente virtual no windows:

<ol>
  <li>Na pasta do projeto, digite no terminal: python -m venv venv</li>
  <li>Ativando a venv: venv\Scripts\activate</li>
  <li>Verificando se está com a ultima versão do pip: python -m pip install --upgrade pip</li>
</ol>

#### 2 - Instalando as bibliotecas

<ol>
    <li>Instalação do Pandas: pip install pandas</li>
    <li>Criação do gitignore e adicionando a venv nele</li>
    <li>Salvando as versoes usadas: pip freeze > requirements.txt</li>
</ol>

#### 3 - Lendo todos os arquivos em csv

Dentro da pasta do projeto tem o arquivo readFile.py que possue a classe ReadFile(). Dentro dessa classe temos os métodos que fazem a leitura dos csv usando a biblioteca glob que permite listar arquivos de um diretório. Dessa forma, conseguimos juntar todos os csv com o prefixo clientes, por exemplo, em um só arquivo .csv.

#### 4 - Gerando relatório de fraude

A classe intercept() é responsável por encontrar as fraudes entre transações realizadas em menos de 2 minutos. Dentro dessa classe temos métodos que interceptam fraude de clientes e de transações. Essas funções fazem a leitura do csv com todas as transações, ordena por id do cliente e data e agrupa os clientes. Para cada cliente e verificado o tempo entre as transações com a função diff e, sendo menor q 2 minutos, é incluida nas fraudes. Nessa função a biblioteca pandas é usada para ler arquivos csv, criar dataframes, converter formatos de datas, concatenar e mergear tabelas.

#### 5 - Criando um servidor na Azure
![image](https://user-images.githubusercontent.com/70452464/225177156-8a02b07e-2023-4f33-a770-c008fb54bdec.png)
obs:  Lembre de adicionar o firewall do ip da máquina que vai acessar o servidor

#### 6 - Fazer a conexão com banco

<ol>
    <li>pip install pyodbc</li>
    <li>instalção do drive 18: https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver15</li>
    <li>Instalação da biblioteca python-dotenv: pip install python-dotenv </li>
    <li>Configurar a conexão com senha e login</li>
</ol>

#### 7 - Criar a lógica para inserir os dados no banco 

Dentro da classe connectionDB() temos as funções de conectar com o banco, criar tabelas se não existir, inserir dados se não existir e fechar conexão. Dessa forma buscamos separar as responsabilidades de cada função. Além disso usamos orientação a objeto para encapsular as funções do banco. Também optamos por usar um try except para identificar possíveis problemas. 


### Grupo - SheAnalyses

![1678919788585](image/README/1678919788585.png)![1678922005355](image/README/1678922005355.png)

| Ana Paula Santos de Queiroz<br /><br />Linkedin: [/ana-paula-santos-de-queiroz-086807166](https://www.linkedin.com/in/ana-paula-santos-de-queiroz-086807166/)<br />Github: [/Queirozaps](https://github.com/Queirozaps) | ![1678913762981](image/README/1678913762981.png) |
| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------: |
|  **Arianna Silveira Santos**<br />  <br />Linkedin: [/arianna-silveira-aa474514b](https://www.linkedin.com/in/arianna-silveira-aa474514b/)<br />Github: [/AriannaSilveira](https://github.com/AriannaSilveira)  | ![1678880182631](image/README/1678880182631.png) |
|                            **Carolina Gois**<br /><br />Linkedin: [/carolina-gois](https://www.linkedin.com/in/carolina-gois/)<br />Github: [/carolgois](https://github.com/carolgois)                            | ![1678915457372](image/README/1678915457372.png) |
|                   **Emilly Correa Santiago**<br /><br />Linkedin: [/emillysantiago23](https://www.linkedin.com/in/emillysantiago23/)<br />Github: [/emillysant](https://github.com/emillysant)                   | ![1678881122291](image/README/1678881122291.png) |
|                              **Mariana Freire**<br /><br />Linkedin: [/maricf](https://www.linkedin.com/in/maricf/)<br />Github: [/marianafreire](https://github.com/marianafreire)                              | ![1678915794465](image/README/1678915794465.png) |
|             **Priscila Assumpção Fernandes**<br /><br />Linkedin: [/priscila-af](https://www.linkedin.com/in/priscila-af/)<br />Github: [/priscilaassumpcao](https://github.com/priscilaassumpcao)             | ![1678916901964](image/README/1678916901964.png) |
|                    **Vivian Medina**<br /><br />Linkedin: [/vivian-medina-b7250961](https://www.linkedin.com/in/vivian-medina-b7250961/)<br />Github: [/medinavi](https://github.com/medinavi)                    | ![1678885040168](image/README/1678885040168.png) |
