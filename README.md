# TicketMania

### Programma in python per la prenotazioni di biglietti tramite MongoDB
<a name="readme-top"></a>

<div align="center">
   <img src="https://img.shields.io/badge/mongodb-%FFFFF.svg?&style=for-the-badge&logo=mongodb&logoColor=white">
   <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue">
   <img src="https://img.shields.io/badge/windows%20terminal-4D4D4D?style=for-the-badge&logo=windows%20terminal&logoColor=white">
   <img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white">
</div>

---
<div align="center">
  <img src="https://github.com/NobruLcnITS/Mongo_booking_project/assets/168713245/b0ed8b73-fc6c-410c-ad8f-82f3e3b8fdbd" alt="RedisChat Logo" />
</div>
<hr>

TicketMania è un'applicazione efficiente e sicura per comprare biglietti di concerti, eventi e teatro.
TicketMania utilizza come database MongoDB, quest'ultimo offre una gestione migliore e più efficiente rispetto ai concorrenti. <br>

Con TicketMania, è possibile, una volta registrati ed effettuato il login, ricercare i concerti disponibili sulla base di vari filtri, cumulabili fra loro.
Questi sono:  <b>

- Nome del concerto
- Artista presente
- Data
- Posizione e distanza
- Non sold out
- Prezzo del biglietto
- Genere musicale
</b> 
<br>
L'applicazione permette inoltre di visualizzare i biglietti acquistati, tutti con il proprio identificativo univoco.
<br>

## Indice

- <p align="left"><a href="#Requisiti">Requisiti</a></p>
- <p align="left"><a href="#Installazione-e-configurazione-TicketMania">Installazione e configurazione TicketMania</a></p>
- <p align="left"><a href="#3A-Installazione-di-Docker-Desktop-installazione-immagine-MongoDB-creazione-di-container-e-collegamento-con-Python"> 3A. Installazione di Docker Desktop, installazione dell'immagine MongoDB, creazione di container e collegamento con Python</a></p>
- <p align="left"><a href="#3B-Apertura-di-un-server-MongoDB-cloud-e-collegamento-con-Python"> 3B. Apertura di un server MongoDB cloud e collegamento con Python.</a></p>
- <p align="left"><a href="#3C-Uso-di-un-server-MongoDB-cloud-esistente"> 3C. Uso di un server MongoDB cloud esistente</a></p>
- <p align="left"><a href="#4-Installazione-di-MongoDB-Compass-e-aggiunta-del-database">4. Installazione di MongoDB Compass e aggiunta del database</a></p>
- <p align="left"><a href="#5-Installazione-delle-librerie-Python">5. Installazione delle librerie Python</a></p>
- <p align="left"><a href="#6-Avvio-di-TicketMania">6. Avvio di TicketMania</a></p>

## Requisiti

Per avviare l'applicazione, è necessario/preferibile avere:

- **Python v.3.12**
- **Docker Desktop** *(In caso non si utilizzi MongoDB Atlas)*
- **Un Database MongoDB Atlas** *(In caso non si usi Docker)*
- **MongoDBCompass** (Opzionale, ma consigliato)
  
- **Le seguenti librerie Python**:
  - `pymongo`
  - `geopy`
  - `regex`
  - `colorama`
  - `os`
  - `time`
  - `datetime`
  - `random`
  - `re`
  - `hashlib`

<p align="right">(<a href="#readme-top">torna in cima</a>)</p>

## Installazione e configurazione TicketMania


### 1. Clona il repository di TicketMania:

   - Apri il terminale e vai nella directory dove vuoi clonare il repository tramite `cd 'yo/ur/path'`
   - Esegui il seguente comando:
     
     ```sh
     git clone https://github.com/NobruLcnITS/Mongo_booking_project.git
     ```

### 2. Installazione di Python 3.12

