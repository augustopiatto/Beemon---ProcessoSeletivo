FROM python:3.10-alpine3.17
WORKDIR /code/
ADD ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
CMD ["scrapy", "crawl", "quote", "-O ./quotes_to_scrape/json_files/quote_infos.json"]