# 🚀 Projeto Docker Compose - API com Banco de Dados

## 📌 Descrição

Este projeto consiste em uma aplicação utilizando **Docker Compose** com múltiplos containers:

* 🖥️ Container da aplicação (API)
* 🗄️ Container do banco de dados

A aplicação permite o gerenciamento de usuários através de uma API REST.

---

## 🛠️ Tecnologias utilizadas

* Python (FastAPI)
* MySQL
* Docker
* Docker Compose

---

## 📁 Estrutura do projeto

```
projeto-docker/
│
├── docker-compose.yml
├── app/
│   └── (código da API)
└── README.md
```

---

## 🚀 Como executar o projeto

### ✅ Pré-requisitos

* Docker instalado
* Docker Desktop em execução

---

### ▶️ Passo a passo

1. Acesse a pasta do projeto:

```
cd projeto-docker
```

2. Execute o Docker Compose:

```
docker compose up --build
```

---

## 🌐 Acessando a aplicação

Após subir os containers, acesse:

* API: http://localhost:8000
* Documentação (Swagger): http://localhost:8000/docs

---

## 🧪 Endpoints disponíveis

* GET /usuarios → Lista todos os usuários
* GET /usuarios/{id} → Busca usuário por ID

---

## 🛑 Parar a aplicação

Para parar os containers:

```
CTRL + C
docker compose down
```

---

## 📌 Observações

* O banco de dados é iniciado automaticamente pelo Docker
* Os containers se comunicam entre si através da rede do Docker Compose

---

## 👨‍💻 Autor

Gabriel Buske Wolff
