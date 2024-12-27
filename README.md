# Inteli - Instituto de Tecnologia e Liderança 

<p align="center">
<a href= "https://www.inteli.edu.br/"><img src="https://res.cloudinary.com/de8ca4say/image/upload/v1733257415/inteli_igd6f6.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0"></a>
</p>

# INTEGRAÇÃO, GERENCIAMENTO E ANÁLISE DE BIG DATA

## Quartzo

### Integrantes: 
- <a href="https://www.linkedin.com/in/celine-souza-1a38aa225?trk=blended-typeahead">Celine Souza</a>
- <a href="https://www.linkedin.com/in/joao-pedro-brandao/">João Pedro Brandão de Moura</a>
- <a href="https://www.linkedin.com/in/matheusmeendes/">Matheus Ferreira Mendes</a>
- <a href="https://www.linkedin.com/in/paulooctaviodepaula?trk=blended-typeahead">Paulo Octavio De Paula</a>
- <a href="https://www.linkedin.com/in/rafaella-bianca-cavalcante/">Rafaella Bianca Cavalcante</a>
- <a href="https://www.linkedin.com/in/stefano-parente/">Stefano Tamer Parente</a>
- <a href="https://www.linkedin.com/in/yan-m-coutinho/">Yan Mendonça Coutinho</a>

## 📝 Descrição

O projeto é denominado "Desenvolvimento de um Pipeline de Big Data" e tem como objetivo auxiliar a Companhia Paulista de Trens Metropolitanos (CPTM) a processar grandes volumes de dados de forma eficiente, otimizando a tomada de decisões operacionais e administrativas. A proposta é criar um pipeline de Big Data baseado em uma infraestrutura de nuvem, como a AWS, para realizar análises estatísticas e descritivas de dados armazenados em um Data Lake ou Data Warehouse.

## 📁 Estrutura de pastas
```
|--> assets\imagens
|--> document
|----> apresentação
|----> outros
|----> documentation.md
|----> README.md
|--> src
| README.md
```

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>assets</b>: Aqui estão os arquivos relacionados a parte gráfica do projeto, as imagens e vídeos que os representam. A subpasta <b>imagens</b> armazena mídias visuais.

- <b>document</b>: Aqui estão todos os documentos do projeto. A pasta <b>apresentação</b> contém o arquivos das apresentações realizadas durante as cinco Sprints Reviews. A pasta <b>outros</b> contém documentos complementares como diagramas e regras. Além disso, nesta pasta, há um README.md com a organização das entregas feitas durante as cinco sprints.

- <b>src</b>: Aqui estão todos os códigos do projeto.

- <b>README.md</b>: Arquivo que serve como guia e explicação geral sobre o projeto.

## 🔧 Guia de Instalação e Configuração do Projeto

Este guia foi criado para auxiliá-lo no processo de instalação e configuração do ambiente necessário para a execução do projeto.

### Pré-requisitos

Antes de começar, certifique-se de ter os seguintes softwares instalados no seu computador:

1. Python 3.12 ou superior: Linguagem base do projeto.
2. Docker: Ferramenta para criar e gerenciar contêineres.
3. Poetry: Gerenciador de dependências Python.
4. Prefect: Framework de orquestração de fluxos de trabalho.

### Passo a Passo de Instalação

#### 1. Instale Poetry e Prefect

Execute os seguintes comandos para instalar globalmente o Poetry e o Prefect no Python:

```
pip install poetry
pip install prefect
```

#### 2. Configure o Prefect Cloud

1. Crie uma conta ou faça login no Prefect Cloud
2. No terminal, execute o comando para se autenticar:

```
prefect cloud login
```

#### 3. Clone o Repositório do Projeto

No terminal, acesse o local onde deseja salvar o projeto e execute:

```
git clone https://github.com/Inteli-College/2024-2B-T10-SI08-G04.git
```

#### 4. Navegue até o Diretório do Projeto

Após clonar o repositório, entre no diretório principal do projeto:

```
cd 2024-2B-T10-SI08-G04
```

#### 5. Instale as Dependências do Projeto

