# ESERCIZI SECONDA LEZIONE: str, len(), indicizzazione, slicing,
# index(), find(), metodi delle stringhe, f-string, bool, confronti,
# and, or, not.

#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 6
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO:
# TODO Il programma dovrà chiedere una parola e visualizzarla concatenata
# TODO con un'altra parola e successivamente ripeterla 3 volte

parola1 = input("Inserisci la prima parola: ")
parola2 = input("Inserisci la seconda parola: ")

print("Parole concatenate:", parola1 , parola2)
print("Ripetizione:", parola1 * 3)

# ? SPIEGAZIONE:
# ? Con le stringhe l'operatore + non esegue una somma ma una concatenazione,
# ? quindi unisce due stringhe.
# ? L'operatore * permette invece di ripetere una stringa per un numero
# ? intero di volte.

#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 7
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO:
# TODO Il programma dovrà chiedere una parola e restituire la sua lunghezza
# TODO e verificare se contiene la lettera "a"

parola = input("Inserisci una parola: ")

lunghezza = len(parola)
contiene_a = "a" in parola
if(contiene_a):
    contiene_a='si'
else:
    contiene_a='no'

print("La parola contiene", lunghezza, "caratteri")
print("Contiene la lettera 'a'?", contiene_a)

# ? SPIEGAZIONE:
# ? Utilizzo len() per ricavare il numero di caratteri contenuti nella stringa.
# ? Anche gli spazi vengono considerati caratteri.
# ? Con l'operatore in verifico se un determinato carattere o una sottostringa
# ? è presente all'interno della stringa.
# ? Il risultato di in è un valore booleano, quindi True oppure False, lo converto in str.

#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 8
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO:
# TODO Il programma dovrà chiedere un nome e restituire il primo,
# TODO il quinto e l'ultimo carattere

nome = input("Inserisci il tuo nome: ")

print("Primo carattere:", nome[0])
print("Quinto carattere:", nome[4])
print("Ultimo carattere:", nome[-1])

# ? SPIEGAZIONE:
# ? Una stringa è una sequenza ordinata di caratteri.
# ? Posso accedere ad ogni carattere tramite il suo indice.
# ? In Python gli indici partono da 0, quindi il primo carattere è [0].
# ? Utilizzando gli indici negativi posso partire dalla fine della stringa.
# ? L'indice -1 rappresenta quindi l'ultimo carattere.

#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 9
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI SISTEMARE IL SEGUENTE ESERCIZIO:
# TODO Il programma deve visualizzare un carattere che non esiste nella stringa

# ! nome = "Python"
# ! print(nome[6])

nome = "Python"
print(nome[6])

# ? SPIEGAZIONE:
# ? La stringa "Python" contiene 6 caratteri e quindi gli indici validi
# ? vanno da 0 a 5.
# ? L'indice 6 non esiste e genera un IndexError.
# ? L'errore indica che l'indice richiesto è fuori dall'intervallo disponibile.

#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 10
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO:
# TODO Il programma dovrà chiedere una parola e visualizzare una parte
# TODO della stringa utilizzando lo slicing

parola = input("Inserisci una parola: ")

print("Primi 3 caratteri:", parola[0:3])
print("Dal quarto carattere:", parola[3:])
print("Tutta la parola:", parola[:])

# ? SPIEGAZIONE:
# ? Con lo slicing posso estrarre una parte della stringa utilizzando
# ? la sintassi [start:end].
# ? L'indice start viene incluso mentre l'indice end viene escluso.
# ? Se ometto start parto dall'inizio, mentre se ometto end arrivo fino
# ? alla fine della stringa.

#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 11
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO:
# TODO Il programma dovrà visualizzare una parola saltando caratteri
# TODO tramite lo step e successivamente visualizzarla al contrario

parola = input("Inserisci una parola: ")

print("Un carattere ogni due:", parola[::2])
print("Un carattere ogni tre:", parola[::3])
print("Parola al contrario:", parola[::-1])

# ? SPIEGAZIONE:
# ? La sintassi completa dello slicing è [start:end:step].
# ? Lo step indica di quanto deve avanzare l'indice dopo ogni carattere.
# ? Con uno step positivo mi sposto da sinistra verso destra.
# ? Con uno step negativo mi sposto da destra verso sinistra.
# ? Utilizzando [::-1] posso quindi ottenere la stringa al contrario.

#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 12
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO:
# TODO Il programma dovrà cercare la posizione della parola "Python"
# TODO all'interno di una frase

testo = "Sto imparando Python all'università"

posizione = testo.index("Python")

print("La parola Python inizia all'indice:", posizione)

# ? SPIEGAZIONE:
# ? Con index() posso cercare una sottostringa all'interno di una stringa.
# ? Il metodo restituisce un int che rappresenta l'indice della prima
# ? occorrenza della sottostringa cercata.
# ? Se la sottostringa non viene trovata index() genera un ValueError.

#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 13
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO:
# TODO Il programma dovrà cercare una parola utilizzando find()
# TODO e verificare cosa succede quando la parola non viene trovata

testo = "Sto imparando Python all'università"

print("Posizione di Python:", testo.find("Python"))
print("Posizione di Java:", testo.find("Java"))

