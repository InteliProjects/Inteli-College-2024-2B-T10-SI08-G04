 <h1>Linha Quartzo</h1>
 <h2>Sumário</h2>

- [1 Experiência do Usuário](#1-experiência-do-usuário)
  - [1.1 Personas](#11-personas)
  - [1.2 User Stories](#12-user-stories)
  - [1.3 Mapa de Jornada do Usuário](#13-mapa-de-jornada-do-usuário)
- [2 Análise de Negócios](#2-análise-de-negócios)
  - [2.1 Canvas Proposta de Valor](#21-canvas-proposta-de-valor)
    - [2.1.2 Descrição dos pontos do VPC](#212-descrição-dos-pontos-do-vpc)
  - [2.2 Total Addressable Market, Service Addressable Market, e Service Obtainable Market](#22-total-addressable-market-service-addressable-market-e-service-obtainable-market)
    - [TAM (Total Addressable Market)](#tam-total-addressable-market)
    - [SAM (Serviceable Available Market)](#sam-serviceable-available-market)
    - [SOM (Serviceable Obtainable Market)](#som-serviceable-obtainable-market)
  - [2.3 Matriz de Risco e Oportunidades](#23-matriz-de-risco-e-oportunidades)
    - [2.3.1 Plano de Resposta para Riscos e Oportunidades](#231-plano-de-resposta-para-riscos-e-oportunidades)
      - [2.3.1.1 Ameaças](#2311-ameaças)
      - [2.3.1.2 Oportunidades](#2312-oportunidades)
- [3 Arquitetura e Design do Sistema](#3-arquitetura-e-design-do-sistema)
  - [3.1 Wireframes](#31-wireframes)
    - [3.1.1 Wireframe Desktop](#311-wireframe-desktop)
  - [3.1.2 Wireframe Mobile.](#312-wireframe-mobile)
  - [3.2 Diagrama UML](#32-diagrama-uml)
    - [3.2.1 Diagrama de Componentes - Arquitetura do Sistema (Sprint 1)](#321-diagrama-de-componentes---arquitetura-do-sistema-sprint-1)
    - [3.2.2 Diagrama de Componentes - Arquitetura do Sistema (Sprint 4)](#322-diagrama-de-componentes---arquitetura-do-sistema-sprint-4)
- [4 Exploração de Dados](#4-exploração-de-dados)
  - [4.1 Data Model Canvas](#41-data-model-canvas)
    - [4.1.1 Proposta de Valor:](#411-proposta-de-valor)
    - [4.1.2 Estrutura de Dados:](#412-estrutura-de-dados)
    - [4.1.3 Perfil dos Usuários:](#413-perfil-dos-usuários)
    - [4.1.4 Casos de Uso:](#414-casos-de-uso)
    - [4.1.5 Métricas de Sucesso: Indicadores](#415-métricas-de-sucesso-indicadores)
    - [4.1.6 Análise de Dados:](#416-análise-de-dados)
  - [4.2 Relatório ETL](#42-relatório-etl)
    - [4.2.1 Extrair (Extract)](#421-extrair-extract)
    - [4.2.2 Transformar (Transform)](#422-transformar-transform)
    - [4.2.3 Carregar (Load)](#423-carregar-load)
    - [4.2.4 Conclusão](#424-conclusão)
- [5. Análise de Impacto Ético](#5-análise-de-impacto-ético)
  - [5.1 Privacidade e proteção de dados](#51-privacidade-e-proteção-de-dados)
  - [5.2 Equidade e justiça](#52-equidade-e-justiça)
  - [5.3 Transparência e consentimento informado](#53-transparência-e-consentimento-informado)
  - [5.4 Responsabilidade social](#54-responsabilidade-social)
  - [5.5 Viés e discriminação](#55-viés-e-discriminação)
  - [5.6 Conclusão](#56-conclusão)
- [6 Documentação da Primeira Versão do Datapp](#6-documentação-da-primeira-versão-do-datapp)
  - [6.1 Lógica de Criação do Infográfico](#61-lógica-de-criação-do-infográfico)
    - [Estrutura e Abordagem:](#estrutura-e-abordagem)
  - [6.2 Implementação de Filtros](#62-implementação-de-filtros)
  - [6.2 Implementação de Filtros](#62-implementação-de-filtros-1)
    - [Filtros de Linhas:](#filtros-de-linhas)
    - [Filtros de Estações:](#filtros-de-estações)
    - [Filtros de Data:](#filtros-de-data)
    - [Integração:](#integração)
  - [6.3 Processo de Coleta Automática de Dados](#63-processo-de-coleta-automática-de-dados)
    - [Detalhes Técnicos:](#detalhes-técnicos)
      - [Endpoints da API:](#endpoints-da-api)
      - [Conexão com o ClickHouse:](#conexão-com-o-clickhouse)
      - [Integração com o Frontend:](#integração-com-o-frontend)
- [7 Cubo de Dados Automatizado](#7-cubo-de-dados-automatizado)
  - [7.1 Escolha das Dimensões](#71-escolha-das-dimensões)
    - [7.1.1 **Como foi feita a escolha das Dimensões**](#711-como-foi-feita-a-escolha-das-dimensões)
    - [7.1.2 **Dimensões Escolhidas**](#712-dimensões-escolhidas)
    - [7.1.3 **Por que essas dimensões fazem sentido para o projeto?**](#713-por-que-essas-dimensões-fazem-sentido-para-o-projeto)
    - [7.1.4 **KPIs Relacionados às Dimensões**](#714-kpis-relacionados-às-dimensões)
      - [**Quantidade de PCD por Linha e Grupo PCD**](#quantidade-de-pcd-por-linha-e-grupo-pcd)
      - [**Total de Entradas de Passageiros por Dia**](#total-de-entradas-de-passageiros-por-dia)
      - [**Tempo Médio de Saída Entre Trens**](#tempo-médio-de-saída-entre-trens)
  - [7.2 Estrutura das Planilhas](#72-estrutura-das-planilhas)
    - [7.2.1 Objetivo das Planilhas no Projeto](#721-objetivo-das-planilhas-no-projeto)
    - [7.2.2 Criação das Planilhas](#722-criação-das-planilhas)
  - [7.3 Automatização com Prefect](#73-automatização-com-prefect)
  - [7.4 Conclusão](#74-conclusão)
- [8 Análise de Eficácia e Sugestões de Melhorias](#8-análise-de-eficácia-e-sugestões-de-melhorias)
  - [8.1 Relatórios de Análise de Eficácia](#81-relatórios-de-análise-de-eficácia)
  - [8.2 Sugestões de Melhorias](#82-sugestões-de-melhorias)
- [9 Infográfico](#9-infográfico)
  - [9.1 Pesquisa](#91-pesquisa)
  - [9.2 Relatório de melhorias](#92-relatório-de-melhorias)
    - [Análise de Eficácia](#análise-de-eficácia)
    - [Sugestões de melhoria](#sugestões-de-melhoria)
    - [Conclusão](#conclusão)
- [10 Análise Financeira do Projeto](#10-análise-financeira-do-projeto)
  - [10.1 Custos de Desenvolvimento do MVP](#101-custos-de-desenvolvimento-do-mvp)
  - [10.2 Custos de Implantação do MVP](#102-custos-de-implantação-do-mvp)
  - [10.3 Custos de Manutenção do Projeto Final](#103-custos-de-manutenção-do-projeto-final)
  - [10.4 Levantamento de Lucros Indiretos do Projeto](#104-levantamento-de-lucros-indiretos-do-projeto)
  - [10.5 Cálculo de ROI e Período de Payback](#105-cálculo-de-roi-e-período-de-payback)
  - [10.6 Análise de Cenários de Mercado](#106-análise-de-cenários-de-mercado)
    - [Cenário de Mercado Atual](#cenário-de-mercado-atual)
    - [Cenário Otimista](#cenário-otimista)
    - [Cenário Moderado](#cenário-moderado)
    - [Cenário Pessimista](#cenário-pessimista)
    - [Comparação dos Cenários](#comparação-dos-cenários)
  - [10.7 Conclusão da Análise Financeira](#107-conclusão-da-análise-financeira)
- [11 Plano de Comunicação](#11-plano-de-comunicação)
  - [11.1 Identificação dos Stakeholders](#111-identificação-dos-stakeholders)
  - [11.2 Matriz de Poder/Interesse](#112-matriz-de-poderinteresse)
  - [11.3 Confecção do Plano de Comunicação](#113-confecção-do-plano-de-comunicação)
- [12 Pipeline Completo de Dados na AWS](#12-pipeline-completo-de-dados-na-aws)
  - [12.1 Arquitetura Geral do Pipeline](#121-arquitetura-geral-do-pipeline)
    - [Componentes Principais:](#componentes-principais)
  - [12.2 Fluxo Detalhado do Pipeline](#122-fluxo-detalhado-do-pipeline)
  - [12.3 Conclusão](#123-conclusão)
- [13 Visão Geral das Melhorias e Novos Recursos do Dataapp](#13-visão-geral-das-melhorias-e-novos-recursos-do-dataapp)
    - [Detalhamento das Melhorias](#detalhamento-das-melhorias)
- [14 Referências](#14-referências)
- [ 15. Anexos](#-15-anexos)


# <a id="c1"></a>1 Experiência do Usuário
## <a id="c1.1"></a>1.1 Personas

<p align="justify">&ensp;&ensp; A criação de personas é uma prática essencial para o desenvolvimento de soluções tecnológicas eficazes, permitindo a compreensão profunda das necessidades e comportamentos dos usuários. No contexto do projeto de Big Data da CPTM, as personas ajudam a alinhar os objetivos tecnológicos às expectativas e desafios reais enfrentados por diferentes perfis de colaboradores da empresa. Com isso, o projeto pode ser moldado para otimizar a operação ferroviária, garantindo que as soluções propostas atendam de forma precisa os usuários finais. (NIELSEN NORMAN GROUP, 2022)</p>

<br>
<div align="center">
  <figcaption style="text-align: center; font-size: 10px; margin-bottom: 5px;">Figura 1 - Persona Diretora de Operações</figcaption>
  <img src="https://res.cloudinary.com/dxjfonp85/image/upload/v1731940063/l0giv5xflu5nech1onqw.png" alt="Persona 1" style="width: 100%; display: block; margin: 0 auto;">
  <figcaption style="text-align: center; font-size: 10px; margin-top: 5px;">Fonte: Elaboração Própria</figcaption>
</div>
<br>

<p align="justify">&ensp;&ensp;Silvia Campos é diretora de operações na CPTM, com 20 anos de experiência em engenharia de produção e gestão operacional. Ela lidera equipes multidisciplinares, com um olhar estratégico voltado para a eficiência operacional e redução de custos. No entanto, Silvia enfrenta desafios relacionados à análise de grandes volumes de dados operacionais, além de pressões para manter a qualidade dos serviços.</p>

<p align="justify">&ensp;&ensp;Ela demonstra um grande interesse em soluções tecnológicas que possibilitem visualizações claras e intuitivas de KPI's operacionais. Ela deseja ferramentas de Big Data que transformem dados complexos em insights rápidos e acionáveis, auxiliando em sua rotina de decisões estratégicas. Silvia também busca uma integração mais fluida entre os dados para otimizar operações, com suporte técnico que garanta uma transição suave para novas tecnologias.
</p>

<p align="justify">&ensp;&ensp;Além de ter uma abordagem prática, Silvia também tem uma abordagem emocional em sua busca por soluções. Ela valoriza a eficiência não apenas pelos custos, mas porque sabe que o transporte é vital para os passageiros e para a cidade. Isso conecta sua visão de dados com o impacto humano.
</p>

<br>
<div align="center">
  <figcaption style="text-align: center; font-size: 10px; margin-bottom: 5px;">Figura 2 - Persona Operador de Controle de Estações</figcaption>
  <img src="https://res.cloudinary.com/dxjfonp85/image/upload/v1731940063/hubynbzx5un8jev9rxpz.png" alt="Persona 2" style="width: 100%; display: block; margin: 0 auto;">
  <figcaption style="text-align: center; font-size: 10px; margin-top: 5px;">Fonte: Elaboração Própria</figcaption>
</div>
<br>


<p align="justify">&ensp;&ensp;José Pereira é operador no Centro de Controle de Estações (CCE) da CPTM, com 15 anos de experiência. Ele trabalha monitorando o fluxo de passageiros e situações emergenciais, gerenciando crises e garantindo a redistribuição de passageiros. Apesar de seu profundo conhecimento operacional, ele sente dificuldades em prever congestionamentos inesperados e percebe limitações nos sistemas atuais, como excesso de informações e baixa integração com outros modais.</p>

<p align="justify">&ensp;&ensp;Ele se interessa por ferramentas tecnológicas que simplifiquem sua rotina, principalmente em situações de emergência. Ele valoriza <i>dashboards</i> com informações claras e objetivas, integrados a outros sistemas de transporte. Ferramentas de monitoramento em tempo real, com alertas automáticos, são uma prioridade, pois otimizam sua capacidade de responder rapidamente a situações críticas.
</p>

<p align="justify">&ensp;&ensp;José sente orgulho de seu trabalho e entende o impacto que ele tem na experiência dos passageiros. Sua frustração com sistemas confusos e pouco integrados reflete sua vontade de oferecer um serviço melhor, especialmente em momentos de crise operacional.
</p>


<p align="justify">&ensp;&ensp; As personas José Pereira e Silvia Campos representam dois perfis cruciais dentro da operação da CPTM, com desafios e necessidades distintos, mas complementares. Enquanto José lida diretamente com o monitoramento diário e busca mais eficiência operacional em suas atividades, Silvia tem uma visão macro da operação, focando na gestão de recursos e na melhoria contínua por meio de soluções tecnológicas mais avançadas. Entender essas personas permite que o projeto de Big Data da CPTM direcione esforços para resolver problemas reais, proporcionando maior eficiência e aprimoramento na tomada de decisões operacionais.</p>


## <a id="c1.2"></a>1.2 User Stories

<p align="justify">&ensp;&ensp;User stories, segundo a Interaction Design Foundation, se trata da utilização de uma narrativa para se ter uma interação detalhada do usuário com um produto ou serviço. A sua aplicação no projeto da CPTM visa garantir um produto centrado no cliente e focado em resolver suas necessidades, cobrindo os pontos da rotina diária dos funcionários da CPTM. (INTERACTION DESIGN FOUNDATION, 2024)</p>


<p align="justify">&ensp;&ensp;Além disso, as User Stories do projeto foram feitas seguindo o método INVEST <i> (Independent, Negotiable, Valuable, Estimable, Small, Testable)</i> utilizado por times ágeis para facilitar a implementação das User Stories de maneira padronizada e seguindo cada um dos critérios. As user stories apresentadas são baseadas nas personas Silvia Campos e José João Pereira apresentados na sessão personas.(ZUP, 2024)</p>

<p align="center">Quadro 1 - User Story 1</p>

| Número                        | US001                                                                                                                                                                                                                                                                                                                                                     |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Título                        | Análise dos dados                                                                                                                                                                                                                                                                                                                                         |
| Persona                       | Diretora de operações                                                                                                                                                                                                                                                                                                                                     |
| História                      | Silvia Campos, como diretora de operações, deseja **ver elementos visuais** que **facilitem a sua tomada de decisão**.                                                                                                                                                                                                                                    |
| Critérios de Aceitação        | **CR-01:** O MVP deve ter ao menos um infográfico para cada tabela apresentada.<p> **CR-02:** O MVP deve ter sistema de filtragem de infográfico referentes a dados variáveis. Por exemplo, data(periodo), dia da semana, linha, trem e estação.                                                                                                                                                                                                        |
| Testes de Aceitação **CR-01** | Critério de aceitação: <p> a. Há 4 infográficos para 5 tabelas <p>  &emsp;i. Passou = Errado, deve ser corrigido <p> &emsp;ii. Não passou = Correto <p> b. Há 5 infográficos para 5 tabelas <p>  &emsp;i. Passou = Correto <p> &emsp;ii. Não passou = Errado, deve ser corrigido <p>                                                                      |
| Testes de Aceitação **CR-02** | Critério de aceitação: <p> c. O filtro para a linha coral mostra outras linhas além da coral <p>  &emsp;i. Passou = Errado, deve ser corrigido <p> &emsp;ii. Não passou = Correto <p> d. O filtro para a linha coral mostra apenas a linha coral <p>  &emsp;i. Passou = Correto <p> &emsp;ii. Não passou = Errado, deve ser corrigido <p> |

<p align="center">Fonte: Elaborado pelos autores.</p>


<p align="center">Quadro 2 - User Story 2</p>

| Número                        | US002                                                                                                                                                                                                                                                                                                                 |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Título                        | Velocidade de processamento                                                                                                                                                                                                                                                                                           |
| Persona                       | Diretora de operações                                                                                                                                                                                                                                                                                                 |
| História                      | Silvia Campos, como diretora de operações, deseja **consultar as informações** de maneira **rápida** e **fácil** para não tomar muito tempo de sua rotina.                                                                                                                                                            |
| Critérios de Aceitação        | **CR-01:** O MVP deve ler 6 Gigas de dados em, no máximo, 1 minuto, sendo a conferência feita através do banco de dados de logs.                                                                                                                                                                                                                                                   |
| Testes de Aceitação **CR-01** | Critério de aceitação: <p> e. logs informam que as informações foram geradas em mais de 1 minuto <p>  &emsp;i. Passou = Errado, deve ser corrigido <p> &emsp;ii. Não passou = Correto <p> f. O MVP entrega as informações em menos de 1 minuto <p>  &emsp;i. Passou = Correto <p> &emsp;ii. Não passou = Errado, deve ser corrigido <p> |

<p align="center">Fonte: Elaborado pelos autores.</p>

<p align="center">Quadro 3 - User Story 3</p>

| Número                        | US003                                                                                                                                                                                                                                                                                                                             |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Título                        | Escalabilidade das operações                                                                                                                                                                                                                                                                                                      |
| Persona                       | Diretora de operações                                                                                                                                                                                                                                                                                                             |
| História                      | Silvia Campos, como diretora de operações, deseja  **inserir mais dados no futuro**, para que **tenha escalabilidade** em suas operações.                                                                                                                                                                                         |
| Critérios de Aceitação        | **CR-01:** O MVP deve ser apto a receber novos dados com a mesma estrutura apresentada ao serem passados por um pipeline de dados.                                                                                                                                                                                                                                           |
| Testes de Aceitação **CR-01** | Critério de aceitação: <p> g. O MVP recebe dados com estrutura diferente da apresentada <p>  &emsp;i. Passou = Errado, deve ser corrigido e o pipeline revisado <p> &emsp;ii. Não passou = Correto <p> h. O MVP recebe dados com a mesma estrutura apresentada seguindo o pipeline <p>  &emsp;i. Passou = Correto <p> &emsp;ii. Não passou = Errado, deve ser corrigido <p> |


<p align="center">Fonte: Elaborado pelos autores.</p>


<p align="center">Quadro 4 - User Story 4</p>

| Número                        | US004                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Título                        | Fluxo de pessoas                                                                                                                                                                                                                                                                                                                                                             |
| Persona                       | Operador de Controle de Estações (CCE)                                                                                                                                                                                                                                                                                                                                       |
| História                      | José Pereira, como CCE, deseja **identificar padrões de comportamento de passageiros** em estações para conseguir **verificar anormalidades**.                                                                                                                                                                                                                               |
| Critérios de Aceitação        | **CR-01:** O MVP deve ter um infográfico de correlação que indique em quais horários existe o maior fluxo de pessoas. <br> **CR-02:** O MVP deve destacar os horários com maior fluxo de pessoas, permitindo uma rápida identificação de picos e padrões.  Sendo o maior fluxo definido pela média de fluxo num período definido.                                                                                                                  |
| Testes de Aceitação **CR-01** | Critério de aceitação: <br> i. O MVP apresenta nenhum gráfico que indique o fluxo de pessoas acima da média por período do dia <p><p> &emsp;i. Passou = Errado, deve ser corrigido <p> &emsp;ii. Não passou = Correto <p> j. O MVP apresenta ao menos 1(um) gráfico que indique o fluxo de pessoas por horário <p> &emsp;i. Passou = Correto <p> &emsp;ii. Não passou = Errado, deve ser corrigido |
| Testes de Aceitação **CR-02** | Critério de aceitação: <p> k. O MVP destaca a estação com o maior fluxo de pessoas, sendo o mesmo definido por fluxo acima da média se comparado com as outras estações <p> &emsp;i. Passou = Correto <p> &emsp;ii. Não passou = Errado, deve ser corrigido <p> l. O MVP não destaca a estação com o maior fluxo de pessoas <p> &emsp;i. Passou = Errado, deve ser corrigido <p> &emsp;ii. Não passou = Correto                                                   |



<p align="center">Fonte: Elaborado pelos autores.</p>


<p align="center">Quadro 5 - User Story 5</p>

| Número                        | US005                                                                                                                                                                                                                                                                                                                                                                                  |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Título                        | Satisfação de pessoas                                                                                                                                                                                                                                                                                                                                                                  |
| Persona                       | Operador de Controle de Estações (CCE)                                                                                                                                                                                                                                                                                                                                                 |
| História                      | José Pereira, como CCE, deseja **identificar padrões de comportamento de passageiros** em estações para conseguir **elaborar projetos**baseados nessas informações.                                                                                                                                                                                                                    |
| Critérios de Aceitação        | **CR-01:** O MVP deve ter um infográfico de correlação entre o fluxo de pessoas e o numero de reclamações. <br> **CR-02:** O MVP deve ter um infográfico de correlação entre o numero de incidentes/falhas e as reclamações registradas.                                                                                                                                                                                        |
| Testes de Aceitação **CR-01** | Critério de aceitação: <p> l. O MVP não apresenta ao menos 1(um) infográfico entre o fluxo de pessoas em certos períodos e as reclamações registrada no mesmo período <p> &emsp;i. Passou = Errado, deve ser corrigido <p> &emsp;ii. Não passou = Correto <p> m. O MVP apresenta ao menos 1(um) gráfico entre o fluxo e as reclamações <p> &emsp;i. Passou = Correto <p> &emsp;ii. Não passou = Errado, deve ser corrigido                       |
| Testes de Aceitação **CR-02** | Critério de aceitação: <p> n. O MVP apresenta ao menos 1(um) gráfico entre os incidentes/falhas e as reclamações <p> &emsp;i. Passou = Correto <p> &emsp;ii. Não passou = Errado, deve ser corrigido <p> o. O MVP não apresenta ao menos 1(um) gráfico entre os incidentes/falhas e as reclamações <p> &emsp;i. Passou = Errado, deve ser corrigido <p> &emsp;ii. Não passou = Correto |

<p align="center">Fonte: Elaborado pelos autores.</p>


<p align="center">Quadro 6 - User Story 6</p>

| Número                        | US006                                                                                                                                                                                                                                                                                                                                                                            |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Título                        | Riscos de segurança aos passageiros                                                                                                                                                                                                                                                                                                                                              |
| Persona                       | Operador de Controle de Estações (CCE)                                                                                                                                                                                                                                                                                                                                           |
| História                      | José Pereira, como CCE, quer **analisar gráficos** que **mostram anomalias** no **fluxo de passageiros**, para **revisar situações passadas** que podem ter **implicado em riscos de segurança**.                                                                                                                                                                                |
| Critérios de Aceitação        | **CR-01:** O sistema deve gerar gráficos que identifiquem variações anômalas no fluxo de passageiros, como grandes desvios em relação à média histórica. <p> **CR-02:** O MVP deve destacar visualmente as anomalias, facilitando a análise de possíveis causas e impactos.                                                                                                      |
| Testes de Aceitação **CR-01** | Critério de aceitação: <p> p. O MVP não gera gráficos que identifiquem variações anômalas no fluxo de passageiros <p> &emsp;i. Passou = Errado, deve ser corrigido <p> &emsp;ii. Não passou = Correto <p> q. O MVP gera gráficos que identifiquem variações anômalas no fluxo de passageiros <p> &emsp;i. Passou = Correto <p> &emsp;ii. Não passou = Errado, deve ser corrigido |
| Testes de Aceitação **CR-02** | Critério de aceitação: <p> r. O MVP destaca visualmente as anomalias <p> &emsp;i. Passou = Correto <p> &emsp;ii. Não passou = Errado, deve ser corrigido <p> s. O MVP não destaca visualmente as anomalias <p> &emsp;i. Passou = Errado, deve ser corrigido <p> &emsp;ii. Não passou = Correto                                                                                   |

<p align="center">Fonte: Elaborado pelos autores.</p>

<p align="justify">&ensp;&ensp;Com as User Stories criadas, a implementação das features do projeto se torna mais direcionada, garantindo um produto centrado no cliente e focado em resolver suas necessidades de forma eficiente. Essas histórias permitem que a equipe de desenvolvimento compreenda de maneira clara as expectativas e objetivos dos usuários da CPTM, facilitando a priorização e entrega de valor. Vale ressaltar que as User Stories, embora bem definidas, estão sujeitas a revisões e adaptações conforme as necessidades do projeto evoluírem, assegurando flexibilidade para atender mudanças ou novos requisitos que possam surgir.</p>


## <a id="c1.3"></a>1.3 Mapa de Jornada do Usuário
<p align="justify">&ensp;&ensp;
"[O mapa de] jornada do usuário é uma visualização do processo pelo qual uma pessoa passa para alcançar um objetivo. Na sua forma mais básica, o mapeamento da jornada do usuário começa compilando uma série de ações do usuário em uma linha do tempo. Em seguida, essa linha do tempo é complementada com pensamentos e emoções do usuário para criar uma narrativa. Essa narrativa é condensada e refinada, resultando, por fim, em uma visualização."(GIBBONS, 2018). Essa ferramenta é extremamente útil para construir um entendimento de como o usuário se relacionará com o produto. O seu uso no projeto da CPTM é essencial para solidificar a compreensão do uso do produto, perceber oportunidades de melhorias e otimizar a jornada.</p>
<p align="justify">&ensp;&ensp; Dito isso, foi criado uma jornada do usuário para cada uma das personas no Miro, sendo elas:</p>

<br>
<div align="center">
  <figcaption style="text-align: center; font-size: 10px; margin-bottom: 5px;">Figura 3 - Jornada do José</figcaption>
  <img src="https://res.cloudinary.com/de8ca4say/image/upload/v1731443439/zbto38nhgorew9pazbt1.jpg" alt="Jornada do José" style="width: 100%; display: block; margin: 0 auto;">
  <figcaption style="text-align: center; font-size: 10px; margin-top: 5px;">Fonte: Elaboração Própria</figcaption>
</div>
<br>


<p align="justify">&ensp;&ensp;
Na jornada da primeira persona é possível observar José João Pereira realizando algumas das suas atividades diárias dentro da CPTM. Sua jornada começa recebendo uma solicitação de sua superior requisitando uma análise da estação do Brás da linha 11, sendo necessário consultar o DataApp e selecionar os dados adequados para análise. Após sua visualização, José prepara seu relatório para ser eviado a sua superior.</p>

<p align="justify">&ensp;&ensp;
Os insights mais relevantes que a jornada levanta para o projeto da CPTM são as oportunidades observadas na fase de visualização dos dados e de finalização de demanda, onde o DataApp vai ter maior impacto. Tendo isso em vista, esses pontos serão explorados ao longo do desenvolvimento do produto.</p>

<br>
<div align="center">
  <figcaption style="text-align: center; font-size: 10px; margin-bottom: 5px;">Figura 4 - Jornada da Silvia</figcaption>
  <img src="https://res.cloudinary.com/de8ca4say/image/upload/v1731443440/wzhg2jtkdl0jhakltohp.jpg" alt="Jornada da Silvia" style="width: 100%; display: block; margin: 0 auto;">
  <figcaption style="text-align: center; font-size: 10px; margin-top: 5px;">Fonte: Elaboração Própria</figcaption>
</div>
<br>


<p align="justify">&ensp;&ensp; Na jornada da persona Silvia Campos, Diretora de Operações, é possível observar suas atividades focadas em melhorar o fluxo de pessoas. Sua jornada começa na fase de análise de dados, onde Silvia lê o relatório do operador do CCE e identifica os indicadores que precisam de aprimoramento. Em seguida, ela avança para a fase de elaboração de estratégias, realizando reuniões com a equipe para definir processos e estabelecer melhorias. Por fim, Silvia implementa as estratégias e acompanha os KPIs por meio do DataApp para monitorar o impacto das ações tomadas.</p> 

<p align="justify">&ensp;&ensp; Os insights mais relevantes que a jornada levanta para o projeto são as oportunidades de aprimoramento na visualização e acessibilidade dos dados no DataApp. É essencial que o sistema permita uma geração de relatórios fácil e intuitiva, com dados acessíveis em tempo real e descrições claras dos indicadores, evitando erros de interpretação. Esses pontos serão fundamentais para o desenvolvimento do produto, visando uma experiência mais eficaz e menos estressante para a Diretoria durante a tomada de decisões.</p>

<p align="justify">&ensp;&ensp; Para concluir, a jornada de José João Pereira e Silvia Campos apresentam desafios e oportunidades cruciais que podem melhorar a experiencia de uso do DataApp no âmbito da CPTM. Ambas a jornadas apontam para um sistema que possibilite a coleta, análise e interpretação de dados de modo eficaz e simplificado, permitindo que o time faça decisões com maior qualidade e rapidez. Por outro lado, as oportunidades encontradas, incluindo a facilitação do relatório gerencial bem como a descrição mais específica dos indicadores, foram incorporadas ao documento de criação do produto.</p>

# <a id="c2"></a>2 Análise de Negócios
## <a id="c2.1"></a>2.1 Canvas Proposta de Valor

<p align="justify">&ensp;&ensp;O projeto de Big Data para a CPTM tem como principal objetivo otimizar a análise de grandes volumes de dados, especialmente nos dados relacionados à movimentação de passageiros e ao desempenho operacional das linhas de trem. A solução, baseada em uma infraestrutura de Big Data na nuvem da AWS, busca criar um pipeline capaz de processar esses dados de maneira escalável e eficiente, gerando insights essenciais para a tomada de decisões estratégicas. O uso do <i>Value Proposition Canvas</i> (VPC) desempenha um papel importante na estruturação do projeto, garantindo que as necessidades e expectativas dos usuários sejam atendidas de forma precisa e alinhada aos objetivos operacionais da CPTM. O VPC é uma ótima ferramenta para conectar os serviços do projeto com os principais desafios e demandas da empresa, maximizando o valor entregue do projeto.</p>

<br>
<div align="center">
  <figcaption style="text-align: center; font-size: 10px; margin-bottom: 5px;">Figura 5 - Value Proposition Canvas</figcaption>
  <img src="https://res.cloudinary.com/dxjfonp85/image/upload/v1730827489/da3wjzlbnonemubsesoo.png" alt="Value Proposition Canvas" style="width: 100%; display: block; margin: 0 auto;">
  <figcaption style="text-align: center; font-size: 10px; margin-top: 5px;">Fonte: Elaboração Própria</figcaption>
</div>
<br>


### 2.1.2 Descrição dos pontos do VPC

**Gain Creators**

- Automação do processo de análise de dados, reduzindo o tempo gasto com tarefas manuais;
- Soluções baseadas em cloud, garantindo escalabilidade e capacidade de lidar com grandes volumes de dados;
- Ferramentas de análise avançadas para obter insights rápidos e precisos;
- Interface visual para criação de infográficos e relatórios, facilitando a comunicação de resultados e insights com stakeholders.

**Products & Services**

<p align="justify">&ensp;&ensp;O projeto envolve o desenvolvimento de um pipeline de Big Data utilizando serviços da AWS para ingestão, transformação e análise de grandes volumes de dados. Será implementada uma interface visual para criação de infográficos gerenciais e painéis interativos, utilizando ferramentas de análise estatística como Apache Spark e Hadoop, suportadas por AWS EMR. Além disso, os dados serão centralizados e armazenados de forma segura em um Data Lake, com suporte para ingestão via batch ou streaming, de acordo com as necessidades operacionais da CPTM.
</p>

**Pain Relievers**

- Implementação de um pipeline de Big Data que permite a ingestão e análise de grandes volumes de dados de forma rápida e escalável;
- Análise estatística automatizada para fornecer insights relevantes em tempo hábil;
- Centralização dos dados em um Data Lake, facilitando o acesso e a análise integrada de diferentes fontes de dados;
- Visualizações interativas com infográficos automatizados, gerando relatórios gerenciais visualmente atraentes e fáceis de interpretar.

**Pains**

- Falta de recursos para analisar grandes volumes de dados de forma rápida e eficiente.
- Dificuldade em gerar relatórios e visualizações úteis a partir dos processos de dados atuais.
- Tomada de decisão por vezes ineficaz devido à falta de insights e análises descritivas.
- Ineficiências operacionais por não conseguir prever com tanta eficiência falhas ou problemas de desempenho.
- Dificuldade na integração de dados entre diferentes sistemas e fontes, tornando a análise fragmentada.

**Gains**

- Decisões mais informadas e baseadas em análises precisas de grandes volumes de dados.
- Melhor visibilidade operacional, permitindo ajustes rápidos e otimizados nas operações.
- Automatização de relatórios e visualizações de dados, economizando tempo e reduzindo erros.
- Previsibilidade aprimorada, permitindo antever problemas e agir antes que afetem o serviço.
- Redução de custos operacionais ao identificar ineficiências nos processos.

**Customer Job(s)**

- Analisar grandes volumes de dados operacionais e administrativos para otimizar a gestão de recursos.
- Tomar decisões baseadas em dados para melhorar a eficiência operacional e reduzir custos.
- Monitorar o desempenho operacional das linhas de trem e detectar problemas antes que se tornem críticos.

<p align="justify">&ensp;&ensp;Com a implementação do pipeline de Big Data, a CPTM ganhará uma solução que centraliza e analisa dados em larga escala, permitindo uma gestão mais eficiente e preditiva dos seus serviços de transporte. A automação na geração de relatórios e a análise de padrões de comportamento dos passageiros proporcionarão decisões mais rápidas e informadas, gerando economia de tempo, redução de custos e melhorias operacionais. Além disso, o <i>Value Proposition Canvas</i> garante que o desenvolvimento do projeto permaneça centrado nas necessidades dos usuários e da empresa, promovendo soluções que aliviem suas dores e aumentem os ganhos operacionais e estratégicos. Isso assegura que o projeto entregue não apenas uma solução tecnológica, mas um valor concreto para a gestão e a eficiência da CPTM.
</p>

## <a id="c2.2"></a>2.2 Total Addressable Market, Service Addressable Market, e Service Obtainable Market

<p align="justify">&ensp;&ensp;A Companhia Paulista de Trens Metropolitanos (CPTM) desempenha um papel crucial no sistema de transporte público da Região Metropolitana de São Paulo, atendendo milhões de passageiros diariamente. Logo, é essencial entender o tamanho do mercado e o qual a taxa de clientes que ela impacta e poderá impactar em curto, médio e longo prazo. "Uma das maiores referências em venture capital no mundo, a Sequoia Capital, recomenda que empreendedores disponibilizem três métricas, para que possa ser avaliado o tamanho de mercado e segmento em que a [empresa] se encontra. São elas:</p>
<ul>
  <li>TAM (Total Addressable Market)</li>
  <li>SAM (Serviceable Addressable Market)</li>
  <li>SOM (Serviceable Obtainable Market)</li>
</ul>

<p align="justify">&ensp;&ensp;[...] Existem duas metodologias básicas [para realizar essa análise]:</p>
<ul>
<li> <b>Top-down:</b> A totalidade ou parte da informação mais importante que [...] vem de um analista de mercado, algum participante do segmento ou alguma organização. Normalmente esses dados são divulgados gratuitamente na internet e podem ser facilmente encontrados em sites de busca. </li>

<li> <b>Bottom-up:</b> Aqui [...] se [...] identifica a quantidade de clientes do segmento e multiplica pela quantidade de receita média. Parte desses dados pode ser encontrada em relatórios emitidos por empresas de capital aberto. Outra opção é analisar infográficos [...]" (Sebrae, 2019).</li>
</ul>

### TAM (Total Addressable Market)

<p align="justify">&ensp;&ensp;"o TAM, também conhecido como Mercado Totalmente Endereçável, representa a dimensão total do mercado, ou seja, o número total de consumidores ou empresas que podem se beneficiar do produto ou serviço oferecido [...]. O TAM é o maior conjunto de consumidores que [o] produto ou serviço pode alcançar no mercado." (‌EQUIPE SEBRAE MG, 2024). Com uma visão clara do tamanho do mercado, a CPTM pode direcionar seus esforços e recursos de forma estratégica, assegurando que suas iniciativas atendam a uma demanda significativa e maximizem o retorno sobre o investimento.</p>

<p align="justify">&ensp;&ensp;Diante disso, foi fundamental determinar a população total que a CPTM pode atender, além do ticket médio e do número de viagens anuais por pessoa. Para isso, foram consultadas as seguintes fontes: a agência de estatísticas do IBGE (2019), a SPTrans (2019) e a CPTM (2019). É importante ressaltar que os dados mais recentes sobre o ticket médio são de 2019, o que torna necessário considerar que todas as informações coletadas se referem a esse ano para garantir a coerência da análise. A partir dessas fontes, foram obtidas as seguintes informações: 20.743.587 habitantes, um ticket médio de R$4,28 e 564,79 viagens por pessoa ao ano. Com esses dados, é possível calcular o TAM:</p>

$$
\text{TAM} = \text{População total da área} \times \text{Ticket Médio} \times \text {Total de viagens p/ pessoa por ano}
$$

$$
\text{TAM} = 20.743.587 \times \text{R\$} 4{,}28 \times 564,79 \, \text{dias}
$$

$$
\text{TAM} = R\$ 50.143.497.747{,}4
$$

<p align="justify">&ensp;&ensp;Com o cálculo do TAM, a CPTM obtém uma estimativa clara do valor total que o mercado pode gerar em receita ao longo do ano, considerando a população da área atendida, o ticket médio e o número médio de viagens anuais. Esse valor fornece uma visão abrangente das oportunidades de mercado disponíveis, permitindo à CPTM direcionar seus esforços com uma perspectiva estratégica e dimensionada. Entender o TAM também é essencial para futuras expansões, planejamento de investimentos e desenvolvimento de iniciativas que visem alcançar o maior número possível de usuários, garantindo que a CPTM possa atender de forma abrangente e maximizar o retorno potencial sobre suas operações.</p>


### SAM (Serviceable Available Market)

<p align="justify">&ensp;&ensp;"O SAM, também conhecido como Mercado Endereçável Disponível, é uma subcategoria do TAM e indica o segmento de mercado que a empresa pode alcançar com seu produto ou serviço. Essa análise considera fatores como localização geográfica, segmentação demográfica e nichos de mercado, entre outros. O SAM fornece um recorte mais específico e direcionado do mercado total, representando a parte do mercado onde a empresa pode competir de forma eficaz." (EQUIPE SEBRAE MG, 2024). Compreendendo claramente o SAM, a CPTM pode concentrar seus esforços em áreas onde tem uma vantagem competitiva, otimizando suas estratégias para atender a esse público específico e potencializando suas oportunidades de crescimento.</p>

<p align="justify">&ensp;&ensp;Dito isso, foi utilizado os dados divulgados no Relatório Integrado da Administração da CPTM e pelo dados divulgados no kickoff é possível observar que a CPTM atua, principalmente, na região metropolitana da cidade de São Paulo. Portanto, o mercado total disponível será equivalente a população dessa área. Dado que o censo do IBGE é feito em intervalos de, em média, 10 anos, será utilizado o censo de 2022. Segundo ele, a população dessa área é de 11.451.245 de habitantes. Logo, é possível calcular o SAM a partir do percentual do mercado que a CPTM tem acesso</p>

$$
\text{SAM} = \text{TAM} \times (\text{Quantidade de habitantes na área metropolitana}/\text{Quantidade de habitantes no estado})
$$

$$
\text{SAM} = R\$ 50.143.497.747{,}4 \times (11.451.245/20.743.587)
$$

$$
\text{SAM} = R\$ 27.681.108.280
$$

<p align="justify">&ensp;&ensp;Com esses cálculos, a CPTM consegue uma visão mais precisa do mercado que pode efetivamente atender na região metropolitana de São Paulo. Esse valor do SAM representa o potencial financeiro que a empresa pode explorar ao focar nesse público específico, permitindo uma alocação estratégica de recursos e esforços de forma direcionada. Ao utilizar o SAM como base para suas decisões, a CPTM está em uma posição vantajosa para planejar expansões e iniciativas que maximizem seu impacto e retorno sobre o investimento na área em que possui maior competitividade. Esse entendimento reforça a importância de uma abordagem baseada em dados para sustentar um crescimento sustentável e alinhado às reais oportunidades de mercado.</p>


### SOM (Serviceable Obtainable Market)

<p align="justify">&ensp;&ensp;"o SOM, ou Mercado Endereçável Obtido, é uma subdivisão ainda menor do SAM e representa a fatia do mercado que sua empresa realmente alcançou e conquistou. O SOM é o resultado das estratégias de marketing, o alcance de clientes e a conquista de mercado, refletindo a porcentagem do mercado disponível que [a] empresa conseguiu atingir até o momento. O SOM é uma medida do desempenho atual do [...] negócio em relação ao mercado total." (‌EQUIPE SEBRAE MG, 2024).  No caso da CPTM, compreender o SOM é fundamental para avaliar o grau de penetração junto ao público-alvo, auxiliando na análise da eficácia de suas estratégias de captação e retenção e orientando melhorias para expandir a participação de mercado.</p>

<p align="justify">&ensp;&ensp;Para calcular o SOM, será utilizado uma abordagem <i>bottom-up,</i> na qual utilizaremos os dados da CPTM para calcular o faturamento estimado. O faturamento é dado pela média de passageiros por dia vezes o ticket médio vezes a quantidade de dias no ano.</p>


$$
\text{SOM} = \text{Média de passageiros por dia} \times \text{Ticket médio} \times \text{Dias}
$$

$$
\text{SOM} = 1.700.000 \times R\$ 4{,}28 \times 250 \, \text{dias}
$$

$$
\text{SOM} = R\$ 1.819.000.000
$$

<p align="justify">&ensp;&ensp;A análise do SOM proporciona à CPTM uma visão realista do mercado que já está efetivamente alcançando e atendendo, permitindo avaliar a eficácia de suas estratégias atuais de operação e marketing. Com um entendimento preciso do SOM, a CPTM pode identificar áreas de oportunidade para melhorar a retenção de clientes e expandir sua base de usuários de maneira estratégica. Este indicador oferece uma base sólida para o aprimoramento das ações direcionadas, auxiliando na formulação de iniciativas que possam aumentar o engajamento e reforçar a presença da CPTM no setor de transporte público da região metropolitana de São Paulo.</p>


## <a id="c2.3"></a>2.3 Matriz de Risco e Oportunidades

<p align="justify">&ensp;&ensp;A implementação de um pipeline de Big Data para análise de grandes volumes de dados da CPTM envolve uma série de desafios e oportunidades que podem impactar o cronograma, a qualidade dos dados e a adoção por parte dos usuários. O projeto se propõe a transformar a forma como a CPTM coleta, analisa e utiliza dados, proporcionando insights valiosos para a tomada de decisões. No entanto, é fundamental identificar os riscos potenciais que podem afetar essa implementação, assim como reconhecer as oportunidades que podem emergir durante o processo. Identificar essas variáveis permitirá à CPTM não apenas mitigar os impactos negativos, mas também maximizar os benefícios da nova abordagem baseada em dados. Esta seção apresenta uma análise detalhada das principais ameaças e oportunidades, assim como o plano de ação correspondente para garantir o sucesso do projeto.</p>

<br>
<div align="center">
  <figcaption style="text-align: center; font-size: 10px; margin-bottom: 5px;">Figura 6 - Matriz de Risco</figcaption>
  <img src="https://res.cloudinary.com/dowilmxvk/image/upload/v1731505796/Templates_4_mvcfgy.png" alt="Matriz de Risco" style="width: 100%; display: block; margin: 0 auto;">
  <figcaption style="text-align: center; font-size: 10px; margin-top: 5px;">Fonte: Elaboração Própria</figcaption>
</div>
<br>


### 2.3.1 Plano de Resposta para Riscos e Oportunidades

<p align="justify">&ensp;&ensp;Através da identificação e análise cuidadosa dos riscos e oportunidades, desenvolvemos um plano de resposta que permite mitigar os impactos negativos e aproveitar as vantagens potenciais da implementação do pipeline de Big Data. Abaixo estão os principais riscos (ameaças) e oportunidades com suas respectivas estratégias de resposta.</p>

#### 2.3.1.1 Ameaças

1. **Baixa Adesão dos Usuários Finais**
   - **Descrição**: Os usuários podem não adotar as novas ferramentas de Big Data devido à falta de compreensão ou falta de interesse nas mudanças.
   - **Estratégia**: Mitigar
   - **Ação**: Implementar sessões de treinamento interativas e fornecer documentação clara e acessível.
   - **Justificativa**: Garantir que os usuários entendam o valor das ferramentas e saibam como usá-las para melhorar as operações.
   - **Responsável**: Equipe de Treinamento e Comunicação.
   - **Probabilidade**: 50%
   - **Impacto**: 4 (Alto)
   - **Pontuação do Risco**: 0.5 * 4 = 2.0

2. **Vazamento de Dados**
   - **Descrição**: Há o risco de que dados sensíveis dos passageiros sejam vazados, levando a multas e danos à reputação da CPTM.
   - **Estratégia**: Mitigar
   - **Ação**: Implementar criptografia avançada, realizar auditorias regulares e adotar práticas robustas de segurança.
   - **Justificativa**: Garantir a proteção dos dados dos passageiros e a conformidade com a LGPD.
   - **Responsável**: Especialista em Segurança da Informação.
   - **Probabilidade**: 30%
   - **Impacto**: 5 (Muito Alto)
   - **Pontuação do Risco**: 0.3 * 5 = 1.5

3. **Falta de Treinamento para Usuários Finais**
   - **Descrição**: A falta de treinamento adequado pode resultar em um uso inadequado das ferramentas de Big Data, comprometendo sua eficácia.
   - **Estratégia**: Mitigar
   - **Ação**: Oferecer um programa de treinamento detalhado e contínuo, com suporte pós-implementação.
   - **Justificativa**: Garantir que os usuários saibam como usar as ferramentas para maximizar seus benefícios.
   - **Responsável**: Líder de Treinamento.
   - **Probabilidade**: 70%
   - **Impacto**: 4 (Alto)
   - **Pontuação do Risco**: 0.7 * 4 = 2.8

4. **Falta de Conformidade com a LGPD**
   - **Descrição**: O projeto pode não cumprir completamente os requisitos da Lei Geral de Proteção de Dados (LGPD), resultando em penalidades legais.
   - **Estratégia**: Mitigar
   - **Ação**: Garantir que todos os dados pessoais sejam tratados de acordo com a LGPD e outras regulamentações aplicáveis.
   - **Justificativa**: Evitar multas e danos à reputação da CPTM.
   - **Responsável**: Consultor Jurídico.
   - **Probabilidade**: 10%
   - **Impacto**: 4 (Alto)
   - **Pontuação do Risco**: 0.1 * 4 = 0.4

5. **Baixa Aderência Inicial das Ferramentas**
   - **Descrição**: Alguns usuários podem inicialmente resistir ao uso das novas ferramentas por falta de familiaridade ou por preferirem métodos antigos.
   - **Estratégia**: Mitigar
   - **Ação**: Facilitar o processo de transição com suporte técnico contínuo e simplificar a interface das ferramentas para facilitar o uso.
   - **Justificativa**: Aumentar a taxa de adoção e garantir que as ferramentas sejam integradas ao trabalho diário.
   - **Responsável**: Equipe de Suporte Técnico.
   - **Probabilidade**: 30%
   - **Impacto**: 2 (Baixo)
   - **Pontuação do Risco**: 0.3 * 2 = 0.6

6. **Escalabilidade Limitada Inicialmente**
   - **Descrição**: O sistema de Big Data pode ter limitações de escalabilidade no início da implementação, o que pode afetar seu desempenho à medida que o volume de dados cresce.
   - **Estratégia**: Mitigar
   - **Ação**: Planejar uma solução de escalabilidade em fases e monitorar o desempenho constantemente.
   - **Justificativa**: Garantir que o sistema possa lidar com volumes crescentes de dados ao longo do tempo.
   - **Responsável**: Líder Técnico do Projeto.
   - **Probabilidade**: 50%
   - **Impacto**: 1 (Muito Baixo)
   - **Pontuação do Risco**: 0.5 * 1 = 0.5

7. **Baixa Qualidade nos Dados Recebidos**
   - **Descrição**: Dados de baixa qualidade podem comprometer a precisão das análises e gerar decisões incorretas.
   - **Estratégia**: Mitigar
   - **Ação**: Implementar processos de verificação e limpeza de dados antes de sua análise.
   - **Justificativa**: Garantir que as análises sejam precisas e baseadas em dados confiáveis.
   - **Responsável**: Equipe de Análise de Dados.
   - **Probabilidade**: 70%
   - **Impacto**: 4 (Alto)
   - **Pontuação do Risco**: 0.7 * 4 = 2.8

8. **Baixa Adoção de Recursos de Cloud**
   - **Descrição**: A resistência interna à adoção de soluções em nuvem pode limitar a eficácia do projeto.
   - **Estratégia**: Mitigar
   - **Ação**: Demonstrar os benefícios da nuvem por meio de testes piloto e comparar custos e vantagens com a infraestrutura tradicional.
   - **Justificativa**: Incentivar a adoção de soluções em nuvem para aumentar a flexibilidade e escalabilidade.
   - **Responsável**: Líder de TI.
   - **Probabilidade**: 50%
   - **Impacto**: 4 (Alto)
   - **Pontuação do Risco**: 0.5 * 4 = 2.0

#### 2.3.1.2 Oportunidades

1. **Treinamento Contínuo dos Usuários**
   - **Descrição**: Implementação de um programa de treinamento contínuo para capacitar os usuários finais, aumentando o entendimento e uso adequado das ferramentas.
   - **Estratégia**: Mitigar o risco de baixa adesão e de falta de treinamento para os usuários finais.
   - **Justificativa**: Treinamentos regulares reduzem o risco de baixa adoção e melhoram a experiência de uso, aumentando a eficiência e precisão na análise de dados.
   - **Responsável**: Equipe de Operações e RH.
   - **Probabilidade**: 50%
   - **Impacto**: 4 (Alto)
   - **Pontuação da Oportunidade**: 0.5 * 4 = 2.0

2. **Implementação de Controles de Qualidade dos Dados**
   - **Descrição**: Criar processos rigorosos de controle de qualidade dos dados para evitar dados corrompidos ou de baixa qualidade.
   - **Estratégia**: Mitigar o risco de baixa qualidade nos dados recebidos e de adoção de recursos de cloud.
   - **Justificativa**: Garantir que os dados sejam de alta qualidade, reduzindo o risco de conclusões erradas devido a dados defeituosos.
   - **Responsável**: Equipe de Qualidade de Dados.
   - **Probabilidade**: 70%
   - **Impacto**: 5 (Muito Alto)
   - **Pontuação da Oportunidade**: 0.7 * 5 = 3.5

3. **Integração com Sistemas Existentes**
   - **Descrição**: Desenvolver uma estratégia de integração para conectar o pipeline de Big Data aos sistemas legados e plataformas já utilizadas na CPTM.
   - **Estratégia**: Mitigar o risco de dificuldade na integração de dados entre diferentes sistemas e fontes.
   - **Justificativa**: Reduzir o risco de fragmentação de dados, garantindo que todos os dados sejam analisados de forma integrada e eficiente.
   - **Responsável**: Arquiteto de Soluções.
   - **Probabilidade**: 70%
   - **Impacto**: 4 (Alto)
   - **Pontuação da Oportunidade**: 0.7 * 4 = 2.8

4. **Monitoramento e Alerta Automatizado**
   - **Descrição**: Implementação de sistemas de monitoramento e alerta para detectar e corrigir falhas em tempo real.
   - **Estratégia**: Mitigar o risco de ineficiências operacionais e antecipar problemas de desempenho.
   - **Justificativa**: O monitoramento automatizado reduz o tempo de resposta a problemas, melhorando a confiabilidade e eficiência das operações.
   - **Responsável**: Equipe de Engenharia.
   - **Probabilidade**: 70%
   - **Impacto**: 3 (Moderado)
   - **Pontuação da Oportunidade**: 0.7 * 3 = 2.1

5. **Processo de Limpeza e Validação de Dados**
   - **Descrição**: Implementação de um processo automatizado para limpeza e validação dos dados antes da análise.
   - **Estratégia**: Mitigar o risco de baixa qualidade nos dados recebidos e problemas de análise devido a dados incorretos.
   - **Justificativa**: Garantir que os dados sejam válidos e consistentes antes de serem analisados, melhorando a qualidade das decisões.
   - **Responsável**: Equipe de Qualidade de Dados.
   - **Probabilidade**: 50%
   - **Impacto**: 4 (Alto)
   - **Pontuação da Oportunidade**: 0.9 * 5 = 4.5

6. **Plano de Contingência para Vazamento de Dados**
   - **Descrição**: Desenvolver um plano de contingência para responder a vazamentos de dados de maneira rápida e eficaz.
   - **Estratégia**: Mitigar o risco de vazamento de dados e fortalecer a segurança da informação.
   - **Justificativa**: Um plano de contingência reduz o impacto de possíveis incidentes de segurança, garantindo uma resposta eficiente e preservando a confiança dos stakeholders.
   - **Responsável**: Equipe de Segurança da Informação.
   - **Probabilidade**: 30%
   - **Impacto**: 5 (Muito Alto)
   - **Pontuação da Oportunidade**: 0.3 * 5 = 1.5


<p align="justify">&ensp;&ensp;A análise detalhada das ameaças e oportunidades para o projeto de implementação do pipeline de Big Data na CPTM revela a importância de um planejamento cuidadoso e de ações proativas. A identificação de riscos, como a baixa adesão dos usuários e a possibilidade de vazamentos de dados, junto às oportunidades de aprimoramento na experiência do usuário e fortalecimento da segurança, permitirá à CPTM não apenas mitigar possíveis impactos negativos, mas também explorar todo o potencial que a análise de dados pode oferecer. A conclusão bem-sucedida desse projeto não só atenderá às necessidades imediatas da empresa, mas também abrirá novas possibilidades de crescimento e inovação no futuro.</p>

# <a id="c3"></a>3 Arquitetura e Design do Sistema
## <a id="c3.1"></a>3.1 Wireframes

<p align="justify">&ensp;&ensp;"Em web design, um wireframe ou diagrama de wireframe é uma representação visual em escala de cinza da estrutura e funcionalidade de uma única página web ou uma tela de aplicativo móvel. Wireframes são usados ​​no início do processo de desenvolvimento para estabelecer a estrutura básica de uma página antes de acrescentar o design visual e conteúdo, e podem ser criados usando papel, em HTML/CSS ou usando aplicativos de software." (Lucidchart, 2022). Nesse sentido, é essencial criar essa idealização simplificada para possibilitar a validação com o parceiro. Desse modo, é possível avaliar a interface do sistema desse projeto um modo mais rápido e barato.</p>
<p align="justify">&ensp;&ensp;Para que seja possível realizar essa prototipação de baixa fidelidade, será utilizada a ferramenta Figma. Essa ferramenta permite o desenvolvimento de interfaces modularizadas e adaptáveis a diferentes resoluções. Portanto, ela garante uma maior similaridade entre o protótipo e a futura interface real.</p>
<p align="justify">&ensp;&ensp;Ademais, é essencial compreender qual será a ferramenta utilizada para codificação das telas, pois ela pode conter limitações visuais. Devido ao contexto do projeto e à grande necessidade de informar dados de forma visual, foi necessário escolher uma biblioteca que atendesse esses requisitos. Dito isso, foi utilizado o Streamlit, que é uma biblioteca em Python que possibilita a criação de gráficos dinâmicos e a apresentação em um website.</p>


### 3.1.1 Wireframe Desktop

<p align="justify">&ensp;&ensp;O seguinte tópico apresenta o wireframe de baixa fidelidade da versão desktop do <i>Data App</i>, com o objetivo de fornecer uma visão estruturada e organizada da interface que será desenvolvida. O <i>wireframe</i> define a disposição de elementos principais, como a <i>sidebar</i> de navegação, áreas de cabeçalho, seções de descrição, filtros e gráficos, garantindo que o usuário tenha uma experiência intuitiva e funcional ao interagir com o sistema. Essa estrutura inicial serve como base para o desenvolvimento visual e funcional do aplicativo, orientando o posicionamento e a funcionalidade de cada componente da interface para facilitar a navegação e a análise de dados no ambiente <i>desktop</i>. Por último, importante ressaltar também que o <i>Data App</i> será desenvolvido em <i>Streamlit</i>, uma tecnologia <i>Python</i> ótima para esse tipo de projeto.</p>

<br>
<div align="center">
  <figcaption style="text-align: center; font-size: 10px; margin-bottom: 5px;">Figura 7 - Wireframe Home</figcaption>
  <img src="https://res.cloudinary.com/dxjfonp85/image/upload/v1730321604/ddrn4zmrsolfcfqpfgfp.png" alt="Wireframe Home" style="width: 100%; display: block; margin: 0 auto;">
  <figcaption style="text-align: center; font-size: 10px; margin-top: 5px;">Fonte: Elaboração Própria</figcaption>
</div>
<br>


<p align="justify">&ensp;&ensp;A página <i>Home</i> do <i>Data App</i> tem como objetivo principal introduzir o sistema, explicando seus objetivos e sua proposta. No lado esquerdo, encontra-se a <i>sidebar</i>, um menu navegável que permite o acesso rápido a todas as seções do app, incluindo cada linha individual e a seção de comparação de linhas. Na área principal, a <i>Home</i> possui um cabeçalho que destaca o título da página e, abaixo, uma descrição que apresenta um resumo de todo <i>Data App</i>, detalhando seus objetivos, benefícios, e principais funcionalidades. Essa página serve como ponto de partida para o usuário, fornecendo uma visão geral da aplicação. Na <i>sidebar</i>, os botões acionáveis estão destacados em vermelho, indicando os botões que levam a outras seções do app ou retrai a <i>sidebar</i>.
</p>

<br>
<div align="center">
  <figcaption style="text-align: center; font-size: 10px; margin-bottom: 5px;">Figura 8 - Linha 7</figcaption>
  <img src="https://res.cloudinary.com/dxjfonp85/image/upload/v1730321604/fjic9ngfn9lg4qiufmzk.png" alt="Linha 7" style="width: 100%; display: block; margin: 0 auto;">
  <figcaption style="text-align: center; font-size: 10px; margin-top: 5px;">Fonte: Elaboração Própria</figcaption>
</div>
<br>


<p align="justify">&ensp;&ensp;A página Linha 7 - Rubi fornece dados específicos sobre a Linha 7, com uma estrutura que permite ao usuário filtrar as informações de acordo com critérios específicos. A <i>sidebar</i> mantém-se como um menu de navegação, possibilitando a mudança para outras linhas e funcionalidades. Na área principal, a seção começa com uma descrição que contextualiza os dados apresentados sobre a Linha 7. Em seguida, a página oferece uma barra de filtros que permite o ajuste da visualização dos dados, com opções como seleção de estação, período do dia (manhã, tarde, noite), dia da semana e um controle deslizante para ajustar o espaço de tempo. Abaixo da barra de filtros, encontra-se a seção de gráficos, onde são exibidas visualizações com base nos dados filtrados. Na parte inferior da página, três pontos vermelhos indicam a continuidade da seção de gráficos, indicando a presença de mais informações ao deslizar ou rolar a página.
</p>

<br>
<div align="center">
  <figcaption style="text-align: center; font-size: 10px; margin-bottom: 5px;">Figura 9 - Linha 10</figcaption>
  <img src="https://res.cloudinary.com/dxjfonp85/image/upload/v1730321604/fitz2h4ekk9ltbhidfnw.png" alt="Linha 10" style="width: 100%; display: block; margin: 0 auto;">
  <figcaption style="text-align: center; font-size: 10px; margin-top: 5px;">Fonte: Elaboração Própria</figcaption>
</div>
<br>

<p align="justify">&ensp;&ensp;A página Linha 10 exibe informações detalhadas sobre a Linha 10, utilizando uma estrutura semelhante à da Linha 7 para facilitar a navegação e compreensão dos dados. A <i>sidebar</i> mantém a navegação entre as diversas linhas e funcionalidades do app. A área principal inicia-se com uma descrição dos dados específicos da Linha 10, seguida pela barra de filtros, que permite selecionar critérios como estação, período do dia, dia da semana e espaço de tempo através de um controle deslizante. Na seção de gráficos, o usuário pode visualizar os dados conforme as configurações aplicadas na barra de filtros. Essa página proporciona uma análise personalizada da Linha 10, permitindo ao usuário ajustar a visualização de acordo com suas necessidades informacionais.
</p>

<br>
<div align="center">
  <figcaption style="text-align: center; font-size: 10px; margin-bottom: 5px;">Figura 10 - Linha 11</figcaption>
  <img src="https://res.cloudinary.com/dxjfonp85/image/upload/v1730321604/x8esuao1udvqpdzbdynh.png" alt="Linha 11" style="width: 100%; display: block; margin: 0 auto;">
  <figcaption style="text-align: center; font-size: 10px; margin-top: 5px;">Fonte: Elaboração Própria</figcaption>
</div>
<br>

<p align="justify">&ensp;&ensp;A página Linha 11 tem como objetivo mostrar dados específicos da Linha 11, seguindo o mesmo <i>layout</i> para garantir consistência na experiência do usuário. A <i>sidebar</i> permite o acesso rápido a outras páginas, enquanto a área principal apresenta uma breve descrição dos dados da Linha 11. Abaixo da descrição, a barra de filtros oferece as mesmas opções das páginas anteriores, incluindo filtros de estação, período do dia, dia da semana e controle deslizante para o espaço de tempo. A seção de gráficos exibe visualizações ajustadas de acordo com os filtros aplicados, facilitando a análise dos dados da Linha 11 de forma personalizada.
</p>

<br>
<div align="center">
  <figcaption style="text-align: center; font-size: 10px; margin-bottom: 5px;">Figura 11 - Linha 12</figcaption>
  <img src="https://res.cloudinary.com/dxjfonp85/image/upload/v1730321603/liwarz1czwdvuqdjji5a.png" alt="Linha 12" style="width: 100%; display: block; margin: 0 auto;">
  <figcaption style="text-align: center; font-size: 10px; margin-top: 5px;">Fonte: Elaboração Própria</figcaption>
</div>
<br>

<p align="justify">&ensp;&ensp;A página Linha 12 é projetada para fornecer uma visão detalhada dos dados relativos à Linha 12, mantendo o padrão de navegação e estrutura das páginas anteriores. A <i>sidebar</i> possibilita a mudança rápida entre diferentes páginas, enquanto a área principal começa com uma descrição que contextualiza os dados da Linha 12. Abaixo da descrição, a barra de filtros permite que o usuário ajuste a visualização de dados de acordo com critérios como estação, período do dia, dia da semana e um controle deslizante para o tempo. A seção de gráficos exibe visualizações específicas para a Linha 12, adaptadas às preferências configuradas na barra de filtros, oferecendo uma experiência personalizada.
</p>

<br>
<div align="center">
  <figcaption style="text-align: center; font-size: 10px; margin-bottom: 5px;">Figura 12 - Linha 13</figcaption>
  <img src="https://res.cloudinary.com/dxjfonp85/image/upload/v1730321603/mj9apqu6brwmoa5mcr8w.png" alt="Linha 13" style="width: 100%; display: block; margin: 0 auto;">
  <figcaption style="text-align: center; font-size: 10px; margin-top: 5px;">Fonte: Elaboração Própria</figcaption>
</div>
<br>

<p align="justify">&ensp;&ensp;A Página Linha 13 apresenta dados específicos da Linha 13, com a mesma estrutura das outras páginas dedicadas às linhas. A <i>sidebar</i> permanece como elemento fixo de navegação entre as diferentes linhas e funcionalidades do app. Na área principal, uma breve descrição introduz os dados relevantes sobre a Linha 13. A barra de filtros permite a personalização dos dados exibidos, com filtros que incluem estação, período do dia, dia da semana e espaço de tempo ajustável. Abaixo da barra de filtros, a seção de gráficos apresenta visualizações dos dados da Linha 13, que podem ser ajustadas conforme as preferências do usuário.
</p>

<br>
<div align="center">
  <figcaption style="text-align: center; font-size: 10px; margin-bottom: 5px;">Figura 13 - Comparar Linhas</figcaption>
  <img src="https://res.cloudinary.com/dxjfonp85/image/upload/v1730321604/bg7cr3gpjsvtlr0ipjvc.png" alt="Comparar Linhas" style="width: 100%; display: block; margin: 0 auto;">
  <figcaption style="text-align: center; font-size: 10px; margin-top: 5px;">Fonte: Elaboração Própria</figcaption>
</div>
<br>

<p align="justify">&ensp;&ensp;Por fim, a página Comparar Linhas permite ao usuário realizar comparações entre os dados de diferentes linhas, oferecendo uma visão comparativa que facilita a análise integrada. A <i>sidebar</i> continua como uma navegação entre todas as páginas do app. Na área principal, há uma descrição inicial explicando o propósito e as funcionalidades da comparação de linhas. Em seguida, uma seção de escolha permite que o usuário selecione as linhas que deseja comparar. Após a seleção, a seção de gráficos exibe visualizações lado a lado das linhas escolhidas, permitindo uma análise comparativa das métricas e dados, proporcionando <i>insights</i> mais abrangentes e estratégicos.
</p>

<p align="justify">&ensp;&ensp;Concluindo, o <i>layout</i> apresentado oferece uma estrutura visual clara e funcional para a interface do <i>Data App</i> na versão <i>desktop</i>, permitindo que os usuários naveguem e analisem dados de forma eficiente e intuitiva. O <i>wireframe</i> estabelece uma base sólida para o desenvolvimento da interface, orientando a disposição dos elementos de navegação, filtros e visualizações de dados. Essa organização preliminar facilita o alinhamento entre as necessidades dos usuários e as funcionalidades do sistema, garantindo que o aplicativo atenda às expectativas de usabilidade e proporcione uma experiência enriquecedora na análise de informações.
</p>

## <a id="c3.1.2"></a>3.1.2 Wireframe Mobile.

<p align="justify">&ensp;&ensp;
O seguinte tópico apresenta o wireframe de baixa fidelidade da versão mobile do Data App, com o objetivo de oferecer uma visão estruturada e simplificada da interface para dispositivos móveis. O wireframe define a disposição dos elementos principais, como o menu de navegação acessível, áreas de cabeçalho, seções de descrição, filtros compactados e gráficos ajustados para o formato mobile, garantindo que o usuário tenha uma experiência intuitiva e eficiente ao utilizar o aplicativo em telas menores. Essa estrutura inicial serve como base para o desenvolvimento visual e funcional, orientando o posicionamento e a funcionalidade de cada componente para uma navegação facilitada e uma análise de dados otimizada no ambiente mobile.
</p>

<br>
<div align="center">
  <figcaption style="text-align: center; font-size: 10px; margin-bottom: 5px;">Figura 14 - Wireframe página Home Mobile</figcaption>
  <img src="https://res.cloudinary.com/dowilmxvk/image/upload/v1731077903/iPhone_14_15_Pro_Max_-_1_qmj0ai.png" alt="Wireframe página Home Mobile" style="width: 100%; display: block; margin: 0 auto;">
  <figcaption style="text-align: center; font-size: 10px; margin-top: 5px;">Fonte: Elaborado pela Equipe Quartzo</figcaption>
</div>
<br>

<p align="justify">&ensp;&ensp;A página Home da versão mobile do Data App foi projetada para apresentar o sistema, destacando seus objetivos e proposta de valor. Para otimizar o espaço limitado da tela em dispositivos móveis, o menu de navegação, que na versão desktop está em uma barra lateral, foi substituído por um ícone de menu hambúrguer no canto superior esquerdo. Essa abordagem permite que os usuários acessem facilmente as diferentes seções do aplicativo sem comprometer a área de conteúdo principal.</p>

<p align="justify">&ensp;&ensp;O menu hambúrguer é amplamente utilizado em design de interfaces de usuário para economizar espaço na tela e fornecer acesso fácil aos itens de menu ocultos. Na área principal, a página exibe um cabeçalho com o título, seguido por uma descrição que resume o Data App, detalhando seus objetivos, benefícios e principais funcionalidades.</p>


<br>
<div align="center">
  <figcaption style="text-align: center; font-size: 10px; margin-bottom: 5px;">Figura 15 - Wireframe Página Navegação Mobile</figcaption>
  <img src="https://res.cloudinary.com/dowilmxvk/image/upload/v1730321043/rxlg0vww8axgluzju0tp.png" alt="Wireframe Página Navegação Mobile" style="width: 100%; display: block; margin: 0 auto;">
  <figcaption style="text-align: center; font-size: 10px; margin-top: 5px;">Fonte: Elaborado pela Equipe Quartzo</figcaption>
</div>
<br>

<p align="justify">&ensp;&ensp;A página de navegação do Data App organiza os dados de fluxo de pessoas segmentados por linhas da CPTM, permitindo que o usuário acesse rapidamente os KPIs específicos de cada linha sem percorrer uma lista extensa de estações. Essa estrutura facilita a visualização dos dados ao agrupar todas as estações de uma mesma linha em uma única seção, proporcionando uma navegação mais eficiente e objetiva. Com esse layout, o usuário pode alternar facilmente entre diferentes linhas para análise, obtendo uma visão clara e organizada dos fluxos de passageiros em cada linha específica da CPTM.</p>

<p align="justify">&ensp;&ensp;A utilização de uma barra lateral para navegação é eficaz em cenários onde há múltiplas categorias ou seções, permitindo acesso rápido e direto às informações desejadas</p>

<br>
<div align="center">
  <figcaption style="text-align: center; font-size: 10px; margin-bottom: 5px;">Figura 16 - Wireframe Página Análise Mobile</figcaption>
  <img src="https://res.cloudinary.com/dowilmxvk/image/upload/v1730321043/z6ggoggvei3ttcoslptl.png" alt="Wireframe Página Análise Mobile" style="width: 100%; display: block; margin: 0 auto;">
  <figcaption style="text-align: center; font-size: 10px; margin-top: 5px;">Fonte: Elaborado pela Equipe Quartzo</figcaption>
</div>
<br>

<p align="justify">&ensp;&ensp;Na versão mobile, a página da Linha 7 - Rubi apresenta uma estrutura focada na navegação e visualização de dados específicos da linha, seguindo um padrão replicado nas páginas das demais linhas da CPTM. No topo, um cabeçalho destaca o nome da linha, seguido de uma descrição recolhível que contextualiza as informações sobre o fluxo de pessoas. Abaixo, uma barra de filtros permite ao usuário ajustar os dados exibidos, com opções como seleção de estação, período do dia e dia da semana.
</p>

<p align="justify">&ensp;&ensp;Em seguida, encontra-se a seção de gráficos, onde as visualizações se atualizam conforme os filtros aplicados, oferecendo uma análise detalhada dos dados. Esse layout facilita o acesso e a comparação das informações entre as diferentes linhas, mantendo a experiência de navegação organizada e eficiente para o ambiente mobile.</p>

<p align="justify">&ensp;&ensp;A disposição dos filtros antes da apresentação dos gráficos permite que o usuário personalize a visualização dos dados de acordo com suas necessidades, melhorando a usabilidade e a eficiência na análise de informações</p>

---

<p align="justify">&ensp;&ensp;A estrutura proposta para os wireframes do Data App, tanto para as versões mobile quanto desktop, visa proporcionar uma interface organizada e intuitiva para a navegação e análise de dados. A versão mobile foi projetada para facilitar o acesso rápido às principais informações e funções em telas menores, com um menu de navegação recolhido, botões de destaque e uma organização segmentada das linhas da CPTM, otimizando a experiência do usuário.</p>

<p align="justify">&ensp;&ensp;Na versão desktop, o uso de uma sidebar fixa permite uma navegação eficiente entre as diferentes seções do aplicativo. Cada página dedicada às linhas de transporte segue um layout consistente, com filtros de dados e gráficos dinâmicos ajustáveis, adaptados às necessidades informativas do usuário. A disposição das ferramentas e visualizações reforça o foco do Data App em fornecer uma análise detalhada e comparativa dos dados, particularmente útil na página de comparação entre linhas, onde o usuário pode visualizar métricas lado a lado.</p>

<p align="justify">&ensp;&ensp;Esse planejamento visual e funcional, baseado em estudos de usabilidade e referências confiáveis, estabelece uma base sólida para o desenvolvimento da interface final. Ao garantir uma experiência intuitiva e otimizada, o Data App consegue alinhar suas funcionalidades com as expectativas dos usuários, permitindo uma navegação fluida e uma análise de dados enriquecedora para diferentes tipos de dispositivos.</p>


## <a id="c3.2"></a>3.2 Diagrama UML

<p align="justify">&ensp;&ensp;"UML, abreviado do inglês Unified Modeling Language (Linguagem de Modelagem Unificada), é uma maneira de representar visualmente a arquitetura, o design e a implementação de sistemas de software complexos. Quando [se escreve] código, é difícil acompanhar os relacionamentos e hierarquias dentro de um sistema de software com as milhares de linhas existentes em uma aplicação. Os diagramas UML dividem esse sistema de software em componentes e subcomponentes." (Lucidchart, 2020). Nesse sentido, é essencial que esse projeto, devido ao seu tamanho, contenha diagramas que representem o tamanho do sistema.</p>

### <a id="c3.2.1"></a>3.2.1 Diagrama de Componentes - Arquitetura do Sistema (Sprint 1)

<br>
<div align="center">
  <figcaption style="text-align: center; font-size: 10px; margin-bottom: 5px;">Figura 17 - Diagrama de Componentes</figcaption>
  <img src="https://res.cloudinary.com/ddgzjcfwi/image/upload/v1731040782/ksdnayznjkmotohouix1.jpg" alt="Diagrama de Componentes" style="width: 100%; display: block; margin: 0 auto;">
  <figcaption style="text-align: center; font-size: 10px; margin-top: 5px;">Fonte: Elaboração Própria</figcaption>
</div>
<br>


1. **Fonte de Dados**: 
   - A seção inicial representa os arquivos de dados em formato CSV (`dmo_anl_vw_estacao` e `dmo_anl_vw_tot_mov`). Esses arquivos contêm os dados brutos que serão processados nas próximas etapas.
   - Esses arquivos são a entrada para o sistema, sendo transferidos para a próxima seção através de um processo automatizado.

2. **Automação e Ingestão de Dados**:
   - Esta etapa é responsável pela automação e ingestão dos dados a partir dos arquivos CSV.
   - O Python, juntamente com a biblioteca **Poetry**, é utilizado para executar scripts que leem e pré-processam os dados. O uso do **Jupyter Notebook** permite uma análise inicial e testes de scripts em um ambiente interativo, facilitando a validação e ajuste de código.
   - Os dados pré-processados são então transferidos para a próxima seção, onde ocorre a preparação e armazenamento de forma estruturada.

3. **Preparação e Armazenamento de Dados**:
   - Após a ingestão, os dados são processados e armazenados utilizando duas tecnologias principais: **ClickHouse** e **Amazon S3**.
   - O **Amazon S3** serve como uma camada de armazenamento de dados brutos e intermediários, oferecendo escalabilidade e segurança para grandes volumes de dados.
   - O **ClickHouse**, um banco de dados columnar, é utilizado para armazenar e organizar os dados de forma otimizada para consultas analíticas. Python atua como intermediário, transferindo os dados do S3 para o ClickHouse, preparando-os para análises mais complexas.
   - Essa arquitetura de armazenamento garante que os dados estejam disponíveis e organizados para as próximas etapas de análise.

4. **Análise Estatística**:
   - Esta seção é focada na aplicação de técnicas estatísticas para análise dos dados, utilizando **Python**.
   - As análises realizadas incluem estatísticas descritivas e possíveis modelagens, dependendo das necessidades do projeto.
   - Os resultados da análise são então enviados para a próxima etapa, onde são transformados em infográficos e visualizações.

5. **Infográfico**:
   - A última seção utiliza **Streamlit** para criar visualizações e infográficos interativos. Streamlit permite a criação de dashboards que facilitam a interpretação dos resultados das análises para os usuários finais.
   - Python transfere os dados analisados para o Streamlit, onde são gerados gráficos e tabelas, oferecendo uma interface visual para a apresentação dos resultados.


<p align="justify">&ensp;&ensp;Em resumo, o diagrama de componentes desempenha um papel crucial na representação da arquitetura do sistema, evidenciando o fluxo de dados desde a ingestão inicial até a apresentação final em infográficos. É importante mencionar que o diagrama está suscetível a mudanças e refinamentos para melhor se adequar ao projeto e suas necessidades.
</p>

### <a id="c3.2.1"></a>3.2.2 Diagrama de Componentes - Arquitetura do Sistema (Sprint 4)

<p align="justify">&ensp;&ensp;Com o andamento do projeto e a escuta de feedbacks da CPTM, a arquitetura do projeto sofreu mudanças para melhor atender as necessidades do cliente. A maior parte da arquitetura se manteve, contudo a partir da etapa de preparação e armazenamento de dados, o projeto teve mudanças mais significativas.
</p>

<br>
<div align="center">
  <figcaption style="text-align: center; font-size: 10px; margin-bottom: 5px;">Figura 17 - Diagrama de Componentes</figcaption>
  <img src="https://res.cloudinary.com/ddgzjcfwi/image/upload/v1733256669/tqvrq6wtzwkbzttp7dyj.jpg" alt="Diagrama de Componentes" style="width: 100%; display: block; margin: 0 auto;">
  <figcaption style="text-align: center; font-size: 10px; margin-top: 5px;">Fonte: Elaboração Própria</figcaption>
</div>
<br>

1. **Mudanças Principais**: 
   - Adição do Docker na fase do ETL e no display dos dados no dataApp.
     - O Docker é uma plataforma que permite criar contêiners que visam facilitar a implementação de um software ao garantir que todos os elementos necessários para sua execução estejam emcapsulados de forma leve e segura. Ele foi utilizado no projeto para facilitar a escalabilidade e sua migração para diferentes ambientes.
   - Utilização do SQS, PostegreSQL e Metabase nas fases de Armazenamento de dados e de display dos infográficos.
  
     - No novo fluxo criado por essas 3 novas tecnologias foram implementadas com o intuito de diminuir o tempo do processo do ETL. Isso ocorre ao delegar a inserção de logs ao banco de dados Postegre por um serviço separado, para que esse serviço tenha escalabilidade, foi criado uma fila em SQS que guarda os logs feitos pelo ETL. Para analisar o andamento desse processo, o Metabase funciona como ferramenta de observação dos logs armazenados ao longo da operação do projeto. 
  
<p align="justify">&ensp;&ensp;Concluindo, com as mudanças feitas, o projeto terá um tempo de processamento melhor, além de apresentar mudanças que facilitam tanto a sua escalabilidade quanto a sua manutenção.</p> 

# <a id="c4"></a>4 Exploração de Dados
## <a id="c4.1"></a>4.1 Data Model Canvas

<p align="justify">&ensp;&ensp;O **Data Model Canvas**, também conhecido como **Data Product Canvas**, é uma ferramenta visual que organiza e estrutura informações essenciais para o desenvolvimento de produtos baseados em dados, facilitando o planejamento e alinhamento entre equipes e stakeholders. Ele permite identificar o problema a ser resolvido, os dados necessários, as hipóteses a serem testadas, os KPIs de sucesso, as ações e os riscos envolvidos. Essa metodologia oferece uma estrutura clara e lógica para conectar os desafios do cliente às soluções e métricas que avaliam o sucesso do projeto, garantindo que o produto de dados gere valor ao negócio (CARVALHO, 2019).</p>

<br>
<div align="center">
  <figcaption style="text-align: center; font-size: 10px; margin-bottom: 5px;">Figura 18 - Data Model Canvas</figcaption>
  <img src="https://res.cloudinary.com/dxjfonp85/image/upload/v1730827489/lykcawm99qeejyow7oce.png" alt="Data Model Canvas" style="width: 100%; display: block; margin: 0 auto;">
  <figcaption style="text-align: center; font-size: 10px; margin-top: 5px;">Fonte: Elaboração Própria</figcaption>
</div>
<br>

<p align="justify">&ensp;&ensp;De acordo com o Data Model Canvas, pode-se extrair as seguintes informações:</p>

### 4.1.1 Proposta de Valor:
<p align="justify">&ensp;&ensp;O produto oferece uma solução robusta de análise de Big Data, projetada especificamente para atender aos desafios operacionais da CPTM, como a gestão do fluxo de passageiros em horários de pico e eventos especiais. Utilizando dados históricos e em tempo real, a solução permite gerar insights preditivos que auxiliam na tomada de decisões mais informadas, como o ajuste da frequência dos trens e a alocação de recursos operacionais. Isso resulta em uma operação mais eficiente e adaptada às demandas diárias e excepcionais do transporte público.

Além disso, a ferramenta contribui diretamente para a melhoria da experiência dos passageiros, reduzindo superlotação e otimizando o fluxo nas estações e nos trens. Com a identificação antecipada de gargalos e demandas críticas, a CPTM pode aumentar a pontualidade, o conforto e a satisfação dos usuários. Dessa forma, o produto entrega valor estratégico ao alinhar eficiência operacional e qualidade do serviço, promovendo um transporte público mais confiável e moderno.</p>

### 4.1.2 Estrutura de Dados:

<br>
<div align="center">
  <figcaption style="text-align: center; font-size: 10px; margin-bottom: 5px;">Figura 19 - Arquitetura Proposta</figcaption>
  <img src="https://res.cloudinary.com/ddgzjcfwi/image/upload/v1731506876/ezkuwegp7cjbod8yijpd.jpg" alt="Arquitetura Proposta" style="width: 100%; display: block; margin: 0 auto;">
  <figcaption style="text-align: center; font-size: 10px; margin-top: 5px;">Fonte: Elaboração Própria</figcaption>
</div>
<br>

**Coleta de Dados:** 
<p align="justify">&ensp;&ensp;Os dados disponibilizados pela CPTM foram coletados de várias fontes internas e estão organizados em diferentes formatos, como CSV, Excel, e relatórios zipados. A diversidade dessas fontes e formatos reflete a amplitude das operações da CPTM, cobrindo aspectos críticos como falhas operacionais, ocorrências diárias, dados de viagens, e outros eventos operacionais. Esses dados fornecem uma visão abrangente da operação ferroviária, permitindo a análise de problemas, otimização de recursos e tomada de decisões estratégicas.</p>

**Armazenamento de Dados**  
<p align="justify">&ensp;&ensp;Os dados coletados serão armazenados de maneira estruturada e organizada em diferentes camadas de armazenamento, como mostrado na arquitetura:</p>

- **Data Lake:**  
  O Data Lake será usado para armazenar dados brutos sem transformações imediatas. Isso inclui logs de falhas, ocorrências, e dados em tempo real de sensores e bilhetagem.

- **Data Warehouses:**  
  O armazenamento dos dados estruturados, como históricos de falhas e dados de viagens, será feito no Data Warehouse. Ele centraliza dados transformados e prontos para serem usados em análises.

- **Cubo de Dados:**  
  Permite a exploração multidimensional dos dados (por exemplo, análise por linha, estação, horários) para gerar insights detalhados.

- **Arquitetura Medalhão (Bronze, Silver, Gold):**  
  Os dados passarão por uma estrutura de níveis. O **ETL Bronze** processa e limpa os dados brutos, que são refinados e movidos para a proxima camada chamada de **ETL Silver** onde os dados são tratados e tem uma granularidade padrão, e por último tem a camada **ETL Gold**, onde os dados já estão correlacionados e já tornam possível o uso de análises e relatórios mais detalhados para gerar insights para o negócio.

---

**Processamento e Utilização dos Dados**  
<p align="justify">&ensp;&ensp;Os dados armazenados serão processados e utilizados para gerar insights acionáveis e ajudar a otimizar a operação ferroviária da CPTM.</p>

- **Análise Exploratória Avançada:**  
  Utilizando ferramentas como **Jupyter Notebook**, análises exploratórias serão realizadas para identificar padrões e tendências. Essa fase serve para entender os dados de maneira mais profunda.

- **Automatização do Pipeline:**  
  O processo de ingestão e transformação dos dados será automatizado para garantir que os dados estejam sempre atualizados para análises em tempo real e preditivas. Isso inclui a geração de métricas e a criação de rotinas de processamento contínuo.

- **Pacote DataAPP:**  
  O pacote **DataAPP** será responsável por organizar os dados finais e disponibilizar insights operacionais para os gestores. Esses pacotes de dados estruturados estarão prontos para serem acessados através de dashboards e relatórios automatizados.

- **Dashboards e Relatórios Gerenciais:**  
  Utilizando ferramentas como **Power BI** ou **Tableau**, os dados processados serão visualizados em tempo real através de dashboards que exibem KPIs críticos, como a taxa de ocupação, atrasos, superlotação, e performance de cada linha.

- **Métricas e Telemetria:**  
  KPIs operacionais serão monitorados em tempo real, permitindo que a equipe da CPTM ajuste a operação conforme as condições variam.

- **Análises Preditivas:**  
  Através da utilização de **machine learning**, o sistema será capaz de prever falhas operacionais e picos de demanda, possibilitando ajustes operacionais proativos, como o aumento da frequência dos trens em horários de pico.

---

**Segurança e Autenticação**  
<p align="justify">&ensp;&ensp;Os dados sensíveis serão protegidos por sistemas de segurança robustos, garantindo que apenas usuários autorizados possam acessar informações operacionais críticas.  </p>

- **Tecnologias sugeridas:** Criptografia de dados, controle de acesso baseado em funções (RBAC), e autenticação multifator.

---

### 4.1.3 Perfil dos Usuários: 
- **Gestores Operacionais:** Necessitam de ferramentas para monitorar em tempo real o fluxo de passageiros, atrasos, e gargalos nas operações diárias. A solução permitirá identificar padrões e prever picos de demanda, otimizando rotas e ajustando a frequência dos trens para melhorar a eficiência operacional e reduzir atrasos.

- **Equipe de Manutenção:** Enfrenta desafios em prever falhas e programar intervenções de forma proativa. Com insights sobre desgaste e falhas recorrentes, a solução ajuda a priorizar reparos preventivos, minimizando interrupções não planejadas no serviço e garantindo a continuidade das operações.

- **Gestores Administrativos:** Precisam planejar e alocar recursos com eficiência, equilibrando custos operacionais com a demanda de passageiros. A análise de dados proporcionará suporte para a criação de estratégias de otimização de custos, alinhando o planejamento financeiro às necessidades operacionais e aumentando a produtividade.

- **Passageiros:** São diretamente impactados pela qualidade do serviço e pela previsibilidade dos horários. A solução contribui para melhorar a experiência de viagem ao reduzir superlotação, garantir maior pontualidade e proporcionar uma jornada mais confortável e confiável.

### 4.1.4 Casos de Uso:

<p align="justify">&ensp;&ensp;A seguir estão detalhados três cenários práticos que ilustram como o sistema de Big Data proposto para a <b>CPTM</b> pode ser aplicado para otimizar operações, prever problemas e melhorar a experiência dos passageiros.</p>

---

**Cenário 1: Aumento no Fluxo de Passageiros Durante um Evento Grande:**<br/>
<p align="justify">&ensp;&ensp;Durante um evento de grande porte na cidade, como um show ou um jogo de futebol, o sistema de Big Data detecta um aumento significativo no fluxo de passageiros nas estações próximas ao local do evento.</p>

**Detecção e Ação:**  
<p align="justify">&ensp;&ensp;O sistema utiliza dados em tempo real dos sensores de fluxo e cruzamento com informações de eventos para identificar picos na movimentação de pessoas. Ao perceber o aumento, o sistema sugere automaticamente o envio de trens extras para evitar superlotação e reduzir o tempo de espera nas plataformas.</p>

**Benefícios:**
- **Melhora na experiência dos passageiros:** Evita superlotação e longos tempos de espera, proporcionando uma viagem mais confortável e ágil.
- **Otimização da operação:** A alocação inteligente de trens reduz o risco de sobrecarga em horários de pico e melhora a eficiência operacional.

---

**Cenário 2: Alerta de Manutenção Preventiva para Evitar Falha Mecânica**

<p align="justify">&ensp;&ensp;Com base em padrões históricos de falhas mecânicas e dados de desempenho operacional, o sistema identifica uma anomalia no comportamento de um dos trens em operação.</p>

**Detecção e Ação:**  
<p align="justify">&ensp;&ensp;A análise preditiva do sistema detecta uma possível falha no sistema de freios de um trem específico, com base em sinais de desgaste ou desempenho abaixo do esperado. Um alerta de manutenção preventiva é enviado automaticamente à equipe de manutenção, recomendando a substituição de peças antes que uma falha grave ocorra.</p>

**Benefícios:**
- **Redução de falhas inesperadas:** A manutenção preventiva evita interrupções na operação e aumenta a segurança dos passageiros.
- **Economia de custos:** A reparação antes da falha reduz custos com manutenção emergencial e evita danos colaterais maiores.

---

**Cenário 3: Melhoria em Estação com Alta Insatisfação**

<p align="justify">&ensp;&ensp;Com base na análise dos feedbacks dos passageiros e nas métricas de utilização da estação, o sistema identifica que uma estação específica apresenta altos níveis de insatisfação, com reclamações frequentes sobre superlotação, atrasos e falta de estrutura.</p>

**Detecção e Ação:**  
<p align="justify">&ensp;&ensp;A análise de feedbacks e de dados operacionais aponta que a estação 'X' tem uma taxa significativamente maior de reclamações em comparação a outras estações. O sistema gera um relatório priorizando essa estação para receber melhorias, que podem incluir aumento da frequência de trens, melhorias na sinalização e ajustes na infraestrutura.</p>

**Benefícios:**
- **Melhoria na satisfação dos passageiros:** A priorização de melhorias com base nos feedbacks diretos dos usuários aumenta a confiança e a percepção de qualidade do serviço.
- **Foco na eficiência:** A alocação de recursos é feita de forma estratégica, priorizando áreas críticas e maximizando o impacto positivo das melhorias realizadas.

---

**Cenário 4: Análise de comportamento de passageiros:**

<p align="justify">&ensp;&ensp; A partir de dashboards que representem diversos âmbitos do comportamento do passageiro, o Data App deve possibilitar que <i>insights</i> sejam gerados.</p>

- **Detecção e Ação:** O sistema analisa padrões de comportamento, como horários de pico e rotas mais utilizadas, para prever as demandas futuras e ajustar a alocação de recursos com antecedência.

- **Benefícios:** Ajuda na melhor distribuição de trens e recursos durante diferentes horários do dia, evitando subutilização ou superlotação.

---

**Cenário 5:** Previsão de Demandas Sazonais

<p align="justify">&ensp;&ensp; Com a análise de dados históricos, torna-se possivel identificar períodos os quais a demanda aumenta, com picos mais intensos e vales com movimentação inconsistente.</p>

- **Detecção e Ação:** O sistema analisa dados históricos de movimentação de passageiros para identificar padrões sazonais, como aumento de fluxo em datas comemorativas ou períodos de férias. Com isso, sugere um planejamento antecipado de trens extras e ajustes de horários.
  
- **Benefícios:** Garante que a operação esteja preparada para picos de demanda previsíveis, melhorando a satisfação dos passageiros e evitando sobrecargas.

---

### 4.1.5 Métricas de Sucesso: Indicadores

<p align="justify">&ensp;&ensp;Para medir a eficácia do sistema implementado e alinhar-se às expectativas da CPTM, foram definidos três KPIs (Key Performance Indicators) que avaliam aspectos fundamentais da operação e do impacto do sistema:</p>

- **Quantidade de PCD por Linha e Grupo PCD:** Indica a quantidade de passageiros por linha, segmentados por grupos de Pessoas com Deficiência (60+, Autista, Cadeira de Rodas, Gestante, Mobilidade Reduzida, Oncológico e Visual). Esse KPI auxilia na análise de acessibilidade e no planejamento para atender às necessidades desses grupos.

- **Total de Entradas de Passageiros por Dia:** Mede o número total de passageiros que validaram sua entrada diariamente, proporcionando uma visão clara do volume de utilização do serviço, fundamental para ajustes operacionais e de recursos.

- **Tempo Médio de Saída Entre Trens:** Avalia a média de tempo necessário para os trens entrarem em circulação, permitindo monitorar a eficiência operacional e identificar oportunidades de otimização no fluxo de trens.

---

### 4.1.6 Análise de Dados: 
<p align="justify">&ensp;&ensp;Foi realizada uma análise de dados utilizando o Jupyter Notebook para explorar os dados de diversas tabelas como fluxo de passageiros, falhas operacionais e ocorrências. A seguir um pouco das análises feitas e seus insights.</p>

<p align="justify">&ensp;&ensp; <b>Tabela Viagens:</b> Na exploração de dados do arquivo VIAGENS.csv, foram realizadas diversas análises para compreender o comportamento dos registros. Inicialmente, os dados foram carregados e preparados, com tratamento de valores nulos e remoção de duplicatas para garantir a integridade. Em seguida, foram aplicadas estatísticas descritivas e identificados outliers em variáveis-chave, revelando pontos com valores extremos que podem representar anomalias ou registros únicos. A análise de correlação entre variáveis mostrou que fatores como origem e destino apresentam interdependências, enquanto variáveis relacionadas à duração das viagens apresentaram baixa correlação com as demais, sugerindo que o fluxo de pessoas pode depender de fatores externos não capturados nos dados. A técnica PCA foi aplicada para reduzir a dimensionalidade e visualizar os dados em dois componentes principais, retendo aproximadamente 43,5% da variância. Isso permitiu simplificar a estrutura para a análise de clusters com o K-Means. Com o uso do método do cotovelo, foram identificados três clusters adequados, destacando grupos de registros com características semelhantes e alguns pontos dispersos, indicando a presença de outliers. Em síntese, essa análise identificou padrões de agrupamento e interdependências entre variáveis, sugerindo potenciais áreas de otimização no planejamento das viagens e no gerenciamento do fluxo de pessoas.</p>

<p align="justify">&ensp;&ensp;<b>Tabela dmo_anl_vw_tot_mov_periodo:</b> Na análise da tabela dmo_anl_vw_tot_mov_periodo, foi explorada a possibilidade de identificar padrões utilizando as técnicas de redução de dimensionalidade por PCA e clusterização com KMeans. No entanto, os dados não apresentaram o distanciamento necessário entre si para a formação de clusters consistentes, indicando uma estrutura de dados sem separação clara entre grupos. Esse fator limita a possibilidade de segmentação ou identificação de padrões de movimentação com essas técnicas. A falta de um dicionário de dados limitou a compreensão precisa de alguns campos, mas há indicativos de que os dados estão relacionados ao sistema de bilhetagem e monitoramento de validações de bilhetes nas estações da CPTM. A tabela apresenta potencial de uso para estudos sobre o fluxo de passageiros, permitindo observar o volume de validações em diferentes estações e como o fluxo varia entre dias úteis e fins de semana, fornecendo dados para ajustes estratégicos no planejamento e operação dos serviços da CPTM.</p>

<p align="justify">&ensp;&ensp;<b>Tabelas da pasta Embarcados por Hora:</b> A análise das tabelas geradas a partir dos arquivos da pasta Embarcados por Hora resultou em três tabelas principais: intervalos_combined, embarque_combined e periodo_combined. Essas tabelas contêm informações organizadas em intervalos de 15 minutos, incluindo volume de embarque, tipo de embarque e classificação do tipo de dia (por exemplo, dia útil ou fim de semana). Cada uma dessas tabelas pode ser cruzada entre si por meio de códigos de bilhete, código da estação e referência ao mês, possibilitando a geração de insights generalizados sobre o volume de passageiros e os meios de embarque mais utilizados. No entanto, os insights extraídos são limitados pela natureza do conjunto de dados, que se refere a uma única estação e a um dia fixo em cada mês, restringindo a abrangência temporal e espacial das conclusões.</p>

<p align="justify">&ensp;&ensp;<b>Tabela CPA_Tabelas:</b> Na análise inicial da planilha CPA_Tabelas, com foco em uma tabela qualitativa, foram observados dados que representam sete trechos de percurso da CPTM, especificando apenas as estações iniciais e finais, mas sem corresponder necessariamente às linhas completas. Cada CD_TRECHO é único, sugerindo que os dados abrangem um conjunto diverso de trechos ao longo da rede da CPTM, possivelmente selecionados como uma amostragem de locais distintos. A coluna ID_LINHA_FK mostra que a maioria das linhas está associada a um único trecho, com exceção das linhas 1 e 3, que têm dois trechos cada. Esse padrão pode indicar que essas linhas demandam mais atenção em diferentes partes do percurso, possivelmente devido a um fluxo de passageiros mais elevado ou à necessidade de monitoramento em múltiplos pontos. As colunas DT_ATUALIZA e DT_INICIO apresentam valores idênticos em todas as entradas, o que pode sinalizar que os dados se referem a um único período de análise ou que não houve atualização recente, limitando o monitoramento da variação do fluxo de pessoas ao longo do tempo. A coluna DT_FIM originalmente apresentava apenas valores nulos, substituídos pelo valor “0.0”, sugerindo que os trechos analisados estão em operação contínua ou que o fim do monitoramento ainda não foi registrado. No contexto de monitoramento de fluxo de pessoas, isso pode ser relevante para identificar se as viagens nesses trechos continuam ativas e ininterruptas, uma informação que auxilia na previsão de congestionamentos e no planejamento de estratégias para controle de fluxo.</p>

<p align="justify">&ensp;&ensp;<b>Tabela Contador de passageiros s2500:</b> A análise dos dados da operação da Linha 13 revela que o dataset abrange informações específicas de cada porta dos vagões, com cada linha repetida 8 vezes para representar as diferentes portas de cada vagão (definidas por Carriage_ID e Door_ID). O principal objetivo dos dados é monitorar o fluxo de entrada e saída de passageiros por porta (IN, OUT) em cada estação (Station_ID) e registrar o tempo que cada porta permaneceu aberta (Open_Time, Closed_Time). Também há a presença de uma linha adicional identificada como 99, que pode representar uma situação especial ou um tipo de operação distinta dentro do conjunto de dados.</p>

<p align="justify">&ensp;&ensp;Alguns insights derivados dessa análise incluem:<p>

- Relacionamento entre o tempo de fechamento das portas e possíveis incidentes: Portas abertas por períodos anormalmente longos, especialmente quando não há um grande fluxo de passageiros, podem indicar acidentes, ocorrências ou outras anomalias operacionais.

- Identificação de mal funcionamento das portas: Portas que apresentam tempo de fechamento irregular com frequência podem sugerir problemas técnicos que afetam a operação normal, indicando a necessidade de manutenção.

- Permanência de passageiros no trem até a estação final: Um número elevado de passageiros que entram sem sair nas estações intermediárias, especialmente na estação final, pode apontar para a permanência de pessoas durante desembarques obrigatórios, o que pode interferir nas operações e planejamento de fluxos de embarque/desembarque.

<p align="justify">&ensp;&ensp;Esses pontos de análise fornecem uma visão estratégica para otimizar a operação, prevenindo incidentes e melhorando a segurança e a confiabilidade do serviço.</p>

---
<p align="justify">&ensp;&ensp;A aplicação do Data Model Canvas no contexto da CPTM demonstra ser uma abordagem eficaz para organizar e alinhar informações essenciais no desenvolvimento de soluções baseadas em dados. A estrutura facilita a compreensão dos desafios operacionais e a definição de ações estratégicas, como monitoramento de fluxo de passageiros, detecção de falhas e análise preditiva para otimização dos serviços. As análises exploratórias e os insights obtidos das diferentes tabelas reforçam a importância de um sistema de Big Data bem estruturado, que não só permite a automação de processos críticos, como também oferece uma visão ampla e preditiva das operações, contribuindo para uma gestão mais eficiente e um serviço de maior qualidade aos usuários.</p>


## <a id="c4.2"></a>4.2 Relatório ETL

<p align="justify">&ensp;&ensp;O ETL (Extract, Transform, Load) é um processo essencial na gestão de dados, utilizado para extrair dados de diferentes fontes, transformá-los e carregá-los em um ambiente de armazenamento. Essas etapas tem como principal objetivo garantir a qualidade e integridade dos dados para seu uso na análise da CPTM. (FIVE ACTS)
</p>

<p align="justify">&ensp;&ensp;Para ter um ETL bem sucedido, é preciso ser composto por 3 etapas distintas, cada uma executando um papel fundamental na padronização da informação, seguindo o fluxo a seguir:
</p>

### <a id="c4.3"></a>4.2.1 Extrair (Extract)

<p align="justify">&ensp;&ensp;A etapa de extração (<i>extract</i>) é a primeira fase do processo ETL, onde os dados são coletados de diversas fontes para serem processados e analisados. No contexto da ingestão de dados da CPTM, a extração é realizada a partir de arquivos Parquet armazenados em um bucket do Amazon S3. Esta fase garante que todas as informações necessárias estejam disponíveis para as etapas subsequentes de transformação e carga.
</p>

<p align="justify">&ensp;&ensp;A função principal utilizada para a extração de dados é <i>get_parquet_files(bucket_name)</i>, que se conecta ao bucket S3 especificado e lista todos os arquivos Parquet disponíveis. Esse processo verifica o conteúdo do bucket e filtra apenas os arquivos com extensão .parquet, assegurando que somente os arquivos de interesse sejam considerados para o pipeline ETL.
</p>

<p align="justify">&ensp;&ensp;Além de listar os arquivos, a função <i>read_parquet_and_insert_to_clickhouse(bucket_name, file_key)</i> é responsável por acessar cada arquivo individualmente. Ela utiliza o S3 client para obter o arquivo Parquet, lê o conteúdo em um buffer de bytes, e prepara os dados para a próxima fase. A leitura dos arquivos no formato Parquet é realizada utilizando a biblioteca <i>PyArrow</i>, que permite manipular e extrair dados de forma eficiente.
</p>

<p align="justify">&ensp;&ensp;O objetivo dessa etapa é fornecer uma coleta de dados confiável e padronizada, independentemente da estrutura das fontes originais. Isso permite que os dados extraídos sejam centralizados em um ponto de processamento e estejam prontos para serem transformados e carregados de maneira consistente, mantendo a integridade das informações. Ao estabelecer um fluxo organizado para a extração, essa fase do ETL possibilita uma ingestão eficiente dos dados, preparando o sistema para as próximas etapas de tratamento e armazenamento em um ambiente de <i>Data Warehouse</i>.
</p>

### <a id="c4.4"></a>4.2.2 Transformar (Transform)

<p align="justify">&ensp;&ensp;Para ter um ETL bem-sucedido, é essencial que a etapa de <b>Transformação</b> execute de maneira eficiente a padronização, limpeza e preparação dos dados antes de serem carregados no destino final (Data Warehouse). Esta etapa, localizada entre a extração e a carga, é responsável por moldar os dados em um formato consistente e adequado para análise, seguindo as melhores práticas de qualidade de dados e otimização.</p>

<h3> Fluxo da Etapa de Transformação </h3>

<p align="justify">&ensp;&ensp; A etapa de <b>Transformar</b> pode ser dividida em várias subetapas fundamentais, conforme o fluxo a seguir:</p>

**Validação de Dados**:
- **Objetivo**: Garantir que os dados extraídos estejam corretos e no formato esperado antes de serem transformados.
- **Ações Realizadas**:
  - Aplicação de regras de negócios e validação de esquema (ex.: uso de modelos Pydantic para validar tipos de dados e formatos).
  - Verificação de conformidade de campos obrigatórios e formatos de data.

**Limpeza de Dados**:
- **Objetivo**: Corrigir ou remover dados que possam impactar a qualidade das análises.
- **Ações Realizadas**:
  - Remoção de registros duplicados, assegurando que apenas dados únicos sejam processados.
  - Tratamento de valores ausentes (ex.: preenchimento de valores `None` com padrões predefinidos).
  - Normalização de strings e padronização de formatos de texto.

**Conversão de Tipos de Dados**:
- **Objetivo**: Converter os tipos de dados para formatos compatíveis com o Data Warehouse.
- **Ações Realizadas**:
  - Conversão de strings para datas, inteiros, floats, etc., garantindo compatibilidade com o banco de destino.
  - Ajuste de tipos de dados conforme a necessidade dos modelos analíticos.

**Enriquecimento de Dados**:
- **Objetivo**: Adicionar informações complementares aos dados para aumentar seu valor analítico.
- **Ações Realizadas**:
  - Inclusão de metadados, como timestamps de ingestão e tags de origem.
  - Derivação de novos campos com base em cálculos simples ou agregações.

**Normalização e Agregação**:
- **Objetivo**: Ajustar os dados para uma estrutura uniforme e otimizada.
- **Ações Realizadas**:
  - Normalização dos dados para que estejam em uma faixa comum e coerente.
  - Agregação de registros para sumarizar grandes volumes de dados em métricas relevantes (ex.: contagens, médias).

**Registro de Métricas de Transformação**:
- **Objetivo**: Monitorar a execução da etapa de transformação e coletar dados para otimizações futuras.
- **Ações Realizadas**:
  - Registro de métricas como o número de registros processados, registros válidos e inválidos, e tempo de execução.
  - Armazenamento dessas métricas em uma tabela de monitoramento (ex.: banco de dados PostgreSQL).

<h3>Resultado Esperado</h3>

Após a conclusão da etapa de **Transformar**, os dados devem estar:
- **Consistentes**: Sem duplicatas e com campos validados e corrigidos.
- **Enriquecidos**: Com metadados e informações adicionais para facilitar análises futuras.
- **Prontos para a Carga (Load)**: Estruturados em um formato que otimize a inserção no Data Warehouse, garantindo consultas eficientes e respostas rápidas para as necessidades de negócios.

<p align="justify">&ensp;&ensp;A etapa de <b>Transformar</b> é um componente crítico do processo ETL, pois é nela que os dados brutos são convertidos em informações estruturadas e padronizadas, prontas para a análise. Um bom processo de transformação assegura que os dados sejam consistentes, completos e relevantes, proporcionando confiabilidade nas análises e nos insights gerados pelo Data Warehouse. Ao executar essa etapa com rigor e boas práticas, como a validação de dados, a remoção de duplicatas e o enriquecimento de informações, garantimos que as análises de negócios sejam precisas e que as decisões baseadas nos dados sejam fundamentadas em uma base sólida e bem preparada.</p>

### <a id="c4.5"></a>4.2.3 Carregar (Load)

<p align="justify">&ensp;&ensp;A etapa de carga (<i>load</i>) é a fase final do processo ETL, em que os dados transformados são transferidos para o sistema de destino. No projeto da CPTM, essa etapa foca na inserção dos dados no <b>ClickHouse</b>, um banco de dados orientado a colunas conhecido por sua eficiência no processamento de grandes volumes de dados analíticos.</p>

<h3>Objetivo da Carga</h3>

<p align="justify">&ensp;&ensp;O principal objetivo da etapa de carga é garantir que os dados estejam disponíveis no <i>Data Warehouse</i> de forma otimizada para consultas analíticas. Isso inclui garantir a integridade dos dados, minimizar o tempo de inserção e maximizar o desempenho das consultas subsequentes.</p>

<p align="justify">&ensp;&ensp;Para garantir que o processo de carga seja bem sucedido é necessário garantir que os seguinte spontos estejam de acordo:.</p>

- Certificar-se de que os dados estão prontos para serem inseridos
- Os dados transformados devem ser enviados para o banco de dados de forma eficiente.
- Garantir que a carga foi bem-sucedida e os dados estão consistentes.
  
 <p align="justify">&ensp;&ensp;Após a conclusão da etapa de <b>Carregar</b>, os dados devem estar completamente disponíveis no ClickHouse, prontos para serem utilizados em análises e relatórios. O am

### 4.2.4 Conclusão

<p align="justify">&ensp;&ensp;Concluindo, podemos afirmar que o processo de Extract, Transform, Load é importante para assegurar a qualidade e a integridade dos dados que serão utilizados nas análises da CPTM. A etapa de Extração permite coletar dados de diferentes fontes e centralizá-los de forma consistente. A fase de Transformação aplica uma série de operações para padronizar, limpar, enriquecer e validar os dados, garantindo que eles estejam prontos para análise e que atendam aos requisitos de qualidade. Finalmente, a etapa de Carga armazena esses dados transformados em um Data Warehouse, estruturado para proporcionar consultas rápidas e eficientes.
</p>

<p align="justify">&ensp;&ensp;Esse processo integrado é importante para que a CPTM tome decisões fundamentadas em dados precisos e confiáveis. Um ETL bem implementado assegura que as análises de negócios sejam baseadas em informações consistentes e relevantes, proporcionando uma base sólida para a geração de insights estratégicos. Dessa forma, o relatório destaca a importância de cada etapa do ETL na construção de um sistema de dados robusto e eficaz, que atende plenamente às necessidades analíticas da CPTM.
</p>

# <a id="c5"></a>5. Análise de Impacto Ético

<p align="justify">&ensp;&ensp;O uso crescente de Big Data traz inúmeras possibilidades de transformação social e ambiental, possibilitando tomadas de decisão mais informadas e a otimização de recursos em diversos setores. No entanto, essa prática também envolve implicações éticas significativas, especialmente quanto ao uso responsável de dados pessoais e à mitigação de impactos negativos, como o consumo excessivo de energia e possíveis violações de privacidade. De acordo com Zwitter, o impacto ético de Big Data envolve questões de privacidade, transparência e justiça, onde o equilíbrio entre inovação e responsabilidade deve ser cuidadosamente ponderado para promover benefícios sociais enquanto protege os direitos individuais. (ZWITTER, 2014). Logo, é essencial pensar nesses aspectos para que o projeto de Big Data da CPTM contribua para uma gestão eficiente e responsável, alinhando-se aos valores éticos e ao impacto positivo na sociedade.
</p>

## <a id="c5.1"></a>5.1 Privacidade e proteção de dados

<p align="justify">&ensp;&ensp;No contexto do projeto, a dimensão de Privacidade e Proteção de Dados é abordada com foco na preservação da confidencialidade e integridade das informações processadas, assegurando que todas as práticas respeitam as normas de privacidade. Neste projeto, os dados trabalhados não envolvem informações pessoais ou sensíveis. A análise acontece apenas em informações agregadas sobre a movimentação e o transporte de passageiros, como volume de pessoas, tipo de acesso à estação, estações frequentadas, datas e horários. Esses dados são coletados com o objetivo de oferecer insights sobre o fluxo nas linhas de trens, visando a otimização das operações da CPTM e melhorias na experiência dos usuários.
</p>

<p align="justify">&ensp;&ensp;A justificativa para a não utilização de dados pessoais está no fato de que o objetivo do projeto é exclusivamente focado em métricas operacionais, sem a necessidade de identificar ou mapear indivíduos específicos. O interesse está voltado para KPIs que permitam melhorias nas operações da CPTM, como o ajuste na frequência de trens e a alocação eficiente de recursos com base no volume de passageiros por faixa horária e estação. Por isso, foi adotada uma abordagem que utiliza exclusivamente dados agregados e não-pessoais, eliminando riscos associados à exposição de informações privadas e garantindo que o projeto esteja em conformidade com regulamentações de privacidade.
</p>

<p align="justify">&ensp;&ensp;Além disso, o processo de ETL utilizado para a coleta e manipulação dos dados segue boas práticas de gestão de dados, incluindo validações rigorosas e limpeza de dados para garantir a qualidade e a integridade das informações antes de carregá-las em um ambiente seguro de armazenamento, como o Data Warehouse da CPTM. Essas medidas reforçam a adequação do projeto às exigências de proteção de dados, garantindo que o sistema seja seguro e que os dados processados sejam confiáveis e apropriados para o escopo analítico.
</p>

## <a id="c5.2"></a>5.2 Equidade e justiça

<p align="justify">&ensp;&ensp;O contexto de equidade e justiça no projeto visa garantir que o uso de informações sobre as operações relacionadas ao transporte nas linhas da CPTM seja realizado de maneira transparente e justa, sem impactos negativos desequilibrados em nenhum grupo específico. Tendo em vista que os dados trabalhados representam apenas o volume de passageiros e padrões de movimentação sem qualquer associação a dados pessoais ou individuais, o risco de impacto direto sobre indivíduos ou grupos específicos é reduzido.
</p>

<p align="justify">&ensp;&ensp;Entretanto, é importante garantir que as análises realizadas com esses dados e as ações derivadas dessas análises considerem a diversidade dos grupos atendidos pela CPTM. Por exemplo, ao implementar ajustes nas operações com base nos insights obtidos, é importante garantir que tais mudanças não geram divergências de acesso ao serviço ou que grupos específicos não sejam impactados de forma negativa por alterações na frequência de trens ou em outros aspectos de operações.
</p>

<p align="justify">&ensp;&ensp;Para promover e garantir a equidade e justiça, as estratégias de mitigação de possíveis impactos negativos incluem:
</p>

- **Monitoramento contínuo:** Monitorar como as mudanças nas operações, baseadas nos dados analisados, afetam diferentes horários, linhas e estações, garantindo que áreas com alta dependência do transporte público sejam beneficiadas de forma iguais;

- **Inclusão na tomada de decisão:** Ter o envolvimento de representantes das comunidades atendidas na análise dos dados e na implementação de mudanças, para assegurar que o impacto seja positivo e equitativo .

- **Atenção a horários de pico e regiões específicas:** Durante a análise dos insights obtidos e as recomendações operacionais, a equipe deve observar o comportamento de movimentação em horários de pico e em regiões com alta dependência do transporte público, se atentando a evitar alterações que poderiam comprometer o acesso equitativo ao serviço.

<p align="justify">&ensp;&ensp;Priorizando essas práticas, a solução desenvolvida se compromete a fazer uso de dados para otimizar operações sem comprometer a justiça e a equidade no serviço oferecido pela CPTM. Dessa forma, essa abordagem permite minimizar a chance de diferenças, assegurando que todas as ações tomadas sejam baseadas em uma análise que considere o bem-estar e a igualdade de acesso para todos os passageiros.
</p>

## <a id="c5.3"></a>5.3 Transparência e consentimento informado

<p align="justify">&ensp;&ensp;A transparência e o consentimento informado são princípios fundamentais na gestão ética de dados, especialmente em projetos de Big Data. Transparência refere-se à prática de fornecer clareza sobre como os dados são coletados, processados e utilizados, garantindo que todas as partes interessadas compreendam os processos e propósitos envolvidos (Lei nº 13.709/2018). Já o consentimento informado, segundo a definição da LGPD (Lei nº 13.709/2018), implica que os indivíduos ou grupos afetados pelo uso dos dados tenham dado autorização clara e explícita para tal uso, após serem devidamente informados sobre suas finalidades e implicações. Esses princípios são cruciais para estabelecer a confiança e a responsabilização no uso de dados, conforme enfatizado em estudos sobre governança de dados éticos (MENDES, 2018).
</p>

<p align="justify">&ensp;&ensp;No projeto de Big Data para a CPTM, a transparência é garantida por meio de apresentações realizadas ao final de cada sprint, onde os gestores e operadores da CPTM têm acesso detalhado ao andamento do projeto, incluindo explicações sobre a coleta e análise dos dados agregados. Para os usuários da CPTM (os passageiros), é essencial acessar o link da Política de Privacidade da CPTM (CPTM), onde é possível acessar informações sobre como os dados são coletados e protegidos. Adicionalmente, uma comunicação clara de que dados de navegação dos passageiros podem ser utilizados exclusivamente para os fins deste projeto, garantindo que tais dados sejam anonimizados conforme necessário e respeitem a Lei Geral de Proteção de Dados (LGPD). A inclusão desses métodos reforça a confiança mútua e assegura que todas as partes envolvidas, desde os gestores até os passageiros, compreendam e aceitem as práticas adotadas, alinhando o projeto com os princípios de governança ética e proteção de dados. 
</p>

<p align="justify">&ensp;&ensp;O projeto de Big Data da CPTM adota diretrizes éticas e legais para garantir o consentimento informado, mesmo no uso de dados agregados e anônimos. Além da anonimização para preservar a privacidade dos usuários, medidas concretas são implementadas para assegurar que todas as partes compreendam como os dados são tratados. Os gestores e operadores têm acesso a relatórios detalhados em apresentações ao final de cada sprint, enquanto os passageiros podem consultar a Política de Proteção de Dados da CPTM (CPTM), que esclarece as práticas de coleta e proteção de dados. Para reforçar essa transparência, o projeto informa de forma clara que dados de navegação podem ser analisados exclusivamente para os fins definidos, sempre alinhados à LGPD, promovendo uma gestão de dados ética e responsável.
</p>

<p align="justify">&ensp;&ensp;
Assim, a transparência e o consentimento informado estabelecem as bases éticas e legais para o projeto de Big Data da CPTM, promovendo práticas responsáveis na gestão de dados. Ao garantir que todas as partes envolvidas tenham acesso claro às informações relevantes e ao implementar métodos robustos de comunicação e anonimização, o projeto não apenas cumpre as exigências legais, mas também fortalece a confiança entre a CPTM, seus gestores e os usuários dos serviços.
</p>

## <a id="c5.4"></a>5.4 Responsabilidade social

<p align="justify">&ensp;&ensp;Responsabilidade social significa que empresas e organizações se comprometem a apoiar o desenvolvimento sustentável e o bem-estar das comunidades e do meio ambiente onde atuam. Esse conceito vai além de cumprir apenas o que a lei exige, envolve ações voluntárias que trazem impactos positivos para a sociedade. Empresas que praticam a responsabilidade social buscam equilibrar seus objetivos financeiros com os impactos sociais e ambientais de suas atividades, agindo com ética e transparência (Carroll, A. B., 1991). 
<p align="justify">&ensp;&ensp;No caso da Companhia Paulista de Trens Metropolitanos (CPTM), o projeto de Big Data mostra um comprometimento claro com a responsabilidade social. A seguir, destacam-se os principais pontos de impacto social e ambiental do projeto, com base em conceitos de responsabilidade corporativa e uso de Big Data.

1. **Impacto Social Positivo:** A utilização de Big Data no dia a dia da CPTM traz ganhos reais para o transporte público, melhorando a operação de trens e beneficiando os passageiros. Com as análises de dados em tempo real sobre o fluxo de pessoas, é possível ajustar a capacidade dos trens nos horários de pico, redirecionar trens para as linhas mais movimentadas e prever aumentos de demanda em períodos específicos, como em eventos ou feriados. Por exemplo, ao observar os dados de uso das estações e os horários de maior movimento, a CPTM pode decidir aumentar a frequência dos trens nesses momentos mais críticos, ajudando a evitar superlotação e oferecendo uma viagem mais confortável para os passageiros. Esse tipo de ajuste melhora diretamente a vida dos usuários, especialmente em áreas com grande circulação, onde o transporte público é essencial para a mobilidade diária.

2. **Impacto Ambiental Positivo:** O projeto de Big Data também pode ajudar a reduzir o consumo de combustível e a otimizar as rotas com base no fluxo de pessoas, o que contribui para a diminuição das emissões de gases de efeito estufa. Ao identificar padrões de demanda, a CPTM pode ajustar as operações para maximizar a eficiência energética, por exemplo, reduzindo a quantidade de trens circulando em horários de baixa demanda e concentrando a operação em horários de pico. Além disso, a análise do fluxo de pessoas pode orientar investimentos em infraestrutura para evitar desperdícios, como a instalação de portas automáticas nas estações para reduzir a necessidade de ventilação e iluminação constantes, promovendo um uso mais eficiente dos recursos naturais.

3. **Mitigação de Impactos Negativos:** O uso de dados sobre o fluxo de pessoas envolve considerações importantes sobre a privacidade dos usuários. Garantir a proteção das informações pessoais dos passageiros é fundamental para evitar a exposição indevida e o mau uso dos dados. Para isso, a conformidade com legislações como a Lei Geral de Proteção de Dados (Lei nº 13.709, de 14 de agosto de 2018) é essencial, assegurando que as informações coletadas, como padrões de movimentação nas estações, sejam tratadas de forma segura e ética. A LGPD estabelece diretrizes específicas para a coleta, armazenamento, processamento e compartilhamento de dados pessoais, exigindo que as empresas implementem medidas de segurança e privacidade para proteger os direitos dos indivíduos. Por exemplo, a análise do fluxo de pessoas pode ser realizada de forma anônima, agregando dados para identificar tendências sem comprometer a privacidade individual dos usuários, o que demonstra o compromisso da CPTM com a segurança das informações e a confiança no sistema.

4. **Promoção da Inclusão e Acessibilidade:** O projeto pode ainda identificar áreas onde melhorias de acessibilidade são necessárias, promovendo um sistema de transporte mais inclusivo e equitativo. Com o monitoramento do fluxo de pessoas, é possível identificar horários e locais em que pessoas com deficiência ou mobilidade reduzida enfrentam dificuldades para acessar o transporte. Um exemplo prático seria a análise de dados sobre o uso de elevadores e rampas, permitindo à CPTM ajustar a disponibilidade desses recursos ou implementar melhorias nas infraestruturas para tornar as estações mais acessíveis. Essa abordagem facilita a inclusão social, promovendo a acessibilidade e alinhando-se ao Objetivo de Desenvolvimento Sustentável (ODS) 10, que visa reduzir as desigualdades entre e dentro dos países, promovendo a inclusão de todos, independentemente de idade, gênero, deficiência, raça, etnia, origem, religião, condição econômica ou outra condição (United Nations, 2015).

5. **Sustentabilidade e Responsabilidade Corporativa:** Projetos que integram Big Data com estratégias de responsabilidade corporativa reforçam o compromisso das empresas com o desenvolvimento sustentável e o bem-estar social. A análise do fluxo de pessoas permite à CPTM monitorar e responder às necessidades da população em tempo real, planejando expansões e melhorias nas linhas com base em dados de uso e demanda. Um exemplo prático seria o uso desses dados para justificar o investimento em novas linhas de transporte em áreas onde o fluxo de passageiros é alto e os recursos são limitados, ajudando a desenvolver uma infraestrutura de transporte mais sustentável e eficiente, em alinhamento com o ODS 11, que promove cidades e comunidades sustentáveis. A responsabilidade corporativa da CPTM, ao adotar essas práticas, demonstra uma visão de longo prazo que contribui para a criação de um ambiente urbano mais equilibrado (United Nations, 2015).

<p align="justify">&ensp;&ensp;O projeto de Big Data da CPTM destaca um compromisso com a responsabilidade social, buscando não só aprimorar a qualidade e eficiência do transporte público, mas também reduzir impactos ambientais e promover um sistema de transporte mais inclusivo e sustentável. Ao utilizar análises de dados para ajustar operações, otimizar recursos e garantir a proteção de informações dos usuários, a CPTM demonstra uma abordagem ética para atender às necessidades da população.

## <a id="c5.5"></a>5.5 Viés e discriminação

<p align="justify">&ensp;&ensp;O viés algorítmico em Big Data se refere a preconceitos ou distorções que surgem quando algoritmos de análise de dados refletem ou amplificam desigualdades e preconceitos existentes na sociedade. Esses vieses podem ocorrer em diversas etapas, desde a coleta dos dados até a construção e aplicação dos algorítimos. Dados tendenciosos podem resultar em discriminação, afetando negativamente grupos específicos e gerando exclusão involuntária em processos automatizados. Essa questão é particularmente preocupante em setores sensíveis, como transporte, saúde e segurança, onde decisões baseadas em dados podem impactar profundamente a vida de indivíduos e comunidades (O'Neil, 2016).

<p align="justify">&ensp;&ensp;No contexto de transporte público, por exemplo, dados históricos podem refletir padrões de deslocamento que priorizam áreas centrais, enquanto regiões periféricas ou comunidades marginalizadas são sub-representadas. Algoritmos que aprendem a partir desses dados podem perpetuar essas desigualdades, alocando menos recursos ou menos acessibilidade para esses grupos. Esse fenômeno de discriminação algorítmica ocorre quando um sistema automatizado desfavorece ou exclui certos grupos involuntariamente, amplificando preconceitos existentes, como ocorre em casos de reconhecimento facial, onde algoritmos frequentemente apresentam maior taxa de erro para pessoas não brancas (Noble, S. U.,2018).

<p align="justify">&ensp;&ensp;A mitigação desses vieses exige práticas rigorosas de auditoria e revisão dos dados e algoritmos, garantindo a diversidade nos conjuntos de dados e promovendo a transparência nos critérios de decisão. A revisão contínua e o ajuste dos códigos de tratamento de dados ajudam a assegurar que esses sistemas sejam inclusivos e justos para todos os usuários, contribuindo para uma aplicação mais ética e socialmente responsável do Big Data (Barocas, S., Hardt, M., & Narayanan, A., 2019).

<p align="justify">&ensp;&ensp;Para garantir que o pipeline de Big Data desenvolvido esteja livre de vieses e discriminação, foram implementadas duas práticas principais para identificar, monitorar e corrigir possíveis distorções nos dados. Essas abordagens asseguram que o sistema seja justo e inclusivo para todos.

1. **Análise Anônima e Agregada dos Dados:** Para proteger a privacidade e evitar discriminação indireta, as análises do fluxo de pessoas são feitas de forma anônima e em conjunto. Isso ajuda a identificar padrões gerais de uso e movimentação sem expor informações individuais, em conformidade com a Lei Geral de Proteção de Dados (LGPD). Dessa forma, o foco da análise recai sobre tendências coletivas em vez de características específicas, minimizando o risco de que decisões ou otimizações baseadas nos dados favoreçam involuntariamente alguns grupos em detrimento de outros.

2. **Equipe Diversificada na Revisão dos Algoritmos:** A revisão e auditoria dos algoritmos são realizadas por uma equipe diversa, o que contribui para a prevenção de vieses. A diversidade permite trazer diferentes perspectivas, ajudando a identificar potenciais pontos de viés que poderiam passar despercebidos em uma equipe mais homogênea. Essa prática é fundamental para que o pipeline de Big Data evite discriminação ou favorecimento de grupos específicos, promovendo um sistema de transporte justo e acessível para todos.

<p align="justify">&ensp;&ensp;Essas práticas refletem um esforço proativo para que o pipeline de Big Data contribua positivamente, reduzindo desigualdades e promovendo um transporte acessível e justo para todos. A contínua revisão e a responsabilidade na aplicação desses princípios éticos asseguram que o sistema evolua de forma alinhada com os valores de inclusão, transparência e respeito à diversidade, essencial para o impacto social que se espera alcançar com esta tecnologia.

## <a id="c5.6"></a>5.6 Conclusão

<p align="justify">&ensp;&ensp;A análise dos impactos éticos do uso de Big Data no projeto, demonstra um compromisso claro com práticas responsáveis e alinhadas aos princípios de privacidade, equidade, transparência, responsabilidade social e mitigação de vieses. As medidas adotadas para preservar a privacidade e a integridade dos dados, o foco em informações agregadas e anônimas, e a conformidade com a LGPD garantem que o projeto respeite os direitos dos usuários. Além disso, a atenção à equidade e à justiça busca assegurar que os insights gerados promovam benefícios equitativos para todas as comunidades atendidas, enquanto a transparência nas práticas e a comunicação com stakeholders fortalecem a confiança e a colaboração. Esses elementos destacam o potencial do projeto em criar soluções éticas e eficazes para otimizar o transporte público sem comprometer os valores fundamentais de inclusão e respeito aos direitos individuais.
</p>

<p align="justify">&ensp;&ensp;Ao integrar esses princípios éticos no desenvolvimento do pipeline de Big Data, o projeto não apenas atende às demandas operacionais da CPTM, mas também reforça seu papel como agente de transformação social e ambiental. A capacidade de gerar insights precisos e confiáveis, aliada ao cuidado em evitar discriminação e impactos negativos, posiciona o projeto como um modelo de aplicação tecnológica responsável. Assim, o pipeline de Big Data torna-se uma ferramenta estratégica para melhorar a gestão do transporte público, promovendo eficiência, sustentabilidade e acessibilidade, ao mesmo tempo em que demonstra um exemplo prático de como a tecnologia pode ser utilizada para criar valor compartilhado e impacto positivo na sociedade.
</p>

# <a id="c6"></a>6 Documentação da Primeira Versão do Datapp
## <a id="c6.1"></a>6.1 Lógica de Criação do Infográfico
A lógica de criação do infográfico seguiu uma abordagem estruturada, baseada no **wireframe definido previamente** para orientar o design e a funcionalidade. Essa etapa inicial garantiu que os gráficos e elementos visuais estivessem alinhados com os requisitos e expectativas do projeto.

### Estrutura e Abordagem:

1. **Planejamento com Wireframe**:
   - O wireframe serviu como guia para o posicionamento dos gráficos, filtros e componentes interativos.
   - Isso permitiu criar um layout intuitivo, otimizando a experiência do usuário ao navegar pelas diferentes views do Datapp.

2. **Componentização**: 
   - Cada gráfico foi encapsulado em uma classe específica dentro da pasta `graphs`, responsável pela lógica de geração de visualizações, como gráficos de barras, histogramas e gráficos de pizza.
   - O módulo `plot_dispatcher` atua como um orquestrador, mapeando os tipos de gráficos às suas funções correspondentes, de acordo com a view solicitada.

3. **Modularidade**:
   - A configuração da página e da barra lateral foi centralizada em componentes reutilizáveis localizados na pasta `components`. Isso garantiu consistência visual e reduziu redundâncias no código.
   - As constantes, como URLs de base e views disponíveis, foram movidas para arquivos dedicados, facilitando atualizações centralizadas.

4. **Reusabilidade**:
   - A lógica de conexão com o banco de dados ClickHouse foi isolada em uma classe (`ClickhouseConnector`), promovendo a reutilização e abstração do acesso a dados.
   - Gráficos foram desenvolvidos de forma modular, permitindo que novos tipos de visualização possam ser facilmente adicionados no futuro.

A construção do infográfico com base no wireframe proporcionou uma estrutura clara e organizada, garantindo que os elementos visuais e interativos fossem desenvolvidos de maneira alinhada às necessidades do usuário. A utilização de uma arquitetura modular e orientada a objetos tornou o Datapp uma aplicação escalável, eficiente e fácil de manter. Além disso, a separação de responsabilidades e a reutilização de componentes e gráficos destacam o potencial do Datapp em crescer e incorporar novos recursos, assegurando sua relevância em cenários futuros.


## <a id="c6.2"></a>6.2 Implementação de Filtros
## 6.2 Implementação de Filtros

Os filtros implementados foram projetados para oferecer uma experiência de usuário mais intuitiva e personalizável. Eles permitem que os usuários explorem os dados de maneira detalhada e direcionada:

### Filtros de Linhas:
- Aplicado em todas as views.
- Os dados são automaticamente filtrados para refletir apenas as informações correspondentes à linha selecionada (e.g., LINHA 7 - RUBI, LINHA 10 - TURQUESA).
- Essa funcionalidade é essencial para análises específicas de cada linha, mantendo a clareza e relevância das visualizações.

### Filtros de Estações:
- **View "Movimentação por Período"**:
  - Utiliza o componente `st.selectbox` do Streamlit para que o usuário selecione uma estação específica.
  - Os dados apresentados no gráfico de validações são automaticamente filtrados para refletir apenas a estação selecionada.

### Filtros de Data:
- **View "Total de Validações por Dia"**:
  - Adicionamos campos interativos para selecionar a data inicial e final (`st.date_input`).
  - A seleção das datas delimita os intervalos exibidos no gráfico, permitindo análises temporais mais precisas.

### Integração:
- Esses filtros foram integrados diretamente com os gráficos por meio de funções interativas, garantindo que os dados carregados sejam consistentes com as escolhas dos usuários.
- A implementação modular dos filtros permite futuras extensões e ajustes com mínima intervenção no código-base.

A integração desses filtros com os gráficos de visualização não apenas simplifica a navegação, mas também reforça a modularidade e a escalabilidade do código. Essa abordagem cria uma base para futuras expansões, tornando o Datapp uma ferramenta robusta, adaptável e centrada no usuário. A capacidade de entregar informações relevantes, alinhadas com as preferências e escolhas dos usuários, posiciona o Datapp como um recurso essencial para análises e tomadas de decisão baseadas em dados.

## <a id="c6.3"></a>6.3 Processo de Coleta Automática de Dados

A coleta de dados foi completamente automatizada e integrada à API desenvolvida em Flask. Isso elimina processos manuais e garante que o Datapp sempre apresente informações atualizadas.

### Detalhes Técnicos:

#### Endpoints da API:
- Cada endpoint foi projetado para atender a uma view específica do Datapp, como:
  - `/acompanhamentopcd` para dados de PCD.
  - `/intervalos` para dados de intervalos.
  - `/movimentacaoporperiodo` para movimentação.
  - `/totaldevalidacoesporDia` para validações por dia.
- Os endpoints utilizam a classe `ClickhouseConnector` para executar queries no banco de dados e retornam os resultados no formato JSON.

#### Conexão com o ClickHouse:
- A conexão com o banco de dados foi implementada utilizando o `clickhouse_driver`, que permite:
  - Abrir e fechar conexões automaticamente.
  - Executar queries SQL de maneira eficiente e segura.
  - Formatar os resultados como dicionários para integração direta com o frontend.

#### Integração com o Frontend:
- O frontend utiliza a biblioteca `requests` para fazer chamadas HTTP aos endpoints da API.
- Os dados recebidos são carregados dinamicamente em visualizações do Streamlit, garantindo atualizações em tempo real.

A automação da coleta de dados e a integração entre o ClickHouse, a API em Flask e o frontend no Streamlit consolidaram um ecossistema eficiente e confiável para o Datapp. Essa estrutura não apenas melhora a experiência do usuário, fornecendo informações precisas e em tempo real, mas também facilita a escalabilidade e a manutenção do sistema. Ao centralizar a lógica de extração e apresentação de dados, o Datapp se posiciona como uma ferramenta estratégica para análise e visualização, possibilitando decisões informadas com base em dados confiáveis e continuamente atualizados.

# <a id="c7"></a>7 Cubo de Dados Automatizado

  <p align="justify">
  &ensp;&ensp;Um Cubo de Dados Automatizado é uma estrutura multidimensional que organiza e armazena grandes volumes de dados de forma eficiente, permitindo análises rápidas e detalhadas. Diferentemente dos cubos de dados tradicionais, que exigem processos manuais para sua construção e atualização, o cubo automatizado utiliza ferramentas e algoritmos para automatizar essas tarefas, garantindo maior agilidade e precisão na manipulação dos dados.
  </p>
  <p align="justify">
  &ensp;&ensp;O principal objetivo de um cubo de dados é fornecer uma visão consolidada e interativa das informações, facilitando a tomada de decisões estratégicas. Ao organizar os dados em dimensões e medidas, o cubo permite que os usuários explorem diferentes perspectivas e identifiquem padrões e tendências relevantes. A automação desse processo assegura que os dados estejam sempre atualizados e prontos para análise, sem a necessidade de intervenções manuais frequentes.
  </p>
  <p align="justify">
  &ensp;&ensp;No contexto do projeto, a implementação de um cubo de dados automatizado visa otimizar a análise de informações provenientes de diversas fontes. Ao integrar e automatizar a estruturação dos dados, buscamos oferecer aos usuários uma ferramenta poderosa para explorar e interpretar as informações de maneira eficiente, apoiando decisões mais informadas e estratégicas.
  </p>

## 7.1 Escolha das Dimensões

As dimensões são atributos ou categorias que oferecem contexto para os dados analisados, permitindo segmentar e filtrar informações para uma análise mais detalhada e eficiente. Em um sistema de análise de dados, as dimensões ajudam a organizar os dados de forma estruturada, tornando possível explorar diferentes perspectivas, como linha, estação e horários. As dimensões são elementos essenciais em sistemas analíticos para criar estruturas multidimensionais que conectam métricas operacionais a decisões estratégicas (Kimball & Ross, 2002). 

No contexto deste projeto, as dimensões são fundamentais para categorizar e detalhar os dados coletados, suportando os KPIs definidos para o pipeline de fluxo de pessoas.

---

### 7.1.1 **Como foi feita a escolha das Dimensões**

As dimensões foram escolhidas com base em critérios operacionais, estratégicos e práticos. Focamos em elementos que:
1. **Relevância Operacional**: Impactam diretamente a operação da CPTM, como linhas e estações.
2. **Segmentação Necessária para KPIs**: Suportam os KPIs definidos, como fluxo de passageiros e acessibilidade.
3. **Acessibilidade dos Dados**: Dados disponíveis nas tabelas fornecidas pela CPTM.
4. **Impacto Estratégico**: Dimensões que ajudam a identificar gargalos e oportunidades de melhoria.

### 7.1.2 **Dimensões Escolhidas**

1. **Linha**:
   - **Descrição**: Identifica a linha específica da CPTM.
   - **Justificativa**: Linhas têm características e demandas distintas, sendo essencial entender e comparar sua performance.

2. **Grupo PCD (Pessoas com Deficiência)**:
   - **Descrição**: Categorização de grupos prioritários, como 60+, Autistas, Cadeirantes, Gestantes, Mobilidade Reduzida, Oncológicos e Deficiência Visual.
   - **Justificativa**: Permite avaliar o atendimento às necessidades de acessibilidade, identificando lacunas e áreas prioritárias.

3. **Estação**:
   - **Descrição**: Identifica estações específicas.
   - **Justificativa**: Facilita a análise localizada, destacando estações com maior demanda ou desafios específicos.

4. **Dia da Semana**:
   - **Descrição**: Segmenta os dados entre dias úteis e finais de semana.
   - **Justificativa**: Comportamentos de fluxo variam entre dias úteis e finais de semana, sendo importante para planejamento.

5. **Horário**:
   - **Descrição**: Identifica intervalos de tempo durante o dia.
   - **Justificativa**: Importante para identificar picos de movimentação e horários críticos.

### 7.1.3 **Por que essas dimensões fazem sentido para o projeto?**

Essas dimensões foram escolhidas porque refletem os aspectos operacionais mais relevantes para a CPTM e suportam os KPIs definidos para o pipeline de fluxo de pessoas. Elas possibilitam:

- **Identificar padrões e gargalos operacionais específicos.**
- **Melhorar a acessibilidade e o atendimento ao público prioritário (PCD).**
- **Planejar estratégias de alocação de trens e recursos humanos de forma mais eficiente.**
- **Acompanhar o desempenho e a satisfação dos passageiros em diferentes contextos** (linhas, estações, horários).

---

### 7.1.4 **KPIs Relacionados às Dimensões**

#### **Quantidade de PCD por Linha e Grupo PCD**
- **Dimensões Utilizadas:** Linha, Grupo PCD.
- **Finalidade:** Monitorar o atendimento às pessoas com deficiência, identificar onde estão concentradas e planejar melhorias específicas.

#### **Total de Entradas de Passageiros por Dia**
- **Dimensões Utilizadas:** Linha, Estação, Dia da Semana.
- **Finalidade:** Avaliar o fluxo geral de passageiros por dia, segmentado por estação e linha, para detectar padrões e demandas específicas.

#### **Tempo Médio de Saída Entre Trens**
- **Dimensões Utilizadas:** Linha, Horário, Dia da Semana.
- **Finalidade:** Medir a eficiência operacional e planejar ajustes na frequência de trens em horários críticos.

---

As dimensões escolhidas são essenciais para categorizar os dados e garantir que o pipeline de fluxo de pessoas da CPTM seja eficiente e alinhado às necessidades operacionais e estratégicas. Essas dimensões permitem uma análise detalhada de questões como ocupação dos trens, atendimento ao público PCD e desempenho operacional por linha e estação. Ao conectar métricas operacionais a categorias contextuais, criamos uma base sólida para melhorar a eficiência, a acessibilidade e a experiência dos passageiros, alinhando o sistema às metas do projeto. 


## 7.2 Estrutura das Planilhas
<p align="justify">&emsp;&emsp;As planilhas desenvolvidas no projeto são views criadas em SQL, atuando como tabelas virtuais que permitem acessar e manipular dados de forma eficiente. Diferentemente das tabelas físicas, as views não armazenam dados por si mesmas, elas representam o resultado de uma consulta armazenada que pode envolver uma ou mais tabelas do banco de dados. (DEVMEDIA)</p>

### 7.2.1 Objetivo das Planilhas no Projeto
<p align="justify">&emsp;&emsp;O objetivo principal das planilhas é monitorar as KPI’s do projeto, estruturando os dados de maneira clara e eficiente para facilitar sua análise e visualização. Elas foram criadas para organizar e consolidar informações críticas, como o comportamento dos passageiros PCD, o total de entradas por dia e o tempo médio de saída entre trens. Essas métricas são essenciais para subsidiar a tomada de decisões, garantindo insights relevantes para o planejamento e otimização das operações da CPTM.</p>

<p align="justify">&emsp;&emsp;Optou-se pela utilização do Metabase como ferramenta de visualização devido à sua flexibilidade, facilidade de integração com bancos de dados SQL e capacidade de gerar dashboards interativos e acessíveis. Essa escolha permite que os stakeholders tenham acesso rápido e direto às métricas calculadas. Além disso, na entrega final do projeto, as KPI’s serão disponibilizadas em um dataApp desenvolvido pelo grupo, que oferecerá uma interface dedicada e funcional para consulta de dados de forma prática e personalizada.</p>

<br>
<div align="center">
  <figcaption style="text-align: center; font-size: 10px; margin-bottom: 5px;">Figura 20 - Metabase com views </figcaption>
  <img src="https://res.cloudinary.com/dbzxxlr35/image/upload/v1732373022/Views_hekcjp.jpg" alt=“Views” style="width: 100%; display: block; margin: 0 auto;">
  <figcaption style="text-align: center; font-size: 10px; margin-top: 5px;">Fonte: Elaboração Própria</figcaption>
</div>
<br>

As KPI’s do projeto são diretamente representadas nos gráficos da imagem acima, garantindo uma visualização clara e integrada dos indicadores:
1. Quantidade de PCD por Linha e Grupo PCD: Representada no gráfico de barras inferior, onde é possível observar a distribuição de passageiros PCD (Pessoas com Deficiência) por linha da CPTM e grupos específicos, como Autista, Cadeira de Rodas, Mobilidade Reduzida, entre outros. Essa visualização permite analisar quais grupos e linhas possuem maior demanda.
2. Total de Entradas de Passageiros por Dia: Refletido no gráfico de linhas central, que demonstra as validações diárias de passageiros ao longo do mês. Ele destaca tendências e padrões no volume de passageiros, auxiliando no planejamento operacional.
3. Tempo Médio de Saída Entre Trens: Representado pelo indicador numérico no canto superior esquerdo, onde é exibida a média de tempo que os trens levam para entrar em circulação. Esse dado é essencial para monitorar e otimizar a eficiência operacional.

### 7.2.2 Criação das Planilhas
<p align="justify">&emsp;&emsp;As planilhas foram desenvolvidas utilizando SQL, com o uso estratégico de Common Table Expressions (CTEs). As CTEs são estruturas temporárias que tornam as queries mais organizadas e eficientes, permitindo a criação de processos de extração e análise escaláveis.</p>

<p align="justify">&emsp;&emsp;A base do projeto foi construída no sistema ClickHouse, um banco de dados de alta performance projetado para a análise de grandes volumes de dados em tempo real. O ClickHouse é conhecido por sua capacidade de processar bilhões de registros rapidamente, o que é essencial para projetos de Big Data que exigem respostas rápidas e consultas otimizadas. (DATACOSMOS)</p>


## 7.3 Automatização com Prefect
<p align="justify">&emsp;&emsp;Segundo sua documentação (Prefect.io, 2024), o Prefect é uma plataforma de orquestração e observabilidade que capacita desenvolvedores a criar e escalar fluxos de trabalho rapidamente. Isso permite que seja possível observar diversos fluxos simultâneos, suas etapas e seus tempos de execução. Logo, é essencial a implementação dessa ferramenta no projeto a fim de possibilitar a identificação de processos demorados e erros que possam ocorrer.</p>

<p align="justify">&emsp;&emsp;No Prefect, as principais estruturas são as <i>tasks</i> e os <i>flows</i>. As <i>tasks</i> representam pequenos blocos de código reutilizáveis em diferentes partes da aplicação. Já o <i>flow</i> é uma sequência estruturada dessas <i>tasks</i>. No ETL bronze, a automatização foi dividida em três etapas principais:</p> 

<ul> 
<li><i><b>ingest_data</b> (flow)</i>: Orquestra o fluxo da aplicação para processar cada arquivo `.parquet` no S3, tratá-lo e enviá-lo ao ClickHouse;</li>
<li><i><b>get_parquet_files</b> (task)</i>: Obtém os arquivos `.parquet` armazenados no S3;</li>
<li><i><b>read_parquet_and_insert_to_clickhouse</b> (task)</i>: Processa cada arquivo `.parquet` e realiza sua inserção no ClickHouse.</li>
</ul>

<p align="justify">&emsp;&emsp;A partir dessas atividades, foi possível executar a aplicação e obter o seguinte registro de execução:</p>

<br>
<div align="center">
  <figcaption style="text-align: center; font-size: 10px; margin-bottom: 5px;">Figura X - Registro da execução da ingestão de dados</figcaption>
  <img src="https://res.cloudinary.com/de8ca4say/image/upload/v1732048221/Ingest-log_eer5r3.png" alt="Registro da execução da ingestão de dados" style="width: 100%; display: block; margin: 0 auto;">
  <figcaption style="text-align: center; font-size: 10px; margin-top: 5px;">Fonte: Elaboração Própria via Prefect Cloud</figcaption>
</div>
<br>

<br>
<div align="center">
  <figcaption style="text-align: center; font-size: 10px; margin-bottom: 5px;">Figura X - Gráfico da execução do processo de ingestão de dados</figcaption>
  <img src="https://res.cloudinary.com/de8ca4say/image/upload/v1732047933/ingest-data_bwqfut.png" alt="Gráfico da execução do processo de ingestão de dados" style="width: 100%; display: block; margin: 0 auto;">
  <figcaption style="text-align: center; font-size: 10px; margin-top: 5px;">Fonte: Elaboração Própria via Prefect Cloud</figcaption>
</div>
<br>

<p align="justify">&emsp;&emsp;A partir dessas atividades, foi possível executar a aplicação e analisar o registro de execução. Observou-se que a segunda chamada de <i>read_parquet_and_insert_to_clickhouse</i> consumiu mais tempo devido à maior quantidade de linhas processadas. Esses dados evidenciam o benefício do Prefect para o projeto, aprimorando a observabilidade e identificando gargalos no processamento.</p>

## 7.4 Conclusão

<p align="justify">&ensp;&ensp;A implementação do Cubo de Dados Automatizado no projeto representa um marco na organização e análise dos dados operacionais da CPTM. A escolha criteriosa das dimensões, como linha, estação, grupo PCD, dia da semana e horário, reflete uma abordagem estratégica para atender aos KPIs definidos, possibilitando insights detalhados sobre padrões de fluxo de passageiros, acessibilidade e eficiência operacional. O uso de planilhas estruturadas em SQL e a adoção do Metabase para visualização dos indicadores garantiram clareza na interpretação das métricas, permitindo que os stakeholders tomem decisões fundamentadas e otimizem recursos. A automação com Prefect, por sua vez, trouxe maior observabilidade e eficiência ao fluxo ETL, identificando gargalos e promovendo uma execução mais robusta e confiável.</p> 

<p align="justify">&ensp;&ensp;Esse conjunto de ferramentas e metodologias, além de facilitar o monitoramento contínuo das operações, também alinha o projeto às melhores práticas de análise de dados, como a organização de grandes volumes de informações em tempo real e a criação de estruturas escaláveis. Ao integrar essas soluções, o Cubo de Dados Automatizado não apenas atende às necessidades operacionais da CPTM, mas também se posiciona como um elemento estratégico para transformar os dados em valor, promovendo melhorias na gestão do transporte público. Dessa forma, o projeto demonstra sua capacidade de gerar impactos positivos tanto na eficiência quanto na experiência dos passageiros, consolidando-se como um modelo inovador e funcional na aplicação de tecnologias de Big Data.</p>

# <a id="c8"></a>8 Análise de Eficácia e Sugestões de Melhorias
## <a id="c8.1"></a>8.1 Relatórios de Análise de Eficácia
## <a id="c8.2"></a>8.2 Sugestões de Melhorias

# <a id="c9"></a>9 Infográfico

<p align="justify">&ensp;&ensp;O infográfico foi desenvolvido com o objetivo de comunicar de forma clara e visual os serviços de acessibilidade oferecidos pela CPTM. Pensado principalmente para atender às necessidades de informação de diferentes públicos, o infográfico apresenta dados informativos e operacionais relacionados à mobilidade e inclusão, com foco na população de Pessoas com Deficiência (PCD).
</p>

<p align="justify">&ensp;&ensp;Transmitir informações sobre o fluxo de passageiros PCD, os esforços de acessibilidade da CPTM e os impactos dessas ações no transporte público de São Paulo foram os principais objetivos definidos para o infográfico. Por meio de gráficos e storytelling, se busca destacar a importância da acessibilidade nos serviços de transporte da CPTM, apresentar os KPIs principais relacionados à mobilidade inclusiva e informar de maneira intuitiva as iniciativas da CPTM que promovem uma experiência de transporte mais acessível e eficiente.
</p>

<br>
<div align="center">
  <figcaption style="text-align: center; font-size: 10px; margin-bottom: 5px;">Figura X - Infográfico</figcaption>
  <img src="https://res.cloudinary.com/dxjfonp85/image/upload/v1733255332/hxa5sqwgkrljicadmpda.png" alt="Infográfico" style="width: 100%; display: block; margin: 0 auto;">
  <figcaption style="text-align: center; font-size: 10px; margin-top: 5px;">Fonte: Elaboração Própria</figcaption>
</div>
<br>

<p align="justify">&ensp;&ensp;Ao destacar os esforços e resultados da CPTM no campo da acessibilidade, o infográfico reforça o compromisso da companhia em atender a todas as necessidades da população, especialmente a PCD. Combinando dados relevantes, visualizações atrativas e informações claras, este material se posiciona como uma referência informativa e um exemplo de comunicação eficaz.
</p>

## <a id="c9.1"></a>9.1 Pesquisa

<p align="justify">&ensp;&ensp;No projeto para a CPTM, a realização de pesquisas é essencial para fundamentar decisões estratégicas e garantir que os resultados estejam alinhados às necessidades do público-alvo. A pesquisa conduzida neste projeto busca compreender percepções e interações com o infográfico desenvolvido, promovendo ajustes baseados em dados concretos para maior assertividade no design final.</p>

<p align="justify">&ensp;&ensp;A realização de pesquisas é amplamente reconhecida como uma ferramenta indispensável para o desenvolvimento de soluções eficazes. Segundo Alves e Aquino (2012), a pesquisa qualitativa permite aprofundar o entendimento sobre comportamentos e necessidades, orientando decisões baseadas em evidências e alinhadas ao contexto investigado.
</p>

<p align="justify">&ensp;&ensp;Após realizar a pesquisa no ambiente do Inteli, envolvendo alunos como participantes, obtivemos resultados valiosos sobre a eficácia do infográfico em comunicar informações sobre mobilidade PCD. Esses resultados, detalhados em termos de clareza, organização e design, podem ser encontrados no documento <i>Pesquisa Sobre Infográfico (Anexo B)</i>.</p>

<p align="justify">&ensp;&ensp;A pesquisa realizada com base no infográfico sobre mobilidade PCD da CPTM foi aplicada a 10 participantes, abordando suas percepções quanto à clareza, organização, design e relevância das informações apresentadas. A maioria dos entrevistados avaliou positivamente a experiência, destacando a organização lógica e o uso adequado de gráficos e cores. Comentários frequentes ressaltaram a clareza dos dados e o layout bem pensado, com elogios ao equilíbrio visual e à capacidade do infográfico de atrair curiosidade sobre o tema. Contudo, algumas críticas apontaram necessidade de detalhamento em gráficos específicos, maior contraste de cores.</p>

<p align="justify">&ensp;&ensp;Os pontos mais fortes identificados incluem a clareza das informações, o design visual atrativo e a abordagem educativa do tema. Aspectos a serem melhorados incluem explicações mais detalhadas para gráficos relacionados a linhas de menor uso e uma melhor integração entre diferentes seções. A pesquisa revelou que o infográfico é amplamente recomendado para educar sobre acessibilidade, embora ajustes pontuais possam aumentar sua eficácia e impacto. Essa análise oferece insights valiosos para futuras revisões e desenvolvimento de materiais similares.</p>


## <a id="c9.2"></a>9.2 Relatório de melhorias

###  Análise de Eficácia

**Clareza das Informações**
<p align="justify">&ensp;&ensp;Como demonstrado na pesquisa acima, o infográfico foi avaliado como claro e bem organizado pela maioria dos participantes. As informações foram bem apresentadas e possui uma lógica por trás, facilitando a compreensão do público. Gráficos e textos se comunicam bem, garantindo que todos dados sejam interpretados de maneira bem intuitiva.
</p>

- **Ponto positivo:** Os dados sobre PCD por linha e grupo prioritário se destacaram como um dos pontos mais claros e estruturados do infográfico.
- **Ponto a melhorar:** Alguns participantes sugeriram ter uma melhor conexão entre os gráficos, como uma explicação mais detalhada sobre os critérios para escolha dos dados.

**Concisão**
<p align="justify">&ensp;&ensp;Os gráficos se mostram eficientes em resumir os dados e minimizar o uso de texto. A escolha por elementos visuais permitiu mostrar as informações rapidamente, sem deixar o infográfico com descrições extensas.
</p>

- **Ponto positivo:** A visualização gráfica dos KPIs (ex.: "Quantidade de PCD por Linha") permitiu uma interpretação rápida e eficaz pelos participantes.
- **Ponto a melhorar:** Linhas menos utilizadas poderiam receber mais destaque, garantindo que os dados não pareçam incompletos ou pouco informativos.

**Atração Visual**
<p align="justify">&ensp;&ensp;O design foi bem elogiado pela harmonia nas cores, inspiração nas outras linhas da CPTM, layout organizado e informações legíveis. A escolha de tons contrastantes garantiu uma certa acessibilidade visual, enquanto o estilo limpo melhorou a exploração do conteúdo.
</p>

- **Ponto positivo:** A paleta de cores e o design minimalista tornaram o infográfico atraente e limpo.
- **Ponto a melhorar:** Ajustar as cores de alguns gráficos para melhorar ainda mais o contraste.

**Interesse gerado**
<p align="justify">&ensp;&ensp;A maioria dos participantes falou que o infográfico acabou trazendo interesse pelo tema, incentivando a exploração de mais informações. Isso mostra a eficiência do material em promover conscientização e engajamento sobre acessibilidade no transporte público.
</p>

### Sugestões de melhoria

**Melhorar a conexão entre gráficos**
- **Motivação:** Alguns participantes relataram que as transições entre gráficos não estavam suficientemente claras, dificultando um pouco a compreensão do fluxo de informações e storytelling.
- **Sugestão:** Adicionar mais legendas explicativas para contextualizar a relação entre os dados apresentados.

**Destaque para linhas menos utilizadas**
- **Motivação:** Linhas com menor demanda de passageiros PCD foram notadas como secundárias, reduzindo a sua importância no contexto geral.
- **Sugestão:** Criar gráficos adicionais ou focar em desmonstrações específicas dessas linhas para aumentar o contexto e valorizar todos os dados.

**Contraste de cores**
- **Motivação:** Alguns usuários mencionaram que o contraste poderia ser mais eficiente em determinadas áreas do infográfico.
- **Sugestão:** Revisar a paleta de cores para maximizar o contraste.

**Explicitar os critérios de análise**
- **Motivação:** Alguns usuários mostraram dificuldade em entender como os dados foram agrupados ou os critérios para calcular KPIs/métricas.
- **Sugestão:** Inserir uma seção curta explicando os métodos de coleta e análise dos dados, garantindo maior transparência.

### Conclusão

<p align="justify">&ensp;&ensp;O infográfico demonstrou ser uma ferramenta bem eficiente para comunicar as informações sobre acessibilidade e transporte público. Ele foi bem recebido quanto à clareza, concisão e design, mas ainda pode ser aprimorado para aumentar seu impacto e aderência pelo público. Implementar as melhorias sugeridas pode fortalecer sua capacidade de educar o público, sendo um bom material sobre a acessibilidade nos serviços da CPTM.
</p>

# <a id="c10"></a>10 Análise Financeira do Projeto

<p align="justify">&emsp;&emsp;<i>Este tópico pode ser encontrado em PDF no anexo D.</i></p>

<p align="justify">&emsp;&emsp;A análise financeira desempenha um papel muito importante na aplicação do projeto, pois permite avaliar a viabilidade econômica e os impactos financeiros da sua implementação. O objetivo é fornecer uma visão clara e detalhada sobre os custos e os ganhos associados, medindo o retorno do investimento e sua contribuição para os objetivos estratégicos da CPTM. Essa análise é essencial para garantir que os recursos sejam direcionados de forma eficiente, com base em dados concretos.
</p>

<p align="justify">&emsp;&emsp;Um dos aspectos centrais da análise financeira são os custos e ganhos do projeto. Essa etapa cobre a identificação dos investimentos necessários, como infraestrutura em tecnologias (servidores, licenças de software e serviços em nuvem), treinamento de equipes e manutenção do sistema. Em contrapartida, avaliam-se os ganhos esperados, incluindo a redução de custos operacionais, aumento da eficiência nas operações ferroviárias e a geração de valor a partir de insights obtidos com a análise de dados.
</p>

<p align="justify">&emsp;&emsp;A viabilidade financeira é outra etapa importante, pois analisa se os benefícios projetados justificam o investimento inicial do proejto. No contexto da CPTM, a implementação de um sistema de Big Data não só visa à otimização dos processos internos, mas também à melhoria do serviço oferecido aos passageiros. Esse alinhamento entre os ganhos financeiros e os benefícios sociais reforça a relevância do desenvolvimento do projeto.
</p>

<p align="justify">&emsp;&emsp;Além disso, o cálculo de payback é imprescindível para determinar o tempo necessário para recuperar o investimento inicial com os ganhos que serão proporcionados pelo projeto. Para a CPTM, esse indicador é importante, pois ajuda a projetar o retorno em médio e longo prazo, considerando as economias operacionais geradas pela melhoria na gestão de recursos e processos.
</p>

<p align="justify">&emsp;&emsp;Por fim, o impacto financeiro mede como o projeto afeta a operação atual da CPTM. Isso inclui não apenas os ganhos diretos, como a redução de custos e aumento de produtividade, mas também impactos indiretos, como uma tomada de decisão mais precisa e o aumento da confiabilidade das operações. Esses fatores são importantes para assegurar que o projeto contribua positivamente tanto para a sustentabilidade financeira da organização quanto para a experiência dos passageiros.
</p>

<p align="justify">&emsp;&emsp;Dessa forma, ao estruturar a análise financeira em torno desses etapas, o projeto garante uma base sólida para a tomada de decisões, reforçando sua importância como uma iniciativa estratégica para a modernização e eficiência da companhia.
</p>

## <a id="c10.1"></a>10.1 Custos de Desenvolvimento do MVP

<p align="justify">&emsp;&emsp;Para iniciar a análise financeira é essencial considerar os custos de desenvolvimento do <i>MVP</i> - sigla em inglês para Produto Mínimo Viável. Essa etapa envolve avaliar todos os fatores necessários para criar a versão inicial do produto, com apenas as funcionalidades essenciais para funcionar e ser lançada no mercado. o <i>MVP</i>, permite coletar dados relevantes e identificar os pontos de melhoria a serem trabalhados, destacando a importância de incluir os seus custos na análise financeira. Além disso, a primeira versão a ser desenvolvida e entregue pelo grupo Quartzo à CPTM é um <i>MVP</i>, reforçando a importância dessa etapa (Franco Zanette, 2024).</p>

<p align="justify">&emsp;&emsp;Para esse fim, após uma pesquisa aprofundada, o grupo Quartzo realizou o cálculo de custos de desenvolvimento do <i>MVP</i> considerando dois principais pilares: Custos com o time e custos com ferramentas. Dessa forma, serão considerados os salários, benefícios, horas de trabalho da equipe e as ferramentas utilizadas. Não serão considerados custos de computadores e equipamentos, uma vez que estes são custos operacionais recorrentes e fazem parte de uma infraestrutura pré-concebida.</p>

<p align="justify">&emsp;&emsp;Começando pela análise do time, é importante levar em consideração que, para o desenvolvimento do projeto, o grupo Quartzo é composto por sete integrantes, sendo eles um <i>Product Owner (PO)</i>, um <i>Scrum Master (SM)</i> e cinco desenvolvedores seniores. Entretanto, o grupo Quartzo deve ser considerado como uma equipe <i>freelance</i>. Dessa forma, ao incluir na análise os benefícios e os gastos adicionais que uma empresa normalmente tem com seus funcionários, o cálculo dos valores por hora será simplificado, adotando o equivalente ao dobro do salário base.</p>

<p align="justify">&emsp;&emsp;Após uma pesquisa de mercado intensiva, será considerado o salário de um <i>Product Owner</i> em uma base de R$9.000,00 com uma carga horária de 160 horas ao mês, totalizando R$56,25 a hora, dobrando, teremos o valor de R$112,50. Partindo para <i>Scrum Master</i>, o salário mensal também é de R$9.000,00. Adiantando os cálculos ao seguir a mesma lógica, o valor que chegaremos é o de R$112,50. Por último, para o cargo de desenvolvedor sênior, o salário médio mensal é de R$10.000,00, sendo a hora R$62,50, seguindo mais uma vez a mesma lógica, o total é de R$125,00 a hora(Glassdoor, 2024).</p>

<p align="justify">&emsp;&emsp;Também é necessário considerar que o time trabalha um período de desenvolvimento de duas horas por dia, cinco dias por semana, por 10 semanas, totalizando 100 horas de trabalho no projeto por integrante. </p>

<table><tr><td></table>
<table>
  <thead>
    <tr>
      <th>Função</th>
      <th>Salário por Hora</th>
      <th>Horas de Trabalho no Projeto</th>
      <th>Quantidade de Pessoas</th>
      <th>Total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Scrum Master</td>
      <td>R$112,50</td>
      <td>100</td>
      <td>1</td>
      <td>R$11.250,00</td>
    </tr>
    <tr>
      <td>Product Owner</td>
      <td>R$112,50</td>
      <td>100</td>
      <td>1</td>
      <td>R$11.250,00</td>
    </tr>
      <tr>
      <td>Desenvolvedor Sênior</td>
      <td>R$125,00</td>
      <td>100</td>
      <td>5</td>
      <td>R$62.500,00</td>
    </tr>
  </tbody>
</table>

<p align="justify">&emsp;&emsp;Dessa forma, o total de gastos com a equipe é igual a soma do total do <i>Scrum Master</i>, <i>Product Owner</i> e desenvolvedores seniores, resultando em R$85.000,00.</p>

<p align="justify">&emsp;&emsp;O próximo passo é calcular os custos das tecnologias utilizadas, uma vez que existem os gastos relacionados a AWS. Para isso, no dia 26 de novembro, foi realizada a cotação no site da AWS Calculator (2024), a qual o custo mensal resultou em 141.47 USD, totalizando 1,697.64 USD em 12 meses, referentes aos seguintes serviços:</p>

<p align="justify">&emsp;&emsp;- Amazon S3 (Simple Storage Service): Configurado como Data Lake (sem custos adicionais na estimativa), com esse será possível armazenar dados em uma estrutura simplicada, permitindo acesso remoto de formas diversas, sendo acessado, por exemplo, na API de ETL, como visto na documentação oficial da <a href="https://docs.aws.amazon.com/s3/?nc2=h_ql_doc_s3">AWS S3</a>.</p>

<p align="justify">&emsp;&emsp;- AWS Lambda: Configuração com 200 solicitações diárias, armazenamento temporário alocado de 512 MB, sem custo mensal adicional. Esse serviço será utilizado para o disparo/execução de tarefas alinhadas ao ETL, permitindo a automatização das Lambda dos dados inseridos no DataApp. As especificações desse serviço podem ser visto no site oficial da <a href="https://docs.aws.amazon.com/lambda/?icmpid=docs_homepage_featuredsvcs">AWS Lambda</a></p>

<p align="justify">&emsp;&emsp;- Amazon EC2 (Elastic Compute Cloud): Instância configurada com sistema operacional Linux, plano de economia de 1 ano (Compute Savings Plans), resultando em 141,47 USD/mês para uma instância t4g.2xlarge. As instâncias de <i>Cloud Computing</i> serão utilizadas para a hospedagem de serviços como API's de ETL e consulta ao cubo de dados. As especificações desse serviço podem ser conferidos em sua <a href="https://docs.aws.amazon.com/ec2/?icmpid=docs_homepage_featuredsvcs">documentação oficial</a>.</p>

<p align="justify">&emsp;&emsp;Esses valores podem ser validados segundo o documento <i>Calculadora de Preços da AWS (Anexo A)</i>. Para trabalhar com os valores apresentados, o grupo Quartzo realizá as conversões para valor Real na data de 26/12/2024. Dessa forma, obtém-se  R$820,22 no valor mensal e R$9.842,67 no anual. Entretando, como o serviço pode ser cancelado a qualquer momento, sem custos adicionais, iremos realizar o cálculo para o período de 10 semanas, correspondente a duração do projeto. Com os valores anteriores, é válido considerar os custos semanais iguais a R$205,055 e, ao multiplicar por 10, totalizamos em R$2050,55.</p>

<p align="justify">&emsp;&emsp;Dessa forma, somando os valores de gastos com a equipe e com as tecnologias utilizadas, totalizamos a análise de custos de desenvolvimento do MVP em R$87.050,55. Esse investimento é significado, mas que deve ser analisado em conjunto com os próximos passos da análise financeira.</p>

## <a id="c10.2"></a>10.2 Custos de Implantação do MVP

<p align="justify">&emsp;&emsp;Nessa etapa da análise financeira, serão explorados os custos referente ao próximo passo da vida de um <i>MVP</i>, que é a sua implantação. Essa etapa é extremamente necessária ao considerar que o grupo Quartzo entregará para a CPTM um projeto que deve ser implantado pela mesma. Mais uma vez, os gastos serão divididos entre os custos de funcionários e os custos tecnológicos de mantimento da operação do DataApp com ferramentas AWS, previamente explicado.</p>

<p align="justify">&emsp;&emsp;Dessa forma, ao avaliar o resultado esperado final do projeto, a equipe avaliou a necessidade de um engenheiro de dados, um analista de dados e um engenheiro de <i>sotfware</i> para realizar a implantação do DataApp. O analista de dados será responsável por tratar as bases de dados que alimentam o DataApp desenvolvido no <i>MVP</i>, além de realizar os testes necessários para validar a aplicação. O engenheiro de dados fará a construção de toda a infraestrutura e arquitetura da solução, garantindo uma base eficiente para que os demais possam trabalhar. Já o engenheiro de <i>software</i> será indispensável para realizar atualizações no projeto, atendendo a quaisquer necessidades que possam surgir nessa transição de dados para o DataApp. Nesse sentido, vale citar que a projeção de custos será para o período de um ano de implantação.</p>

<p align="justify">&emsp;&emsp;Seguindo para os gastos relacionados aos funcionários, será considerada uma pesquisa média do mercado para considerar o salário, entretando, os custos que uma empresa tem com seus funcionários pode, de maneira simplicada, ser considerado o dobro do seu salário (ÉPOCA NEGÓCIOS, 2012). Essa simplificação se dará, assim como o cálculo do salário dos membros do grupo Quartzo, com base em uma extensa pesquisa de mercado. A primeira fase da pesquisa foi realizar uma busca pelo salário desses cargos na CPTM, entretando, não foram encontradas informações diretamente relacionadas, logo, iremos utilizar médias salariais de cada função.</p>

<p align="justify">&emsp;&emsp;Começando pela função de Engenheiro de Dados, a média salarial anual é de R$96.000,00. Seguindo a lógica de dobrar o valor para chegar a uma aproximação dos gastos que a empresa teria, o total é de R$192.000,00. Seguindo para Analista de Dados, o salário anual é de R$60.000,00. Com a mesma lógica, obtêm-se R$120.000,00. Por fim, para o salário de Engenheiro de <i>Software</i>, o anual é de R$108.000,00 ao ano, dobrando para 216.000,00. Ao somar, o resultado final é de R$528.000,00 como o custo total com a equipe (Glassdoor, 2024).</p>

<p align="justify">&emsp;&emsp;Seguindo para os custos relacionados à AWS, teremos os mesmos gastos referentes ao tópico anterior, com a mudança de que será uma conversão para Real do preço anual de 1,697.64 USD, resultando no montante de R$9.880,68 ao ano. Para mais detalhes sobre as características do serviço contrato, é relevante consultar o tópico 10.1 Custos de Desenvolvimento do MVP.</p>

<p align="justify">&emsp;&emsp;Por fim, o resultado da soma dos custos relacionados a funcionários, com os custos de AWS perfaz um montante total de R$537.880,68. Esse valor representa a estimativa necessária para a implantação e operação do DataApp ao longo de um ano, considerando os gastos com a equipe técnica e a infraestrutura tecnológica. Esse investimento reflete o compromisso em garantir que a solução desenvolvida pelo grupo Quartzo seja implementada com eficiência e atenda às necessidades da CPTM, assegurando a funcionalidade e a sustentabilidade do projeto.</p>

## <a id="c10.3"></a>10.3 Custos de Manutenção do Projeto Final

<p align="justify">&emsp;&emsp;Nesta etapa da análise financeira, serão apresentados os custos estimados para a manutenção anual do projeto final. Considerando que o DataApp será implantado em um prazo de um ano, os custos projetados para manutenção coincidem com os custos de implantação. Principalmente pelo fato de que os requisitos de pessoal e infraestrutura permanecem os mesmos. O grupo Quartzo optou por utilizar esse período de análise para refletir a necessidade de continuidade operacional e o funcionamento da solução desenvolvida, além da sua atualização conforme necessário.</p>

<p align="justify">&emsp;&emsp;Assim como na implantação, os custos de manutenção serão divididos entre os gastos com a equipe e os custos com as ferramentas tecnológicas da AWS. A equipe técnica se manterá composta por um engenheiro de dados, um analista de dados e um engenheiro de <i>software<i/>. A mesma continuará desempenhando papéis de tratamento de dados, manutenção e atualização da infraestrutura, além de suporte para eventuais melhorias no sistema.</p>

<p align="justify">&emsp;&emsp;Mantendo os salários médios anuais dos cargos citados anteriormente no tópico 10.2 Custos de Implantação do MVP e aplicando a mesma lógica de dobrar o valor para refletir os custos totais de um funcionário para a empresa, os custos estimados permanecem os mesmos:</p>

<ul>
  <li>Engenheiro de Dados: R$192.000,00</li>
  <li>Analista de Dados: R$120.000,00</li>
  <li>Engenheiro de Software: R$216.000,00</li>
</ul>
st
<p align="justify">&emsp;&emsp;Dessa forma, o custo total relacionado à equipe técnica é novamente de **R$528.000,00**.</p>

<p align="justify">&emsp;&emsp;No que diz respeito aos cuos tecnológicos, a operação anual do DataApp, utilizando serviços da AWS, também seguirá a mesma estimativa descrita no tópico 10.2 Custos de Implantação do MVP
, baseada no tópico 10.1 Custos de Desenvolvimento do MVP. O valor total para os serviços AWS no período de um ano é de <b>R$9.880,68</b>.</p>

<p align="justify">&emsp;&emsp;Assim, o custo total estimado para a manutenção anual do projeto final é de <b>R$537.880,68</b>, equivalente ao custo de implantação. Essa continuidade operacional assegura que o DataApp atenda às demandas futuras da CPTM e mantenha sua relevância em suas próximas operações.</p>

## <a id="c10.4"></a>10.4 Levantamento de Lucros Indiretos do Projeto

<p align="justify">&emsp;&emsp;Ao considerar o tópico de lucros indiretos do projeto, é muito relevante considerar que, estes gastos não se limitam ao retorno financeiro, especialmente no contexto da CPTM, uma vez que a mesma é uma empresa pública e estatal. Diferentemente de organizações privadas, a CPTM prioriza a prestação de serviços de qualidade à população e o cumprimento de sua função social, o que torna os benefícios intangíveis e os impactos sociais igualmente relevantes.</p>

<p align="justify">&emsp;&emsp;Nesse sentido, entre os principais lucros indiretos, podemos citar a retenção de clientes, resultante das melhorias no serviço prestado. Para um melhor detalhamento, o DataApp tem como resultado esperado pelo grupo Quartzo um sistema mais eficiente e transparente, elevando a confiança dos passageiros no transporte público, incentivando sua fidelização e o aumento da demanda. Esse impacto, mesmo que indireto, contribui para a sustentabilidade financeira da CPTM a longo prazo, representando uma mudança significativa em relação ao cenário atual, no qual, assim como foi comunicado no <i>kickoff</i>, a empresa depende de subsídios estatais para operar.</p>

<p align="justify">&emsp;&emsp;Outro benefício está nas melhorias na experiência do cliente. Com informações mais claras e precisas, os passageiros terão menos incertezas e podem planejar suas viagens com maior eficiência. Essa percepção positiva gera satisfação e pode reduzir a evasão de usuários para meios de transporte alternativos, promovendo um transporte público mais atrativo.</p>

<p align="justify">&emsp;&emsp;Por fim, deve-se considerar que, após todas as mudanças apresentadas, haverá um fortalecimento da marca CPTM. A adoção dessa tecnologia inovadora, unido ao fato de que, assim como apontada pela mesma em suas reuniões de entrega de sprint com o grupo Quartzo, a marca quer se tornar data-driven, reforça a imagem da empresa como uma operadora de transporte público moderna, comprometida com a melhoria contínua e a transparência. Esse fortalecimento institucional pode abrir portas para novas parcerias estratégicas e atrair investimentos voltados ao transporte público.</p>

<p align="justify">&emsp;&emsp;Embora esses ganhos sejam intangíveis, é possível estimar seus impactos financeiros baseando-se em dados de mercado, como a correlação entre melhorias no serviço e aumento na quantidade de passageiros, uma sugestão de estudo que pode ser feita pela CPTM após a entrega do <i>MVP</i>. Além disso, a valorização da marca pode resultar em economias indiretas, como maior apoio governamental ou redução de custos com campanhas de conscientização e marketing. Assim, os lucros indiretos desempenham um papel crucial na justificativa da viabilidade e relevância do projeto no contexto público da CPTM.</p>

## <a id="c10.5"></a>10.5 Cálculo de ROI e Período de Payback

<p align="justify">&ensp;&ensp; Nessa seção, abordaremos o cálculo do Retorno sobre Investimento (ROI) e do Período de Payback para o projeto desenvolvido pelo grupo Quartzo. O ROI e o Payback são métricas financeiras amplamente utilizadas para avaliar a viabilidade de investimentos e o tempo necessário para a recuperação do capital investido. De acordo com Damodaran (2012), o ROI mede a eficiência de um investimento em gerar retornos em relação aos custos totais, enquanto o Payback fornece uma estimativa de quanto tempo será necessário para que o investimento se torne autossustentável. Esses indicadores, foram adaptados ao projeto devido ao seu foco em benefícios intangíveis e financeiros indiretos, como a valorização da marca e a fidelização de clientes. A análise foi elaborada para incorporar métricas qualitativas e indicadores financeiros indiretos, avaliando o impacto positivo nas operações da CPTM e os possíveis cenários de mercado.</p>

<p align="justify">&ensp;&ensp; Para calcular o ROI, foram considerados os ganhos estimados do projeto em duas categorias principais: impactos financeiros indiretos e benefícios intangíveis. Entre os impactos financeiros indiretos, projetamos uma economia operacional de 5%, decorrente da eficiência proporcionada pela solução, e um aumento na retenção de usuários em 2%, atribuído à melhoria na percepção do serviço. Segundo a ABEPro (2021), melhorias na qualidade dos serviços de transporte público impactam positivamente a fidelização de clientes e a valorização da marca, reforçando a relevância desse tipo de investimento. Para embasar essas estimativas, utilizamos como referência a estratégia implementada pela Metropolitan Transportation Authority (MTA) de Nova York para melhorar o serviço do metrô da cidade. O plano de ação incluiu a atualização de equipamentos de trilhos e sinalização, programas para lidar com a intrusão de água, limpeza completa do sistema e uma atualização significativa na manutenção dos carros do metrô, com inspeções e reparos realizados 24 horas por dia. Essas medidas resultaram em melhorias na eficiência operacional e na satisfação dos passageiros, demonstrando que investimentos em infraestrutura e manutenção podem levar a economias operacionais e ao aumento da retenção de usuários (Metro Magazine, 2024).</p>

Com base nos custos totais do projeto, que incluem desenvolvimento (R$87.050,55), implantação e manutenção (R$537.880,68), o montante atinge R$624.931,23. O ROI foi calculado considerando ganhos anuais estimados em R$14 milhões (R$9 milhões pela retenção de usuários e R$5 milhões em economia operacional). A fórmula utilizada foi:

ROI = (Ganhos Estimados / Custos Totais) x 100 
ROI = (14.000.000 / 624.931,23) x 100 ≈ 2240%. 

O Período de Payback, foi calculado pela fórmula:

Payback = Custos Totais / Ganhos Anuais Estimados 
Payback = 624.931,23 / 14.000.000 ≈ 0,05 anos, ou 18 dias.

<p align="justify">&ensp;&ensp; Adicionalmente, foi realizada uma análise de cenários para explorar possíveis variações nos ganhos. No cenário otimista, projetou-se um aumento na retenção de usuários para 5% e uma economia operacional de 10%, baseado em casos de empresas com alta implementação tecnológica e adesão de usuários, como o exemplo da Maryland Transit Administration (MTA). A MTA implementou um Painel de Experiência do Cliente para monitorar indicadores-chave de desempenho, como pontualidade, número de passageiros e disponibilidade de informações em tempo real. Essa iniciativa resultou em melhorias significativas na eficiência operacional e na satisfação dos usuários, demonstrando que a adoção de tecnologias avançadas pode levar a economias operacionais e ao aumento da retenção de clientes (MTA, 2024). Já no cenário pessimista, sem aumento na retenção e com economia operacional limitada a 2%, o ROI seria mais modesto, e o Payback se estenderia para cerca de um ano. Essas projeções demonstram a flexibilidade e a resiliência do projeto a diferentes condições de mercado.</p>

<p align="justify">&ensp;&ensp; O cálculo do ROI e do Período de Payback demonstram que o projeto desenvolvido pelo grupo Quartzo é uma iniciativa de alto impacto, tanto em termos operacionais quanto institucionais. Apesar de não gerar lucros financeiros diretos, os benefícios intangíveis, como a valorização da marca, a fidelização de clientes e a modernização da operação, justificam o investimento realizado.</p>

## <a id="c10.6"></a>10.6 Análise de Cenários de Mercado

### Cenário de Mercado Atual

<p align="justify">&ensp;&ensp;Para contextualizar a análise de cenários de mercado, é importante considerar o desempenho financeiro recente da CPTM. No ano de 2021, a CPTM obteve um lucro bruto de R$ 282 milhões, revertendo um déficit bruto de R$ 215 milhões registrado no ano anterior. Esse cálculo é feito através da diferença entre a receita líquida e o custo dos serviços prestados. Em termos líquidos, a companhia registrou um prejuízo de 469 milhões de reais, o que representa uma melhora em relação ao prejuízo líquido de 963 milhões de reais em 2020. O prejuízo líquido leva em consideração as despesas administrativas e financeiras (CARLOS, 2022).</p>

### Cenário Otimista

<p align="justify">&ensp;&ensp;No cenário otimista, assumimos que a economia está em crescimento, com baixa inflação e alta demanda por serviços de transporte público. A eficiência operacional do DataApp resulta em uma economia de custos de 10%, e a melhoria na experiência do cliente aumenta a retenção de passageiros em 5%. Além disso, a valorização da marca CPTM atrai novos investimentos e parcerias estratégicas.</p>

- **Economia Operacional:** 10% de redução nos custos, resultando em uma economia de R$10 milhões anuais.
- **Aumento na Retenção de Passageiros:** 5% de aumento, gerando um ganho adicional de R$22,5 milhões por ano.
- **Receitas Indiretas:** Novos investimentos e parcerias resultam em R$5 milhões adicionais.
- **Total de Ganhos:** R$37,5 milhões anuais.

### Cenário Moderado

<p align="justify">&ensp;&ensp;No cenário moderado, a economia apresenta um crescimento estável, com inflação controlada e demanda constante por serviços de transporte público. A eficiência operacional do DataApp proporciona uma economia de custos de 5%, e a retenção de passageiros aumenta em 2%. A valorização da marca CPTM continua a atrair parcerias, mas em menor escala.</p>

- **Economia Operacional:** 5% de redução nos custos, resultando em uma economia de R$5 milhões anuais.
- **Aumento na Retenção de Passageiros:** 2% de aumento, gerando um ganho adicional de R$9 milhões por ano.
- **Receitas Indiretas:** Parcerias estratégicas resultam em R$2 milhões adicionais.
- **Total de Ganhos:** R$16 milhões anuais.

### Cenário Pessimista

<p align="justify">&ensp;&ensp;No cenário pessimista, a economia enfrenta desafios, com alta inflação e demanda reduzida por serviços de transporte público. A eficiência operacional do DataApp resulta em uma economia de custos de apenas 2%, e não há aumento significativo na retenção de passageiros. A valorização da marca CPTM é limitada, com poucas novas parcerias.</p>

- **Economia Operacional:** 2% de redução nos custos, resultando em uma economia de R$2 milhões anuais.
- **Aumento na Retenção de Passageiros:** Nenhum aumento significativo, mantendo os ganhos adicionais em R$0.
- **Receitas Indiretas:** Parcerias limitadas resultam em R$0,5 milhão adicional.
- **Total de Ganhos:** R$2,5 milhões anuais.

### Comparação dos Cenários

<p align="justify">&ensp;&ensp;A comparação dos cenários otimista, moderado e pessimista destaca a importância de considerar variações econômicas e de demanda ao planejar a implementação e manutenção do DataApp. No cenário otimista, os ganhos são substanciais, com um ROI elevado e um período de payback muito curto. No cenário moderado, os ganhos são menores, mas ainda significativos, garantindo a viabilidade do projeto. No cenário pessimista, os ganhos são limitados, mas o projeto ainda se justifica pela melhoria na eficiência operacional e pela valorização da marca.</p>

<p align="justify">&ensp;&ensp;Essa análise de cenários de mercado permite à CPTM preparar-se para diferentes condições econômicas, ajustando suas estratégias conforme necessário para maximizar os benefícios do DataApp e garantir a sustentabilidade do projeto a longo prazo.</p>

## <a id="c10.7"></a>10.7 Conclusão da Análise Financeira

<p align="justify">&emsp;&emsp;Como observado, a seguinte análise financeira confirmou sua viabilidade econômica e alinhamento estratégico com a CPTM. Abordando custos de desenvolvimento, implantação e manutenção, além de indicadores como ROI e Payback, a análise demonstrou que o projeto pode oferecer retornos rápidos e relevantes, mesmo em cenários moderados.
</p>

<p align="justify">&emsp;&emsp;Além dos ganhos diretos, o projeto trás alguns benefícios indiretos, como fidelização de passageiros e fortalecimento da CPTM, importantes para uma empresa pública focada no impacto social na mobilidade de São Paulo. O estudo de cenários reforçou a eficiência do projeto em diferentes contextos econômicos, afirmando sua relevância estratégica.
</p>

<p align="justify">&emsp;&emsp;O projeto não apenas otimiza operações e reduz custos, mas também melhora a experiência dos passageiros e promove inclusão, reforçando o compromisso da CPTM com um transporte público mais moderno e eficiente.
</p>


  
# <a id="c11"></a>11 Plano de Comunicação

<p align="justify">&emsp;&emsp;<i>Este tópico pode ser encontrado em PDF no anexo D.</i></p>


<p align="justify">&ensp;&ensp;O Plano de Comunicação é um componente importante em projetos, garantindo que as informações, atualizações e decisões críticas sejam transmitidas de forma eficiente entre todas as partes interessadas. Ele define canais, frequências e responsabilidades, assegurando que todos os membros da equipe e stakeholders estejam alinhados durante o ciclo de vida do projeto.(IRON CARROT, 2022)</p>

<p align="justify">&ensp;&ensp;Essa estratégia está sendo aplicada no projeto da CPTM com o intuito de manter os stakeholders da CPTM e do Inteli informados de maneira efetiva e padronizada, o que torna a comunicação entre as partes do projeto mais diretas e com planejamento previsto. Com essas medidas, possíveis imprevistods que ocorram no projeto já tem de forma padronizada com quem, como e de que forma se deve comunicar com todos os envolvidos.</p>

<p align="justify">&ensp;&ensp;O plano de comunicação foi feito baseando se no modelo apresentado pelo professor Afonso Brandão (2024). O modelo se baseia em seguir os seguintes passos:</p>

- Identificar os stakeholders
- Relação de Poder e Interesse dos Stakeholders
- Montar o plano de comunicação


## <a id="c11.1"></a>11.1 Identificação dos Stakeholders

<p align="justify">&ensp;&ensp;Para mapear os stakeholders, que segundo Jason Fernando (2024) são grupos ou indivíduos que possuem interesse no sucesso do negócio ou do projeto, é necessário separa-los em:</p>

- internos e externos ;
- Clientes, usuários, patrocinadores e Equipe ;

<p align="justify">&ensp;&ensp;Seguido essas características, podemos separar os stakeholders do projeto da seguinte forma:</p>

<p align="center">Quadro 7 - Identificação dos Stakeholders</p>

|Stakeholder|Pertencimento|Tipo|
|---|---|---|
|Grupo Quartzo|Interno|Equipe|
|Corpo docente|Interno|Equipe|
|Pareceiro de projeto|Externo|Cliente|

<p align="center">Fonte: Elaborado pelos autores.</p>

## <a id="c11.2"></a>11.2 Matriz de Poder/Interesse

<p align="justify">&ensp;&ensp;Outra etapa importante para a construção do plano de comunicação é identificar o quanto os stakeholders estão interessados no projeto e quanta influência eles possuem sobre ele. Para melhor identificar essas características, será utilizado a matriz poder/interesse para analisar a melhor maneira de manter a comunicação com cada stakeholder.</p>

<p align="center">Quadro 8 - Matriz de interesse/poder</p>

||Alto interesse|Baixo Interesse|
|---|---|---|
|**Alto poder**|Gerenciar de perto|Manter satisfeito|
|**Baixo poder**|Manter informado|Monitorar com esforço mínimo|

<p align="center">Fonte: Elaborado pelos autores.</p>

<p align="justify">&ensp;&ensp;Seguindo as sessões da matriz, podemos separar os envolvidos no projeto da seguinte maneira:</p>

- **Genrenciar de Perto:** Corpo docente.
- **Manter Informado** Grupo Quartzo, Parceiro de projeto.

<p align="justify">&ensp;&ensp;A separação feita é extremamente importante porque é por meio dela que é feita a forma de comunicação e a frequência em que o stakeholder vai ser atualizado sobre o status do projeto que está em andamento. Como por exemplo, um stakeholder com baixo interesse e poder pode ser comunicado de maneira mensal ou semestral por email, em quanto um com alto poder e interesse deve ser informado semanalmente ou por sprint com reuniões presenciais.</p>

<p align="justify">&ensp;&ensp;Uma vez que os stakeholders estão definidos, é de extrema importância definir a <b>mensagem chave</b> de cada um deles, que é a informação mais importante a ser passada para esse stakeholder. As mensagem chave de cada um são as seguintes:</p>

- **Grupo Quartzo:** Progresso do projeto, metas, expectativas, desafios e soluções
  
- **Corpo Docente:** Aderência ao cronograma, qualidade das entregas e desafios críticos
  
- **Parceiro de Projeto:** Status do projeto, resultados, gestão de riscos e solicitação de feedback


## <a id="c11.3"></a>11.3 Confecção do Plano de Comunicação

<p align="justify">&ensp;&ensp;Levando em consideração as informações levantadas nos tópicos 11.1 e 11.2, o plano foi montado de maneira a atender todas as especificidades de cada stakeholder. Para isso, também foi feito um plano de implementação para o conseguir estabelecer o padrão de maneira mais clara e objetivo no projeto e seus envolvidos.</p>

<p align="justify">&ensp;&ensp;A implementação será realizada em três etapas principais: Preparação, execução e monitoramento, e avaliação. Cada etapa inclui atividades específicas que garantem a efetividade da comunicação entre os stakeholders do projeto.</p>

<h4>Revisão e Validação</h4>

<p align="justify">&ensp;&ensp;Na etapa de preparação, primeiramente, será feita uma revisão e validação das mensagens-chave definidas para cada stakeholder, assegurando que elas estejam em alinhamento com os objetivos organizacionais e adequadas ao perfil de cada público. Em seguida, a equipe alinhará como cada etapa do plano vai ser seguida, com ênfase na importância da clareza ao transmitir mensagens. Além disso, serão desenvolvidos templates padronizados para e-mails, Incluindo relatórios e apresentações elaborados pelo corpo docente, com o objetivo de manter a uniformidade na comunicação.</p>

<h4>Templates</h4>

<p align="justify">&ensp;&ensp;Durante o desenvolvimento de templates padronizados, será realizada a criação de modelos específicos para e-mails, relatórios e apresentações, garantindo que todos os documentos sigam a mesma identidade visual e o tom de voz do grupo Quartzo. Esses templates serão disponibilizados no github do projeto relacionado ao grupo 4, facilitando o uso consistente em todas as comunicações. Além disso, haverá uma revisão periódica dos materiais, assegurando que permaneçam relevantes e atualizados de acordo com as necessidades do projeto.</p>

<h4>Execução e monitoramento</h4>

<p align="justify">&ensp;&ensp;Na etapa de execução e monitoramento, a implementação da comunicação seguirá rigorosamente as diretrizes estabelecidas, iniciando as atividades conforme a matriz de poder/interesse. As ações planejadas incluem a realização de reuniões regulares com os stakeholders, respeitando as frequências previamente definidas, para garantir alinhamento contínuo.</p>

<p align="justify">&ensp;&ensp;Além disso, serão distribuídos relatórios e atualizações por meio dos canais mais adequados: o Slack será utilizado para comunicações internas diárias, enquanto e-mails serão o principal meio de atualização para o parceiro do projeto. A coleta contínua de feedback dos stakeholders será fundamental nesse processo, pois permitirá identificar possíveis melhorias e ajustes necessários na comunicação ao longo do projeto.</p>

<h4>Avaliação e ajustes</h4>

<p align="justify">&ensp;&ensp;Na etapa de avaliação e ajustes, a eficácia do plano de comunicação será monitorada continuamente, utilizando indicadores de desempenho, como a taxa de resposta e a satisfação dos stakeholders. 

<p align="justify">&ensp;&ensp;Serão realizadas reuniões quinzenais (reviews) para revisar o desempenho das comunicações internas e externas, com o objetivo de avaliar a consistência e o impacto das mensagens transmitidas. Com base nessas avaliações, serão implementados ajustes necessários, garantindo que a comunicação se adapte às mudanças nas necessidades do projeto e continue atendendo de forma eficaz às expectativas.</p>

<h4>Plano de contingência</h4>

<p align="justify">&ensp;&ensp;O plano de contenção foi desenvolvido para lidar com possíveis desafios durante a execução do projeto, garantindo que a comunicação se mantenha eficiente e alinhada com os objetivos organizacionais. Caso algum problema ocorra, ações imediatas serão implementadas para mitigar os impactos e assegurar o fluxo contínuo de informações.</p>

<p align="center">Quadro 9 - Plano de Contenção</p>

|**Problema**| **Descrição**| **Ação Imediata**| **Responsável**|
|---|---|---|---|
|**Falta de resposta**| Corpo Docente não responde a Slacks ou mensagens importantes. | Realizar um follow-up em até 24 horas |PO do time dev|
|**Informações inconsistentes**| Divergência entre o que foi comunicado e o status real do projeto. | Revisar o status do projeto com a equipe e enviar uma atualização corrigida. |PO do time dev|
|**Frequência inadequada**| Comunicação muito frequente ou insuficiente, causando desalinhamento.| Ajustar a frequência das comunicações e revisar com a equipe os cronogramas.| Gestor de projeto|
|**Falha na entrega de mensagens**| Mensagens importantes não chegam ao destinatário.| Confirmar recebimento e reenviar utilizando um canal alternativo. | Gestor de projeto|
|**Mal-entendidos**| Stakeholders interpretam informações de maneira incorreta.| Organizar uma reunião para esclarecer dúvidas e reforçar a mensagem.|Time dev|

<p align="justify">&ensp;&ensp;Vale reforçar que o plano de contenção está sujeito a possíveis modificações caso sejam percebidas falhas ou outros erros não mapeados venham a acontecer. Contudo, caso o quadro venha a ser utilizado é de extrema importância seguir conforme programado.</p>

<p align="center">Fonte: Elaborado pelos autores.</p>

<h4>Plano de Comunicação</h4>

<p align="justify">&ensp;&ensp;Com todas as informações agrupadas, o plano de comunicação foi montado de maneira a facilitar a comunicação de todas as partes do projeto. Segue no quadro 10 o plano completo</p>

<p align="center">Quadro 10 - Plano de Comunicação</p>

| **Stakeholder**| **Forma de Comunicação** | **Frequência**| **Responsável** | **Objetivo da Comunicação**| **Canal Alternativo** | **Formato da Comunicação** | **Critério de Sucesso**|
|---|---|---|---|---|---|---|---|
|**Grupo Quartzo**|Reuniões / Slack|Diária|Grupo Quartzo|Alinhamento diário (daily) e fechamento| Whatsapp|Reunião / Mensagem Slack|Participação e feedback da equipe|
|**Corpo docente**|Reuniões / Slack|Semanal|Grupo Quartzo|Atualização de progresso|E-mail relatório semanal|Reuniões|Aprovação do corpo docente|
|**Parceiro de projeto (CPTM)**| E-mail e Reuniões | A cada sprint| Corpo docente|Relatar status do projeto|Reunião online|Relatório de sprint|Confirmação de recebimento|


<p align="center">Fonte: Elaborado pelos autores.</p>


<p align="justify">&ensp;&ensp;Em conclusão, o Plano de Comunicação estruturado para o projeto da CPTM desempenha um papel essencial na manutenção da transparência e alinhamento entre todas as partes envolvidas. Ao definir claramente os canais, a frequência das comunicações e os responsáveis, a equipe assegura que informações críticas sejam transmitidas de forma eficiente e sem ruídos, minimizando riscos e garantindo que todos os stakeholders estejam cientes do progresso e dos desafios do projeto.</p> 

<p align="justify">&ensp;&ensp;Com essa abordagem, a comunicação não apenas fortalece a colaboração entre o Inteli e a CPTM, mas também proporciona uma base sólida para a resolução rápida de imprevistos, promovendo um ambiente mais coeso e organizado. Assim, o projeto beneficia-se de uma estrutura de comunicação robusta, contribuindo significativamente para o sucesso das entregas e para a satisfação de todos os envolvidos.</p>

# <a id="c12"></a>12 Pipeline Completo de Dados na AWS

## <a id="c12.1"></a>12.1 Arquitetura Geral do Pipeline

A arquitetura do pipeline foi projetada para suportar um fluxo contínuo de coleta, processamento e visualização de dados, utilizando ferramentas leves e eficientes. O objetivo é garantir a automação e integração completa do ciclo de vida dos dados, desde a fonte até a visualização interativa. 

### Componentes Principais:

1. **Fonte de Dados:**
   - Os dados iniciais são armazenados em **arquivos CSV** (`dmo_anl_vw_estacao` e `dmo_anl_vw_tot_mov`), contendo informações brutas sobre estações de trem e movimentações diárias de passageiros.
   - Esses arquivos servem como base para as análises subsequentes, garantindo que os dados brutos estejam disponíveis para auditorias ou reprocessamentos.

2. **Exploração e Ingestão de Dados:**
   - **Jupyter Notebooks e Python Scripts:** 
     - Utilizados para inspecionar os arquivos CSV e explorar padrões ou possíveis inconsistências nos dados.
     - Scripts Python processam os dados em formato tabular para organizar e preparar os registros para o próximo estágio do pipeline.

3. **Preparação e Armazenamento de Dados:**
   - **Amazon S3:** 
     - Atuando como um data lake, o S3 armazena os arquivos CSV brutos e intermediários, facilitando a centralização e o acesso para múltiplas etapas do pipeline.
   - **Pydantic:** 
     - Biblioteca utilizada para validar os dados processados, assegurando conformidade com os esquemas e formatos definidos previamente.
     - A validação ocorre antes do envio ao banco de dados ClickHouse.
   - **ClickHouse:** 
     - Banco de dados de alta performance para armazenamento estruturado.
     - Ideal para consultas analíticas rápidas e operações de agregação devido à sua arquitetura columnar.

4. **Middleware de Integração:**
   - **API em Flask:** 
     - Criação de endpoints RESTful para permitir que o frontend interaja diretamente com os dados armazenados no ClickHouse.
     - Cada endpoint é projetado para atender a uma view específica no Streamlit (e.g., `/acompanhamentopcd`, `/intervalos`).
     - Utiliza a biblioteca `clickhouse_driver` para realizar consultas e manipular dados no banco.

5. **Visualização de Dados:**
   - **Streamlit:** 
     - Framework de visualização que fornece gráficos interativos e painéis, permitindo ao usuário explorar os dados processados.
     - As visualizações incluem gráficos de barras, histogramas, gráficos de pizza e filtros interativos (e.g., seleção por linha ou intervalo de datas).

---

## <a id="c12.2"></a>12.2 Fluxo Detalhado do Pipeline

1. **Coleta e Ingestão de Dados:**
   - Os arquivos CSV são carregados nos notebooks Jupyter para uma inspeção inicial, garantindo que os dados brutos estejam em um formato utilizável.
   - Após a inspeção, os dados relevantes são processados por scripts Python e enviados ao S3 para armazenamento centralizado.

2. **Validação e Armazenamento:**
   - Os dados armazenados no S3 são processados por um script Python que utiliza o Pydantic para validar a integridade e formato dos registros.
   - Após a validação, os dados são carregados no ClickHouse, onde são armazenados em tabelas específicas para cada view do Datapp.

3. **Consulta e Integração:**
   - A API em Flask atua como middleware, permitindo que o frontend consulte os dados do ClickHouse.
   - Os endpoints RESTful, como `/movimentacaoporperiodo` e `/totaldevalidacoesporDia`, encapsulam a lógica de consulta ao banco e retornam os resultados no formato JSON.

4. **Visualização Interativa:**
   - O Streamlit consome os dados fornecidos pela API para gerar gráficos interativos e painéis.
   - Os gráficos incluem:
     - **Distribuições de Intervalos**: Histogramas com a duração média de intervalos.
     - **Movimentação por Período**: Gráficos de barras ou pizza segmentados por tipo de dia.
     - **Total de Validações**: Séries temporais filtradas por intervalo de datas selecionado pelo usuário.
   - Filtros interativos permitem aos usuários explorar os dados por linha, estação e períodos específicos.

---

## <a id="c12.3"></a>12.3 Conclusão

O pipeline implementado representa uma solução robusta e escalável para coleta, validação, armazenamento e visualização de dados. Ao adotar ferramentas específicas para cada etapa, o pipeline consegue equilibrar simplicidade e eficiência, atendendo às necessidades atuais do projeto e facilitando futuras expansões.

1. **Eficiência:** 
   - A utilização do ClickHouse garante desempenho excepcional em consultas analíticas.
   - O Pydantic assegura a integridade dos dados antes do armazenamento, reduzindo erros e inconsistências.

2. **Escalabilidade:** 
   - A centralização dos dados no Amazon S3 permite fácil integração com outras ferramentas ou pipelines.
   - A arquitetura modular da API e do Streamlit facilita a adição de novas views e funcionalidades.

3. **Interatividade e Acessibilidade:**
   - O Streamlit oferece uma interface amigável e responsiva, permitindo que os usuários explorem os dados em tempo real com filtros intuitivos.

Com essa abordagem, o Datapp se consolida como uma ferramenta essencial para análise e visualização de dados, promovendo insights valiosos e decisões baseadas em informações confiáveis. O pipeline está preparado para atender a demandas crescentes, garantindo flexibilidade e sustentabilidade a longo prazo.

# <a id="c13"></a>13 Visão Geral das Melhorias e Novos Recursos do Dataapp

<p align="justify">&ensp;&ensp; Ao longo da Sprint 5, o dataapp passou por uma série de aprimoramentos que não apenas ampliam as suas capacidades de análise, mas também tornam sua utilização mais ágil, intuitiva e acessível. Com foco na experiência do usuário, foram incorporadas melhorias na interface e na organização das informações, bem como na qualidade e interatividade das visualizações gráficas. Além disso, novos recursos permitem um nível mais aprofundado de análise, incluindo a segmentação por horário e tipo de PCD, a criação de mapas de calor e a possibilidade de exportar e compartilhar resultados. Essas adições e ajustes não somente facilitam a extração de insights, como também reforçam o papel do dataapp como uma ferramenta essencial para a tomada de decisões estratégicas na CPTM, oferecendo um ambiente analítico mais robusto e aderente às necessidades de uma empresa inserida em um contexto de Big Data. A seguir, detalhamos as melhorias implementadas e seus respectivos impactos. </p>

### Detalhamento das Melhorias

- Interface e UX: Melhorias na clareza visual, tornando mais simples encontrar informações e interpretar dados.
- Otimização de Filtros: Filtros mais rápidos e intuitivos, permitindo análise segmentada de dados sem entraves.
- Detalhes de PCD por Horário e Estação: Identificação mais precisa da demanda por acessibilidade, auxiliando em decisões operacionais (como alocação de recursos).
- Heatmap de PCD: Visualização de distribuição geográfica e temporal de PCD, agora com filtro de datas para análises mais específicas.
- Visualização com Plotly: Gráficos interativos que facilitam a exploração e o entendimento dos dados.
- Gráfico de Tipos de Bilhete por Dia: Acompanhamento da distribuição diária de diferentes tipos de bilhetes, apoiando estratégias tarifárias e de marketing.
- Exportação e Compartilhamento: Criação de relatórios e compartilhamento rápido de insights com outras equipes ou stakeholders.
- Organização em Páginas: Botão de adicionar páginas no topo da aplicação, nova página para informações gerais, e realocação dos gráficos de validação, facilitando navegação e foco analítico.

<p align="justify">&ensp;&ensp; As melhorias implementadas tornam o dataapp mais eficiente, intuitivo e completo. Com visualizações mais ricas, dados melhor segmentados e recursos de exportação, o dataapp apoia a tomada de decisão da CPTM de forma mais ágil e assertiva, reforçando seu papel como ferramenta estratégica em um contexto de Big Data. </p>

# <a id="c14"></a>14 Referências

1. SEBRAE. TAM/SAM/SOM: qual o tamanho do mercado da sua startup?. 2019. Disponível em: <https://sebraers.com.br/start-up/tam-sam-som-qual-o-tamanho-do-mercado-da-sua-startup/>. Acesso em: 26 out. 2024.
2. EQUIPE SEBRAE MG. TAM SAM SOM: calcule corretamente o tamanho do seu mercado. 2024. Disponível em: <https://inovacaosebraeminas.com.br/artigo/tam-sam-som>. Acesso em: 26 out. 2024.
3. SP‌Trans. Valores das Tarifas Vigentes a partir de 01/01/2020. 2019. Disponível em: <https://capital.sp.gov.br/web/mobilidade/w/institucional/sptrans/acesso_a_informacao/227887>. Acesso em: 26 out. 2024.

4. AGÊNCIA IBGE NOTÍCIAS. IBGE divulga as estimativas da população dos municípios para 2019 | Agência de Notícias. Agência de Notícias - IBGE. 2019. Disponível em: <https://agenciadenoticias.ibge.gov.br/agencia-sala-de-imprensa/2013-agencia-de-noticias/releases/25278-ibge-divulga-as-estimativas-da-populacao-dos-municipios-para-2019>. Acesso em: 26 out. 2024.

5. CPTM (COMPANHIA PAULISTA DE TRENS METROPOLITANOS). Relatório Integrado da Administração CPTM 2019. São Paulo, 2019.

6. IBGE. Panorama do Censo 2022. Panorama do Censo 2022. 2022. Disponível em: <https://censo2022.ibge.gov.br/panorama/index.html?localidade=BR&tema=1>. Acesso em: 26 out. 2024.
   
7. CARVALHO, Leandro. Data Product Canvas: A practical framework for building high-performance data products. Medium, 22 jul. 2019. Disponível em: https://medium.com/@leandroscarvalho/data-product-canvas-a-practical-framework-for-building-high-performance-data-products-7a1717f79f0. Acesso em: 17 out. 2024.

8. GIBBONS, S. Journey Mapping 101. Disponível em: <https://www.nngroup.com/articles/journey-mapping-101/>. Acesso em: 25 out. 2024.

9.  INTERACTION DESIGN FOUNDATION. User stories. Disponível em: <https://www.interaction-design.org/literature/topics/user-stories>. Acesso em: 24 out. 2024.

10. ZUP. Técnica INVEST: como aplicar user stories em microsserviços. Disponível em: <https://zup.com.br/blog/tecnica-invest-user-stories-microsservicos>. Acesso em: 25 out. 2024.

11. NIELSEN NORMAN GROUP. Personas: A Study Guide. Nielsen Norman Group, 9 out. 2022. Disponível em: <https://www.nngroup.com/articles/personas-study-guide/>. Acesso em: 26 out. 2024.

12. FIVE ACTS. ETL: o que é, importância e como aplicar na sua estratégia BI. Disponível em: <https://www.fiveacts.com.br/etl>. Acesso em: 4 nov. 2024.12. LUCIDCHART.O que é wireframe?. 2022. Disponível em: <https://www.lucidchart.com/pages/pt/o-que-e-wireframe>. Acesso em: 29 out. 2024.

13. LUCIDCHART. Apresentação dos tipos de diagramas UML. 2020. Disponível em: <https://www.lucidchart.com/blog/pt/tipos-de-diagramas-UML#:~:text=O%20que%20%C3%A9%20UML%3F,de%20sistemas%20de%20software%20complexos.>. Acesso em: 29 out. 2024.

‌14. LUCIDCHART. Diagrama de componentes UML: o que é, como fazer e exemplos. 2024. Disponível em: <https://www.lucidchart.com/pages/pt/diagrama-de-componentes-uml#:~:text=O%20diagrama%20de%20componentes%20mostra,com%20o%20restante%20do%20sistema.>. Acesso em: 29 out. 2024.

‌15. Estúdio Durer. **O que é Menu Hambúrguer?** Disponível em: <https://blog.estudiodurer.com.br/glossario/o-que-e-menu-hamburguer/>. Acesso em: 08 nov. 2024.

16. Fidelizarte. **Menu Hambúrguer: Vantagens e Desvantagens**. Disponível em: <https://www.fidelizarte.pt/blog/menu-hamburguer/>. Acesso em: 08 nov. 2024.

17. Google Developers. **Color Contrast Accessibility**. Disponível em: <https://codelabs.developers.google.com/color-contrast-accessibility?hl=pt-br>. Acesso em: 08 nov. 2024.

18. Carroll, A. B. The pyramid of corporate social responsibility: Toward the moral management of organizational stakeholders. Business Horizons, 1991. Disponível em: https://www.sciencedirect.com/science/article/abs/pii/000768139190005G. Acesso em: 12 nov. 2024.

19. Brasil. Lei Geral de Proteção de Dados Pessoais (LGPD), Lei nº 13.709, de 14 de agosto de 2018. Disponível em: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm. Acesso em: 12 nov. 2024.

20. United Nations. Transforming our world: The 2030 Agenda for Sustainable Development. 2015. Disponível em: https://sustainabledevelopment.un.org/post2015/transformingourworld. Acesso em: 12 nov. 2024.

20. ZWITTER, A. Big Data Ethics. 2014. Disponível em: https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID2384174_code400644.pdf?abstractid=2384174&mirid=1. Acesso em: 13 nov. 2024.

21. O'Neil, C. Weapons of Math Destruction: How Big Data Increases Inequality and Threatens Democracy. Crown Publishing Group, 2016.

22. Noble, S. U. Algorithms of Oppression: How Search Engines Reinforce Racism. NYU Press, 2018.

23. Barocas, S., Hardt, M., & Narayanan, A. Fairness and Machine Learning: Limitations and Opportunities. MIT Press, 2019.

24. BRASIL. Lei nº 13.709, de 14 de agosto de 2018. Lei Geral de Proteção de Dados Pessoais (LGPD). Disponível em: http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/L13709.htm. Acesso em: 14 nov. 2024.

25. MENDES, Liliana. Ética e Big Data: Governança de Dados e os Desafios do Consentimento Informado. Revista Brasileira de Ciência da Informação, 2018. Disponível em: https://www.scielo.br/j/pci/a/HhLyd6FMjFrf6hjHnfdH8GR/. Acesso em: 14 nov. 2024.

26. CPTM – Companhia Paulista de Trens Metropolitanos. Política de Proteção de Dados Pessoais. Disponível em: https://cptm.sp.gov.br/LGPD/Paginas/Politica-LGPD.aspx. Acesso em: 18 nov. 2024.

27. Prefect.io. Quickstart - Prefect. 2024. Disponível em: <https://docs.prefect.io/v3/get-started/quickstart>. Acesso em: 19 nov. 2024.

28. KIMBALL, Ralph; ROSS, Margy. The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling. 2. ed. New York: Wiley, 2002.

29. DEVMEDIA. Conceitos e criação de views no SQL Server. Disponível em: https://www.devmedia.com.br/conceitos-e-criacao-de-views-no-sql-server/22390. Acesso em: 22 nov. 2024.

30. DATACOSMOS. ClickHouse: solução de banco de dados para grandes volumes e alto desempenho. Disponível em: https://www.datacosmos.com.br/post/clickhouse-solu%C3%A7%C3%A3o-de-banco-de-dados-para-grandes-volumes-e-alto-desempenho. Acesso em: 22 nov. 2024.

31. Aero Engenharia. O que é: Cubo de Dados. Disponível em: <https://aeroengenharia.com/glossario/o-que-e-cubo-de-dados/>. Acesso em: 13 nov. 2024. 

32. RD Station. Confira um guia sobre MVP – Minimum Viable Product. Disponível em: https://www.rdstation.com/blog/marketing/mvp-minimo-produto-viavel/. Acesso em: 22 nov. 2024.

33. GLASSDOOR. Product Owner Salários. Disponível em: <https://www.glassdoor.com.br/Salários/product-owner-salário-SRCH_KO0,13.htm>. Acesso em: 22 nov. 2024.

34. GLASSDOOR. Scrum Master Salários. Disponível em: <https://www.glassdoor.com.br/Salários/scrum-master-salário-SRCH_KO0,12.htm>. Acesso em: 22 nov. 2024.

35. GLASSDOOR. Desenvolvedor Sênior Salários. Disponível em: <https://www.glassdoor.com.br/Salários/desenvolvedor-senior-salário-SRCH_KO0,20.htm>. Acesso em: 22 nov. 2024.

36. GLASSDOOR. Engenheiro de Dados Salários. Disponível em: <https://www.glassdoor.com.br/Salários/engenheiro-de-dados-salário-SRCH_KO0,19.htm>. Acesso em: 22 nov. 2024.

37. GLASSDOOR. Analista de Dados Salários. Disponível em: <https://www.glassdoor.com.br/Salários/analista-de-dados-salário-SRCH_KO0,17.htm>. Acesso em: 22 nov. 2024.

38. GLASSDOOR. Engenheiro de Software Salários. Disponível em: <https://www.glassdoor.com.br/Salários/engenheiro-de-software-salário-SRCH_KO0,22.htm>. Acesso em: 22 nov. 2024.

39. ÉPOCA NEGÓCIOS. Custo de trabalhador é de até 183% do salário, diz FGV. Disponível em: <https://epocanegocios.globo.com/Informacao/Resultados/noticia/2012/05/custo-de-trabalhador-e-de-ate-183-do-salario-diz-fgv.html>. Acesso em: 26 nov. 2024.

40. ABEPro. (2021). Impactos na fidelização e percepção da marca em serviços públicos. Disponível em: https://abepro.org.br/biblioteca/TN_STO_345_1773_40343.pdf. Acesso em: 5 dez. 2024.

41. CARLOS, Jean. CPTM registrou R$ 282 milhões de lucro bruto em 2021. 2022. Disponível em: <https://www.metrocptm.com.br/cptm-registrou-r-282-milhoes-de-lucro-bruto-em-2021/>. Acesso em: 26 nov. 2024.

42. Damodaran, A. (2012). Investment Valuation: Tools and Techniques for Determining the Value of Any Asset. Wiley Finance.

43. Metro Magazine. (2024). A look at the MTA’s strategy to improve NYC subway service. Disponível em: https://www.metro-magazine.com/10033683/a-look-at-the-mtas-strategy-to-improve-nyc-subway-service. Acesso em: 5 dez. 2024.

44. Maryland Transit Administration (MTA). (2024). Customer Experience Dashboard. Disponível em: https://www.mta.maryland.gov/customer-experience-dashboard. Acesso em: 5 dez. 2024.
  
45. ALVES, E. C.; AQUINO, M. A. A pesquisa qualitativa: origens, desenvolvimento e utilização nas dissertações do PPGCI/UFPB - 2008 a 2012. 2012. Disponível em: https://edisciplinas.usp.br/pluginfile.php/4580948/mod_folder/content/0/Metodologia%20de%20Pesquis_CHIZOTTI.pdf. Acesso em: 04 dez. 2024.

46. IRON CARROT. What is a Data Governance Communications Plan, and How do I create one? Disponível em: <https://ironcarrot.com/what-is-a-data-governance-communications-plan/>. Acesso em: 28 nov. 2024.

47. BRANDÃO, Afonso. Gestão de Stakeholders - Módulo 7 SI. Disponível em: <https://afonsobrandaointeli.github.io/modulo7si/06stakeholders/>. Acesso em: 2 dez. 2024.

# <a id="c15"></a> 15. Anexos

ANEXO A - [CALCULADORA DE PREÇOS DA AWS](../assets/anexos/My_Estimate_Calculadora_de_Preços_da_AWS.pdf)

ANEXO B - [Pesquisa](../assets/anexos/Pesquisa_Infografico.pdf)

ANEXO C - [Infográfico](../assets/anexos/Pesquisa_Infografico.pdf)

ANEXO D - [Análise Financeira e Plano de Comunicação](../assets/anexos/AnaliseFinanceira_PlanoDeComunicacaoDoProjeto.pdf)