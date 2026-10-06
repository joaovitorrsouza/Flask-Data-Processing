# Flask Data Processing API

API Back-End desenvolvida em **Python + Flask** para processamento de dados enviados por arquivo CSV.

O projeto foi estruturado com separação de responsabilidades entre rotas, serviços, repositórios e utilitários, com o objetivo de manter a aplicação organizada e facilitar manutenção e evolução.

## Stack

- Python
- Flask
- Pandas
- SQLAlchemy
- SQLite
- Docker

## Funcionalidades

- upload de arquivo CSV
- processamento de dados com Pandas
- persistência utilizando SQLAlchemy
- exposição de métricas agregadas por API REST
- health check da aplicação

## Formato do CSV

O endpoint de upload espera um arquivo contendo as colunas:

```text
category,value
```

## Endpoints

### `POST /upload`

Recebe o arquivo CSV para processamento.

### `GET /metrics`

Retorna métricas agregadas a partir dos dados processados.

### `GET /health`

Verifica a disponibilidade da aplicação.

## Arquitetura

```text
app/
├── models/
├── repositories/
├── routes/
├── services/
└── utils/
```

A organização segue a separação de responsabilidades:

- **Routes:** entrada das requisições e respostas HTTP
- **Services:** regras de negócio
- **Repositories:** persistência e acesso a dados
- **Models:** representação dos dados
- **Utils:** processamento e transformação com Pandas

## Estrutura do repositório

```text
flask-data-processing-api/
├── app/
├── instance/
├── database.db
├── dockerfile
├── run.py
└── README.md
```

## Execução local

Entre na pasta do projeto:

```bash
cd flask-data-processing-api
```

Crie um ambiente virtual e instale as dependências utilizadas pela aplicação conforme seu ambiente Python.

Depois, execute:

```bash
python run.py
```

## Docker

O repositório também contém um Dockerfile para execução da aplicação em ambiente containerizado.

## O que este projeto demonstra

- desenvolvimento Back-End com Flask
- processamento de dados com Pandas
- criação de endpoints REST
- persistência com SQLAlchemy
- organização em camadas
- separação de responsabilidades
- containerização
