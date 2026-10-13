# ESERCIZI PER CASA: funzioni, Dizionari, Liste, Tuple, Insiemi e Sort

#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 1: Manipolazione base delle liste
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO: Crea una lista con i numeri da 1 a 10
# TODO Aggiungi il numero 11 alla fine della lista
# TODO Inserisci il numero 0 all'inizio della lista
# TODO Rimuovi il numero 5
# TODO Stampa la lunghezza della lista finale


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 2: Operazioni con liste
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO: Data la lista numeri = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
# TODO Trova la somma di tutti gli elementi
# TODO Trova il valore massimo e minimo
# TODO Conta quante volte appare il numero 1
# TODO Crea una nuova lista con solo i numeri pari


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 3: Liste annidate
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO: Crea una lista di liste che rappresenti una matrice 3x3
# TODO Utilizza i seguenti valori per la matrice
# TODO 1 2 3
# TODO 4 5 6
# TODO 7 8 9
# TODO Scrivi il codice per stampare la diagonale principale (1, 5, 9)


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 4: Conteggio caratteri con dizionari
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO: Scrivi una funzione che prenda una stringa
# TODO E restituisca un dizionario con il conteggio di ogni carattere

# * Esempio di codice:
# * def conta_caratteri(testo):
# *     # Il tuo codice qui
# *     pass
# *
# * Test:
# * print(conta_caratteri("hello world"))
# *
# * Output atteso:
# * {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 5: Unione dizionari
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO: Dati due dizionari, scrivi il codice per unirli
# TODO Se una chiave è presente in entrambi i dizionari, somma i valori

# * Esempio di codice:
# * dict1 = {'a': 1, 'b': 2, 'c': 3}
# * dict2 = {'b': 3, 'c': 4, 'd': 5}
# * # Il tuo codice qui
# *
# * Risultato atteso:
# * {'a': 1, 'b': 5, 'c': 7, 'd': 5}


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 6: Coordinate con tuple
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO: Crea una lista di tuple che rappresentino coordinate (x, y)
# TODO Crea 5 punti casuali
# TODO Trova il punto più lontano dall'origine (0, 0)
# TODO Ordina i punti per distanza dall'origine

# * Esempio di codice:
# * import math
# * # Il tuo codice qui


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 7: Scambio di variabili con tuple
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO: Usa le tuple per scambiare i valori di due variabili
# TODO Esegui lo scambio senza usare una variabile temporanea

# * Esempio di codice:
# * a = 10
# * b = 20
# * # Il tuo codice qui per scambiare a e b
# * print(f"a = {a}, b = {b}")
# *
# * Output atteso:
# * a = 20, b = 10


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 8: Ritorno multiplo con tuple
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO: Scrivi una funzione che prenda una lista di numeri
# TODO E restituisca una tupla contenente minimo, massimo e media

# * Esempio di codice:
# * def statistiche(numeri):
# *     # Il tuo codice qui
# *     pass
# *
# * Test:
# * print(statistiche([1, 5, 3, 9, 2]))
# *
# * Output atteso:
# * (1, 9, 4.0)


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 9: Operazioni base con insiemi (Set)
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO: Dati due insiemi di numeri
# TODO set1 = {1, 2, 3, 4, 5}
# TODO set2 = {4, 5, 6, 7, 8}
# TODO Calcola l'unione dei due insiemi
# TODO Calcola l'intersezione dei due insiemi
# TODO Calcola la differenza (elementi in set1 ma non in set2)
# TODO Calcola la differenza simmetrica

# * Esempio di codice:
# * set1 = {1, 2, 3, 4, 5}
# * set2 = {4, 5, 6, 7, 8}
# * # Il tuo codice qui


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 10: Rimozione duplicati
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO: Scrivi una funzione che prenda una lista
# TODO E restituisca una nuova lista senza duplicati, mantenendo l'ordine originale

# * Esempio di codice:
# * def rimuovi_duplicati(lista):
# *     # Il tuo codice qui
# *     pass
# *
# * Test:
# * print(rimuovi_duplicati([1, 2, 2, 3, 1, 4, 5, 4]))
# *
# * Output atteso:
# * [1, 2, 3, 4, 5]


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 11: Lettere uniche
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO: Scrivi una funzione che prenda due parole
# TODO E restituisca le lettere che appaiono in entrambe

# * Esempio di codice:
# * def lettere_comuni(parola1, parola2):
# *     # Il tuo codice qui
# *     pass
# *
# * Test:
# * print(lettere_comuni("python", "java"))
# *
# * Output atteso:
# * {'a'}


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 12: Ordinamento personalizzato
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO: Data una lista di nomi, ordinali in ordine alfabetico
# TODO Ordina i nomi per lunghezza dal più corto al più lungo
# TODO Ordina i nomi per lunghezza inversa dal più lungo al più corto

# * Esempio di codice:
# * nomi = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
# * # Il tuo codice qui


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 13: Ordinamento di dizionari
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO: Data una lista di dizionari che rappresentano persone
# TODO Ordina i dizionari in base all'età crescente

# * Esempio di codice:
# * persone = [
# *     {'nome': 'Alice', 'eta': 25},
# *     {'nome': 'Bob', 'eta': 30},
# *     {'nome': 'Charlie', 'eta': 20}
# * ]
# * # Il tuo codice qui


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 14: Ordinamento complesso
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO: Data una lista di tuple (nome, voto)
# TODO Ordina le tuple per voto decrescente
# TODO In caso di parità, ordina per nome alfabetico

# * Esempio di codice:
# * studenti = [('Alice', 85), ('Bob', 92), ('Charlie', 85), ('Diana', 78)]
# * # Il tuo codice qui


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 15: Funzione con parametri opzionali
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO: Scrivi una funzione che calcoli l'area di un rettangolo
# TODO Se viene passato un solo parametro, considera il rettangolo come un quadrato

# * Esempio di codice:
# * def area_rettangolo(larghezza, altezza=None):
# *     # Il tuo codice qui
# *     pass
# *
# * Test:
# * print(area_rettangolo(5))
# * print(area_rettangolo(4, 6))
# *
# * Output atteso:
# * 25 (quadrato)
# * 24 (rettangolo)


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 16: Elaborazione dati studenti
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO: Scrivi un programma che gestisca i voti degli studenti
# TODO Suddividi il programma in funzioni più piccole
# TODO Scrivi una funzione elabora_voti(dati_studenti) che prenda una lista di tuple (nome, lista_voti)
# TODO Restituisci un dizionario con nome e media dei voti
# TODO Restituisci una lista di studenti ordinata per media decrescente
# TODO Restituisci un insieme degli studenti che hanno almeno un voto maggiore o uguale a 9
# TODO Restituisci le statistiche globali con media della classe, voto massimo e voto minimo

# * Esempio di codice:
# * def elabora_voti(dati_studenti):
# *
# *     """
# *     Prende una lista di tuple (nome, lista_voti) e restituisce:
# *     - Dizionario con nome -> media voti
# *     - Lista studenti ordinata per media decrescente
# *     - Set degli studenti che hanno almeno un voto >= 9
# *     - Statistiche globali (media classe, voto max, voto min)
# *     """
# *
# *     # Il tuo codice qui
# *     pass
# *
# * Test:
# * studenti = [
# *     ("Alice", [8, 7, 9, 6]),
# *     ("Bob", [9, 8, 10, 7]),
# *     ("Charlie", [6, 5, 7, 8]),
# *     ("Diana", [10, 9, 9, 8])
# * ]
# *
# * risultati = elabora_voti(studenti)
# * print(risultati)