FROM python:3.10-alpine3.17
WORKDIR /app/
ADD ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
ADD ./quotes_to_scrape ./quotes_to_scrape
CMD ["scrapy", "crawl", "quote", "-O ./output/json_files/quote_infos.json"]