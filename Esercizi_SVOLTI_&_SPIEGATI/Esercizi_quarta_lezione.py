# ESERCIZI QUARTA LEZIONE: list, indicizzazione, slicing, mutabilità, append(),
# extend(), insert(), remove(), pop(), in, for, enumerate(), aliasing, copy(),
# == e is, tuple, unpacking, set, dict.

#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 1
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO:
# TODO Il programma dovrà creare una lista con i nomi di 4 amici
# TODO e visualizzare la lista, il numero di elementi,
# TODO il primo elemento e l'ultimo elemento (usando un indice negativo)


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 2
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO:
# TODO Data la seguente lista, visualizzare tramite slicing:
# TODO i primi 3 elementi, gli elementi dal secondo al quinto,
# TODO un elemento ogni due e la lista al contrario

personaggi = ["Harry", "Hermione", "Ron", "Luna", "Neville", "Ginny"]


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 3
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI SISTEMARE IL SEGUENTE ESERCIZIO CONTENENTE ERRORI:
# TODO Il programma dovrebbe visualizzare l'ultimo elemento della lista
# TODO e sostituire il secondo elemento con "Draco"
# TODO il programma però genera degli errori

# ! case = ["Grifondoro", "Serpeverde", "Corvonero", "Tassorosso"]
# ! print(case[4])
# ! case = "Draco"
# ! print(case)


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 4
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO:
# TODO Il programma dovrà chiedere all'utente 3 nomi uno alla volta
# TODO e inserirli in una lista usando append(),
# TODO poi visualizzare la lista finale e la sua lunghezza


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 5
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO:
# TODO Date le seguenti liste, visualizzare cosa succede
# TODO usando append() sulla prima copia e extend() sulla seconda copia
# TODO e confrontare le due lunghezze ottenute

A = ["Harry", "Hermione"]
B = ["Ron", "Luna"]


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 6
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO:
# TODO Data la lista di pozioni, il programma dovrà:
# TODO inserire "Amortentia" in posizione 1, rimuovere "Polisucco",
# TODO estrarre l'ultimo elemento con pop() e visualizzare
# TODO l'elemento estratto e la lista finale

pozioni = ["Polisucco", "Felix Felicis", "Veritaserum"]


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 7
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI SISTEMARE IL SEGUENTE ESERCIZIO CONTENENTE ERRORI:
# TODO Il programma dovrebbe aggiungere "Ron" alla lista
# TODO e visualizzare la lista aggiornata
# TODO il programma però non visualizza il risultato atteso

# ! studenti = ["Harry", "Hermione"]
# ! studenti = studenti.append("Ron")
# ! print(studenti)


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 8
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO:
# TODO Il programma dovrà chiedere un incantesimo e verificare
# TODO se è presente nella lista, visualizzando "Incantesimo conosciuto"
# TODO oppure "Incantesimo non conosciuto"

incantesimi = ["Lumos", "Alohomora", "Expelliarmus"]


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 9
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO:
# TODO Data la lista dei voti, il programma dovrà costruire una nuova lista
# TODO contenente solo i voti maggiori o uguali a 18
# TODO utilizzando for, if e append()

voti = [12, 18, 25, 16, 30, 21]


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 10
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO:
# TODO Data la lista dei voti, il programma dovrà calcolare
# TODO la somma e la media dei voti utilizzando un accumulatore
# TODO e visualizzarle con una f-string

voti = [28, 30, 25, 27]


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 11
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO:
# TODO Il programma dovrà visualizzare ogni elemento della lista
# TODO insieme alla sua posizione utilizzando enumerate()
# TODO nel formato: 0 Harry

personaggi = ["Harry", "Hermione", "Ron"]


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 12
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO:
# TODO Data la lista di numeri, il programma dovrà costruire
# TODO una nuova lista contenente solo i numeri pari
# TODO senza modificare la lista originale mentre la attraversa

numeri = [1, 2, 3, 4, 5, 6, 7, 8]


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 13
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO:
# TODO Il programma dovrà creare B come alias di A e modificare il primo
# TODO elemento attraverso B, poi creare C come copia indipendente di A
# TODO e modificare C. Visualizzare A, B e C
# TODO e verificare con == e is cosa hanno in comune

A = [1, 2, 3]


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 14
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO:
# TODO Il programma dovrà creare una tupla con nome, età e casa di uno studente,
# TODO visualizzarne il primo e l'ultimo elemento, fare l'unpacking
# TODO in tre variabili e infine scambiare due variabili
# TODO senza usare una variabile temporanea

studente = ("Hermione", 17, "Grifondoro")


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 15
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO:
# TODO Il programma dovrà rimuovere i duplicati da una lista usando un set
# TODO, aggiungere un nuovo elemento al set con add()
# TODO e verificare se un elemento è presente con in

case_studenti = ["Grifondoro", "Serpeverde", "Grifondoro", "Corvonero", "Serpeverde"]


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 16
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO:
# TODO Dato il seguente dizionario, il programma dovrà visualizzare
# TODO il voto di Hermione, aggiungere Luna con voto 29,
# TODO modificare il voto di Ron a 27 e attraversare il dizionario
# TODO con .items() visualizzando nome e voto

voti = {"Harry": 28, "Hermione": 30, "Ron": 25}


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 17
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI COMPLETARE IL PROGRAMMA: Dato un elenco di studenti con il voto,
# TODO il programma deve contare quanti sono promossi (voto >= 18)
# TODO e costruire la lista dei nomi dei bocciati

# * studenti = {"Harry": 28, "Hermione": 30, "Ron": 15, "Luna": 17, "Neville": 21}
# * promossi = 
# * bocciati = []
# * for nome, voto in studenti.items():
# *     if voto  :
# *         promossi = 
# *     else:
# *         bocciati.
# * print("Promossi:", )
# * print("Bocciati:", )


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 18 - MINI CHALLENGE
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO:
# TODO Data la lista delle case, rispondere a queste domande:
# TODO 1. Quanti studenti sono in "Serpeverde"?
# TODO 2. Costruisci una lista contenente solo le case diverse da "Serpeverde".
# TODO 3. Quali case compaiono almeno una volta? Usa un set.
# TODO 4. Costruisci un dizionario che associ a ogni casa
# TODO    il numero di studenti che ne fanno parte.

case_studenti = [
    "Grifondoro",
    "Serpeverde",
    "Grifondoro",
    "Corvonero",
    "Serpeverde",
    "Tassorosso",
    "Grifondoro",
    "Serpeverde"
]