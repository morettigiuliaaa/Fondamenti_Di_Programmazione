# ESERCIZI PER CASA: assegnamenti, Condizioni (if, match) e Cicli (for, while)

#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 1: Assegnamenti potenziati
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO: Chiede di inserire un numero intero N - Lo modifica
# TODO In sequenza con += 5, *= 3, -= 4, //= 2, %= 7, **= 2 - Stampa il valore di N
# TODO Dopo ogni operazione - Chiede poi una parola W, le aggiunge '!' con += e la
# TODO Ripete 3 volte con *=, stampando W dopo ogni passo

# * Esempio di output:
# * Inserisci un numero intero: 10
# * Dopo += 5: 15
# * Dopo *= 3: 45
# * Dopo -= 4: 41
# * Dopo //= 2: 20
# * Dopo %= 7: 6
# * Dopo **= 2: 36
# * Inserisci una parola: ciao
# * Dopo += '!': ciao!
# * Dopo *= 3: ciao!ciao!ciao!


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 2: Scambio e rotazione di variabili
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO: Chiede due numeri interi A e B e li scambia con un
# TODO Assegnamento multiplo (senza variabili temporanee) - Chiede poi tre parole
# TODO A, B e C e le ruota di una posizione verso sinistra: A prende il valore di B,
# TODO B quello di C e C quello di A (sempre con un solo assegnamento multiplo) -
# TODO Stampa i valori prima e dopo ciascuna operazione

# *  Esempio di output:
# * Inserisci il primo numero: 3
# * Inserisci il secondo numero: 8
# * Prima dello scambio: A = 3, B = 8
# * Dopo lo scambio: A = 8, B = 3
# * Inserisci la prima parola: uno
# * Inserisci la seconda parola: due
# * Inserisci la terza parola: tre
# * Prima della rotazione: A = uno, B = due, C = tre
# * Dopo la rotazione: A = due, B = tre, C = uno


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 3: Spacchettamento di una lista
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO: Chiede di inserire in una sola riga nome, cognome
# TODO E anno di nascita separati da spazi - Usa split() e un assegnamento multiplo
# TODO Per spacchettare i tre valori in tre variabili - Calcola l’età assumendo che l’anno
# TODO Corrente sia 2026 - Stampa una scheda con i dati usando l’interpolazione (f-string)

# * Esempio di output:
# * Inserisci nome, cognome e anno di nascita: Mario Rossi 2001
# * --- Scheda ---
# * Nome: Mario
# * Cognome: Rossi
# * Anno di nascita: 2001
# * Età nel 2026: 25


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 4: Che tipo di triangolo è? (if, elif, else)
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO: Chiede di inserire le lunghezze di tre lati a, b e c 
# TODO (numeri interi positivi)
# TODO Se i tre lati non formano un triangolo (cioè un lato è maggiore o uguale alla somma degli altri due)
# TODO Stampa che non è un triangolo
# TODO Altrimenti stampa se il triangolo è equilatero (tre lati uguali)
# TODO Isoscele (esattamente due lati uguali) o scaleno (tre lati diversi)

# * Esempi di output (tre esecuzioni diverse):
# * Inserisci il lato a: 5
# * Inserisci il lato b: 5
# * Inserisci il lato c: 8
# * Il triangolo è isoscele
# *
# * Inserisci il lato a: 1
# * Inserisci il lato b: 2
# * Inserisci il lato c: 5
# * Non è un triangolo
# * 
# * Inserisci il lato a: 6
# * Inserisci il lato b: 6
# * Inserisci il lato c: 6
# * Il triangolo è equilatero

#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 5: Calcolatrice con match
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO: Chiede due numeri interi A e B e un operatore
# TODO Tra +, -, *, x, /, //, %, ** - Usa l'istruzione match sull'operatore e stampa
# TODO L'operazione completa con il suo risultato - Accetta sia * che x per il prodotto
# TODO (usando | in un unico case) - Per /, // e % controlla prima che B non sia 0:
# TODO In quel caso stampa un messaggio di errore - Per qualsiasi altro operatore stampa
# TODO Che non è valido (caso di default _)

