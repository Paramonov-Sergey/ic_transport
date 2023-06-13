from bs4 import BeautifulSoup

from core.config import settings
from utils.parsers.base_parser import BaseParser


class NewsParser(BaseParser):
    def __init__(self, html):
        self.parser = BeautifulSoup(html, 'html.parser')
        self.__data = []

    def parse(self):
        tables = self.parser.find_all('table', class_=False, id=False, style="font-family:Arial;font-size:15px")
        for table in tables:
            for tr in table.find_all('tr'):
                image = tr.find('img')
                header = tr.find_all('b')
                data = {
                    'url': f'{settings.NEWS_URI}/news/{image.get("src")}' if image else '',
                    'header': header[1].text if header else ''
                }
                self.__data.append(data)

    @property
    def data(self):
        return self.__data
