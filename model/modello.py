from time import time
from functools import lru_cache
import copy

class Model:
    def __init__(self):
        self.lista_soluzioni=[]
        self.set_soluzioni = set()

    def calcola_anagrammi(self, parola: str): #dice all'editor che la parola è una stringa
        #entry point
        #parte da una soluzione parziale e si va ad espandere. self, parziale, rimanenti
        self.lista_soluzioni = []                 #resetti ogni volta che inizi una nuova parola
        self.set_soluzioni = set()
        self._ricorsione("", parola)
        return self.set_soluzioni

    # --------------------------------------------------------------------------------------------------------------------------------------
    @lru_cache(maxsize=None)
    def _ricorsione(self, parziale, rimanenti):                        #vuota, dog
        if len(rimanenti)==0:
            self.set_soluzioni.add(parziale)
        else:
            for i in range(len(rimanenti)):                            #for da 0 a 2
                parziale += rimanenti[i]                               #parziale=D cioè in pos 0
                # chiamare ricorsione con parziale e tutte le lettere rimanenti meno la lettera
                nuove_rimanenti = rimanenti[:i] + rimanenti[i+1:]      #togliamo la D
                self._ricorsione(parziale, nuove_rimanenti)
                #backtracking
                parziale= parziale[:-1] #considero tutte le lettere tranne l'ultima. tu aggiungi ogni volta che cerchi la soluzione

#LISTE: --------------------------------------------------------------------------------------------------------------------------------------

    def calcola_anagrammi_list(self, parola):
        self.lista_soluzioni = []
        self._ricorsione_list([], parola)
        return self.lista_soluzioni

    def _ricorsione_list(self, parziale, rimanenti):
        if len(rimanenti)==0:
            #devi fare una copia con la lista
            self.lista_soluzioni.append(copy.deepcopy(parziale)) #altrimetni hai tutte lista vuote--> succede perchè hai il backtraking

        else:
            for i in range(len(rimanenti)):
                parziale.append(rimanenti[i])

                # chiamare ricorsione con parziale e tutte le lettere rimanenti meno la lettera
                nuove_rimanenti = rimanenti[:i] + rimanenti[i+1:]      #togliamo la D
                self._ricorsione_list(parziale, nuove_rimanenti)

                #backtracking
                parziale.pop()

#----------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    model = Model()
    start=time()
    risultato = model.calcola_anagrammi("casa")
    end=time()
    print(f"Elapsed time: {end-start}")
    print(risultato)
    #--------------------------------------------
    risultato2 = model.calcola_anagrammi("giocare")
    end = time()
    print(f"Elapsed time: {end - start}")
    print(risultato2)
    # --------------------------------------------
    risultato3 = model.calcola_anagrammi("casa")
    end = time()
    print(f"Elapsed time: {end - start}")
    print(risultato3)

    #Nel caso in cui parziale e rimanenti non fossero str ma list non puoi usare @cache



