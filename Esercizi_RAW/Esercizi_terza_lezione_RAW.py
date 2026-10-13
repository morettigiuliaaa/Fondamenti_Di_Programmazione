#  ESERCIZI TERZA LEZIONE: errori, if, for, while, funzioni, stringhe

#  * ------------------------------------------------------------------------------
#  * COME LAVORARE
#  * ------------------------------------------------------------------------------

# TODO Aprite questo file nella VM con VS Code
# TODO Completate una funzione alla volta
# TODO Eseguite il file con "Run Python File" oppure da terminale
# TODO Provate anche casi diversi da quelli forniti

# ? SPIEGAZIONE:
# ? Completo una funzione alla volta, poi eseguo il programma e provo altri input
# ? I test con print() servono a controllare i risultati senza costruire un framework di test


#  * ------------------------------------------------------------------------------
#  * ESERCIZI DA SVOLGERE DURANTE IL LABORATORIO
#  * ------------------------------------------------------------------------------

# TODO Durante le 2 ore di laboratorio concentratevi, nell'ordine, sugli esercizi principali
# TODO 0.1 Caccia all'errore
# TODO 0.2 Leggere un traceback
# TODO 1.1 check_grade
# TODO 1.2 check_date
# TODO 2.1 somma_cifre
# TODO 3.2 even_minus_odd
# TODO 4.1 chiedi_voto
# TODO Se terminate questi esercizi, continuate con gli esercizi aggiuntivi
# TODO 2.2 bin_str_to_dec
# TODO 3.1 cubic_root
# TODO 4.2 strip_spazi
# TODO In fondo al file trovate inoltre una sezione di esercizi optional
# TODO Non è necessario completare tutti gli esercizi durante il laboratorio
# TODO Per ogni esercizio leggete la consegna, completate la funzione, decommentate i test, eseguite il programma e provate un caso diverso


#  * ------------------------------------------------------------------------------
#  * RECAP VELOCE: FUNZIONI, IF E CICLI
#  * ------------------------------------------------------------------------------

# Esempio: funzione + if + return

def voto_valido(voto):
    return 0 <= voto <= 30

print("Recap voto_valido:", voto_valido(27), voto_valido(35))

# ? SPIEGAZIONE:
# ? Ricevo un voto e controllo se è compreso tra 0 e 30
# ? Ritorno True se il voto è valido, altrimenti ritorno False


# Esempio: for + contatore

def conta_a(parola):
    contatore = 0
    for carattere in parola.lower():
        if carattere == "a":
            contatore += 1
    return contatore

print("Recap conta_a:", conta_a("Azkaban"))

# ? SPIEGAZIONE:
# ? Prendo una parola e la trasformo in minuscolo
# ? Scorro i caratteri con for e aumento il contatore ogni volta che trovo la lettera a
# ? Ritorno il numero totale di occorrenze


#  * ------------------------------------------------------------------------------
#  * TEMA 0: CAPIRE E CORREGGERE GLI ERRORI
#  * ------------------------------------------------------------------------------

# TODO Riconoscete i tre principali tipi di errore in Python
# TODO SyntaxError: Python non riesce a comprendere il codice e il programma non parte
# TODO Runtime error: il programma parte ma si interrompe durante l'esecuzione
# TODO Errore logico: il programma viene eseguito ma produce un risultato sbagliato


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 0.1: CACCIA ALL'ERRORE
#  * ------------------------------------------------------------------------------

# TODO Per ciascun frammento indicate il tipo di errore
# TODO Individuate la riga che causa l'errore
# TODO Correggete il codice e provatelo

# A)
# def saluta(nome):
#     print("Ciao " + nome)
#
# saluta()  # Che cosa manca?

# B)
# def maggiore(a, b):
#     if a > b:
#         return b
#     else:
#         return a  # Il programma parte, ma il risultato è corretto?

# C)
# eta = int(input("Inserisci la tua età: "))
# if eta >= 18  # Osservate attentamente questa riga
#     print("Maggiorenne")

# ? SPIEGAZIONE:
# ? Esamino ogni frammento, individuo il problema e correggo la riga interessata


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 0.2: LEGGERE UN TRACEBACK
#  * ------------------------------------------------------------------------------

