# Flask Data Processing API

API desenvolvida em Flask para demonstrar processamento de dados com Pandas,
organização em camadas e exposição de métricas via endpoints REST.

## Tecnologias
- Python
- Flask
- Pandas
- SQLAlchemy
- SQLite

## Endpoints
### POST /upload
Recebe um arquivo CSV com as colunas:
- category
- value

### GET /metrics
Retorna dados agregados processados.

### GET /health
Health check da aplicação.

## Arquitetura
- Routes: controle de requisições
- Services: regras de negócio
- Repositories: persistência
- Utils: processamento com Pandas