Na raiz do repositório, instale as dependências utilizando o Poetry:

```
poetry install
```

#### 6. Configure o Ambiente Virtual

Ative o ambiente virtual gerenciado pelo Poetry:

```
poetry shell
```

Com o ambiente virtual ativo, todos os pacotes instalados estarão disponíveis.

### Configuração do Docker

#### DataAPP

Para configurar e rodar o DataAPP, siga os passos abaixo:

1. Entre na pasta `dataapp`:

```
cd ./dataapp
```

2. Copie o arquivo `.env.example` e renomeie-o para `.env`:

```
cp .env.example .env
```

3. Edite o arquivo `.env` para preencher as variáveis necessárias.

4. Construa a imagem Docker para o DataAPP:

```
docker build -t streamlit-app -f Dockerfile .
```

5. Execute o contêiner Docker:

```
docker run -p 5000:5000 --env-file .env streamlit-app
```

Após esses passos, a aplicação estará disponível em: http://localhost:5000/.

#### ETL

Para rodar os scripts de ETL, siga as etapas:

1. Acesse a pasta `etl_project`:

```
cd ./etl_project
```

2. Copie o arquivo `.env.example` e renomeie-o para `.env`:

```
cp .env.example .env
```

1. Entre da pasta dataapp `cd ./dataapp`
2. Copie o arquivo .env.example
3. Renomeie o arquivo .env.example para .env e preencha-o

#### Backend
Além dos comandos já mencionados, para rodar o backend será necessário executar essas ações:

4. Executar o comando 
   ```
   docker build -t streamlit-backend -f backend.Dockerfile .
   ```
   com o docker aberto
5. Após isso, será necessário executar 
    ```
    docker run -p 7000:7000 --env-file .env streamlit-backend
    ```
    com o docker aberto

Após esse passo, é possível acessar a aplicação em: `http://172.17.0.1:7000`. Lembre-se de colocar esse endereço no .env antes de executar o docker do frontend.

#### Frontend

4. Executar o comando 
   ```
   docker build -t streamlit-frontend -f frontend.Dockerfile .
   ```
   com o docker aberto
5. Após isso, será necessário executar 
    ```
    docker run -p 8501:8501 --env-file .env streamlit-frontend
    ```
    com o docker aberto

4. Construa a imagem Docker para o ETL:

```
docker build -f Dockerfile -t etl_project_image .
```

5. Execute o contêiner Docker para o ETL:

```
docker run --rm -it -p 5000:5000 -v [caminho do .prefect]:/root/.prefect --env-file .env etl_project_image
```

- Nota: Substitua `[caminho do .prefect]` pelo caminho da pasta `.prefect` no seu computador.

A aplicação estará acessível em: http://127.0.0.1:5000/.

### Execução dos Testes

Para realizar testes no projeto:

1. Certifique-se de que o ambiente virtual está ativo.
2. Entre na pasta desejada para testar (`dataapp` ou `etl_project`).
3. Instale as dependências (caso ainda não tenha feito):

```
poetry install
```

4. Execute os testes utilizando o `pytest`:

```
poetry run pytest -v
```

## Entregas de Sprint

O projeto é estruturado em 5 sprints, cada uma com entregáveis e objetivos específicos, que são detalhados abaixo:

#### Sprint 1: Entendimento do projeto

