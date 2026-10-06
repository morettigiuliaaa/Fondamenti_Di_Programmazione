# ESERCIZI TERZA LEZIONE: errori, if(), for(), while(), funzioni(), stringhe()

# * ###############################################################################
# * ESERCIZI 21- DA SVOLGERE DURANTE IL LABORATORIO
# * ###############################################################################

# TODO Per ogni esercizio:
# TODO  1. leggete attentamente la consegna;
# TODO  2. completate la funzione al posto di TODO/pass;
# TODO  3. decommentate i test corrispondenti in fondo al file;
# TODO  4. eseguite il programma;
# TODO  5. provate almeno un caso diverso da quelli forniti.

# * Esempio: funzione + if + return
def voto_valido(voto):
    return 0 <= voto <= 30

print("Recap voto_valido:", voto_valido(27), voto_valido(35))


# * Esempio: for + contatore
def conta_a(parola):
    contatore = 0

    for carattere in parola.lower():
        if carattere == "a":
            contatore += 1

    return contatore

print("Recap conta_a:", conta_a("Azkaban"))


# ? ###############################################################################
# ? TEMA 0 - CAPIRE E CORREGGERE GLI ERRORI
# ? ###############################################################################

# ? In Python possiamo incontrare soprattutto tre tipi di errore:
# ? 1. ERRORE DI SINTASSI (SyntaxError)
# ?  Python non riesce a comprendere il codice e il programma non parte.
# ? 2. ERRORE DURANTE L'ESECUZIONE (runtime error)
# ?  Il programma parte, ma si interrompe durante l'esecuzione.
# ? 3. ERRORE LOGICO
# ?  Il programma viene eseguito senza messaggi di errore,
# ?  ma produce un risultato sbagliato.


#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 22 - CACCIA ALL'ERRORE
#  * ------------------------------------------------------------------------------

# TODO Per ciascun frammento:
# TODO - indicate il tipo di errore;
# TODO - individuate la riga che lo causa;
# TODO - correggete il codice e provatelo.

# ! A)
# ! def saluta(nome):
# !   print("Ciao " + nome)
# ! saluta()   # Che cosa manca?

def saluta(nome):
    print("Ciao " + nome)
saluta("Giulia")

# ? SPIEGAZIONE:
# ? Il valore da utilizzare nella funzione è mancante


# ! B)
# ! def maggiore(a, b):
# !   if a > b:
# !       return b
# !   else:
# !       return a   # Il programma parte, ma il risultato è corretto?

def maggiore(a, b):
    if a > b:
        return a
    else:
        return b

# ? SPIEGAZIONE:
# ? Il valori dei return erano invertiti

# ! C)
# ! eta = int(input("Inserisci la tua età: "))
# ! if eta >= 18   # Osservate attentamente questa riga
# !     print("Maggiorenne")

eta = int(input("Inserisci la tua età: "))
if (eta>=18): 
    print("Maggiorenne")

# ? SPIEGAZIONE:
# ? Mancano degli elementi di sintassi

# * ------------------------------------------------------------------------------
# * ESERCIZIO 23 - LEGGERE UN TRACEBACK
# * ------------------------------------------------------------------------------

# TODO Eseguite, una alla volta, le istruzioni seguenti togliendo il simbolo #.
# TODO Leggete il messaggio dal basso verso l'alto e individuate:
# TODO - il tipo di errore;
# TODO - la riga in cui si è verificato;
# TODO - la possibile correzione.

#print(6)                    # ! NameError
#print(int("ciao"))          # ! ValueError
#print("età: " + 20)         # ! TypeError
#print(10 / 0)               # ! ZeroDivisionError


# ? ###############################################################################
# ? TEMA 1 - CONDIZIONI
# ? ###############################################################################

# * ------------------------------------------------------------------------------
# * ESERCIZIO 24 - check_grade
# * ------------------------------------------------------------------------------

# TODO Scrivere una funzione check_grade(a, b, c) che:
# TODO - ritorna la somma dei tre voti se TUTTI sono compresi tra 0 e 30;
# TODO - ritorna -1 altrimenti.

# * Esempi:
# * check_grade(21, 18, 2)  -> 41
# * check_grade(21, 32, 2)  -> -1

