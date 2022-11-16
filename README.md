# TP Youtube Scraper


## Comment lancer le script:

Dans un terminal, exécutez les commandes suivantes:  

``python3.8 -m venv .venv``  
``source .venv/bin/activate``   
``pip install --upgrade pip``    
``python scraper.py --input input.json --output.json``  


## Comment exécuter les tests unitaires:

Dans un terminal, exécutez la commande suivante:

``python -m pytest test_scraper.py``

## Obtenir le coverage:

Toujours dans un terminal, exécutez la commande suivante:

``pytest --cov=. test_scraper.py``

Le taux de couverture global est de 79%
