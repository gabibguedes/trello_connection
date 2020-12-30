# Trello Connection

Aplicação para a conexão com o trello e criação automatizada de cards.

## Como rodar

Primeiramente é necessário ter uma chave e um token do trello, caso tenha dificuldade em gera-los, veja a [documentação da API do trello](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/).

Já tendo o token e a chave necessárias, descubra, navegando pela API do trello, o id da lista onde quer que  o card seja criado.

Adicione todas essas chaves a um arquivo `.env` na raiz do projeto. Siga o formato:

```
TOKEN=[Token para conexão com a API do Trello]
KEY=[Chave para conexão com a API do Trello]
CARD_LIST=[ID da lista onde o card será criado]
```

Com todas as variaveis de ambiente salvas, rode a aplicação utilizando o comando abaixo:

``` sh
docker-compose up
```