# ? SPIEGAZIONE:
# ? find() funziona in modo simile a index() e restituisce la posizione
# ? della prima occorrenza della sottostringa.
# ? La differenza è che se non trova la sottostringa find() restituisce -1
# ? invece di generare un errore.

#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 14
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO:
# TODO Il programma dovrà chiedere una frase e visualizzarla in minuscolo,
# TODO maiuscolo e con una parola sostituita

frase = input("Inserisci una frase: ")

print("Minuscolo:", frase.lower())
print("Maiuscolo:", frase.upper())
print("Frase modificata:", frase.replace("Python", "Informatica"))

# ? SPIEGAZIONE:
# ? lower() restituisce una nuova stringa con tutti i caratteri in minuscolo.
# ? upper() restituisce una nuova stringa con tutti i caratteri in maiuscolo.
# ? replace() sostituisce una parte della stringa con un'altra.
# ? Questi metodi non modificano direttamente la stringa originale,
# ? ma restituiscono una nuova stringa.

#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 15
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO:
# TODO Il programma dovrà chiedere nome e cognome separati da uno spazio
# TODO e dividere la stringa nelle sue singole parole

nome_completo = input("Inserisci nome e cognome: ")

parole = nome_completo.split()

print("Nome e cognome divisi:", parole)

# ? SPIEGAZIONE:
# ? split() permette di dividere una stringa in più parti.
# ? Se non viene indicato un separatore, la divisione viene effettuata
# ? utilizzando gli spazi.
# ? Il risultato è una lista di stringhe.

#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 16
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO:
# TODO Il programma dovrà chiedere nome ed età e utilizzare una f-string
# TODO per creare una frase contenente i dati inseriti

nome = input("Come ti chiami? ")
eta = int(input("Quanti anni hai? "))

print(f"Ciao {nome}, hai {eta} anni!")
print(f"L'anno prossimo avrai {eta + 1} anni.")

# ? SPIEGAZIONE:
# ? Le f-string permettono di inserire variabili ed espressioni direttamente
# ? all'interno di una stringa.
# ? Per utilizzare una f-string metto la lettera f prima delle virgolette
# ? e inserisco le variabili tra parentesi graffe {}.
# ? Posso inserire anche direttamente delle espressioni, come eta + 1.

#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 17
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO:
# TODO Il programma dovrà chiedere un prezzo e uno sconto e visualizzare
# TODO i valori formattati tramite una f-string

prezzo = 45.9876
sconto = 0.25

print(f"Prezzo: {prezzo:.2f} euro")
print(f"Sconto: {sconto:.0%}")

# ? SPIEGAZIONE:
# ? Nelle f-string posso anche decidere come visualizzare i numeri.
# ? :.2f permette di visualizzare un numero con due cifre decimali.
# ? :.0% permette di visualizzare un valore decimale come percentuale
# ? senza cifre decimali.

#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 18
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO:
# TODO Il programma dovrà chiedere l'età e verificare tramite un confronto
# TODO se l'utente è maggiorenne

eta = int(input("Quanti anni hai? "))

maggiorenne = eta >= 18

print("Sei maggiorenne?", maggiorenne)

# ? SPIEGAZIONE:
# ? Il tipo bool può assumere solamente due valori: True e False.
# ? Gli operatori di confronto producono un valore booleano.
# ? In questo caso verifico se eta è maggiore o uguale a 18.
# ? Se la condizione è vera ottengo True, altrimenti False.
# ? Gli operatori di confronto affrontati sono:
# ? == uguale
# ? != diverso
# ? < minore
# ? > maggiore
# ? <= minore o uguale
# ? >= maggiore o uguale

#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 19
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO:
# TODO Il programma dovrà verificare se una persona può entrare ad un evento
# TODO considerando che deve avere almeno 18 anni e un documento

eta = int(input("Quanti anni hai? "))
ha_documento = input("Hai il documento? ")

ha_documento = ha_documento == "si"

puo_entrare = eta >= 18 and ha_documento

print(f"Può entrare? {puo_entrare}")

# ? SPIEGAZIONE:
# ? Utilizzo un confronto per verificare se l'età è almeno 18.
# ? Con un altro confronto trasformo la risposta dell'utente in un valore bool.
# ? L'operatore and restituisce True solamente se entrambe le condizioni
# ? risultano True.
# ? Quindi la persona può entrare solamente se è maggiorenne e possiede
# ? il documento.

#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 20
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO:
# TODO Il programma dovrà utilizzare gli operatori and, or e not
# TODO per combinare diverse condizioni

piove = True
ho_ombrello = False

mi_bagno = piove and not ho_ombrello

print("Mi bagno?", mi_bagno)

# ? SPIEGAZIONE:
# ? and restituisce True solamente quando entrambe le condizioni sono True.
# ? or restituisce True quando almeno una delle condizioni è True.
# ? not inverte il valore booleano:
# ? True diventa False e False diventa True.
# ? In questo caso piove è True e ho_ombrello è False.
# ? Con not ho_ombrello ottengo True, quindi entrambe le condizioni
# ? di and sono vere e mi_bagno diventa True.