def check_grade(a, b, c):
    if(0<=a<=30 and 0<=b<=30 and 0<=c<=30):
        return a+b+c
    else:
        return -1

check_grade(21, 18, 2)
check_grade(21, 32, 2)

# ? SPIEGAZIONE:
# ? Controllo tramite 'and' che tutti i valori siano nei range compresi
# ? Restituisco la somma di tutti in return se if = true
# ? Se if = false allora restituisco -1

# * ------------------------------------------------------------------------------
# * ESERCIZIO 25 - check_date
# * ------------------------------------------------------------------------------

# TODO Scrivere una funzione check_date(d, m, y) che ritorna True se la data è valida,
# TODO False altrimenti.
# TODO Possiamo ignorare gli anni bisestili.

# * Esempi:
# * check_date(30, 2, 2017) -> False
# * check_date(1, 1, 1111)  -> True
# * check_date(31, 4, 2011) -> False

def check_date(d, m, y):
    if (m < 1 or m > 12):
        return False

    if (d < 1):
        return False

    if (m == 2):
        if (y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)):
            return d <= 29
        else:
            return d <= 28

    elif (m == 4 or m == 6 or m == 9 or m == 11):
        return d <= 30

    else:
        return d <= 31

# ? SPIEGAZIONE:
# ? Come prima cosa controllo se il mese sia nel range dei mesi esistenti in un anno
# ? Controllo poi che il valore del giorno non sia inferiore allo 0
# ? Procedo nel controllare il mese di febbraio per vedere se sia bisestile
# ? Controllo che il giorno di febbraio non sia maggiore dei giorni disponibili
# ? Controllo che il giorno non superi 30 o 31 in base al mese

# ? ###############################################################################
# ? TEMA 2 - FOR E STRINGHE
# ? ###############################################################################

# * ------------------------------------------------------------------------------
# * ESERCIZIO 26 - somma_cifre
# * ------------------------------------------------------------------------------

# TODO Scrivere una funzione somma_cifre(s) che riceve una stringa composta da cifre
# TODO decimali e ritorna la somma delle cifre.

# * Esempio:
# * somma_cifre("85721") -> 23

def somma_cifre(s):
    somma = 0
    for i in s:
        somma += int(i)
    return somma

# ? SPIEGAZIONE:
# ? Pongo la veriabile somma a 0, faccio un for che scorra ogni singolo elemento della string s
# ? Addiziono ogni cifra e la dichiaro come intero, ottengo in output la somma di tutti N

# * ------------------------------------------------------------------------------
# * ESERCIZIO 27 - bin_str_to_dec
# * ESERCIZIO AGGIUNTIVO / SE FINITE PRIMA
# * ------------------------------------------------------------------------------

# TODO Scrivere una funzione bin_str_to_dec(s) che riceve una stringa binaria
# TODO e ritorna il corrispondente numero decimale.

# * Esempio:
# * bin_str_to_dec("00101") -> 5

# ! Suggerimento:
# ! nuovo_valore = vecchio_valore * 2 + nuova_cifra

def bin_str_to_dec(s):
    risultato = 0
    for c in s:
        risultato = risultato * 2 + int(c)
    return risultato

# ? SPIEGAZIONE:
# ? Pongo risultato a 0 e scorro la stringa s carattere per carattere.
# ? Ad ogni cifra raddoppio il valore accumulato (sposta le cifre già lette di una
# ? posizione, come ×10 in base 10) e sommo la nuova cifra convertita con int().
# ? Alla fine risultato contiene il numero decimale corrispondente.

# ? ###############################################################################
# ? TEMA 3 - FUNZIONI
# ? ###############################################################################

# * ------------------------------------------------------------------------------
# * ESERCIZIO 28 - cubic_root
# * ESERCIZIO AGGIUNTIVO / SE FINITE PRIMA
# * ------------------------------------------------------------------------------

# TODO Scrivere una funzione cubic_root(n) che prende un numero e ritorna
# TODO la sua radice cubica.

# ! Deve funzionare anche per numeri negativi.

# * Esempi:
# * cubic_root(8)  -> 2.0
# * cubic_root(-8) -> -2.0