# TODO Eseguite una alla volta le istruzioni seguenti togliendo il simbolo #
# TODO Leggete il messaggio dal basso verso l'alto e individuate il tipo di errore
# TODO Individuate la riga in cui si è verificato e la possibile correzione

# print(numero_non_definito)  # NameError
# print(int("ciao"))          # ValueError
# print("età: " + 20)          # TypeError
# print(10 / 0)               # ZeroDivisionError

# ? SPIEGAZIONE:
# ? Eseguo un'istruzione alla volta e leggo il traceback per trovare il tipo e la posizione dell'errore


#  * ------------------------------------------------------------------------------
#  * TEMA 1: CONDIZIONI
#  * ------------------------------------------------------------------------------


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 1.1: check_grade
#  * ------------------------------------------------------------------------------

# TODO Scrivete una funzione check_grade(a, b, c) che ritorni la somma dei tre voti se tutti sono compresi tra 0 e 30
# TODO Se almeno un voto non è valido, ritornate -1

# * Esempi:
# * check_grade(21, 18, 2) -> 41
# * check_grade(21, 32, 2) -> -1

def check_grade(a, b, c):
    # TODO
    pass

# ? SPIEGAZIONE:
# ? Controllo che ogni voto sia compreso tra 0 e 30
# ? Se tutti i voti sono validi, ritorno la loro somma, altrimenti ritorno -1


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 1.2: check_date
#  * ------------------------------------------------------------------------------

# TODO Scrivete una funzione check_date(d, m, y) che ritorni True se la data è valida e False altrimenti
# TODO Per semplicità ignorate gli anni bisestili

# * Esempi:
# * check_date(30, 2, 2017) -> False
# * check_date(1, 1, 1111) -> True
# * check_date(31, 4, 2011) -> False

def check_date(d, m, y):
    # TODO
    pass

# ? SPIEGAZIONE:
# ? Controllo che il mese sia valido e che il giorno rientri nel numero di giorni del mese
# ? Ritorno True se la data è valida, altrimenti ritorno False


#  * ------------------------------------------------------------------------------
#  * TEMA 2: FOR E STRINGHE
#  * ------------------------------------------------------------------------------


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 2.1: somma_cifre
#  * ------------------------------------------------------------------------------

# TODO Scrivete una funzione somma_cifre(s) che riceva una stringa composta da cifre decimali
# TODO Ritornate la somma delle cifre presenti nella stringa

# * Esempio:
# * somma_cifre("85721") -> 23

def somma_cifre(s):
    # TODO
    pass

# ? SPIEGAZIONE:
# ? Scorro la stringa carattere per carattere, converto ogni cifra in intero e la aggiungo alla somma
# ? Ritorno la somma ottenuta


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 2.2: bin_str_to_dec
#  * ESERCIZIO AGGIUNTIVO / SE FINITE PRIMA
#  * ------------------------------------------------------------------------------

# TODO Scrivete una funzione bin_str_to_dec(s) che riceva una stringa binaria
# TODO Ritornate il numero decimale corrispondente
# TODO Utilizzate il suggerimento nuovo_valore = vecchio_valore * 2 + nuova_cifra

# * Esempio:
# * bin_str_to_dec("00101") -> 5

def bin_str_to_dec(s):
    # TODO
    pass

# ? SPIEGAZIONE:
# ? Scorro le cifre binarie da sinistra a destra e aggiorno il valore moltiplicandolo per 2 e aggiungendo la cifra
# ? Ritorno il valore decimale calcolato


#  * ------------------------------------------------------------------------------
#  * TEMA 3: FUNZIONI
#  * ------------------------------------------------------------------------------


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 3.1: cubic_root
#  * ESERCIZIO AGGIUNTIVO / SE FINITE PRIMA
#  * ------------------------------------------------------------------------------

# TODO Scrivete una funzione cubic_root(n) che prenda un numero e ritorni la sua radice cubica
# TODO La funzione deve funzionare anche per numeri negativi

# * Esempi:
# * cubic_root(8) -> 2.0
# * cubic_root(-8) -> -2.0

def cubic_root(n):
    # TODO
    pass

# ? SPIEGAZIONE:
# ? Calcolo la radice cubica del numero mantenendo il segno anche quando il numero è negativo
# ? Ritorno il risultato


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 3.2: even_minus_odd
#  * ------------------------------------------------------------------------------

