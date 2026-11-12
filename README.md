🚀 Task Manager API

Un'applicazione robusta e moderna basata su FastAPI per la gestione di attività (To-Do) e utenti, completa di validazione avanzata dei dati, gestione delle priorità, ruoli utente e hashing sicuro delle password.

🛠️ Tecnologie Utilizzate

Python 3.10+

FastAPI – Framework web moderno e ad alte prestazioni per la creazione di API

Pydantic v2 – Validazione dei dati e gestione degli schemi (EmailStr, SecretStr, Enum)

Pwdlib – Hashing sicuro delle password

Pytest & TestClient – Suite di testing automatizzato

📂 Struttura del Progetto

task-manager-API/
│
├── app/
│   ├── __init__.py
│   ├── main.py          # Punto di ingresso dell'applicazione FastAPI
│   ├── database.py      # Database in-memory per la gestione di task e utenti
│   ├── schemas.py       # Modelli Pydantic ed Enum (Priorita, Ruolo)
│   └── routes/
│       ├── todos.py     # Endpoint CRUD, filtri e statistiche per i task
│       └── users.py     # Endpoint per la registrazione e gestione utenti
│
├── tests/
│   ├── test_todo.py     # Test automatizzati per i task
│   └── test_user.py     # Test automatizzati per gli utenti
│
├── requirements.txt
└── README.md


⚙️ Installazione e Avvio

Clona il repository:

git clone https://github.com/ssantorotech/task-manager-API.git
cd task-manager-API


Crea e attiva un ambiente virtuale:

python -m venv venv
source venv/bin/activate  # Su Windows: venv\Scripts\activate


Installa le dipendenze:

pip install -r requirements.txt


Avvia il server di sviluppo:

uvicorn app.main:app --reload


L'API sarà raggiungibile su http://127.0.0.1:8000. Puoi testare gli endpoint tramite la documentazione interattiva su http://127.0.0.1:8000/docs (Swagger UI) oppure /redoc.

🧪 Esecuzione dei Test

Per avviare tutti i test di unità e integrazione con pytest:

pytest


📋 Endpoints Principali

🔹 Todos (/todos)

GET /todos – Restituisce la lista dei task (supporta filtri per completed, ricerca testuale q, priorita e paginazione skip/limit).

POST /todos – Crea un nuovo task associando titolo, descrizione e livello di priorità (bassa, media, alta).

GET /todos/stats – Fornisce un riepilogo statistico dei task (totali, completati, da completare e conteggio per priorità).

GET /todos/{todo_id} – Recupera i dettagli di un singolo task tramite ID.

PUT /todos/{todo_id} – Sostituisce interamente un task esistente.

PATCH /todos/{todo_id} – Aggiorna parzialmente un task esistente.

DELETE /todos/{todo_id} – Elimina un task dal database.

🔹 Users (/users)

GET /users – Restituisce l'elenco completo degli utenti registrati.

POST /users – Registra un nuovo utente con validazione dell'email, password criptata e controllo sull'unicità di username ed email.

GET /users/{user_id} – Recupera i dettagli di un utente specifico tramite ID.