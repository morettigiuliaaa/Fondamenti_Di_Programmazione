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

# * LA FUNZIONE DA I NOMI
def amici():
    lista_amici = ['Lucia','Marco','Luca','Sandra']
    print(f'Lista amici: {lista_amici}')
    print(f'Numero di elementi: {len(lista_amici)}')
    print(f'Primo elemento: {lista_amici[0]}')
    print(f'Ultimo elemento: {lista_amici[-1]}')

amici()

# ? SPIEGAZIONE:
# ? Creo una lista con i nomi degli amici, scritta tra parentesi quadre e con gli
# ? elementi separati da virgole. Poi uso delle f-string per stampare i dati.
# ? Stampo la lista intera, che viene mostrata con le parentesi e gli apici.
# ? len() restituisce il numero di elementi della lista (4).
# ? Con l'indice [0] accedo al primo elemento, perché gli indici partono da 0.
# ? Con l'indice negativo [-1] accedo all'ultimo elemento, senza dover conoscere
# ? la lunghezza della lista (equivale a lista_amici[len(lista_amici) - 1]).
# ? La funzione stampa soltanto, non ritorna nulla: per vedere l'output va chiamata
# ? con amici().

# * I NOMI VENGONO RICAVATI DA STRINGA
def amici_split(s):
    lista_amici = s.split(',')
    print(f'Lista amici: {lista_amici}')
    print(f'Numero di elementi: {len(lista_amici)}')
    print(f'Primo elemento: {lista_amici[0]}')
    print(f'Ultimo elemento: {lista_amici[-1]}')

amici_split('Lucia,Marco,Luca,Sandra')

# ? SPIEGAZIONE:
# ? La funzione riceve una stringa con i nomi separati da virgole. Con il metodo
# ? split(',') divido la stringa in corrispondenza di ogni virgola e ottengo una
# ? lista di stringhe: ['Lucia', 'Marco', 'Luca', 'Sandra'].
# ? Da qui in poi il resto è identico alla funzione precedente: len() per il numero
# ? di elementi, [0] per il primo e [-1] per l'ultimo.
# ? Il vantaggio rispetto alla prima versione è che la funzione funziona con
# ? qualsiasi stringa, non solo con quei quattro nomi.
# ? Se la stringa avesse degli spazi dopo le virgole ('Lucia, Marco'), gli spazi
# ? resterebbero dentro i nomi (' Marco'): in quel caso si può usare split(', ').
# ? Come nella prima funzione, la chiamata finale stampa i risultati.

#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 2
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO:
# TODO Data la seguente lista, visualizzare tramite slicing:
# TODO i primi 3 elementi, gli elementi dal secondo al quinto,
# TODO un elemento ogni due e la lista al contrario

personaggi = ["Harry", "Hermione", "Ron", "Luna", "Neville", "Ginny"]

def slicing_personaggi(personaggi):
    print(f'Primi 3 elementi: {personaggi[:3]}')
    print(f'Dal secondo al quinto: {personaggi[1:5]}')
    print(f'Un elemento ogni due: {personaggi[::2]}')
    print(f'Lista al contrario: {personaggi[::-1]}')

slicing_personaggi(personaggi)

# ? SPIEGAZIONE:
# ? La funzione riceve una lista di personaggi e utilizza lo slicing per
# ? selezionare gli elementi in base alla loro posizione.
# ? Con personaggi[:3] prendo gli elementi dall'inizio della lista fino
# ? all'indice 3 escluso, quindi ottengo i primi 3 elementi:
# ? ['Harry', 'Hermione', 'Ron'].
# ? Con personaggi[1:5] parto dall'indice 1, cioè dal secondo elemento,
# ? e arrivo fino all'indice 5 escluso, ottenendo quindi gli elementi
# ? dal secondo al quinto: ['Hermione', 'Ron', 'Luna', 'Neville'].
# ? Con personaggi[::2] non specifico né l'inizio né la fine e imposto
# ? solo il passo a 2: questo significa prendere un elemento e saltarne
# ? uno, ottenendo ['Harry', 'Ron', 'Neville'].
# ? Infine, con personaggi[::-1] imposto un passo di -1, quindi percorro
# ? la lista dalla fine all'inizio e ottengo la lista al contrario:
# ? ['Ginny', 'Neville', 'Luna', 'Ron', 'Hermione', 'Harry'].
# ? La chiamata finale esegue la funzione passando la lista personaggi
# ? e stampa tutti i risultati.

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

