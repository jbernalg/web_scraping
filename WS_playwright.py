# librerias
import asyncio
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright


async def main():
    # definir url
    url =  'https://quotes.toscrape.com/scroll'

    # inicio de interaccion
    async with async_playwright() as p:

        # lanzar navegador
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        # obtener la pagina
        page = await context.new_page()

        # pasar url a la pagina
        await page.goto(url)
        # esperar 3 segundos
        await page.wait_for_timeout(3000)

        # obtener el HTML de la pagina renderizada
        html = await page.content()
        # cerrar el navegador
        await browser.close()

        # Procesar con beautifulSoup
        soup = BeautifulSoup(html, 'html.parser')
        quotes = soup.select('div.quote')

        print('Citas encontradas: ', len(quotes))
        for quote in quotes:
            text = quote.find('span', class_='text').get_text()
            autor = quote.find('small', class_='author').get_text()
            print(f'{text} - {autor}')

# Ejecutar el script
asyncio.run(main())