# TODO Scrivete una funzione even_minus_odd(a, b, c, d, e) che ritorni la somma dei numeri pari meno la somma dei numeri dispari
# TODO Provate a risolvere l'esercizio senza usare liste

# * Esempio:
# * even_minus_odd(1, 2, 3, 4, 5) -> -3

def even_minus_odd(a, b, c, d, e):
    # TODO
    pass

# ? SPIEGAZIONE:
# ? Controllo ciascun numero e aggiungo i numeri pari alla prima somma e quelli dispari alla seconda
# ? Ritorno la differenza tra la somma dei pari e quella dei dispari


#  * ------------------------------------------------------------------------------
#  * TEMA 4: WHILE E INPUT
#  * ------------------------------------------------------------------------------


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 4.1: chiedi_voto
#  * ------------------------------------------------------------------------------

# TODO Scrivete una funzione chiedi_voto() che legga un voto da input
# TODO Continuate a chiedere il voto finché non è compreso tra 0 e 30
# TODO Ritornate il voto valido
# TODO Per semplicità assumete che l'utente inserisca sempre un numero intero

def chiedi_voto():
    # TODO
    pass

# ? SPIEGAZIONE:
# ? Leggo un voto e utilizzo while per richiederlo finché non rientra nell'intervallo da 0 a 30
# ? Ritorno il voto valido


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 4.2: strip_spazi
#  * ESERCIZIO AGGIUNTIVO / SE FINITE PRIMA
#  * ------------------------------------------------------------------------------

# TODO Scrivete una funzione strip_spazi(s) che elimini gli spazi all'inizio e alla fine della stringa
# TODO Non utilizzate il metodo str.strip()

# * Esempi:
# * strip_spazi("   ciao mondo   ") -> "ciao mondo"
# * strip_spazi("ciao") -> "ciao"
# * strip_spazi("     ") -> ""

def strip_spazi(s):
    # TODO
    pass

# ? SPIEGAZIONE:
# ? Individuo il primo e l'ultimo carattere che non sono spazi
# ? Ritorno la parte di stringa compresa tra questi due estremi


#  * ------------------------------------------------------------------------------
#  * TEST DEGLI ESERCIZI PRINCIPALI
#  * ------------------------------------------------------------------------------

# TODO Decommentate progressivamente i test quando avete completato le funzioni

# print("\ncheck_grade")
# print(check_grade(21, 18, 2))      # 41
# print(check_grade(21, 32, 2))      # -1
# print(check_grade(21, 18, -2))     # -1

# print("\ncheck_date")
# print(check_date(30, 2, 2017))     # False
# print(check_date(1, 1, 1111))      # True
# print(check_date(31, 4, 2011))     # False
# print(check_date(30, 4, 2011))     # True

# print("\nsomma_cifre")
# print(somma_cifre("85721"))        # 23
# print(somma_cifre("00000"))        # 0

# print("\nbin_str_to_dec")
# print(bin_str_to_dec("00101"))     # 5
# print(bin_str_to_dec("1111"))      # 15

# print("\ncubic_root")
# print(cubic_root(8))               # circa 2.0
# print(cubic_root(-8))              # circa -2.0

# print("\neven_minus_odd")
# print(even_minus_odd(1, 2, 3, 4, 5))  # -3
# print(even_minus_odd(2, 2, 2, 2, 2))  # 10
# print(even_minus_odd(1, 1, 1, 1, 1))  # -5

# print("\nchiedi_voto")
# print("Voto accettato:", chiedi_voto())

# print("\nstrip_spazi")
# print(repr(strip_spazi("   ciao mondo   ")))  # 'ciao mondo'
# print(repr(strip_spazi("ciao")))             # 'ciao'
# print(repr(strip_spazi("     ")))            # ''


#  * ------------------------------------------------------------------------------
#  * OPTIONAL: ESERCIZI AGGIUNTIVI
#  * ------------------------------------------------------------------------------


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO OPTIONAL A: PICCOLI ESPERIMENTI CON GLI ERRORI
#  * ------------------------------------------------------------------------------