case = ["Grifondoro", "Serpeverde", "Corvonero", "Tassorosso"]
print(case[-1])
case[1] = "Draco"
print(case)

# ? SPIEGAZIONE:
# ? La lista contiene quattro elementi e gli indici vanno da 0 a 3.
# ? Per visualizzare l'ultimo elemento uso case[-1], perché l'indice -1
# ? indica sempre l'ultimo elemento della lista: 'Tassorosso'.
# ? Nel codice iniziale case[4] genera un errore perché l'indice 4 non
# ? esiste: l'ultimo elemento si trova infatti all'indice 3.
# ? Per sostituire il secondo elemento devo usare case[1], perché gli
# ? indici partono da 0: l'indice 0 è il primo elemento e l'indice 1 è il secondo.
# ? Con case[1] = "Draco" modifico direttamente il secondo elemento
# ? della lista, sostituendo 'Serpeverde' con 'Draco'.
# ? Nel codice iniziale case = "Draco" era sbagliato perché non modificava
# ? un elemento della lista, ma sostituiva completamente la variabile
# ? case con una stringa.
# ? La stampa finale visualizza quindi la lista modificata:
# ? ['Grifondoro', 'Draco', 'Corvonero', 'Tassorosso'].

#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 4
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO:
# TODO Il programma dovrà chiedere all'utente 3 nomi uno alla volta
# TODO e inserirli in una lista usando append(),
# TODO poi visualizzare la lista finale e la sua lunghezza

def inserisci_nomi():
    nomi = []
    for i in range (3):
        nome = input(f"Inserisci il nome {i + 1}: ")
        nomi.append(nome)
    print(f'Lista finale: {nomi}')
    print(f'Lunghezza della lista: {len(nomi)}')

inserisci_nomi()

# ? SPIEGAZIONE:
# ? La funzione crea inizialmente una lista vuota chiamata nomi, nella quale
# ? verranno inseriti i nomi forniti dall'utente.
# ? Con il ciclo for i in range(3) ripeto le istruzioni 3 volte, perché
# ? devo chiedere all'utente esattamente 3 nomi.
# ? La variabile i assume i valori 0, 1 e 2. Per visualizzare correttamente
# ? il numero del nome richiesto uso i + 1, così vengono mostrati 1, 2 e 3
# ? invece di 0, 1 e 2.
# ? Con input() chiedo all'utente di inserire un nome e salvo il valore
# ? nella variabile nome.
# ? Con nomi.append(nome) aggiungo il nome inserito alla fine della lista.
# ? Dopo il ciclo, la lista contiene quindi tutti e 3 i nomi inseriti.
# ? Con print() visualizzo la lista finale, mentre len(nomi) restituisce
# ? il numero di elementi presenti nella lista, che in questo caso sarà 3.
# ? La chiamata finale inserisci_nomi() esegue la funzione e permette
# ? all'utente di inserire i tre nomi.

#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 5
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO:
# TODO Date le seguenti liste, visualizzare cosa succede
# TODO usando append() sulla prima copia e extend() sulla seconda copia
# TODO e confrontare le due lunghezze ottenute

A = ["Harry", "Hermione"]
B = ["Ron", "Luna"]

A.append(B)
B.extend(A)

