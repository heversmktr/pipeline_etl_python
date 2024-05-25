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
 

 ### Créditos 
Esse projeto foi feito com base no que foi ensinado no Workshop __Pipeline ETL com Python do Zero__ ministrado por Luciano Vasconcelos https://www.linkedin.com/in/lucianovasconcelosf/ <br>
Deixo os meus agradecimentos por ter compartilhado seu conhecimento de forma muito didática.