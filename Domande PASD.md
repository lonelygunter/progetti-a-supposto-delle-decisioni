# Esonero scritto PASD - DOMANDE

## Introduzione a Sistemi a Supporto delle Decisioni ed Intelligenza Artificiale

1. fornire la definizione di decisione strategica, tattica e operative
   > decisione operativa: di breve periodo, reversibili, limitate a n persone nel team

   > decisione tattica: di medio periodo, coinvolge solo una parte del team

   > decisione strategica: di lungo periodo, non reversibile, coinvolge denaro

2. fornire la definizione di decisione strutturata, non strutturata e semi-strutturata
   > decisione strutturata: con procedura di risoluzione specifica

   > decisione non strutturata: richiede creatività e/o esperienza

   > decisione semi-strutturata: usate per valutare le prestazioni di un sistema che magari presenta dei comportamenti randomici

3. fornire un esempio di decisione strategica
   > rifornimento di magazzino per l'intero anno 

4. lo scheduling del generatore dell'impianto elettrico è una decisione strategica, tattica o operazionale?
   > decisione strategica

5. illustrare la relazione tra decisione stategica e non strutturata
   > dovendo prendere una decisione di lungo periodo e che coninvolge notevoli somme di denaro (strategica) è più ragionevole usare creatività e/o esperienza (non strutturata) 


## Discipline correlate

1. cos'è la Business Intelligence?
   > indica un sistema dedicato alla raccolta di dati e alla loro elaborazione al fine di un reporting (Intelligence). Usato quindi su dati atomici per conoscenze più approfondite

2. cosa sono i Sistemi a Supporto delle Decisioni?
   > indica un sistema computerizzato dotato di un sistema di "data managment" per creare un modello di ottimizzazione

3. qual è la relazione tra Machine Learning e Artificial Intelligence?
   > il Machine Learning è una sottobranca dell'Artificial Intelligence infatti comprende l'apprendimento automatico e l'esperienza pregressa di agenti sottoposti a training. Invece l'Artificial Intelligence comprende tutti i tipi di automazione, dal learning al planning e alla manipolazione dell'ambiente da parte di agenti

4. cosa sono gli Agenti Autonomi?
   > tramite un'istruzione sintetica sviluppa delle azioni per raggiungere il goal cercando di gestire eventuali imprevisti

5. qual è la relazione tra Machine Learning e Data Mining?
   > fanno entrambi parte dell'Artifical Intelligence, il primo di occupa dell'apprendimento automatico e dell'esperienza pregresse di agenti, la seconda dell'estrazione di pattern da dai dati trovando delle regolarità o trend

6. quale è la relazione tra Data Mining e Knowledge Discovery nei Databases?
   > 


## Ottimizzazione base

1. cos'è una soluzione ammissibile?
   > 
2. fornire un esempio di soluzione ammissibile del problema senza soluzione ottima
3. risolvere graficamente il seguente problema di ottimizzazione:
$$\max z = -2x_1 + x_2$$
con vincoli:
- $2x_1 x_2 = 10$
- $x_1 + 2x_2 \leq 10$
- $x_1, x_2 \geq 0$


## Ottimizzazione del modello

1. descrivere un problema di product-mix
2. descrivere il modello di scheduling di un progetto dove la durata di un task dipende dall'importo delle risorse ad esso assegnate e l'obiettivo è ridurre al minimo la durata del progetto subordinatamente a un vincolo di bilancio
3. descrivere il modello EOQ
4. descrivere il modello EOQ con cun vincolo massimo di inventario


## Ottimizzazione lineare

1. convertire il seguente problema alla forma standard: ...
2. eseguire un passaggio dell'algoritmo del simplesso: ...
3. quante soluzioni di base ha il seguente problema? ...
4. descrivere lo pseudocodice dell'algoritmo del simplesso
5. l'algoritmo del simplesso è convergente? discurre brevemente
6. la funzione obiettivo è monotonicamente crescente/decrescente nell'algoritmo del simplesso? se no, perché?
7. cos'è una soluzione di base degenere?
8. se una BFS è degenere o non ottima, lo può essere la successiva? vuole un $\Delta z = 0$?
9. guardando il tableau: ... 
    - qual è la soluzione di base associata?
    - è ammissibile?
    - è ottima? (assumendo che la funzione obiettivo sia minimizzata)
    - se non lo è, quali sono le variabili in entrata e in uscita?
    - quale valore prende la variabile in entrata?
10. guardando il tableau: ...
    - il BFS è ottimo? (assumendo che la funzione obiettivo sia minimizzata)
    - se lo è, la soluzione ottima è unica?
    - se non lo è, qual è un'altra BFS ottima? e qual è una soluzione ottima che non sia BFS?
11. usando il metodo delle variabili artificiali eseguire una sua iterazione sul seguente problema: ...


## Algoritmo Branch-and-Bound

1. descrivere lo peseudocodice (ricerca di profondità)
2. descrivere lo peseudocodice (ricerca del bound migliore)
3. vedendo il seguente problema di ottimizzazione lineare intera e il suo rilassamento continuo, cosa fa l'algortimo nel prossimo step?


## Ottimizzzione lineare intera (mix)

1. descrivere lo pseudocodice dell'algoritmo di Branch-and-Bound (ricerca del bound migliore)
2. nell'algortimo di Branch-and-Bound quando un sottoproblema può essere preso in considerazione?
3. applicare il metodo Branch-and-Bound al seguente problema e risolvere graficamente i rilassamenti: ...
4. considerando il seguente problema di ottimizzazione lineare intera e i suoi rilassamenti ... eseguire uno step dell'algoritmo di Branch-and-Bound