# ? SPIEGAZIONE:
# ? Abbiamo due liste separate: A contiene 'Harry' e 'Hermione', mentre B
# ? contiene 'Ron' e 'Luna'.
# ? Con A.append(B) aggiungo l'intera lista B come un unico elemento alla
# ? fine di A. Dopo questa operazione A diventa:
# ? ['Harry', 'Hermione', ['Ron', 'Luna']].
# ? Quindi append() aggiunge la lista B come elemento singolo e la lunghezza
# ? di A diventa 3, non 4.
# ? Con B.extend(A) aggiungo invece a B tutti gli elementi presenti nella
# ? lista A, uno alla volta. È importante ricordare che in questo momento
# ? A è già stata modificata da append().
# ? Di conseguenza B diventa:
# ? ['Ron', 'Luna', 'Harry', 'Hermione', ['Ron', 'Luna']].
# ? La lunghezza di B diventa quindi 5.
# ? La differenza principale è che append() aggiunge un elemento alla volta,
# ? anche se quell'elemento è una lista, mentre extend() aggiunge alla lista
# ? tutti gli elementi contenuti nell'altra lista.
# ? In questo esercizio l'ordine delle istruzioni è importante: quando viene
# ? eseguito B.extend(A), A contiene già la lista B al suo interno.

#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 6
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO:
# TODO Data la lista di pozioni, il programma dovrà:
# TODO inserire "Amortentia" in posizione 1, rimuovere "Polisucco",
# TODO estrarre l'ultimo elemento con pop() e visualizzare
# TODO l'elemento estratto e la lista finale

pozioni = ["Polisucco", "Felix Felicis", "Veritaserum"]

def modifica_pozioni(pozioni):
    pozioni.insert(1, "Amortentia")
    pozioni.remove("Polisucco")
    ultimo_estratto = pozioni.pop()
    print(f'Ultimo elemento estratto: {ultimo_estratto}')
    print(f'Lista finale: {pozioni}')

modifica_pozioni(pozioni)

# ? SPIEGAZIONE:
# ? La lista pozioni contiene inizialmente tre elementi: "Polisucco",
# ? "Felix Felicis" e "Veritaserum".
# ? Con insert(1, "Amortentia") aggiungo "Amortentia" nella posizione
# ? con indice 1, quindi tra "Polisucco" e "Felix Felicis".
# ? Con remove("Polisucco") elimino dalla lista l'elemento con quel valore.
# ? Con pop() estraggo e rimuovo l'ultimo elemento della lista. Il valore
# ? estratto viene restituito da pop() e può essere salvato in una variabile.
# ? In questo modo posso visualizzare sia l'elemento estratto sia la lista
# ? rimasta dopo le modifiche.
# ? La differenza tra remove() e pop() è che remove() elimina un elemento
# ? specificando il suo valore, mentre pop() elimina un elemento in base
# ? alla sua posizione e restituisce l'elemento eliminato.


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

studenti = ["Harry", "Hermione"]
studenti.append("Ron")
print(studenti)

# ? SPIEGAZIONE:
# ? La lista contiene inizialmente due elementi. Con studenti.append("Ron")
# ? aggiungo "Ron" alla fine della lista, quindi la lista diventa:
# ? ['Harry', 'Hermione', 'Ron'].
# ? Nel codice errato era presente studenti = studenti.append("Ron").
# ? Questo è sbagliato perché append() modifica direttamente la lista e
# ? non restituisce una nuova lista: restituisce None.
# ? Di conseguenza, assegnando il risultato a studenti, la variabile avrebbe
# ? assunto il valore None e la stampa non avrebbe mostrato la lista attesa.
# ? Per questo motivo bisogna semplicemente usare studenti.append("Ron")
# ? senza assegnare il risultato alla variabile.
# ? La stampa finale visualizza quindi la lista aggiornata.

#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 8
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO:
# TODO Il programma dovrà chiedere un incantesimo e verificare
# TODO se è presente nella lista, visualizzando "Incantesimo conosciuto"
# TODO oppure "Incantesimo non conosciuto"

incantesimi = ["Lumos", "Alohomora", "Expelliarmus"]

def chiedi_incantesimo(incantesimi):
    incantesimo_chiesto = input('Dimmi un incantesimo')
    if(incantesimo_chiesto in incantesimi):
        print('Incantesimo conosciuto')
    else:
        print('Incantesimo non conosciuto')

chiedi_incantesimo(incantesimi)

