# ESERCIZI PRIMA LEZIONE: print(), input(), int(), float(), str(), if().

#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 1 
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO: Il programma dovrà chiedere l'età ed il nome
# TODO dovrà restituire in output il valore dell'età nell'anno successivo

nome = input("Come ti chiami?")
eta = int(input("Quanti anni hai?"))
print("Ciao", nome , "il prossimo anno avrai", eta + 1, "anni!")

# ? SPIEGAZIONE:
# ? Prendo in input la stringa del nome e l'int dell'età per poi manipolarlo e fare delle operazioni aritmetiche
# ? Tramite addizione ricavo l'età futura dell'utente e stampo il tutto in output

#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 2
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI COMPLETARE IL PROGRAMMA: Il programma deve chiedere la marca della macchina e anno di immatricolazione
# TODO dovrà restituire in output l'anno della macchina nel 2026 e verificare se abbia almeno 10 anni

# * marca = 
# * anno = 
# * eta_macchina= 2026 - 
# * maggiore_dieci_anni =    > 10
# * print("La tua",  , "ha",  , "anni")
# * print("È da cambiare?", )

marca = input("Di che marca è la tua macchina?")
anno = int(input("Di che anno è la tua macchina?"))

eta_macchina= 2026 - anno
if(eta_macchina>10):
    maggiore_dieci_anni = 'si'
else:
    maggiore_dieci_anni = 'no'

print("La tua", marca, "ha", eta_macchina , "anni")
print("È da cambiare?", maggiore_dieci_anni)

# ? SPIEGAZIONE:
# ? Prendo il programma dato a metà e ne aggiungo la sintassi per i dati che avremo in input
# ? Ricavo tramite formula l'età della macchina e tramite un if dichiaro il valore stringa della variabile maggiore_dieci_anni 
# ? Se il boolean di maggiore_dieci_anni risulta true o false avrà un si o no come risposta per l'output

#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 3
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO: Il programma deve chiedere base ed altezza di un rettangolo con valore float
# TODO dovrà restituire in output area e perimetro

base = float(input("Valore della base:"))
altezza = float(input("Valore dell'altezza:"))

perimetro = (altezza+base) * 2
area = base * altezza

print("Il perimetro è di", perimetro ,"cm, mentre l'area è di", area , "cm")

# ? SPIEGAZIONE:
# ? Prendo i numeri in input che rappresentino base ed altezza dichiarandoli come FLOAT ( numeri aventi virgola )
# ? Ricavo area e perimetro tramite formule e stampo in output i risultati

#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 4
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO: Il programma riceverà in input un tempo N espresso in secondi
# TODO dovrà restituire in input lo stesso tempo convertito in ore, minuti, e secondi

durata_n = int(input("Indicami il tempo in secondi:"))

ore = int(durata_n / 3600)
resto_ore = durata_n % 3600
min = int(resto_ore / 60)
resto_min = resto_ore % 60

print("Il tuo tempo è di", ore , ":", min , ":", resto_min)

# ? SPIEGAZIONE:
# ? Prendo il numero dato in sec, lo divido per il quantitativo di sec in un ora e ricavo le ore totali
# ? Ricavo il resto dei secondi rimanenti alla precedente operazione e ripeto di nuovo l'operazione per i minuti
# ? Infinte facendo il resto ricavo i secondi rimanenti

#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 5
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI SISTEMARE IL SEGUENTE ESERCIZIO CONTENENTE ERRORI: Il programma dovrebbe chiedere 2 numeri e visualizzarne la somma
# TODO il programma però presenta vari errori

# ! primo = input("Inserisci il primo numero: 
# ! secondo = input("Inserisci il secondo numero: "")
# ! somma = primo + secondo
# ! print("La somma è : " somma)

primo = int(input("Inserisci il primo numero:"))
secondo = int(input("Inserisci il secondo numero: "))

somma = primo + secondo

print("La somma è :", somma)

# ? SPIEGAZIONE:
# ? Nella prima e seconda riga non vengono definiti gli int e ci sono vari errori nella sintassi del testo
# ? Due type string non possono fare un return di type int e il print è sintassato male