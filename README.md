# Trello Redmine Connection

Aplicação para a conexão do Redmine com o Trello e criação automatizada de cards a partir de issues.

## Como rodar

Primeiramente é necessário ter uma chave e um token do trello, caso tenha dificuldade em gera-los, veja a [documentação da API do trello](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/).

Tambem é necessário ter a chave de acesso a API do Redmine, para acessa-la vá em **Minha Conta > Chave de acesso à API** e clique em **Exibir** .

Já tendo o token e as chaves necessárias, descubra, navegando pela API do trello, o id da lista onde quer que o card seja criado.

Adicione todas essas chaves e ids a um arquivo `.env` na raiz do projeto. Adicione também as informações para acesso ao banco de dados. Siga o formato:

```
TRELLO_TOKEN=[Token para conexão com a API do Trello]
TRELLO_KEY=[Chave para conexão com a API do Trello]
TRELLO_CARD_LIST=[ID da lista onde o card será criado]

REDMINE_KEY=[Chave para conexão com a API do Redmine]

POSTGRES_USER=[Usuário do banco de dados]
POSTGRES_PASSWORD=[Senha do banco de dados]
POSTGRES_DB=db
POSTGRES_PORT=5432
POSTGRES_HOST=database
```

Com todas as variaveis de ambiente salvas, rode a aplicação utilizando o comando abaixo:

``` sh
docker-compose up
```