def cubic_root(n):
    if n < 0:
        return -round((-n) ** (1/3), 10)
    return round(n ** (1/3), 10)

# ? SPIEGAZIONE:
# ? La radice cubica di n equivale a n elevato a 1/3. Python però, con una base
# ? negativa e un esponente frazionario, restituisce un numero complesso, quindi
# ? gestisco il segno a parte: se n è negativo calcolo la radice cubica del suo
# ? valore assoluto (-n) e poi cambio il segno del risultato, perché la radice
# ? cubica di un numero negativo è negativa (es. -8 -> -2.0).
# ? Se n è positivo o zero calcolo direttamente n ** (1/3).

# * ------------------------------------------------------------------------------
# * ESERCIZIO 29 - even_minus_odd
# * ------------------------------------------------------------------------------

# TODO Scrivere una funzione even_minus_odd(a, b, c, d, e) che ritorna:
# TODO somma dei numeri pari - somma dei numeri dispari

# * Esempio:
# * even_minus_odd(1, 2, 3, 4, 5) -> -3
# ! Provate a risolverlo SENZA usare liste.

# * CON LISTA
def even_minus_odd(a, b, c, d, e):
    somma_pari=0
    somma_dispari=0
    for i in [a,b,c,d,e]:
        if(i%2==0):
            somma_pari+=i
        else:
            somma_dispari+=i

    return somma_pari-somma_dispari

# * SENZA LISTA
def even_minus_odd(a, b, c, d, e):
    somma_pari=0
    somma_dispari=0
    if(a%2==0):
        somma_pari+=a
    else:
        somma_dispari+=a

    if(b%2==0):
        somma_pari+=b
    else:
        somma_dispari+=b

    if(c%2==0):
        somma_pari+=c
    else:
        somma_dispari+=c

    if(d%2==0):
        somma_pari+=d
    else:
        somma_dispari+=d

    if(e%2==0):
        somma_pari+=e
    else:
        somma_dispari+=e

    return somma_pari-somma_dispari    


# ? SPIEGAZIONE:
# ? Uso due variabili, somma_pari e somma_dispari, inizializzate a 0.
# ? Per ciascuno dei cinque numeri controllo con l'operatore % se il resto della
# ? divisione per 2 è 0: in quel caso il numero è pari e lo aggiungo a somma_pari,
# ? altrimenti è dispari e lo aggiungo a somma_dispari. Uso cinque if/else
# ? indipendenti, così ogni numero viene valutato.
# ? Alla fine ritorno somma_pari - somma_dispari. L'operatore % funziona
# ? correttamente anche con i numeri negativi.

# ? ###############################################################################
# ? TEMA 4 - WHILE E INPUT
# ? ###############################################################################

# * ------------------------------------------------------------------------------
# * ESERCIZIO 30 - chiedi_voto
# * ------------------------------------------------------------------------------

# TODO Scrivere una funzione chiedi_voto() che:
# TODO - legge un voto da input;
# TODO - continua a chiederlo finché non è compreso tra 0 e 30;
# TODO - ritorna il voto valido.

# ! Per semplicità assumiamo che l'utente inserisca sempre un intero.

def chiedi_voto():
    voto=int(input('Che voto hai?'))
    while voto<0 or voto>30:
        voto=int(input('Che voto hai?'))
    return voto

# ? SPIEGAZIONE:
# ? Leggo il voto con input() e lo converto in intero con int(). Finché il voto
# ? è fuori dall'intervallo valido (minore di 0 oppure maggiore di 30) rimango
# ? nel ciclo while e lo richiedo all'utente. Quando il voto è compreso tra 0 e 30
# ? (estremi inclusi) la condizione diventa falsa, il ciclo termina e la funzione
# ? ritorna il voto valido.

# * ------------------------------------------------------------------------------
# * ESERCIZIO 31 - strip_spazi
# * ESERCIZIO AGGIUNTIVO / SE FINITE PRIMA
# * ------------------------------------------------------------------------------

# TODO Scrivere una funzione strip_spazi(s) che elimina gli spazi " "
# TODO all'inizio e alla fine della stringa SENZA usare str.strip().