1. **Scarica Python 3.12**:
   - Clicca su questo link: [python.org](https://www.python.org/downloads/release/python-3120/)
   - Scarica Python 3.12 per il tuo sistema operativo ed installalo.

2. **Verifica l'installazione**:
   - Apri il terminale.
   - Digita `python --version` per assicurarti di aver installato correttamente Python 3.12.

<p align="right">(<a href="#readme-top">torna in cima</a>)</p>

---

### 3A Installazione di Docker Desktop installazione immagine MongoDB creazione di container e collegamento con Python

*Solo nel caso si voglia eseguire TicketMania in locale*

1. **Scarica Docker Desktop**:
   - Clicca su questo link: [docker.com](https://www.docker.com/products/docker-desktop)
   - Scarica Docker Desktop per il tuo sistema operativo e installalo.

2. **Verifica l'installazione**:
   - Apri il terminale.
   - Digita `docker --version` per assicurarti che Docker sia installato correttamente.

3. **Esegui un container MongoDB con porta 27017**

   - Usa il comando seguente per creare e avviare un container MongoDB con la porta predefinita `27017` esposta:

     ```sh
     docker run --name my-mongo -p 27017:27017 -d mongo
     ```

     - **Spiegazione del comando**:
       - `--name my-mongo`: Assegna il nome `my-mongo` al container.
       - `-p 27017:27017`: Espone la porta `27017` del container (porta predefinita di MongoDB) sulla porta `27017` del tuo host.
       - `-d mongo`: Esegue il container MongoDB in modalità "detached", ossia in background.

   - Dopo aver eseguito il comando, verifica che il container sia stato avviato con successo utilizzando:

     ```sh
     docker ps
     ```

     Oppure, visualizza il container tramite Docker Desktop, se lo stai utilizzando.

2. **Collegamento con MongoDB Python**
   - Aggiungi le seguenti righe di codice all'inizio di ogni modulo Python per collegarti al tuo server MongoDB in esecuzione nel container:

     ```python
     from pymongo import MongoClient

     # Collegamento al server MongoDB in esecuzione sul container Docker locale
     client = MongoClient('mongodb://localhost:27017/')
     db = client['nome_del_tuo_database']

     # Verifica la connessione
     print(db.list_collection_names())  # Questo dovrebbe stampare le collezioni nel database
     ```



     - **Spiegazione del codice**:
       - `MongoClient('mongodb://localhost:27017/')`: Crea un client MongoDB che si connette al server in esecuzione su `localhost` sulla porta `27017`.
       - `client['nome_del_tuo_database']`: Sostituisci `'nome_del_tuo_database'` con il nome del database che desideri utilizzare.
       - `db.list_collection_names()`: Esegue un comando per elencare tutte le collezioni nel database specificato.

<p align="right">(<a href="#readme-top">torna in cima</a>)</p>

---
### 3B Apertura di un server MongoDB cloud e collegamento con Python.

*Solo nel caso si voglia utilizzare MongoDB da host per altri utenti*

1. **Avviamento MongoDB cloud**
   - Clicca su questo link: [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
   - Registrati e crea un cluster gratuito o a pagamento su MongoDB Atlas.
   - Segui la procedura guidata per configurare il tuo cluster. MongoDB Atlas offre un cluster gratuito chiamato M0, che è ottimo per cominciare.

2. **Collegamento con MongoDB Python**
   - Una volta creato il cluster, vai nella sezione "Clusters" e clicca su "Connect" per il cluster che hai creato.
   - Nella finestra di connessione, seleziona "Connect your application" per ottenere la stringa di connessione URI.
   - La stringa URI sarà simile a `mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority`.
   - Ottieni il nome utente (`<username>`) e la password (`<password>`) che hai configurato durante la creazione del cluster.
   - Ottieni il nome del database (`<dbname>`), che puoi specificare nella URI o nel tuo codice.
   - Una volta ottenute queste credenziali, inseriscile all'interno delle seguenti righe di codice contenute all'inizio di ogni modulo Python:

     ```python
     from pymongo import MongoClient

     # Sostituisci i placeholder nella URI con le tue credenziali
     client = MongoClient('mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority')
     db = client['<dbname>']

     # Verifica la connessione
     print(db.list_collection_names())  # Questo dovrebbe stampare le collezioni nel database
     ```

     **Nota**: Assicurati di sostituire `<username>`, `<password>`, `<dbname>` e altre parti della URI con le informazioni effettive del tuo cluster MongoDB Atlas.

<p align="right">(<a href="#readme-top">torna in cima</a>)</p>

---

### 3C Uso di un server MongoDB cloud esistente

*Solo nel caso si voglia utilizzare un database MongoDB già esistente di cui si conoscono i dettagli di connessione*

1. **Ottieni le credenziali dall'host**
   - Ottieni l'endpoint (URI di connessione), il nome utente, la password e il nome del database dal proprietario dell'host.
   - Tipicamente, l'endpoint avrà una forma simile a `mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority`.

2. **Collegamento con MongoDB Python**
   - Una volta ottenute queste credenziali, inseriscile all'interno delle seguenti righe di codice all'inizio di ogni modulo Python:

     ```python
     from pymongo import MongoClient

     # Sostituisci i placeholder nella URI con le tue credenziali
     client = MongoClient('mongodb+srv://<username>:<password>@<endpoint>/<dbname>?retryWrites=true&w=majority')
     db = client['<dbname>']

     # Verifica la connessione
     print(db.list_collection_names())  # Questo dovrebbe stampare le collezioni nel database
     ```

     - **Spiegazione del codice**:
       - `MongoClient('mongodb+srv://<username>:<password>@<endpoint>/<dbname>?retryWrites=true&w=majority')`: Crea un client MongoDB utilizzando l'endpoint e le credenziali fornite.
         - Sostituisci `<username>` con il nome utente.
         - Sostituisci `<password>` con la password.
         - Sostituisci `<endpoint>` con l'endpoint del server MongoDB (di solito finisce con `.mongodb.net`).
         - Sostituisci `<dbname>` con il nome del database.
       - `db = client['<dbname>']`: Collega il client al database specificato dal nome `<dbname>`.
       - `db.list_collection_names()`: Elenca le collezioni presenti nel database per verificare la connessione.

<p align="right">(<a href="#readme-top">torna in cima</a>)</p>

---

### 4 Installazione di MongoDB Compass e aggiunta del database

*Opzionale, programma utile per eseguire test sui database e visualizzare i dati*

MongoDB Compass è uno strumento GUI (Graphical User Interface) che permette di esplorare e interagire con i tuoi database MongoDB. Puoi utilizzarlo per eseguire query, analizzare documenti, visualizzare indici e molto altro.

1. **Scarica MongoDB Compass**:
   - Clicca su questo link: [MongoDB Compass](https://www.mongodb.com/products/compass)
   - Scarica MongoDB Compass per il tuo sistema operativo (Windows, macOS o Linux) e installalo seguendo le istruzioni fornite.

2. **Aggiunta del database**
   - Apri MongoDB Compass.
   - Clicca su 'New Connection' o 'Connect' se è la prima volta che avvii Compass.
   - Nella finestra di connessione, inserisci la stringa URI del tuo database. Questa sarà simile a:

     ```plaintext
     mongodb+srv://<username>:<password>@<endpoint>/<dbname>?retryWrites=true&w=majority
     ```

     - **Spiegazione dei campi**:
       - `<username>`: Il nome utente che hai ottenuto.
       - `<password>`: La password associata all'utente.
       - `<endpoint>`: L'endpoint del server MongoDB, spesso termina con `.mongodb.net`.
       - `<dbname>`: Il nome del database a cui vuoi connetterti.

     - Se non hai la stringa URI completa, puoi riempire manualmente i campi richiesti come "Hostname", "Port" (tipicamente `27017` per MongoDB) e altri dettagli di autenticazione.

   - Dopo aver inserito le credenziali, clicca su 'Connect' per aggiungere il database a MongoDB Compass.

   - Una volta connesso, puoi esplorare il database, eseguire query e gestire i dati utilizzando l'interfaccia grafica di MongoDB Compass.

<p align="right">(<a href="#readme-top">torna in cima</a>)</p>

---


### 5 Installazione delle librerie Python

1. **Apri il terminale**:
   - Su Windows, puoi usare il prompt dei comandi o PowerShell.
   - Su macOS e Linux, puoi usare il terminale di default.

2. **Controlla quali librerie sono presenti nel tuo ambiente**
   - Attiva il tuo ambiente virtuale tramite CONDA, VENV ecc.
   - Esegui il comando `pip list` per capire quali delle librerie menzionate sono già presenti.

3. **Installa le librerie mancanti**:
   - Esegui il seguente comando per installare le librerie mancanti:
     ```sh
     pip install pymongo geopy regex colorama
     ```

<p align="right">(<a href="#readme-top">torna in cima</a>)</p>

---


### 6 Avvio di TicketMania

1. **Cambio directory**
   - Apri il terminale e tramite `cd yo/ur/path` accedi alla cartella dove hai clonato la repository di GitHub.

2. **Attiva il tuo ambiente virtuale**

   - Per attivare il tuo ambiente virtuale, utilizza il comando specifico del gestore di ambienti:

      - Con `conda`: `conda activate 'nome-ambiente'`
      - Con `venv` (integrato in Python): `source env/bin/activate`
      - Con `virtualenv`: `source venv/bin/activate`

   **Nota**: Assicurati di navigare nella directory del tuo progetto prima di eseguire il comando.
   
3. **Esegui il codice**:
   
   - Esegui il seguente comando per avviare TicketMania:

     ```sh
     python main.py
     ```
  
### Conclusione

Ora dovresti avere tutto il necessario per eseguire TicketMania sul tuo dispositivo.
<br>

Speriamo questo README ti sia stato utile!

<p align="right">(<a href="#readme-top">torna in cima</a>)</p>

---
