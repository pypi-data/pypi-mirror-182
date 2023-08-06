from typing import Dict

from bs4 import BeautifulSoup
from requests_html import HTMLSession


class Scraper:
    def __init__(self):
        super().__init__()
        self._session = HTMLSession()
        self._url = None
        self._soup = None
        self._search_settings = dict()

    @property
    def search_settings(self) -> Dict:
        return self._search_settings

    def set_search_settings(self, **kwargs):
        for k, v in kwargs.items():
            self._search_settings.update({k: v})

    @property
    def url(self) -> str:
        return self._url

    @url.setter
    def url(self, url: str):
        self._url = url
        self._soup = None

    @property
    def soup(self) -> BeautifulSoup:
        if self._soup is None:
            sess = self._session.get(self._url)
            self._soup = BeautifulSoup(
                sess.text,
                "html.parser",
            )
        return self._soup