# * Esempi:
# * strip_spazi("   ciao mondo   ") -> "ciao mondo"
# * strip_spazi("ciao")             -> "ciao"
# * strip_spazi("     ")            -> ""

# * CON STRIP
def strip_spazi(s):
    return s.strip()

# * SENZA STRIP
def strip_spazi(s):
    x=0
    while x<len(s) and s[x]==' ':
        x+=1

    y=len(s) - 1
    while y>= 0 and s[y]==' ':
        y-=1
    return s[x:y + 1]

# ? SPIEGAZIONE:
# ? Uso due indici: x parte dall'inizio della stringa e y dall'ultimo carattere
# ? (len(s) - 1). Con un primo while faccio avanzare x finché il carattere s[x]
# ? è uno spazio, quindi x si ferma sul primo carattere diverso da spazio.
# ? Con un secondo while faccio retrocedere y finché s[y] è uno spazio, quindi
# ? y si ferma sull'ultimo carattere diverso da spazio.
# ? Nella condizione del primo while controllo prima x < len(s) e poi s[x],
# ? così non leggo mai un indice fuori dalla stringa (IndexError); lo stesso
# ? vale per y >= 0 nel secondo while.
# ? Alla fine ritorno la porzione s[x:y + 1]: il + 1 serve perché con lo
# ? slicing l'indice finale è escluso e voglio includere l'ultimo carattere utile.
# ? Gli spazi in mezzo non vengono toccati. Se la stringa è vuota o composta
# ? solo da spazi, x supera y e lo slicing restituisce la stringa vuota "".

# ! ###############################################################################
# ! TEST DEGLI ESERCIZI PRINCIPALI
# ! ###############################################################################

print("\ncheck_grade")
print(check_grade(21, 18, 2))      # 41
print(check_grade(21, 32, 2))      # -1
print(check_grade(21, 18, -2))     # -1

print("\ncheck_date")
print(check_date(30, 2, 2017))     # False
print(check_date(1, 1, 1111))      # True
print(check_date(31, 4, 2011))     # False
print(check_date(30, 4, 2011))     # True

print("\nsomma_cifre")
print(somma_cifre("85721"))         # 23
print(somma_cifre("00000"))         # 0

print("\nbin_str_to_dec")
print(bin_str_to_dec("00101"))      # 5
print(bin_str_to_dec("1111"))       # 15

print("\ncubic_root")
print(cubic_root(8))                # circa 2.0
print(cubic_root(-8))               # circa -2.0

print("\neven_minus_odd")
print(even_minus_odd(1, 2, 3, 4, 5))   # -3
print(even_minus_odd(2, 2, 2, 2, 2))   # 10
print(even_minus_odd(1, 1, 1, 1, 1))   # -5

print("\nchiedi_voto")
print("Voto accettato:", chiedi_voto())

print("\nstrip_spazi")
print(repr(strip_spazi("   ciao mondo   ")))  # 'ciao mondo'
print(repr(strip_spazi("ciao")))               # 'ciao'
print(repr(strip_spazi("     ")))              # ''


# ? ###############################################################################
# ? OPTIONAL - ESERCIZI AGGIUNTIVI
# ? Tratti anche dai laboratori degli anni precedenti.
# ? ###############################################################################

# * ------------------------------------------------------------------------------
# * OPTIONAL 32 - PICCOLI ESPERIMENTI CON GLI ERRORI
# * ------------------------------------------------------------------------------

# TODO A.1 Cosa succede se dimenticate gli apici alla fine di una stringa?
# ? SyntaxError: la stringa non viene chiusa (unterminated string literal).
# ? L'errore è segnalato sulla riga stessa. Solo con le triple virgolette
# ? ("""...""") il testo continuerebbe sulle righe successive.

# TODO A.2 Cosa succede se dividete un numero per 0?
# ? ZeroDivisionError

# TODO A.3 Cosa succede se in print dimenticate una o entrambe le parentesi?
# ? In Python 3 print è una funzione, quindi senza parentesi la chiamata non
# ? avviene. Con print "ciao" si ottiene SyntaxError (Missing parentheses in
# ? call to 'print'). Con print da solo non c'è errore ma non stampa nulla:
# ? l'espressione restituisce l'oggetto funzione. Con una sola parentesi,
# ? print("ciao", si ottiene SyntaxError (parentesi non chiusa).

