FROM python:3.10
WORKDIR /quotes_to_scrape
ADD ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
CMD ["scrapy", "crawl quote -o quote.json"]
