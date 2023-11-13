# Beemon
## Visão geral do projeto

Este é um projeto que usa Scrapy, MongoDB e Docker.

É uma stack moderna utilizada para se fazer raspagem de dados de páginas especificadas.

## Preview

O objetivo é vasculhar o site [Quotes to Scrape](https://quotes.toscrape.com/), estruturar seus dados e salvá-los em banco não relacional, comparando o último registro com os dados mais recentes e salvando a informação somente caso haja uma alteração, criando assim uma forma de histórico.

## Começando

Para iniciar o projeto, siga os passos abaixo:

- Clone o repositório em sua máquina local.
- a

## Estrutura de pasta

```
├── quotes_to_scrape              # Pasta principal
|   ├── spiders
|   |   └── quote_spider.py 
│   ├── items.py                  # Variáveis do banco RDS
│   ├── middleware.py             # Pasta com arquivos estáticos
│   ├── pipelines.py              # Pasta com as funções lambdas
│   └── settings.py               # Pasta com funções de suporte
└── scrapy.cfg                    # 
```

## Tecnologias e funcionalidades

### Tecnologias

O projeto inclui as seguintes tecnologias:

- 

### Funcionalidades

O projeto possui as seguintes funcionalidades:

- 

## Scripts

O projeto inclui os seguintes scripts:

``

## Decisões técnicas
log está sobrescrevendo para melhor testar, em aplicação real seria um histórico
json está sobrescrevendo para melhor testar, em aplicação real seria um histórico
### Scrapy

- 

### MongoDB

- 

## Referências

### Scrapy

- 

### MongoDB

- 

## Melhorias futuras

- 
