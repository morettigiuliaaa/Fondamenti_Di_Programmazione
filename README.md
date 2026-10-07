# 🐍 Fondamenti di Programmazione: esercizi in Python

Repository con il materiale di studio del corso di **Fondamenti di Programmazione**: esercizi, soluzioni commentate, una legenda dei comandi e le macchine virtuali per lavorare con lo stesso ambiente del laboratorio.

> 📌 Il repository **si aggiorna man mano che le lezioni procedono**.

---

## 📑 Indice

- [Cosa contiene il repository](#-cosa-contiene-il-repository)
- [Struttura delle cartelle](#-struttura-delle-cartelle)
- [Esercizi](#-esercizi)
- [Notebook degli esercizi Persico](#-notebook-degli-esercizi-persico)
- [Commenti colorati con VS Code](#-commenti-colorati-con-vs-code)
- [Legenda dei comandi](#-legenda-dei-comandi)
- [Macchina virtuale](#%EF%B8%8F-macchina-virtuale)
- [Argomenti trattati finora](#-argomenti-trattati-finora)
- [Aggiornamenti](#-aggiornamenti)
- [Da dove arrivano gli esercizi](#-da-dove-arrivano-gli-esercizi)

---

## 📦 Cosa contiene il repository

| Contenuto | Descrizione |
|---|---|
| 📝 **Esercizi raw** | Solo le consegne, senza soluzione, per provare a risolverli da soli |
| ✅ **Esercizi svolti e spiegati** | Le soluzioni complete, con una spiegazione di ogni passaggio |
| 📖 **Legenda** | Un riepilogo di tutti i comandi e i concetti visti fino ad ora |
| 💻 **Macchine virtuali** | I file per scaricare la VM, simile al laboratorio della Sapienza, per **Mac** e per **Windows** |

---

## 🗂️ Struttura delle cartelle

```text
.
├── README.md
├── Eserciziario_prof.md   # link alla pagina web degli esercizi
├── esercizi-raw/          # consegne senza soluzione
├── esercizi-svolti/       # soluzioni con spiegazione
├── legenda/               # comandi e concetti visti finora
└── ambiente_VM_Sapienza_Windows&Mac/
    ├── MAC_ARM64/
    │   └── README.md      # istruzioni e link di installazione per Mac
    └── WINDOWS_AMD64/
        └── README.md      # istruzioni e link di installazione per Windows
    │
    └──VIRTUALBOX
        └──README_Virtualbox.md     # istruzioni di installazione per tutti
```

---

## 📝 Esercizi

Gli esercizi sono disponibili in **due versioni**.

### Esercizi raw
Contengono soltanto le consegne (i commenti `TODO`) e, quando serve, il codice di partenza. Sono pensati per **provare a risolvere gli esercizi da soli**, prima di guardare la soluzione.

Alcuni esercizi hanno un formato particolare:

- **Da eseguire**: scrivi il programma da zero.
- **Da completare**: ti viene dato un programma a metà da completare.
- **Da sistemare**: ti viene dato un programma con degli errori da correggere.

### Esercizi svolti e spiegati
Ogni esercizio ha la sua soluzione e una **spiegazione** che racconta cosa fa il codice e perché.

> 💡 **Consiglio:** prova prima la versione raw, confronta poi con quella svolta e leggi la spiegazione.

---

## 🎨 Commenti colorati con VS Code

I file degli esercizi usano dei **commenti speciali**, che cambiano colore in base al loro utilizzo (consegne, spiegazioni, errori e così via).

Per vedere i file **formattati correttamente, con i commenti di colori diversi**, è necessario:

1. **programmare con [VS Code](https://code.visualstudio.com/)** (Visual Studio Code);
2. **scaricare l'estensione _Better Comments_ di Aaron Bond**.

### Come installare l'estensione

1. Apri **VS Code**.
2. Clicca sull'icona **Estensioni** nella barra laterale (oppure premi `Ctrl + Maiusc + X`, su Mac `Cmd + Maiusc + X`).
3. Cerca **Better Comments**.
4. Scegli quella dell'autore **Aaron Bond** e clicca su **Install**.

### Cosa significano i colori

| Commento | Utilizzo nei file | Colore |
|---|---|---|
| `# TODO` | Consegna dell'esercizio | 🟠 Arancione |
| `# ?` | Spiegazione della soluzione | 🔵 Blu |
| `# !` | Codice con errori da sistemare | 🔴 Rosso |
| `# *` | Intestazioni e programmi da completare | 🟢 Verde |

> 💡 Senza l'estensione i file funzionano comunque, ma i commenti compaiono tutti dello stesso colore.

---

## 🧠 Notebook degli esercizi Persico

Nel repository è presente anche una cartella con i notebook dedicati agli esercizi di Persico, pensati per lavorare in modo interattivo direttamente in VS Code.

### Dove trovarli

- `esercizi_notebook/`
- `esercizi_notebook/esercizi_raw_notebook/`

Qui trovi i file `.ipynb` con esercizi in versione vuota e, se necessario, con soluzioni o struttura già pronta da completare.

### Come configurarlo

1. Apri **VS Code**.
2. Installa l'estensione **Jupyter** (se non è già presente).
3. Apri il notebook desiderato (`.ipynb`).
4. Se richiesto, seleziona il **kernel Python** corretto.
5. Verifica che nel tuo ambiente sia installato **Python 3.x** e che il comando `python` sia disponibile.
6. Se VS Code non trova il kernel, usa **Select Kernel** e scegli l'interprete Python installato sul tuo computer.

### Info utili

- I notebook sono ideali per provare codice subito senza creare file separati.
- Sono perfetti per testare brevi script, verificare output e correggere errori in tempo reale.
- Se fai fatica a eseguire le celle, controlla che l'estensione **Python** e **Jupyter** sia installata correttamente.
- Per un lavoro più ordinato, puoi usare il notebook per fare prove veloci e poi trasferire il codice negli esercizi standard del repository.

---

## 📖 Legenda dei comandi

Nel repository è presente una **legenda** con tutti i comandi e i concetti visti fino ad ora, da consultare velocemente quando serve ricordare una sintassi. La legenda cresce insieme al corso.

---

## 🖥️ Macchina virtuale

Per lavorare con un ambiente simile a quello del **laboratorio della Sapienza** sono presenti i file per scaricare la **macchina virtuale**.

| Sistema | Cartella | Istruzioni |
|---|---|---|
| 🍎 **Mac** | `virtual-machine/mac/` | `README.md` nella cartella |
| 🪟 **Windows** | `virtual-machine/windows/` | `README.md` nella cartella |

Ogni cartella ha **un proprio README** con le istruzioni passo passo per l'installazione.

---

## 📚 Argomenti trattati finora

| Lezione | Argomenti |
|---|---|
| **1** | `print()`, `input()`, `int()`, `float()`, `str()`, `if` |
| **2** | Stringhe, `len()`, indicizzazione e slicing, `index()`, `find()`, metodi delle stringhe, f-string, `bool`, confronti, `and`, `or`, `not` |
| **3** | `if` / `elif` / `else`, `for`, `range()`, `while`, funzioni con parametri e `return` |
| **4** | Contenitori: `list`, `tuple`, `set`, `dict`, mutabilità, metodi delle liste, `enumerate()`, aliasing e copia |

---

## 🔄 Aggiornamenti

Il repository **viene aggiornato in base alle lezioni** e a quello che viene svolto in aula. Con ogni nuova lezione si aggiungono nuovi esercizi, nuove soluzioni e nuove voci nella legenda.

---

## 🤖 Da dove arrivano gli esercizi

- Quando la professoressa **assegna degli esercizi**, vengono usati quelli.
- Quando **non sono presenti esercizi** dati dalla professoressa, gli esercizi vengono **creati con Claude o ChatGPT**, basandosi sulle **slide** del corso e sugli **argomenti svolti a lezione**.

---

## ✨ Come usare al meglio il repository

- Inizia sempre dagli esercizi in versione `raw` per provare a risolverli da solo.
- Confronta poi la soluzione svolta e leggi i commenti per capire il ragionamento.
- Consulta la legenda quando ti serve ripassare un comando o un concetto.
- Se lavori in laboratorio, usa la VM per avere lo stesso ambiente di riferimento del corso.

---

<p align="center">Buono studio! 🚀</p>
