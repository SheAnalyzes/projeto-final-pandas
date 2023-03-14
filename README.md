
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
#### Criando um ambiente virtual no windows:

<ol>
  <li>Na pasta do projeto, digite no terminal: python -m venv venv</li>
  <li>Ativando a venv: venv\Scripts\activate</li>
  <li>Verificando se está com a ultima versão do pip: python -m pip install --upgrade pip</li>
</ol>

#### Instalando as bibliotecas

<ol>
    <li>Instalação do Pandas: pip install pandas</li>
    <li>Criação do gitignore e adicionando a venv nele</li>
    <li>Salvando as versoes usadas: pip freeze > requirements.txt</li>
</ol>

#### Criação das funções que fazem a leitura do csv

#### Criar a lógica para gerar o relatório de fraude

#### Fazer a conexão com banco

<ol>
    <li>pip install pyodbc</li>
    <li>instalção do drive 18: https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver15</li>
    <li>Configurar a conexão com senha e login</li>
</ol>

##### Criar a lógica para inserir os dados no banco 