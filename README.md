# 📚 Livraria API

API REST de e-commerce de livros com autenticação JWT, gerenciamento de catálogo, controle de estoque e pedidos.

Desenvolvida com **Django** e **Django REST Framework**, com documentação automática via **OpenAPI/Swagger**.

! O Categorias foi usado como estudo do funcionamento do Django, pode ser observado views com ClassBased, APIView e posteriormente o ModelViewSet

---

## 🚀 Stack

- Python 3
- Django
- Django REST Framework
- SimpleJWT (autenticação JWT)
- drf-spectacular (Swagger / OpenAPI)
- SQLite (ambiente de desenvolvimento)

---

## ⚙️ Funcionalidades

- Autenticação com JWT
- CRUD completo de livros
- Controle de estoque
- Gestão de pedidos
- Permissões por usuário
- Documentação automática da API

---

## 🧱 Entidades principais

- Livro
- Usuário
- Compra / Pedido
- Itens da compra
- Estoque

---
👥 Configuração de Grupos e Permissões

Este projeto utiliza o sistema de grupos e permissões do Django para controle de acesso.
Após clonar o projeto, é necessário criar manualmente os grupos no painel administrativo.

📌 Passos

Crie um superusuário:
python manage.py createsuperuser

Inicie o servidor:
python manage.py runserver

Acesse o admin:
http://127.0.0.1:8000/admin/

---
## 🔐 Autenticação

A API utiliza **JWT (JSON Web Token)**.

### Obter token
POST `/api/token/`

### Atualizar token
POST `/api/token/refresh/`

### Header de autenticação
