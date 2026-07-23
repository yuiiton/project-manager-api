# Project Manager API

Uma API REST desenvolvida com **FastAPI** para gerenciamento de projetos. A aplicação oferece operações de cadastro, consulta, atualização e remoção de projetos, seguindo uma arquitetura em camadas que favorece organização, manutenção e evolução do código.

O projeto é desenvolvido de forma incremental, adotando práticas e ferramentas amplamente utilizadas no desenvolvimento de APIs modernas em Python.

---

## ✨ Objetivos

* Implementar uma API REST utilizando FastAPI.
* Aplicar uma arquitetura em camadas com separação de responsabilidades.
* Manter uma base de código organizada, legível e de fácil manutenção.
* Evoluir continuamente a aplicação com ferramentas e práticas comuns em projetos reais.

---

## 🚀 Funcionalidades

Atualmente, a API oferece:

* Cadastro de projetos
* Listagem de projetos
* Consulta de um projeto por ID
* Atualização de projetos
* Exclusão de projetos
* Validação de dados de entrada
* Tratamento de erros com respostas padronizadas
* Persistência em banco de dados SQLite

---

## 📌 Endpoints

| Método   | Endpoint         | Descrição                   |
| -------- | ---------------- | --------------------------- |
| `POST`   | `/projects`      | Cria um novo projeto        |
| `GET`    | `/projects`      | Lista todos os projetos     |
| `GET`    | `/projects/{id}` | Obtém um projeto específico |
| `PUT`    | `/projects/{id}` | Atualiza um projeto         |
| `DELETE` | `/projects/{id}` | Remove um projeto           |

A documentação interativa é gerada automaticamente pelo FastAPI através do Swagger UI e ReDoc.

---

## 🏗️ Arquitetura

A aplicação segue uma arquitetura em camadas, onde cada parte possui uma responsabilidade bem definida.

```text
Controller
    │
    ▼
Service
    │
    ▼
Repository
    │
    ▼
Database
```

### Controller

Responsável por expor os endpoints da API, receber as requisições HTTP e encaminhá-las para a camada de serviço.

### Service

Implementa as regras de negócio da aplicação, realiza validações e coordena o fluxo das operações.

### Repository

Centraliza o acesso aos dados, realizando operações de leitura, escrita, atualização e remoção no banco de dados.

### Models e Schemas

* **Models** representam as entidades persistidas utilizando SQLModel.
* **Schemas** definem os contratos de entrada e saída da API através do Pydantic.

---

## 🗄️ Modelo de dados

Cada projeto possui os seguintes atributos:

| Campo          | Descrição           |
| -------------- | ------------------- |
| `id`           | Identificador único |
| `name`         | Nome do projeto     |
| `description`  | Descrição           |
| `status`       | Status do projeto   |
| `priority`     | Prioridade          |
| `created_at`   | Data de criação     |
| `completed_at` | Data de conclusão   |

---

## 🛠️ Tecnologias

* Python 3.11
* FastAPI
* SQLModel
* Pydantic
* SQLite
* Uvicorn
* Docker
* Docker Compose

---

## 📁 Estrutura do projeto

```text
project-manager-api/
├── controller/         # Endpoints da aplicação
├── core/               # Configurações, exceções e utilitários
├── data/               # Banco SQLite
├── models/             # Modelos SQLModel
├── repository/         # Acesso aos dados
├── schemas/            # Schemas de entrada e saída
├── services/           # Regras de negócio
├── main.py             # Inicialização da aplicação
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

---

## ▶️ Executando o projeto

### Com Docker Compose

```bash
docker compose up --build
```

A aplicação ficará disponível em:

* API: http://localhost:8000
* Swagger UI: http://localhost:8000/docs
* ReDoc: http://localhost:8000/redoc

### Executando localmente

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

---

## 🧪 Próximas evoluções

O desenvolvimento da aplicação continuará incorporando melhorias de arquitetura, infraestrutura e qualidade de código.

### Planejado

* [x] CRUD de projetos
* [x] Persistência com SQLite
* [x] Docker
* [x] Docker Compose
* [ ] Suporte ao PostgreSQL
* [ ] Migrações com Alembic
* [ ] Testes automatizados com Pytest


