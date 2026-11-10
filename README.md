# Task Manager API

REST API per la gestione di attività (Todo) e utenti, sviluppata con Python e FastAPI.

Il progetto nasce come esercizio pratico per approfondire lo sviluppo backend, la progettazione di API REST, la validazione dei dati con Pydantic e la gestione delle operazioni CRUD.

## Tecnologie utilizzate

- Python 3.13
- FastAPI
- Pydantic
- Uvicorn
- Argon2 tramite `pwdlib`
- Pytest
- HTTPX

## Funzionalità implementate

### Todo

- Creazione di un Todo.
- Recupero di tutti i Todo.
- Recupero di un singolo Todo tramite ID.
- Modifica completa tramite PUT.
- Modifica parziale tramite PATCH.
- Eliminazione tramite DELETE.
- Filtri per stato di completamento.
- Ricerca per titolo.
- Filtro per priorità.
- Paginazione tramite `skip` e `limit`.
- Statistiche sui Todo.

### Utenti

- Registrazione di un nuovo utente.
- Recupero dell'elenco degli utenti.
- Controllo degli username duplicati.
- Controllo delle email duplicate.
- Hashing delle password tramite Argon2.
- Assegnazione automatica del ruolo iniziale `user`.
- Generazione automatica della data di iscrizione.

## Endpoint API

### Todo

| Metodo | Endpoint | Descrizione |
|---|---|---|
| GET | `/todos` | Recupera i Todo |
| GET | `/todos/{todo_id}` | Recupera un Todo |
| GET | `/todos/stats` | Recupera le statistiche |
| POST | `/todos` | Crea un Todo |
| PUT | `/todos/{todo_id}` | Sostituisce un Todo |
| PATCH | `/todos/{todo_id}` | Modifica parzialmente un Todo |
| DELETE | `/todos/{todo_id}` | Elimina un Todo |

### Filtri Todo

L'endpoint `GET /todos` supporta i seguenti parametri:

| Parametro | Tipo | Descrizione |
|---|---|---|
| `completed` | Boolean | Filtra per stato di completamento |
| `q` | String | Cerca una parola nel titolo |
| `priorita` | Enum | Filtra per priorità |
| `skip` | Integer | Numero di risultati da saltare |
| `limit` | Integer | Numero massimo di risultati |

Esempi:

```text
GET /todos?completed=false
GET /todos?q=studio
GET /todos?priorita=alta
GET /todos?skip=10&limit=5
GET /todos?completed=false&priorita=alta
```

Priorità disponibili:

- `bassa`
- `media`
- `alta`

### Utenti

| Metodo | Endpoint | Descrizione |
|---|---|---|
| GET | `/users/` | Recupera gli utenti |
| POST | `/users/` | Registra un nuovo utente |

## Struttura del progetto

```text
task-manager-API/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── schemas.py
│   │
│   └── routes/
│       ├── __init__.py
│       ├── todos.py
│       └── users.py
│
├── tests/
│   └── test_todo.py
│
├── requirements.txt
├── pyproject.toml
├── uv.lock
└── README.md
```

## Installazione

Clona la repository:

```bash
git clone https://github.com/ssantorotech/task-manager-API.git
cd task-manager-API
```

Crea e attiva un ambiente virtuale:

```bash
python -m venv .venv
source .venv/bin/activate
```

Installa le dipendenze:

```bash
uv sync
```

In alternativa, se utilizzi `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Avvio dell'applicazione

Avvia il server con:

```bash
uv run uvicorn app.main:app --reload
```

L'API sarà disponibile all'indirizzo:

```text
http://127.0.0.1:8000
```

Documentazione interattiva:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Database

Attualmente il progetto utilizza dizionari Python per simulare un database in memoria.

I dati vengono persi quando l'applicazione viene riavviata.

La persistenza tramite SQLite è prevista tra i prossimi sviluppi.

## Test

Per eseguire i test automatici:

```bash
uv run pytest -v
```

La copertura dei test per gli endpoint Todo e User è in fase di sviluppo.

## Sviluppi futuri

- [ ] Completare i test automatici per Todo e User.
- [ ] Implementare PUT, PATCH e DELETE per gli utenti.
- [ ] Implementare autenticazione e autorizzazione.
- [ ] Integrare SQLite.
- [ ] Introdurre SQLAlchemy.
- [ ] Collegare gli utenti ai rispettivi Todo.
- [ ] Implementare un frontend con React.

---

Progetto personale a scopo didattico.