# ? SPIEGAZIONE:
# ? La funzione chiede all'utente di inserire un incantesimo tramite input()
# ? e salva il valore inserito nella variabile incantesimo_chiesto.
# ? Con l'operatore in verifico se l'incantesimo inserito è presente nella
# ? lista incantesimi. L'espressione incantesimo_chiesto in incantesimi
# ? restituisce True se l'elemento è presente e False se non è presente.
# ? Se la condizione è True viene eseguito il primo print() e viene
# ? visualizzato "Incantesimo conosciuto".
# ? Se invece la condizione è False viene eseguito else e viene visualizzato
# ? "Incantesimo non conosciuto".
# ? In questo caso è preferibile usare in invece di index(), perché non ci
# ? interessa conoscere la posizione dell'incantesimo, ma solo sapere se
# ? è presente oppure no nella lista.
# ? La chiamata finale esegue la funzione passando la lista degli incantesimi.

#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 9
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO:
# TODO Data la lista dei voti, il programma dovrà costruire una nuova lista
# TODO contenente solo i voti maggiori o uguali a 18
# TODO utilizzando for, if e append()

voti = [12, 18, 25, 16, 30, 21]

def fix_voti(voti):
    lista_ordinata = []
    for i in voti:
        if(i>=18):
            lista_ordinata.append(i)
    print(lista_ordinata)

fix_voti(voti)

# ? SPIEGAZIONE:
# ? La funzione crea inizialmente una lista vuota chiamata lista_ordinata,
# ? nella quale verranno inseriti solamente i voti maggiori o uguali a 18.
# ? Con il ciclo for i in voti scorro direttamente tutti gli elementi della
# ? lista voti. Ad ogni iterazione, quindi, i contiene direttamente il valore
# ? del voto corrente e non la sua posizione nella lista.
# ? Con if(i >= 18) controllo se il voto corrente è maggiore o uguale a 18.
# ? Se la condizione è vera, con append(i) aggiungo il voto alla lista
# ? lista_ordinata.
# ? Il ciclo analizza quindi tutti i voti: 12 e 16 vengono esclusi perché
# ? sono minori di 18, mentre 18, 25, 30 e 21 vengono aggiunti alla nuova
# ? lista.
# ? Alla fine lista_ordinata contiene [18, 25, 30, 21].
# ? Con print(lista_ordinata) visualizzo la nuova lista ottenuta dopo aver
# ? terminato il ciclo.
# ? La chiamata finale fix_voti(voti) esegue la funzione passando la lista
# ? dei voti come parametro.

#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 10
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO:
# TODO Data la lista dei voti, il programma dovrà calcolare
# TODO la somma e la media dei voti utilizzando un accumulatore
# TODO e visualizzarle con una f-string

voti = [28, 30, 25, 27]

def som_med_voti(voti):
    accomulatore=0
    for i in voti:
        accomulatore+=i
    print(f'La media è {accomulatore/len(voti)}')
    print(f'La somma è {accomulatore}')

som_med_voti(voti)

# ? SPIEGAZIONE:
# ? La funzione inizializza la variabile accumulatore a 0. Questa variabile
# ? viene utilizzata per sommare progressivamente tutti i voti presenti
# ? nella lista.
# ? Con il ciclo for i in voti scorro direttamente tutti gli elementi della
# ? lista. Ad ogni iterazione, con accumulatore += i aggiungo il voto corrente
# ? al valore già presente nell'accumulatore.
# ? Alla fine del ciclo, l'accumulatore contiene la somma di tutti i voti,
# ? quindi in questo caso contiene 110.
# ? Per calcolare la media divido la somma per il numero di voti, ottenuto
# ? con len(voti). In questo caso 110 / 4 = 27.5.
# ? Con le f-string posso inserire direttamente i valori delle variabili
# ? all'interno del testo da visualizzare.
# ? La prima print() visualizza quindi la media, mentre la seconda visualizza
# ? la somma dei voti.
# ? La chiamata finale som_med_voti(voti) esegue la funzione passando la
# ? lista dei voti come parametro.

#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 11
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO:
# TODO Il programma dovrà visualizzare ogni elemento della lista
# TODO insieme alla sua posizione utilizzando enumerate()
# TODO nel formato: 0 Harry

personaggi = ["Harry", "Hermione", "Ron"]

def enum_lista(personaggi):
    for i, personaggio in enumerate(personaggi):
        print(f'{i} {personaggio}')

enum_lista(personaggi)

