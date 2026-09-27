# Project Manager API

API REST desenvolvida em Python com FastAPI para gerenciamento de projetos. A aplicação oferece CRUD completo de projetos com validações, status e prioridade, além de tratamento padronizado de erros.

---

## Visão geral

A estrutura atual do projeto foi organizada para seguir uma visão em camadas mais próxima do domínio da aplicação:

- `main.py`: inicialização da aplicação FastAPI e registro dos routers.
- `project/`: módulo principal do domínio de projetos.
- `core/`: configuração, banco de dados, utilitários e tratamento de exceções.
- `tests/`: validações de schema e regras de negócio.

---

## Estrutura atual

```text
project-manager-api/
├── main.py
├── Dockerfile
├── docker-compose.yml
├── alembic.ini
├── requirements.txt
├── .env.example
├── alembic/
│   ├── versions/
├── core/
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   └── exceptions/
│       ├── __init__.py
│       ├── commom_exceptions.py
│       └── handlers.py
├── project/
│   ├── __init__.py
│   ├── controller.py
│   ├── model.py
│   ├── repository.py
│   ├── schema.py
│   └── service.py
├── tests/
│   ├── conftest.py
│   └── schemas/
│       ├── test_projectcreate.py
│       └── test_projectupdate.py
└── README.md
```

### Organização por módulo

#### `project/`

Contém a lógica do domínio de projetos:

- `controller.py`: endpoints da API
- `service.py`: regras de negócio
- `repository.py`: acesso ao banco
- `model.py`: modelo SQLModel
- `schema.py`: validações e contratos de entrada/saída

#### `core/`

Responsável por infraestrutura e comportamento global da aplicação:

- `config.py`: leitura das variáveis de ambiente
- `database.py`: conexão e sessão do banco
- `exceptions/`: classes e handlers de erro da API

---

## Configuração

A aplicação lê a URL do banco a partir do arquivo `.env` usando `pydantic-settings`.

Exemplo de `.env`:

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/project_manager
```

> O projeto usa SQLModel e cria as tabelas automaticamente ao iniciar a aplicação via `create_tables()` em `main.py`.

---

## Endpoints

### Projetos

| Método    | Endpoint                   | Descrição                      |
| ---------- | -------------------------- | -------------------------------- |
| `GET`    | `/projects/`             | Lista todos os projetos          |
| `GET`    | `/projects/{project_id}` | Busca um projeto pelo ID         |
| `POST`   | `/projects/`             | Cria um novo projeto             |
| `PATCH`  | `/projects/{project_id}` | Atualiza parcialmente um projeto |
| `DELETE` | `/projects/{project_id}` | Remove um projeto                |

A documentação interativa está disponível em:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

---

## Modelos e regras

### `ProjectStatus`

Valores aceitos:

- `pendente`
- `em_progresso`
- `concluido`
- `cancelado`

### `ProjectPriority`

Valores aceitos:

- `1` = alta
- `2` = média
- `3` = baixa

### Campos do projeto

| Campo            | Tipo                | Descrição            |
| ---------------- | ------------------- | ---------------------- |
| `id`           | `int`             | Identificador único   |
| `name`         | `str`             | Nome do projeto        |
| `description`  | `str`             | Descrição do projeto |
| `status`       | `ProjectStatus`   | Situação atual       |
| `priority`     | `ProjectPriority` | Prioridade             |
| `created_at`   | `datetime`        | Data de criação      |
| `completed_at` | `datetime           | null`                  |

### Validações relevantes

- `name` e `description` não podem ficar vazios ou com espaços em branco.
- Não é permitido cadastrar dois projetos com o mesmo nome.
- `completed_at` só pode ser informado quando `status` for `concluido`.
- `completed_at` deve possuir timezone UTC e não pode estar no futuro.

---

## Exemplos de payload

### Criar projeto

```json
{
  "name": "Projeto Alpha",
  "description": "Desenvolvimento do novo portal interno",
  "priority": 1
}
```

### Atualizar projeto

```json
{
  "status": "em_progresso",
  "priority": 2,
  "description": "Planejamento revisado"
}
```

---

## Tecnologias

- Python 3.11+
- FastAPI
- SQLModel
- Pydantic
- PostgreSQL
- Uvicorn
- Docker
- Docker Compose
- Pytest

---

## Como executar

### Localmente

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

### Com Docker Compose

```bash
docker compose up --build
```

A aplicação ficará disponível em:`http://localhost:8000`

---

## Testes

Os testes de schema e validação podem ser executados com:

```bash
pytest -q
```