# TODO A.4 Cosa succede con +2? E con 2++2?
# ? +2 vale 2: il + è l'operatore unario "più", che lascia il numero invariato.
# ? 2++2 vale 4: viene letto come 2 + (+2).

# TODO A.5 Cosa succede se scrivete 02?
# ? SyntaxError (leading zeros in decimal integer literals are not permitted).
# ? In Python 3 uno zero iniziale non è ammesso nei numeri interi decimali.
# ? Fa eccezione 0 da solo (e 00). Per l'ottale si scrive 0o2.

# TODO A.6 In Python possiamo scrivere xy al posto di x*y?
# ? No. xy viene letto come il nome di un'unica variabile, quindi se non è
# ? definita si ottiene NameError. Il prodotto va sempre scritto con *.

# TODO A.7 Cosa succede se facciamo 42 = n?
# ? SyntaxError (cannot assign to literal). A sinistra dell'= ci deve essere
# ? una variabile, non un valore. Si scrive n = 42.

# TODO A.8 Cosa succede con x = y = 1?
# ? È un assegnamento multiplo: sia x sia y valgono 1. Viene assegnato prima
# ? y = 1 e poi x prende lo stesso valore.

# TODO A.9 Cosa succede se mettete ; alla fine di un'istruzione? E un punto?
# ? Il ; è permesso: serve a separare più istruzioni sulla stessa riga
# ? (x = 1; y = 2) e alla fine non dà errore, anche se non si usa.
# ? Il punto invece dà SyntaxError, perché in Python indica l'accesso a un
# ? attributo o un metodo (come s.strip()) e dopo di esso si aspetta un nome.


# * ------------------------------------------------------------------------------
# * OPTIONAL 33 - CALCOLI
# * ------------------------------------------------------------------------------

# TODO B.1 Scrivere una espressione che calcoli il numero di secondi
# TODO che ci sono in 42 minuti e 42 secondi.

# ? 42 * 60 + 42

# TODO B.2 Scrivere una espressione che calcoli il numero di miglia
# TODO che ci sono in 10 chilometri. (1 miglio = 1.61 km).

# ? 10/1.61 

# TODO B.3 Calcolare la velocità media e la cadenza media
# TODO (tempo per miglio, in minuti e secondi) di un corridore
# TODO che corre 10 km in 42 minuti e 42 secondi.

# ? vel med = (10/1.61)/(42*60+42) && cad med = (42*60+42)/(10/1.61) 
# ? cad med min = cad med // 60 && cad med sec = cad med % 60

# TODO B.4 Il volume di una sfera di raggio r è:
# TODO 4/3 * PI * r^3
# TODO Calcolare il volume di una sfera di raggio 5.

# ? 4/3 * 3.14 * 5^3

# TODO B.5 Il prezzo di copertina di un libro è 24.95 euro.
# TODO Una libreria ottiene il 40% di sconto.
# TODO La spedizione costa 3 euro per la prima copia e 0.75 euro
# TODO per ogni copia aggiuntiva.
# TODO Calcolare il costo totale di 60 copie.

# ? Formula sconto: prezzo - ((prezzo*sconto)/100)
# ? (24.95*60) - (((24.95*60)*40)/100) + 3 +(0.75*59)

# TODO B.6 Si esce di casa alle 6:52.
# TODO Primo miglio: 8 min 15 sec
# TODO Tre miglia: 7 min 12 sec per miglio
# TODO Ultimo miglio: 9 min 45 sec
# TODO A che ora si torna a casa?

# ? secondi=15+(3*12)+45
# ? secondi_rimasti=secondi%60
# ? min_aggiuntivi=secondi//60
# ? min_per_ora=(min_aggiuntivi+8+(3*7)+9+52)
# ? min=min_per_ora%60
# ? ore=(min_per_ora//60)+6
# ? ore:min:secondi_rimasti


# * ------------------------------------------------------------------------------
# * OPTIONAL 34 - STRINGHE
# * ------------------------------------------------------------------------------