# ? SPIEGAZIONE:
# ? La funzione riceve una lista di personaggi e utilizza enumerate() per
# ? ottenere contemporaneamente la posizione e l'elemento della lista.
# ? Con for i, personaggio in enumerate(personaggi) ad ogni iterazione
# ? la variabile i contiene l'indice dell'elemento, mentre personaggio
# ? contiene il valore corrispondente.
# ? Gli indici partono da 0, quindi per la lista data otteniamo:
# ? 0 Harry
# ? 1 Hermione
# ? 2 Ron
# ? Con la f-string f'{i} {personaggio}' visualizzo l'indice seguito
# ? dall'elemento, nel formato richiesto dall'esercizio.
# ? La chiamata finale enum_lista(personaggi) esegue la funzione passando
# ? la lista dei personaggi.

#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 12
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO:
# TODO Data la lista di numeri, il programma dovrà costruire
# TODO una nuova lista contenente solo i numeri pari
# TODO senza modificare la lista originale mentre la attraversa

numeri = [1, 2, 3, 4, 5, 6, 7, 8]

def pari(numeri):
    lista = []
    for i in numeri:
        if(i%2==0):
            lista.append(i)
    print(lista)

pari(numeri)

# ? SPIEGAZIONE:
# ? La funzione crea inizialmente una lista vuota chiamata lista, nella quale
# ? verranno inseriti solamente i numeri pari.
# ? Con il ciclo for i in numeri scorro direttamente tutti gli elementi
# ? della lista numeri senza modificarla.
# ? Con if(i % 2 == 0) controllo se il numero corrente è pari. L'operatore %
# ? restituisce il resto della divisione: se il resto della divisione per 2
# ? è 0, significa che il numero è pari.
# ? Se la condizione è vera, con append(i) aggiungo il numero alla nuova
# ? lista.
# ? Alla fine del ciclo lista contiene [2, 4, 6, 8].
# ? Con print(lista) visualizzo la nuova lista contenente solamente i numeri
# ? pari.
# ? La lista numeri originale non viene modificata, perché durante il ciclo
# ? vengono solamente letti i suoi elementi e inseriti quelli pari in una
# ? lista separata.

#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 13
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO:
# TODO Il programma dovrà creare B come alias di A e modificare il primo
# TODO elemento attraverso B, poi creare C come copia indipendente di A
# TODO e modificare C. Visualizzare A, B e C
# TODO e verificare con == e is cosa hanno in comune

A = [1, 2, 3]

B=A
B[0]=19
C=A.copy()
C[2]=90
print(A,B,C)
print(A == B)
print(A is B)
print(A == C)
print(A is C)

# ? SPIEGAZIONE:
# ? La lista A viene inizialmente creata con i valori [1, 2, 3].
# ? Con B = A creo un alias di A, quindi B non è una nuova lista, ma un
# ? secondo riferimento alla stessa lista.
# ? Per questo, modificando B[0] = 19, viene modificato anche il primo
# ? elemento di A. A e B avranno quindi entrambe i valori [19, 2, 3].
# ? Con C = A.copy() creo invece una copia indipendente della lista A.
# ? C contiene inizialmente gli stessi valori di A, ma rappresenta una
# ? lista diversa e può essere modificata senza modificare A.
# ? Con C[2] = 90 modifico quindi solo il terzo elemento di C, che diventa
# ? [19, 2, 90], mentre A rimane [19, 2, 3].
# ? L'operatore == verifica se due liste hanno gli stessi valori, mentre
# ? l'operatore is verifica se due variabili fanno riferimento allo stesso
# ? oggetto.
# ? A == B restituisce True perché A e B hanno gli stessi valori e
# ? A is B restituisce True perché sono la stessa lista.
# ? A == C restituisce False perché le due liste hanno valori diversi,
# ? mentre A is C restituisce False perché C è una copia indipendente di A.

#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 14
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO:
# TODO Il programma dovrà creare una tupla con nome, età e casa di uno studente,
# TODO visualizzarne il primo e l'ultimo elemento, fare l'unpacking
# TODO in tre variabili e infine scambiare due variabili
# TODO senza usare una variabile temporanea

studente = ("Hermione", 17, "Grifondoro")

