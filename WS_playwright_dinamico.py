# librerias
import asyncio
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright

async def main():
    # definir url
    url =  'https://quotes.toscrape.com/scroll'
    # realizar scroll cada 2 segundos
    scroll_pause_time = 2

    # inicio de interaccion
    async with async_playwright() as p:

        # lanzar navegador
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        # obtener la pagina
        page = await context.new_page()
        # pasar url a la pagina
        await page.goto(url)

        # definir set para guardar frases
        quotes_set = set()
        # definir altura del scroll
        last_height = await page.evaluate('document.body.scrollHeight')

        # ejecutar 3 scroll
        for i in range(3):
            await page.evaluate('window.scrollTo(0, document.body.scrollHeight);')
            await page.wait_for_timeout(scroll_pause_time*1000)

            # extraer todas las frases actualmente visibles
            quote_elements = await page.query_selector_all('.quote')
            for quote in quote_elements:
                text_span = await quote.query_selector('.text')
                if text_span:
                    text = await text_span.inner_text()
                    quotes_set.add(text)

            # sistema de validacion del final del scroll
            new_weight = await page.evaluate('document.body.scrollHeight')
            if new_weight == last_height:
                break
            last_height = new_weight

        # cerrar navegador
        await browser.close()

    # mostrar frases cargadas
    print(f'Total de frases cargadas: {len(quotes_set)}')
    for quote in quotes_set:
        print(quote)

# Ejecutar script
asyncio.run(main())   