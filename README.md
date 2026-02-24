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

## 🔐 Autenticação

A API utiliza **JWT (JSON Web Token)**.

### Obter token
POST `/api/token/`

### Atualizar token
POST `/api/token/refresh/`

### Header de autenticação
