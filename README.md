# pipeline_etl_python

### Para rodar o web scraping:
Dentro da pasta __spiders__ (src/coleta/coleta/spiders) execute o comando abaixo:

```bash
scrapy crawl mercadolivre -o ../../data/data.jsonl
```
### Para transformar os dados execute o comando dentro da pasta __src__: 
```bash
python transformacao/main.py
```

### Para rodar o Streamlit e gerar o dashboard execute dentro da pasta __src__:

```bash
streamlit run dashboard/app.py 
```

### Sugestões de melhorias: 
 - Refinar o método de web scraping, para deixar de confundir o preço atual do produto com o valor da parcela 
 