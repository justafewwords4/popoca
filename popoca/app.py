import os

import typer
from fake_useragent import UserAgent
from rich import print

from .utils import FILE_TO_WORK, HOME_DIRECTORY, WORK_DIRECTORY

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])
app = typer.Typer(context_settings=CONTEXT_SETTINGS, no_args_is_help=True)

ua = UserAgent()


@app.command()
def init():
    """Función principal"""
    print("Función principal")
    print("Esta es la función principal")


@app.command()
def table(file: str = "") -> None:
    """Extrae la tablas de un pdf"""
    pdf = pdfplumber.open(FILE_TO_WORK)
    tables = pdf.pages[1].find_tables()
    print(tables[0].extract())
    print(tables[0].page)


@app.command()
def get() -> None:
    """automática"""
    url = "https://www.cenapred.unam.mx/reportesVolcanGobMX/"
    UA = str(ua.random)
    headers = {"User-Agent": UA}
    response = requests.get(url, headers=headers)
    print("imprime el texto")
    print(UA)
    print(response.links)


@app.command()
def wget() -> None:
    """wget"""
    UA = str(ua.random)
    url = "https://www.cenapred.unam.mx/reportesVolcanGobMX/BuscarReportesVolcan"
    UA = "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)"
    os.system(f"wget -U '{UA}' {url} -O reportes.html")


def run():
    app()


if __name__ == "__main__":
    run()
