# SmartShoppingCart
Challenge proposé par Eden AI

## Installation
### Prérequies
- Avoir cloné le repository
- Docker

### Etapes
- Créer un .env avec:
```
SECRET_KEY="MY KEY"
```
- Pour lancer le service et la base de donnée
```
docker-compose up -d
```
- ajouter les fixtures

```
docker-compose run web python manage.py loaddata cart/fixtures/product.json
docker-compose run web python manage.py loaddata cart/fixtures/discount.json
```

## ROUTES DISPONIBLES
### PRODUITS
- POST /products
- GET /products
- GET /products/{id}
- PUT /products/{id}
- PATCH /products/{id}
- DELETE /products/{id}

body de la requête POST
```
{
  "name": "product_name",
  "price": 1.0
}
```

### REMISES
- POST /discounts
- GET /discounts
- GET /discounts/{id}
- PUT /discounts/{id}
- PATCH /discounts/{id}
- DELETE /discounts/{id}

body de la requête POST
```
{
  "category": "one plus one",
}
```

### CALCUL
- POST /calculate

body de la requête :
```
{
    "product_name" : "PS5",
    "quantity" : 7,
    "discounts" : ["one plus one", "50 percent"]
}
```

resultat :
```
{
    "amount": 1393.2499999999995
}
```

## TESTS
- Lancer les tests
```
docker-compose run web python manage.py test
```
