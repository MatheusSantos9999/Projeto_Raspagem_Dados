# Promoções de Jogos — eShop Prices

## Sobre o projeto

Este projeto tem como objetivo **coletar informações de jogos que estão em promoção no site eShop Prices**, utilizando web scraping.

A aplicação acessa a página de promoções, identifica os jogos disponíveis com desconto e extrai informações como:

* Nome do jogo;
* Menor preço global encontrado pelo site;
* Porcentagem de desconto.

O preço exibido em reais **não representa necessariamente o preço praticado na loja brasileira**. O site utilizado como fonte apresenta o menor preço encontrado globalmente e, quando a moeda BRL é utilizada, esse valor é convertido para reais.

Dessa forma, o projeto funciona como uma ferramenta para **acompanhar jogos em promoção e seus menores preços globais**, e não como uma consulta direta aos preços da eShop brasileira.

## Fluxo do projeto

O funcionamento do projeto pode ser resumido da seguinte forma:

```text
Acesso ao eShop Prices
        ↓
Coleta do HTML da página
        ↓
Localização dos jogos em promoção
        ↓
Extração do menor preço global
        ↓
Conversão/apresentação em BRL
        ↓
Exibição dos resultados
```

### 1. Acesso ao site

A aplicação começa realizando uma requisição HTTP para o eShop Prices utilizando a biblioteca `requests`.

A URL utilizada configura a moeda da página como BRL. Entretanto, essa configuração **não significa que o preço coletado seja o preço da loja brasileira**. O site continua fornecendo o menor preço global disponível e apresenta esse valor convertido para a moeda selecionada.

### 2. Coleta e interpretação do HTML

Depois de obter a página, o conteúdo HTML é processado utilizando `BeautifulSoup`.

A aplicação procura pelos elementos correspondentes aos jogos e identifica aqueles que possuem informações de promoção.

São extraídos principalmente:

* Nome do jogo;
* Percentual de desconto;
* Preço apresentado pelo site.

O código também utiliza expressões regulares para identificar os valores de desconto e preço dentro do HTML.

### 3. Menor preço global

Um ponto importante sobre os dados coletados é a origem do preço.

O valor obtido pelo projeto corresponde ao **menor preço global identificado pelo eShop Prices**, e não necessariamente ao preço disponível para compra no Brasil.

Por exemplo, se um jogo estiver sendo vendido por:

```text
EUA: US$ 20
Japão: ¥ 2.000
Brasil: R$ 150
```

o site pode identificar uma dessas regiões como possuindo o menor preço global. Ao utilizar BRL como moeda de apresentação, o valor correspondente será convertido para reais.

Assim, um resultado como:

```text
R$ 100,00
```

não deve ser interpretado automaticamente como:

> "O jogo custa R$ 100,00 na eShop brasileira."

A interpretação correta é:

> "O menor preço global identificado pelo site corresponde aproximadamente a R$ 100,00 após a conversão para BRL."

### 4. Organização dos dados

Depois da extração, os dados são organizados em uma lista de dicionários contendo informações sobre cada promoção.

A estrutura segue aproximadamente este formato:

```python
{
    "nome": "Nome do jogo",
    "preco": "R$ 99,90",
    "desconto": "-50%"
}
```

O código também mantém um controle das URLs já processadas para evitar que o mesmo jogo seja adicionado mais de uma vez.

### 5. Exibição dos resultados

Por fim, as promoções encontradas são exibidas no terminal, apresentando o nome do jogo, o preço convertido para BRL e o percentual de desconto.

Exemplo:

```text
=== Promoções encontradas na eShop ===

Nome do jogo
R$ 99,90 (-50%)

Outro jogo
R$ 79,90 (-30%)
```

Os valores devem ser interpretados como **preços globais convertidos para BRL**, e não necessariamente como preços praticados no mercado brasileiro.

## Estrutura do projeto

```text
.
├── promos_eshop.py
├── requirements.txt
└── .gitignore
```

### `promos_eshop.py`

Arquivo principal da aplicação. Contém a lógica responsável por:

* Realizar a requisição ao site;
* Processar o HTML;
* Encontrar os jogos em promoção;
* Extrair os dados disponibilizados pelo site;
* Evitar resultados duplicados;
* Exibir as promoções no terminal.

### `requirements.txt`

Contém as dependências necessárias para executar o projeto.

Entre elas estão:

* `requests` — realização das requisições HTTP;
* `beautifulsoup4` — interpretação e extração de informações do HTML.

### `.gitignore`

Responsável por impedir que arquivos gerados pelo ambiente Python sejam adicionados ao controle de versão, como:

* `venv/`;
* `.venv/`;
* `__pycache__/`;
* arquivos `.pyc`.

## Tecnologias utilizadas

* **Python**
* **Requests**
* **BeautifulSoup 4**
* **Regex**
* **Web Scraping**

## Como executar

Crie e ative um ambiente virtual:

```bash
python -m venv venv
```

No Windows:

```bash
venv\Scripts\activate
```

No Linux/macOS:

```bash
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o programa:

```bash
python promos_eshop.py
```

O programa realizará a requisição ao eShop Prices, processará os dados disponíveis na página e exibirá as promoções encontradas.

## Limitações

A principal limitação atual está relacionada à origem do preço.

O projeto **não consulta diretamente o preço da eShop brasileira**. Ele depende das informações disponibilizadas pelo eShop Prices e utiliza o menor preço global encontrado pelo serviço.

Além disso, como a aplicação depende da estrutura HTML do site, alterações futuras na página podem exigir mudanças nos seletores e nas expressões utilizadas para localizar os dados.

## Objetivo do projeto

O projeto foi desenvolvido como uma aplicação prática para estudar e aplicar conceitos de:

* Python;
* Requisições HTTP;
* Web scraping;
* Processamento de HTML;
* Expressões regulares;
* Tratamento de erros;
* Organização e filtragem de dados.

A proposta é automatizar a coleta de informações sobre jogos em promoção e facilitar a visualização dos **menores preços globais encontrados pelo eShop Prices**.
