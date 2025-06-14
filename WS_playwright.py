# librerias
import asyncio
from bs4 import BeautifulSoup
from playwrigt.async_api import async_playwright


async def main():
    # definir url
    url =  'https://quotes.toscrape.com/scroll'

    