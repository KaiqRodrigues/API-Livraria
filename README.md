📚 Livraria API
API REST de e-commerce de livros com autenticação JWT, gerenciamento de catálogo, controle de estoque e pedidos.
Desenvolvida com Django e Django REST Framework, com documentação automática OpenAPI.
________________________________________
🚀 Stack
•	Python 3
•	Django
•	Django REST Framework
•	SimpleJWT (JWT Auth)
•	drf-spectacular (Swagger / OpenAPI)
•	SQLite (ambiente de desenvolvimento)
________________________________________
⚙️ Funcionalidades
•	Autenticação com JWT
•	CRUD de livros
•	Controle de estoque
•	Gestão de pedidos
•	Permissões por usuário
•	Documentação automática da API
________________________________________
🧱 Entidades principais
•	Livro
•	Usuário
•	Compra / Pedido
•	Itens da compra
•	Estoque
________________________________________
🔐 Autenticação
A API utiliza JWT (JSON Web Token).

Obter token
POST /api/token/
Atualizar token
POST /api/token/refresh/
Header de autenticação
Authorization: Bearer <seu_token>

________________________________________
📑 Documentação da API

A API possui documentação interativa via Swagger.
Acesse localmente:
exemplo: http://127.0.0.1:8000/swagger/