print(f'Primo elemento: {studente[0]}')
print(f'Ultimo elemento: {studente[-1]}')

nome, età, casa = studente
print(f'Nome: {nome}, Età: {età}, Casa: {casa}')

# ? SPIEGAZIONE:
# ? La tupla studente contiene tre elementi: il nome, l'età e la casa dello
# ? studente. Una tupla viene definita usando le parentesi tonde e, a
# ? differenza delle liste, non può essere modificata dopo la creazione.
# ? Con studente[0] accedo al primo elemento della tupla, quindi al nome
# ? "Hermione".
# ? Con studente[-1] accedo all'ultimo elemento, quindi alla casa
# ? "Grifondoro".
# ? Con nome, età, casa = studente eseguo l'unpacking della tupla:
# ? ogni elemento viene assegnato automaticamente alla variabile
# ? corrispondente. Quindi nome contiene "Hermione", età contiene 17 e
# ? casa contiene "Grifondoro".
# ? L'unpacking permette quindi di assegnare in un'unica istruzione
# ? i diversi elementi della tupla a variabili separate.

#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 15
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO:
# TODO Il programma dovrà rimuovere i duplicati da una lista usando un set
# TODO, aggiungere un nuovo elemento al set con add()
# TODO e verificare se un elemento è presente con in

case_studenti = ["Grifondoro", "Serpeverde", "Grifondoro", "Corvonero", "Serpeverde"]

case_studenti_set = set(case_studenti)
case_studenti_set.add('Elemento')
print(f'{"Elemento" in case_studenti_set}')

# ? SPIEGAZIONE:
# ? La lista case_studenti contiene alcuni elementi duplicati, come
# ? "Grifondoro" e "Serpeverde".
# ? Con set(case_studenti) trasformo la lista in un set. Durante questa
# ? trasformazione i duplicati vengono eliminati automaticamente, perché
# ? un set può contenere ogni elemento una sola volta.
# ? Il set ottenuto contiene quindi "Grifondoro", "Serpeverde" e
# ? "Corvonero".
# ? Con add('Elemento') aggiungo un nuovo elemento al set.
# ? Con l'operatore in verifico se "Elemento" è presente nel set.
# ? L'espressione "Elemento" in case_studenti_set restituisce True perché
# ? l'elemento è stato appena aggiunto.
# ? La f-string permette di inserire direttamente il risultato True
# ? all'interno del testo visualizzato.

#  * ------------------------------------------------------------------------------
#  * ESERCIZIO 16
#  * ------------------------------------------------------------------------------

# TODO SI CHIEDE DI ESEGUIRE IL SEGUENTE ESERCIZIO:
# TODO Dato il seguente dizionario, il programma dovrà visualizzare
# TODO il voto di Hermione, aggiungere Luna con voto 29,
# TODO modificare il voto di Ron a 27 e attraversare il dizionario
# TODO con .items() visualizzando nome e voto

voti = {"Harry": 28, "Hermione": 30, "Ron": 25}

print(f'Voto di Hermione: {voti["Hermione"]}')
voti["Luna"] = 29
voti["Ron"] = 27
for nome, voto in voti.items():
    print(f'{nome}: {voto}')

# ? SPIEGAZIONE:
# ? Il dizionario voti associa a ogni nome di studente il suo voto. I nomi
# ? sono le chiavi, mentre i voti sono i valori.
# ? Con voti["Hermione"] accedo al valore associato alla chiave "Hermione",
# ? quindi visualizzo il suo voto, che è 30.
# ? Con voti["Luna"] = 29 aggiungo una nuova coppia chiave-valore al
# ? dizionario: la chiave è "Luna" e il valore è 29.
# ? Con voti["Ron"] = 27 modifico invece il valore già associato alla
# ? chiave "Ron", sostituendo 25 con 27.
# ? Con il ciclo for nome, voto in voti.items() attraverso il dizionario
# ? ottenendo contemporaneamente ogni chiave e il relativo valore.
# ? La variabile nome contiene quindi il nome dello studente, mentre voto
# ? contiene il suo voto.
# ? La f-string permette infine di visualizzare ogni studente insieme
# ? al suo voto nel formato "nome: voto".

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

