# Notes - API
## Introdução
...
## Refêrencias

Este projeto foi desenvolvido usando as seguintes tecnologias:
- [Python](https://www.python.org/downloads/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [Sqlalchemy](https://sqlalchemy.org/)
## Configurando o projeto:

Clone o repositorio para o seu ambiente local
```bash
git clone https://github.com/wlribeiro/notes-api.git
```

Em seguida execute o comando para instalar as dependencias:
```bash
make install
```

### Rodando o projeto

### Migrations
Você precisa rodar o comando de migração para criar as tabelas necessarias no banco de dados
```bash
make migrate
```
### Iniciando a api
Execute o comando para iniciar o servidor da api na porta 8000:
```bash
make run
```