# * Esempio di output:
# * Primo numero: 7
# * Secondo numero: 2
# * Operatore (+ - * x / // % **): //
# * 7 // 2 = 3
# *
# * Primo numero: 3
# * Secondo numero: 4
# * Operatore (+ - * x / // % **): x
# * 3 * 4 = 12
# *
# * Primo numero: 10
# * Secondo numero: 0
# * Operatore (+ - * x / // % **): /
# * Errore: divisione per zero
# *
# * Primo numero: 2
# * Secondo numero: 5
# * Operatore (+ - * x / // % **): ^
# * Operatore non valido: ^


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 6: Interprete di comandi (match strutturale)
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO: Chiede di inserire un comando e lo divide in parole
# TODO Con split() - Usa match sulla lista di parole con questi case
# TODO ['ciao'] stampa Ciao!
# TODO ['ciao', nome] stampa Ciao seguito dal nome
# TODO ['somma', a, b] stampa la somma dei due numeri (ricordati di convertirli in interi)
# TODO ['esci'] oppure ['fine'] stampa Arrivederci!
# TODO Qualsiasi altra cosa stampa Comando non riconosciuto

# * Esempio di output:
# * Comando: ciao Paperino
# * Ciao Paperino!
# *
# * Comando: somma 12 30
# * 42
# *
# * Comando: fine
# * Arrivederci!
# *
# * Comando: ciao a tutti
# * Comando non riconosciuto


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 7: Tabellina, conto alla rovescia e somma (for e range)
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO: Chiede di inserire un numero intero positivo N
# TODO Stampa la tabellina di N (da 1 a 10) usando for e range
# TODO Stampa su una sola riga il conto alla rovescia da N a 1 usando range con passo negativo
# TODO E print(..., end=' ')
# TODO Calcola con un for e l'operatore += la somma dei numeri pari da 2 a N
# TODO (N compreso, se pari) e la stampa

# * Esempio di output:
# * Inserisci un intero positivo: 4
# *
# * Tabellina del 4:
# * 4 x 1 = 4
# * 4 x 2 = 8
# * ...
# * 4 x 10 = 40
# * Conto alla rovescia: 4 3 2 1
# * Somma dei pari da 2 a 4: 6


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 8: Numero primo (for con break ed else)
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO: Chiede di inserire un numero intero N maggiore
# TODO O uguale a 2 - Con un ciclo for su range(2, N) cerca il primo divisore D di N
# TODO (cioè N % D == 0) - Se lo trova, stampa che N non è primo indicando il divisore
# TODO Ed esce subito dal ciclo con break - Se il ciclo finisce senza interruzioni
# TODO (usa il ramo else del for), stampa che N è primo

# * Esempio di output:
# * Inserisci un intero maggiore o uguale a 2: 91
# * 91 non è primo: è divisibile per 7
# *
# * Inserisci un intero maggiore o uguale a 2: 13
# * 13 è primo


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 9: Indovina il numero (while)
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO: Salva un numero segreto in una variabile
# TODO (per esempio 42) - Usa un ciclo while per chiedere un numero finché l'utente non indovina
# TODO Dopo ogni tentativo sbagliato stampa Troppo alto oppure Troppo basso
# TODO Conta i tentativi con l'operatore +=
# TODO Alla fine stampa quanti tentativi sono serviti

# * Esempio di output:
# * Indovina il numero: 50
# * Troppo alto
# * Indovina il numero: 30
# * Troppo basso
# * Indovina il numero: 42
# * Hai indovinato in 3 tentativi!

# * ATTENZIONE: Nel while aggiornate sempre la variabile usata nella condizione
# * Altrimenti il ciclo non si ferma più


#  * ------------------------------------------------------------------------------
#  * NOTE PER GLI STUDENTI
#  * ------------------------------------------------------------------------------

# TODO Utilizzate input() per leggere dati e convertite con int() quando servono numeri
# TODO Gli assegnamenti potenziati sono +=, -=, *=, /=, //=, %=, **=
# TODO L'assegnamento multiplo valuta prima tutta la parte destra e poi assegna
# TODO A, B = B, A scambia i valori
# TODO Ricordate l'indentazione dopo if, elif, else, match, case, for e while
# TODO range(fine), range(inizio, fine) e range(inizio, fine, passo)
# TODO Il valore fine non viene mai prodotto
# TODO Usate print(..., end=' ') per stampare sulla stessa riga
# TODO break esce dal ciclo, continue passa all'iterazione successiva
# TODO L'else del ciclo parte solo se non c'è stato break
# TODO Sperimentate variando i valori di input