Sumário
- [Testes](#testes)
  - [Execução dos testes](#execução-dos-testes)
  - [Ambiente](#ambiente)
    - [Ambiente linux](#ambiente-linux)
      - [Configuração do Git e do Github](#configuração-do-git-e-do-github)
        - [Dados da conta Github no Git](#dados-da-conta-github-no-git)
      - [Dependências do Linux](#dependências-do-linux)
        - [libpq-dev](#libpq-dev)
        - [Python 3.12](#python-312)
          - [PIP](#pip)
          - [Ambiente Virtual](#ambiente-virtual)
          - [Poetry](#poetry)
  - [Executar os testes](#executar-os-testes)
  - [AWS\_Connections\_test](#aws_connections_test)
  - [Settings\_test](#settings_test)
    - [Funções de preparação para os testes:](#funções-de-preparação-para-os-testes)
    - [Testes realizados](#testes-realizados)
  - [Postgres\_Connection\_test.py](#postgres_connection_testpy)
    - [Uso de Mocks](#uso-de-mocks)
    - [Cenários Testados](#cenários-testados)

# Testes
Aqui será documentado cada arquivo de teste da pasta etl. Para cada arquivo haverá uma seção específica para descrever o código.

## Execução dos testes
Antes de executar os testes, é necessário definir a configuração do ambiente a fim de evitar possíveis erros.

## Ambiente 
Os testes foram realizados utilizando o ambiente linux (Ubuntu 22.04.5 LTS) a fim de evitar erros de importação.

### Ambiente linux
Caso o ambiente linux tenha sido recém instalado. Será necessário realizar as seguintes configurações:


#### Configuração do Git e do Github
Para adicionar esse repositório no ambiente linux, será necessário clona-lo. Para isso, será necessário se conectar com uma conta do GitHub

##### Dados da conta Github no Git
Inicialmente, será necessário inserir seu nome de usuário e email. Isso servirá para assinar os commits que serão feitos.

1. `git config --global user.name "Seu Nome"`
2. `git config --global user.email "seu.email@example.com"`

É possível observaer se as configurações entraram em vigor com `git config --list`

Após isso, para clonar o repositório basta utilizar o comando `git clone https://github.com/Inteli-College/2024-2B-T10-SI08-G04`. Ao enviar esse comando pela primeira vez, ele irá pedir o nome de usuário do github e a senha. Para a senha, será necessário enviar um _classic token_ do GItHub, disponível na _developer settings_ das configurações.

#### Dependências do Linux
Inicialmente, é necessário atualizar as bibliotecas instaladas no Linux, para isso digite:

```
sudo apt update && sudo apt upgrade -y
```

##### libpq-dev
Algumas das bibliotecas utilizadas pelo Python dependem dessa biblioteca do Linux. Para instala-la utilize:

```
sudo apt-get install libpq-dev
```

##### Python 3.12

Após isso, será necessário verificar se o python3 já foi instalado. Para isso, execute 

```
python3 --version
```

Caso apareça que o comando não existe, será necessário instalar as bibliotecas necessárias para o python compilar com:

```
sudo apt install -y software-properties-common
```

Após isso, será necessário instalar o python com:

```
sudo add-apt-repository ppa:deadsnakes/ppa && \
sudo apt install -y python3.12 && \
python3.12 --version
```

Desse modo, o python será instalado corretamente

###### PIP

Para instalar o gerenciador de pacotes do Python, o pip. Será necessário executar o seguinte comando:

```
sudo apt install python3-pip
```

###### Ambiente Virtual

Para que não haja conflitos com o gerenciador de pacotes do linux. Será necessário criar utilizar o pipx para gerenciar as dependências de forma local:

```
sudo apt install pipx
```

Sempre que for instalar uma dependência, utilize
```
pipx install [nome do pacote]
```

###### Poetry

Utilize seguinte comando para instalar o poetry:

```
pipx install poetry
```

Agora, será necessário entrar na pasta src para instalar as dependências de pyproject.toml
```
cd ./src && \
poetry install
```

## Executar os testes

Para rodar os testes, basta executar os seguintes comandos
1. ```cd ./src```
2. ```poetry install```
3. ```poetry run pytest -v```

Assim ele irá rodar todos os arquivos que contenham o prefixo _test\__ ou o sufixo _\_test_. Caso haja algum erro de dependência do sistema, será necessário 


## [AWS_Connections_test](./AWS_Connections_test.py)

O objetivo desse arquivo é testar se a classe Connections está realizando corretamente as conexões com a AWS a partir da função _get_s3_client_. Para isso, a comunicação com a AWS é substituida por um Mock da biblioteca moto. Além disso, é necessário substituir a leitura das variáveis de ambiente do sistema para as que temos controle. Portanto, foi utilizado o Mock built-in do python para sobreescrever o comportamento de settings durante o teste.

Para realizar os testes, foram definidos as seguintes funções de preparação dos testes:

1. s3_env: ela preenche todas as variáveis de ambientes importadas por settings por strings falsas para que o teste execute.
```
@pytest.fixture
def s3_env(self, mocker):
    mock_response = Mock()
    mock_response.AWS_ACCESS_KEY = 'fake_access_key'
    mock_response.AWS_SECRET_KEY = 'fake_secret_key'
    mock_response.AWS_SESSION_TOKEN = 'fake_session_token'
    mock_response.AWS_REGION = 'us-east-1'
    
    mocker.patch('config.Settings.UseSettings.get_settings', return_value=mock_response)
```
2. s3_connection: Essa função irá criar uma conexão falsa com a aws utilizando das variáveis definidas em s3_env. Além disso, irá criar um bucket chamado _my-test-bucket_.
```
@pytest.fixture
def s3_connection(self, s3_env):
    with mock_aws():
        client = Connections.get_s3_client()
        client.create_bucket(Bucket='my-test-bucket')
        yield client
```
3. s3_env_without_access_key: essa função irá inicializar as variáveis de ambiente necessárias para a conexão com a AWS, exceto a AWS_ACCESS_KEY que será None.
```
@pytest.fixture
def s3_env_without_access_key(self, mocker):
    mock_response = Mock()
    mock_response.AWS_ACCESS_KEY = None
    mock_response.AWS_SECRET_KEY = 'fake_secret_key'
    mock_response.AWS_SESSION_TOKEN = 'fake_session_token'
    mock_response.AWS_REGION = 'us-east-1'
    
    mocker.patch('config.Settings.UseSettings.get_settings', return_value=mock_response)
```
A partir dessas funções é possível executar os seguintes testes:

1. test_s3_connection_with_all_data: Esse teste irá verificar se a conexão com a AWS foi criada, se há o atributo _list\_buckets_ e se o bucket _my-test-bucket_ foi criado.

```
def test_s3_connection_with_all_data(self, s3_connection):
    assert s3_connection is not None
    assert hasattr(s3_connection, 'list_buckets')
    
    response = s3_connection.list_buckets()
    buckets = [bucket['Name'] for bucket in response['Buckets']]
    assert 'my-test-bucket' in buckets
```
2. O teste _test_s3_connection_without_access_key_ irá verificar se a conexão com AWS não será feita devido a falta do ambiente _AWS\_ACCESS\_KEY_.
```
def test_s3_connection_without_access_key(self, s3_env_without_access_key):
    with pytest.raises(PartialCredentialsError):
        Connections.get_s3_client()
```

## [Settings_test](./Settings_test.py)

O objetivo deste arquivo é testar a classe **UseSettings** para garantir que as configurações do sistema (variáveis de ambiente) sejam lidas corretamente. Utilizamos o **pytest** para realizar os testes, onde as variáveis de ambiente são simuladas com o **monkeypatch** do pytest. Esse método permite substituir os valores das variáveis de ambiente durante a execução dos testes.

### Funções de preparação para os testes:

1. **successful_env*: Esta função define variáveis de ambiente com valores válidos para AWS, ClickHouse, PostgreSQL e outras configurações necessárias para o teste.
   
```
@pytest.fixture
def successful_env(self, monkeypatch):
    monkeypatch.setenv('AWS_ACCESS_KEY', 'valid_access_key')
    monkeypatch.setenv('AWS_SECRET_KEY', 'valid_secret_key')
    monkeypatch.setenv('AWS_SESSION_TOKEN', 'valid_session_token')
    monkeypatch.setenv('AWS_REGION', 'us-east-1')
    monkeypatch.setenv('CLICKHOUSE_HOST', 'valid_clickhouse_host')
    monkeypatch.setenv('CLICKHOUSE_PORT', '9000')
    monkeypatch.setenv('CLICKHOUSE_USER', 'valid_user')
    monkeypatch.setenv('CLICKHOUSE_PASSWORD', 'valid_password')
    monkeypatch.setenv('POSTGRES_HOST', 'valid_postgres_host')
    monkeypatch.setenv('POSTGRES_PORT', '5432')
    monkeypatch.setenv('POSTGRES_DB', 'valid_db')
    monkeypatch.setenv('POSTGRES_USER', 'valid_user')
    monkeypatch.setenv('POSTGRES_PASSWORD', 'valid_password')
    monkeypatch.setenv('BUCKET_NAME', 'valid_user')
    monkeypatch.setenv('AUTH_TOKEN', 'valid_password')
```
2. **incomplete_env**: Esta função define as mesmas variáveis de ambiente que a successful_env, exceto para a variável POSTGRES_PASSWORD, que é definida como None, simulando um cenário onde uma configuração está faltando.
```
@pytest.fixture
def incomplete_env(self, monkeypatch):
    monkeypatch.setenv('AWS_ACCESS_KEY', 'valid_access_key')
    monkeypatch.setenv('AWS_SECRET_KEY', 'valid_secret_key')
    monkeypatch.setenv('AWS_SESSION_TOKEN', 'valid_session_token')
    monkeypatch.setenv('AWS_REGION', 'us-east-1')
    monkeypatch.setenv('CLICKHOUSE_HOST', 'valid_clickhouse_host')
    monkeypatch.setenv('CLICKHOUSE_PORT', '9000')
    monkeypatch.setenv('CLICKHOUSE_USER', 'valid_user')
    monkeypatch.setenv('CLICKHOUSE_PASSWORD', 'valid_password')
    monkeypatch.setenv('POSTGRES_HOST', 'valid_postgres_host')
    monkeypatch.setenv('POSTGRES_PORT', '5432')
    monkeypatch.setenv('POSTGRES_DB', 'valid_db')
    monkeypatch.setenv('POSTGRES_USER', 'valid_user')
    monkeypatch.setenv('POSTGRES_PASSWORD', None)
    monkeypatch.setenv('BUCKET_NAME', 'valid_user')
```

### Testes realizados

1. test_get_settings_success: Este teste verifica se todas as variáveis de ambiente são lidas corretamente quando configuradas com valores válidos. Ele confirma se as variáveis são atribuídas corretamente ao objeto de configurações.
```
def test_get_settings_success(self, successful_env):
    settings = UseSettings.get_settings()
    assert settings.AWS_ACCESS_KEY == 'valid_access_key'
    assert settings.AWS_SECRET_KEY == 'valid_secret_key'
    assert settings.AWS_SESSION_TOKEN == 'valid_session_token'
    assert settings.AWS_REGION == 'us-east-1'
    assert settings.CLICKHOUSE_HOST == 'valid_clickhouse_host'
    assert settings.CLICKHOUSE_PORT == 9000
    assert settings.CLICKHOUSE_USER == 'valid_user'
    assert settings.CLICKHOUSE_PASSWORD == 'valid_password'
    assert settings.POSTGRES_HOST == 'valid_postgres_host'
    assert settings.POSTGRES_PORT == 5432
    assert settings.POSTGRES_DB == 'valid_db'
    assert settings.POSTGRES_USER == 'valid_user'
    assert settings.POSTGRES_PASSWORD == 'valid_password'
    assert settings.BUCKET_NAME == 'valid_user'
    assert settings.AUTH_TOKEN == 'valid_password'
```

2. test_get_settings_failure: Este teste verifica se ocorre um erro (lançamento de ValidationError) quando uma variável de ambiente necessária não é configurada corretamente. Neste caso, a variável POSTGRES_PASSWORD é definida como None na fixture incomplete_env.
   
```
def test_get_settings_failure(self, incomplete_env):
    with pytest.raises(ValidationError):
        settings = UseSettings.get_settings()
```

## Postgres_Connection_test.py

A função testada é `Connections.get_postgres_connection()`, que tenta estabelecer uma conexão com um banco de dados PostgreSQL usando configurações fornecidas (host, porta, nome do banco, usuário e senha).

O padrão **AAA** *(Arrange, Act, Assert)* foi utilizado para estruturar os testes:

1. **Arrange**: Configura o ambiente de teste, inicializando objetos e configurando mocks.
2. **Act**: Executa a ação que está sendo testada.
3. **Assert**: Verifica se o resultado da ação é o esperado.

### Uso de Mocks

Mocks substituem:
- `psycopg2.connect()`: Simula a conexão com o banco.
- `get_settings()` da classe `UseSettings`: Retorna as configurações necessárias.

### Cenários Testados

1. **Conexão bem-sucedida (`test_postgres_connection_successful`)**  
   Verifica se a conexão é estabelecida corretamente com configurações válidas.

2. **Falha na conexão (`test_postgres_connection_failure`)**  
   Simula configurações inválidas para garantir que uma exceção `OperationalError` seja lançada.

Esses mocks permitem testar os cenários com confiabilidade, sem depender de um banco de dados real.
