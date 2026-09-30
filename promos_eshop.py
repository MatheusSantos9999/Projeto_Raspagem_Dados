import re

import requests
from bs4 import BeautifulSoup

URL_ESHOP_SALES = "https://eshop-prices.com/?currency=BRL"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (compatible; MiniProjetoPromosEshop/1.0; "
        "uso pessoal e educacional)"
    )
}


def buscar_html():
    
    try:
        resposta = requests.get(URL_ESHOP_SALES, headers=HEADERS, timeout=10)
        resposta.raise_for_status()
        return resposta.text

    except requests.exceptions.Timeout:
        print("Erro: o site demorou demais para responder (timeout).")
    except requests.exceptions.ConnectionError:
        print("Erro: não foi possível conectar à internet ou ao site.")
    except requests.exceptions.HTTPError as erro:
        print(f"Erro: o site respondeu com um erro HTTP ({erro}).")
    except requests.exceptions.RequestException as erro:
        print(f"Erro inesperado ao tentar acessar o site: {erro}")

    return None

def extrair_promocoes(html):
    
    soup = BeautifulSoup(html, "html.parser")
    promocoes = []
    links_ja_vistos = set()

    
    links_jogos = soup.find_all("a", href=re.compile(r"/games/\d+-"))

    for link in links_jogos:
        href = link.get("href")

        if href in links_ja_vistos:
            continue

        texto_completo = link.get_text(" ", strip=True)

        desconto_encontrado = re.search(r"-(\d+)%", texto_completo)
        if not desconto_encontrado:
            continue  

        preco_encontrado = re.search(r"R\$\s?[\d.]*\d,\d{2}", texto_completo)
        if not preco_encontrado:
            continue

        img_tag = link.find("img")
        nome_jogo = img_tag.get("alt", "").strip() if img_tag else ""

        if not nome_jogo:
            nome_jogo = texto_completo.split(preco_encontrado.group(0))[0].strip()

        links_ja_vistos.add(href)
        promocoes.append({
            "nome": nome_jogo,
            "preco": preco_encontrado.group(0),
            "desconto": desconto_encontrado.group(0),
        })

    return promocoes

def mostrar_promocoes(promocoes):
    if not promocoes:
        print("Nenhuma promoção encontrada (ou não foi possível ler a página).")
        return

    print(f"=== {len(promocoes)} promoções encontradas na eShop (em R$) ===\n")
    for jogo in promocoes:
        print(f"{jogo['nome']}")
        print(f"{jogo['preco']} ({jogo['desconto']})")
        print()

def main():
    html = buscar_html()

    if html is None:
        return

    promocoes = extrair_promocoes(html)
    mostrar_promocoes(promocoes)


if __name__ == "__main__":
    main()