# TODO Provate a rispondere alle seguenti domande
# TODO A.1 Cosa succede se dimenticate gli apici alla fine di una stringa
# TODO A.2 Cosa succede se dividete un numero per 0
# TODO A.3 Cosa succede se in print dimenticate una o entrambe le parentesi
# TODO A.4 Cosa succede con +2 e con 2++2
# TODO A.5 Cosa succede se scrivete 02
# TODO A.6 In Python possiamo scrivere xy al posto di x*y
# TODO A.7 Cosa succede se scrivete 42 = n
# TODO A.8 Cosa succede con x = y = 1
# TODO A.9 Cosa succede se mettete ; alla fine di un'istruzione e cosa succede con un punto


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO OPTIONAL B: CALCOLI
#  * ------------------------------------------------------------------------------

# TODO B.1 Scrivete un'espressione che calcoli il numero di secondi in 42 minuti e 42 secondi
# TODO B.2 Scrivete un'espressione che calcoli il numero di miglia in 10 chilometri considerando 1 miglio = 1.61 km
# TODO B.3 Calcolate la velocità media e la cadenza media in minuti e secondi per miglio di un corridore che corre 10 km in 42 minuti e 42 secondi
# TODO B.4 Calcolate il volume di una sfera di raggio 5 utilizzando la formula 4/3 * PI * r**3
# TODO B.5 Calcolate il costo totale di 60 libri con prezzo di copertina di 24.95 euro, sconto del 40%, spedizione di 3 euro per la prima copia e 0.75 euro per ogni copia aggiuntiva
# TODO B.6 Calcolate l'ora di ritorno a casa se si esce alle 6:52 e si percorrono il primo miglio in 8 min 15 sec, i tre miglia successivi in 7 min 12 sec ciascuno e l'ultimo miglio in 9 min 45 sec


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO OPTIONAL C: STRINGHE
#  * ------------------------------------------------------------------------------

# TODO Scrivete una funzione dec_frac_str_to_dec(s) che riceva una stringa di 5 caratteri con il punto in posizione centrale
# TODO Convertite la stringa in un numero decimale e non lasciate il risultato come stringa

# * Esempio:
# * s = "52.29"

def dec_frac_str_to_dec(s):
    # TODO
    pass

# ? SPIEGAZIONE:
# ? Separo la parte intera dalla parte decimale e converto entrambe in numeri
# ? Combino le due parti per ottenere il valore decimale


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO OPTIONAL D.1: root_max
#  * ------------------------------------------------------------------------------

# TODO Scrivete una funzione root_max(a, b, c) che calcoli le radici dell'equazione a*x**2 + b*x + c
# TODO Ritornate la radice maggiore
# TODO Se le radici sono complesse, restituite una qualsiasi delle due

def root_max(a, b, c):
    # TODO
    pass

# ? SPIEGAZIONE:
# ? Calcolo il discriminante e ricavo le radici dell'equazione di secondo grado
# ? Ritorno la radice maggiore oppure una delle radici complesse


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO OPTIONAL D.2: roots
#  * ------------------------------------------------------------------------------

# TODO Scrivete una funzione roots(a, b, c) che calcoli le radici dell'equazione a*x**2 + b*x + c
# TODO Ritornate entrambe le radici

def roots(a, b, c):
    # TODO
    pass

# ? SPIEGAZIONE:
# ? Calcolo il discriminante e ricavo entrambe le radici dell'equazione di secondo grado
# ? Ritorno le due radici


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO OPTIONAL D.3: print_hello
#  * ------------------------------------------------------------------------------

# TODO Scrivete una funzione print_hello() che legga un nome da input
# TODO Ritornate una stringa formata da "Ciao " seguito dal nome e da ". Buona giornata!"

def print_hello():
    # TODO
    pass

# ? SPIEGAZIONE:
# ? Leggo il nome con input e costruisco il messaggio concatenando le stringhe
# ? Ritorno il messaggio completo


#  * ------------------------------------------------------------------------------
#  * TEST OPTIONAL
#  * ------------------------------------------------------------------------------

# TODO Decommentate i test dopo aver completato le funzioni optional

# print("\ndec_frac_str_to_dec")
# print(dec_frac_str_to_dec("52.29"))

# print("\nroot_max")
# print(root_max(1, -5, 6))

# print("\nroots")
# print(roots(1, -5, 6))

# print("\nprint_hello")
# print(print_hello())