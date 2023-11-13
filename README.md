# Beemon
## Visão geral do projeto

Este é um projeto que usa Scrapy, Splash, MongoDB e Docker.

É uma stack moderna utilizada para se fazer raspagem de dados de páginas especificadas.

## Preview

O objetivo é vasculhar o site [Quotes to Scrape](https://quotes.toscrape.com/), estruturar seus dados e salvá-los em banco não relacional, porém, de forma que não seja custoso ao banco.

## Começando

Para iniciar o projeto, siga os passos abaixo:

- Clone o repositório em sua máquina local.
- Instale docker localmente
- Rode o comando `docker compose up --build`

## Estrutura de pasta

```
├── output                        # Pasta com dados de saída
│   ├── json_files                # Pasta com dados estruturados da página-alvo
│   ├── logs                      # Pasta com logs de execução do crawler
│   └── screenshots               # Pasta com provas de consulta
├── quotes_to_scrape              # Pasta raiz do Scrapy
|   ├── spiders                   # Pasta com os crawlers
|   |   └── quote_spider.py       # Crawler principal do projeto
│   ├── items.py                  # Estruturação do item gerado pela spider
│   ├── middleware.py             # Funcionalidades customizadas para as spiders
│   ├── pipelines.py              # Arquivo de sequência de execução do crawler
│   └── settings.py               # Configurações do projeto
├── docker-compose.yaml           # Serviços a serem gerados dentro de container docker
├── Dockerfile                    # Comando de estruturação de container docker
├── requirements.txt              # Biblioteca / dependências do projeto
└── scrapy.cfg                    # Configurador da biblioteca Scrapy
```

## Tecnologias e funcionalidades

### Tecnologias

O projeto inclui as seguintes tecnologias:

- Scrapy: Definição e gerenciamento de crawlers para extração de dados da página-alvo
- Splash: Gerar a captura de provas de consulta (screenshot)
- MongoDB: Armazenamento de dados estruturados em formato JSON
- Docker: Container para a aplicação, para que haja uma padronização do projeto independente da máquina utilizada

### Funcionalidades

O projeto possui as seguintes funcionalidades:

- Gerar um crawler que acesse o site [Quotes to Scrape](https://quotes.toscrape.com/)
- Estruturar os dados de retorno
- Capturar foto a cada página que o crawler passar
- Gerar dados de saída (json, log, screenshot)
- Salvar as informações em um banco não relacional (MongoDB)

## Scripts

O projeto inclui os seguintes scripts:

`docker compose build`: Gera a imagem do container com os serviços indicados no `docker-compose.yaml`
`docker compose up`: Sobe a imagem gerada pelo build
`docker compose up --build`: Realiza as duas tarefas anteriores de uma única vez

## Decisões técnicas

### Scrapy

- Uma biblioteca atual com ótima performance e fácil usabilidade para se realizar raspagem de dados em sites
- No projeto atual, os arquivos `log`, `json` e `png` estão sendo sobrescritos, a fim de evitar diversos arquivos e para melhor testar a aplicação. Se considerada uma aplicação, os logs não seriam sobrescritos e formariam um histórico, com um tempo de vida pré definido, sendo salvos no S3

### Splash

- Biblioteca recomendada pelo Scrapy para se realizar a captura de screenshots

### MongoDB

- Banco não relacional, somente para a persistência de dados JSON

## Referências

### Scrapy

- [Funcionamento básico do scrapy](https://www.digitalocean.com/community/tutorials/como-fazer-crawling-em-uma-pagina-web-com-scrapy-e-python-3-pt)
- [Padronização de retornos](https://docs.scrapy.org/en/latest/topics/item-pipeline.html#write-items-to-a-json-lines-file)
- [Padronização de retornos](https://www.youtube.com/watch?v=ALizgnSFTwQ)
- [Logs](https://docs.scrapy.org/en/latest/topics/logging.html)

### Splash

- [Splash no Docker](https://scrapeops.io/python-scrapy-playbook/scrapy-splash/)
- [Recomendação do Scrapy](https://docs.scrapy.org/en/latest/topics/item-pipeline.html#take-screenshot-of-item)
- [Uso de render.json para extração de HTML e de PNG](https://stackoverflow.com/questions/45172260/scrapy-splash-screenshots)

### MongoDB

- [Insert item to MongoDB](https://docs.scrapy.org/en/latest/topics/item-pipeline.html#write-items-to-mongodb)

## Melhorias futuras

- Trazer resultados de forma dinamica sem fixar caminhos no xpath
- Fazer um dataframe que possibilite visualizar os resultados via pandas
- Conseguir agendar uma execução para um dia e horario
- Manutenção de histórico de arquivos `log`, `json` e `png`