# TODO C.1 Avete una stringa di 5 caratteri. Il carattere centrale è il punto.
# * Ad esempio:
# * s = "52.29"
# * Stampare il numero decimale rappresentato dalla stringa
# * come numero, non come stringa.

def dec_frac_str_to_dec(s):
    return float(s)

# ? SPIEGAZIONE:
# ? La funzione float() converte una stringa che rappresenta un numero decimale
# ? (con il punto come separatore) nel corrispondente numero di tipo float.
# ? Quindi float("52.29") restituisce 52.29 come numero e non come stringa,
# ? e non serve separare a mano parte intera e parte decimale.

def dec_frac_str_to_decs(s):
    return int(s[3:])

# ? SPIEGAZIONE:
# ? La stringa ha 5 caratteri e il punto è in posizione 2. Con lo slicing s[3:]
# ? prendo tutto ciò che viene dopo il punto, cioè le cifre decimali, e le
# ? converto in numero con int(). Ritorno quindi 29 come intero e non come stringa.

# * ------------------------------------------------------------------------------
# * OPTIONAL 35 - FUNZIONI
# * ------------------------------------------------------------------------------

# TODO D.1 Scrivere una funzione root_max(a, b, c) che calcola le radici
# * dell'equazione:
# * a*x^2 + b*x + c
# * e ritorna la maggiore.
# * Se le radici sono complesse, restituisce una qualsiasi delle due.

def root_max(a, b, c):
    delta = (b**2) - 4 * a * c
    x1 = (-b + delta ** 0.5) / (2*a)
    x2 = (-b - delta ** 0.5) / (2*a)
    if (delta>=0):
        return max(x1,x2)
    else: 
        return x2

# ? SPIEGAZIONE:
# ? Calcolo il discriminante delta = b**2 - 4*a*c. Poi calcolo le due radici
# ? con la formula risolutiva, usando delta ** 0.5 per la radice quadrata
# ? (con un delta negativo Python restituisce un numero complesso invece di
# ? dare errore) e mettendo tra parentesi tutto il numeratore (-b +/- radice),
# ? perché la divisione ha precedenza sulla somma.
# ? Se delta >= 0 le radici sono reali e ritorno la maggiore con max(); se
# ? delta < 0 sono complesse, non confrontabili, e ritorno x2 (una qualsiasi).

# TODO D.2 Scrivere una funzione roots(a, b, c) che calcola le radici
# * dell'equazione:
# * a*x^2 + b*x + c
# * e le ritorna entrambe.

def roots(a, b, c):
    delta = (b**2) - 4 * a * c
    x1 = (-b + delta ** 0.5) / (2*a)
    x2 = (-b - delta ** 0.5) / (2*a)
    return x1,x2

# ? SPIEGAZIONE:
# ? Calcolo il discriminante delta = b**2 - 4*a*c e con la formula risolutiva
# ? ricavo le due radici x1 = (-b + radice) / (2*a) e x2 = (-b - radice) / (2*a),
# ? usando delta ** 0.5 per la radice quadrata e le parentesi sul numeratore.
# ? Con un delta negativo Python restituisce numeri complessi invece di dare
# ? errore. Ritorno entrambe le radici come tupla con return x1, x2.

# TODO D.3 Scrivere una funzione print_hello() che legge un nome da input
# * e ritorna una stringa formata da:
# * "Ciao " + nome + ". Buona giornata!"

def print_hello():
    nome = input('Come ti chiami?')
    return f'Ciao {nome}. Buona giornata!'

# ? SPIEGAZIONE:
# ? Leggo il nome con input() e lo salvo nella variabile nome. Costruisco poi
# ? la stringa con una f-string, che inserisce il valore di nome tra "Ciao " e
# ? ". Buona giornata!", e la ritorno con return invece di stamparla, come
# ? richiesto dal testo.

# ? ###############################################################################
# ? TEST OPTIONAL
# ? ###############################################################################

print("\ndec_frac_str_to_dec")
print(dec_frac_str_to_dec("52.29"))

print("\ndec_frac_str_to_decs")
print(dec_frac_str_to_decs("52.29"))

print("\nroot_max")
print(root_max(1, -5, 6))

print("\nroots")
print(roots(1, -5, 6))

print("\nprint_hello")
print(print_hello())