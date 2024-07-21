# Gestione Entrate e Uscite

Questo progetto è un sistema di gestione delle entrate e delle uscite scritto in Python con Flask. Permette di tracciare le entrate e le uscite finanziarie, visualizzare grafici e statistiche, e gestire i dati in modo interattivo tramite una dashboard.

## Caratteristiche

- Aggiunta di transazioni di entrata e uscita con descrizione, importo, store e quantità.
- Visualizzazione delle transazioni in una tabella con colorazione per entrate (verde) e uscite (rosso).
- Grafico delle entrate e delle uscite.
- Grafico dei pezzi per store.
- Calcolo della variazione percentuale delle spese rispetto al periodo precedente.
- Filtro delle transazioni per intervallo di date.
- Utilizzo di un file CSV per salvare le transazioni.

## Requisiti

- Python 3.x
- Flask

## Installazione

1. **Clona il repository:**

   ```sh
   git clone https://github.com/Allsafeitalia/entrateUscite.git
   cd entrateUscite
Crea un ambiente virtuale:

sh
Copia codice
python3 -m venv venv
Attiva l'ambiente virtuale:

Su macOS e Linux:

sh
Copia codice
source venv/bin/activate
Su Windows:

sh
Copia codice
.\venv\Scripts\activate
Installa le dipendenze:

sh
Copia codice
pip install -r requirements.txt
Utilizzo
Esegui l'applicazione Flask:

sh
Copia codice
python app.py
Apri un browser web e vai all'indirizzo:

arduino
Copia codice
http://127.0.0.1:5000/
Interagisci con la dashboard:

Aggiungi Transazione: Compila il form per aggiungere una nuova transazione. Inserisci la data, il tipo (entrata o uscita), la descrizione, l'importo, lo store e la quantità. Clicca su "Aggiungi" per salvare la transazione.
Filtra per Data: Utilizza il form in alto per selezionare l'intervallo di date da analizzare. Clicca su "Filtra" per visualizzare le transazioni nell'intervallo selezionato.
Visualizza Grafici: Osserva i grafici per confrontare le entrate e le uscite e i pezzi per store.
Variazione Percentuale: La dashboard mostra la variazione percentuale delle spese rispetto al periodo precedente.
Esempio di finanze.csv
Il file finanze.csv deve avere la seguente struttura:

csv
Copia codice
data,tipo,descrizione,importo,store,quantità
2024-07-18,entrata,stipendio,2000,ufficio,1
2024-07-19,uscita,formaggio,3.90,supermercato despar,1
2024-07-20,uscita,acqua,1.00,supermercato coop,6
2024-07-21,entrata,bonus,500,ufficio,1
2024-07-22,uscita,pane,2.50,supermercato despar,2
File Importanti
app.py: Script principale che esegue l'applicazione Flask.
finanze.csv: File CSV utilizzato per salvare le transazioni.
templates/index.html: Template HTML per la dashboard.
requirements.txt: Elenco delle dipendenze del progetto.
.gitignore: File per ignorare i file e le directory non necessari nel repository.
Contributori
Progetto realizzato da Giuseppe Mastronardi.

Licenza
Questo progetto è concesso in licenza sotto i termini della licenza MIT. Vedi il file LICENSE per i dettagli.

markdown
Copia codice

### Aggiungere il File al Progetto

1. Crea un nuovo file chiamato `README.md` nella directory principale del tuo progetto e incolla il contenuto sopra.
2. Aggiungi e committa il file `README.md` al repository Git:

   ```sh
   git add README.md
   git commit -m "Aggiunto README dettagliato"
   git push
