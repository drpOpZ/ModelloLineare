import numpy as np

# Dati della tabella
data = np.array([[833. ,  37. ],
                 [987. ,  41.6],
                 [883. ,  37.2],
                 [378. ,  15.2],
                 [ 84. ,   3.4],
                 [483. ,  19.6],
                 [835. ,  35.1],
                 [646. ,  28.9],
                 [508. ,  22.6],
                 [ 90. ,   3.7]])

#------------------------
# definizione del modello
#------------------------
class LinearModel:
  def __init__(self):
    #TODO: inizializzare i campi a None
    pass

  def fit(self,train_data):
    # controllo che train_data sia della forma giusta
    try:
      assert(len(train_data.shape)==2)
      assert(train_data.shape[1]==2)
    except:
      raise Exception("Bad train_data shape! {} should be (*,2)".format(train_data.shape))
  
	  # ricavo le x e le y da train_data
    x = train_data[:,0]
    y = #TODO
    
    #TODO: calcolare coefficiente angolare e intercetta e salvarli nei campi definiti in __init__
	  #TODO: salvare train_data nel campo definito in __init__
	
    #... no return

  def predict(self,xs):
    
    #TODO: lancia un eccezione se il coefficiente angolare o l'intercetta non sono none
    
    #TODO: calcola i valori predetti per le xs e restituiscili
    pass

#-------------------------
# applicazione del modello
#-------------------------

#TODO: istanziare il modello
#TODO: effetuare il fit

km_tragitto = #...dati?
#TODO: predire il numero di litri per il tragitto stimato
litri_tragitto = #...?

prezzo_benzina = #...dati?
#TODO: calcolare la spesa di ciascuno
quota_individuale = #...?

# Stampa i risultati a schermo
print("Litri di benzina totali:{}lt\nQuota individuale:{}€".format(litri_tragitto,quota_individuale))
