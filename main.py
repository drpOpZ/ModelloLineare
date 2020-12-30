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
class linear_model:
  def __init__(self):
	
	#TODO: inizializzare i campi a None

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
	
	#Nota: non ritorna nulla

  def predict(self,xs):
	
	#TODO: lancia un eccezione se il coefficiente angolare o l'intercetta non sono none
    
    #TODO: calcola i valori predetti e restituiscili

#-------------------------
# applicazione del modello
#-------------------------

#TODO: istanziare il modello
#TODO: effetuare il fit

#TODO: predire il numero di litri per il tragitto stimato
km_tragitto = #...?
litri_tragitto = #...?

#TODO: calcolare la spesa di ciascuno
prezzo_benzina = #...?
quota_individuale = #...?

print("Litri di benzina totali:{}lt\nQuota individuale:{}€".format(litri_tragitto,quota_individuale))