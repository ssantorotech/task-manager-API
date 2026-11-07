# Todo API

Una REST API sviluppata con **Python e FastAPI** per gestire una lista di attività (Todo).

Il progetto permette di creare, leggere, modificare, eliminare e filtrare le attività. Include validazione dei dati con Pydantic e test automatici con Pytest.

## Tecnologie utilizzate

- Python
- FastAPI
- Pydantic
- Pytest
- HTTPX
- Uvicorn

## Struttura del progetto

```text
task-manager-API/
├── app/
│   ├── routes/
│   │   ├── __init__.py
│   │   └── todos.py
│   ├── __init__.py
│   ├── database.py
│   ├── main.py
│   └── schemas.py
├── tests/
│   └── test_todo.py
├── client.py
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Installazione

Clona il repository:

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
pip install -r requirements.txt
```

## Avvio dell'applicazione

Avvia il server con:

```bash
uvicorn app.main:app --reload
```

L'API sarà disponibile all'indirizzo:

```text
http://localhost:8000
```

Documentazione interattiva:

```text
http://localhost:8000/docs
```

## Endpoint

| Metodo | Endpoint | Descrizione |
|---|---|---|
| GET | `/todos` | Recupera tutte le attività |
| GET | `/todos?completed=true` | Filtra per stato di completamento |
| GET | `/todos?q=studio` | Cerca nel titolo |
| GET | `/todos?priorita=alta` | Filtra per priorità |
| GET | `/todos?skip=0&limit=20` | Paginazione |
| GET | `/todos/stats` | Statistiche delle attività |
| GET | `/todos/{todo_id}` | Recupera una singola attività |
| POST | `/todos` | Crea una nuova attività |
| PUT | `/todos/{todo_id}` | Sostituisce un'attività |
| PATCH | `/todos/{todo_id}` | Modifica parzialmente un'attività |
| DELETE | `/todos/{todo_id}` | Elimina un'attività |

### Esempio di creazione

Richiesta `POST /todos`:

```json
{
    "title": "Studiare Python",
    "description": "Ripassare FastAPI e Pydantic",
    "priorita": "alta"
}
```

Le priorità disponibili sono:

- `bassa`
- `media`
- `alta`

Il campo `completed` viene inizializzato automaticamente a `false`.

## Test

Per eseguire i test automatici:

```bash
pytest -v
```

Per visualizzare anche gli output dei print:

```bash
pytest -v -s
```

## Client HTTP

Il progetto include `client.py`, un semplice client realizzato con HTTPX per provare le operazioni principali dell'API.

Avvia prima il server, poi esegui:

```bash
python client.py
```

## Database

Attualmente i dati vengono conservati in un database temporaneo in memoria tramite un dizionario Python.

I dati vengono persi quando l'applicazione viene riavviata.

## Possibili sviluppi futuri

- Integrazione con SQLite.
- Persistenza dei dati.
- Autenticazione degli utenti.
- Integrazione con un frontend React.