studenti = {"Harry": 28, "Hermione": 30, "Ron": 15, "Luna": 17, "Neville": 21}
promossi = 0
bocciati = []
for nome, voto in studenti.items():
    if voto >= 18:
        promossi += 1
    else:
        bocciati.append(nome)
print("Promossi:", promossi)
print("Bocciati:", bocciati)

# ? SPIEGAZIONE:
# ? Il dizionario studenti contiene i nomi degli studenti come chiavi e i
# ? relativi voti come valori.
# ? La variabile promossi viene inizializzata a 0 e viene utilizzata come
# ? contatore per tenere il numero degli studenti con voto maggiore o uguale
# ? a 18. La lista bocciati viene invece inizializzata vuota e conterrà i
# ? nomi degli studenti con voto minore di 18.
# ? Con studenti.items() ottengo contemporaneamente la chiave e il valore
# ? di ogni elemento del dizionario: nome contiene il nome dello studente
# ? mentre voto contiene il suo voto.
# ? Con if voto >= 18 controllo se lo studente è promosso. Se la condizione
# ? è vera, con promossi += 1 aumento di uno il contatore dei promossi.
# ? Se invece il voto è minore di 18, viene eseguito else e con
# ? bocciati.append(nome) aggiungo il nome dello studente alla lista
# ? dei bocciati.
# ? Alla fine del ciclo promossi contiene 3, mentre bocciati contiene
# ? ['Ron', 'Luna'].
# ? Le due print() finali visualizzano il numero degli studenti promossi
# ? e la lista dei nomi degli studenti bocciati.

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

def analizza_case(case_studenti):
    # 1. Quanti studenti sono in "Serpeverde"?
    num_serpeverde = case_studenti.count("Serpeverde")
    print(f'Numero di studenti in Serpeverde: {num_serpeverde}')

    # 2. Costruisci una lista contenente solo le case diverse da "Serpeverde".
    case_non_serpeverde = [casa for casa in case_studenti if casa != "Serpeverde"]
    print(f'Case diverse da Serpeverde: {case_non_serpeverde}')

    # 3. Quali case compaiono almeno una volta? Usa un set.
    case_uniche = set(case_studenti)
    print(f'Case uniche: {case_uniche}')

    # 4. Costruisci un dizionario che associ a ogni casa il numero di studenti che ne fanno parte.
    conteggio_case = {}
    for casa in case_studenti:
        if casa in conteggio_case:
            conteggio_case[casa] += 1
        else:
            conteggio_case[casa] = 1
    print(f'Conteggio studenti per casa: {conteggio_case}')

analizza_case(case_studenti)

# ? SPIEGAZIONE:
# ? La lista case_studenti contiene il nome della casa di ogni studente,
# ? quindi alcune case possono comparire più volte.
# ?
# ? Con case_studenti.count("Serpeverde") conto quante volte compare
# ? "Serpeverde" nella lista. Il risultato è 3.
# ?
# ? Con la lista case_non_serpeverde creo una nuova lista contenente
# ? solamente le case diverse da "Serpeverde". La condizione
# ? casa != "Serpeverde" permette quindi di escludere tutti gli elementi
# ? uguali a "Serpeverde".
# ?
# ? Con set(case_studenti) trasformo la lista in un set. Il set elimina
# ? automaticamente i duplicati, quindi rimane una sola occorrenza
# ? per ogni casa presente nella lista.
# ?
# ? Infine creo il dizionario conteggio_case vuoto, nel quale ogni chiave
# ? sarà il nome di una casa e il valore sarà il numero di studenti
# ? appartenenti a quella casa.
# ?
# ? Con il ciclo for casa in case_studenti analizzo una casa alla volta.
# ? Se la casa è già presente nel dizionario, aumento il suo conteggio
# ? di 1 con += 1.
# ?
# ? Se invece la casa non è ancora presente, la aggiungo al dizionario
# ? con valore iniziale 1.
# ?
# ? Alla fine il dizionario contiene il numero di studenti per ogni casa:
# ? Grifondoro: 3, Serpeverde: 3, Corvonero: 1 e Tassorosso: 1.