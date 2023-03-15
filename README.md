## Accenture - Gama Academy - Mulheres em Tech - Data Engineer/Azure

### Grupo 3 

<ul>
    <li>
        <a href="https://www.linkedin.com/in/emillysantiago23/">
            Emilly Correa Santiago
        </a>
    </li>
    <li>
        <a href="https://github.com/Queirozaps/">
            Ana Paula Santos de Queiroz
        </a>
    </li>
</ul>

### Apresentação do problema

Desenvolver uma aplicação em Python para carga de arquivos em um banco de dados SQL e gerar relatórios estatísticos visando a descoberta de fraudes em conta correntede cartão de crédito.
<br>
Link do desafio: https://docs.google.com/document/d/10fBZm7Sxm60FEIyNk4rqUE-pJLhXRxDi1grAATF7hVw/edit

### Objetivo

Seu objetivo inicial é analisar estes arquivos criando uma base de dados relacional para fazer a carga e depois analisá-la. O cartão fraudado, será aquele que tiver movimentações abaixo de 2 minutos de espaçamento entre as transações.

### Analisando o problema:

<ul>
    <li>Brainstorm: https://whimsical.com/projeto-final-5zim4iYZrkWQ2Dbpy2knML</li>
    <li>Atribuição das atividades: https://trello.com/b/4JhJb0Iz/project-data-azure-desafio-final</li>
</ul>

### Modelagem dos dados enviados ao Banco SQL
![image](https://user-images.githubusercontent.com/70452464/225104839-128e92fd-3fd5-45ab-a5e3-4a361d39d98c.png)

### Fluxograma dos csvs manipulados com pandas
![image](https://user-images.githubusercontent.com/70452464/225104278-53620e29-1e7b-486a-870a-6ded04cb18e4.png)

### Principais ferramentas utilizadas

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
    <li>Instale as bibliotecas do requirements.txt. Principalmente o pandas e o podbc.</li>
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

A classe intercept é responsável por encontrar as fraudes entre transações realizadas em menos de 2 minutos. Dentro dessa classe temos métodos que interceptam fraude de clientes e de transações. Essas funções fazem a leitura do csv com todas as transações, ordena elas pelo id do cliente e data e agrupa os clientes. Para cada cliente e verificado o tempo entre as transações com a função diff e sendo menor q 2 minutos é incluida nas fraudes. Nessa função a biblioteca pandas é usada para ler arquivos csv, criar dataframes, concatenar tabelas, converter formatos de datas.

#### 5 - Criando um servidor na Azure
![image](https://user-images.githubusercontent.com/70452464/225177156-8a02b07e-2023-4f33-a770-c008fb54bdec.png)
obs:  Lembre de adicionar o firewall do ip da máquina que vai acessar o servidor

#### 6 - Fazer a conexão com banco

<ol>
    <li>pip install pyodbc</li>
    <li>instalção do drive 18: https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver15</li>
    <li>Configurar a conexão com senha e login</li>
</ol>

#### 7 - Criar a lógica para inserir os dados no banco 

Dentro da classe connectionDB() temos as funções de conectar com o banco, criar tabelas se não existir, inserir dados se não existir e fechar conexão. Dessa forma buscamos separar as responsabilidades de cada função. Além disso usamos orientação a objeto para encapsular as funções do banco. Também optamos por usar um try except para identificar possíveis problemas. 