- [Entendimento do negócio](https://github.com/Inteli-College/2024-2B-T10-SI08-G04/blob/main/document/document.md#2-an%C3%A1lise-de-neg%C3%B3cios)
- [Entendimento de UX](https://github.com/Inteli-College/2024-2B-T10-SI08-G04/blob/main/document/document.md#1-experi%C3%AAncia-do-usu%C3%A1rio)
- [Data Model Canvas](https://github.com/Inteli-College/2024-2B-T10-SI08-G04/blob/main/document/document.md#4-explora%C3%A7%C3%A3o-de-dados)

#### Sprint 2: Protopipação e ingestão de dados

- [Prototipação em Baixa fidelidade](https://github.com/Inteli-College/2024-2B-T10-SI08-G04/blob/main/document/document.md#3-arquitetura-e-design-do-sistema)
- [Estrutura de Ingestão de Dados](https://github.com/Inteli-College/2024-2B-T10-SI08-G04/blob/main/document/document.md#42-relat%C3%B3rio-etl)

#### Sprint 3: Cubo de dados e Análises

- [Cubo de Dados Automatizado](https://github.com/Inteli-College/2024-2B-T10-SI08-G04/blob/main/document/document.md#7-cubo-de-dados-automatizado)
- [Documentação de análise de impacto ético](https://github.com/Inteli-College/2024-2B-T10-SI08-G04/blob/main/document/document.md#5-an%C3%A1lise-de-impacto-%C3%A9tico)

#### Sprint 4: DataApp e Infográfico

- [Infográfico](https://github.com/Inteli-College/2024-2B-T10-SI08-G04/blob/main/document/document.md#9-infogr%C3%A1fico)
- [DataApp](https://github.com/Inteli-College/2024-2B-T10-SI08-G04/tree/main/src/dataapp)
- [Análise financeira](https://github.com/Inteli-College/2024-2B-T10-SI08-G04/blob/main/document/document.md#10-an%C3%A1lise-financeira-do-projeto)

#### Sprint 5: Entrega final

- [Documentação final](https://github.com/Inteli-College/2024-2B-T10-SI08-G04/blob/main/document/document.md)
- [Apresentação final](https://github.com/Inteli-College/2024-2B-T10-SI08-G04/tree/main/document/apresentacao)
- [DataApp final](https://github.com/Inteli-College/2024-2B-T10-SI08-G04/tree/main/src/dataapp)

## 🗃 Histórico de lançamentos

* 0.1.0 - 25/10/2024
    * Primeira entrega: Personas, User Storys, Mapa de Jornada do Usuário, TAM, SAM, SOM, Canvas Proposta de Valor, Matriz de Risco e Data Model Canvas.
* 0.2.0 - 08/11/2024
    * Segunda entrega: Wireframe, ETL Bronze, Documentação do ETL e Diagrama UML
* 0.3.0 - 22/11/2024
    * Terceira entrega: Análise de Impacto Ético, Cubo de Dados automatizado e Documentação do Cubo de Dados
* 0.4.0 - 06/12/2024
    * Quarta entrega: Infográfico, DataAPP, Análise Financeira e Plano de comunicação
* 0.5.0 - 19/12/2024
    * Quinta entrega: Apresentação final, Documentação da solução e Versão final do DataAPP
	
## 📋 Licença/License

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/2023M6T4-Inteli">INTEGRAÇÃO, GERENCIAMENTO E ANÁLISE DE BIG DATA</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/InteliProjects">Inteli</a>, <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/Inteli-College/2024-2B-T10-SI08-G04">Quartzo</a>: <a href="https://www.linkedin.com/in/celine-souza-1a38aa225?trk=blended-typeahead">Celine Souza</a>, <a href="https://www.linkedin.com/in/joao-pedro-brandao/">João Pedro Brandão de Moura</a>, <a href="https://www.linkedin.com/in/matheusmeendes/">Matheus Ferreira Mendes</a>, <a href="https://www.linkedin.com/in/paulooctaviodepaula?trk=blended-typeahead">Paulo Octavio De Paula</a>, <a href="https://www.linkedin.com/in/rafaella-bianca-cavalcante/">Rafaella Bianca Cavalcante</a>, <a href="https://www.linkedin.com/in/stefano-parente/">Stefano Tamer Parente</a>, <a href="https://www.linkedin.com/in/yan-m-coutinho/">Yan Mendonça Coutinho</a>, is licensed under <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"></a></p>

## 🎓 Referências


1. CARVALHO, Leandro. Data Product Canvas: A practical framework for building high-performance data products. Medium, 22 jul. 2019. Disponível em: https://medium.com/@leandroscarvalho/data-product-canvas-a-practical-framework-for-building-high-performance-data-products-7a1717f79f0. Acesso em: 17 out. 2024.
