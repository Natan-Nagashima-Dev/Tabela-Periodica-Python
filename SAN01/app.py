import customtkinter as ctk
carga_neutra="0"
carga_positiva="+"
carga_negativa="-"
#carga com base na variação de eletrons

isotopo_estavel="estavel"
isotopo_instavel="radioativo"
#variação de neutrons e estabilidade do atomo

grupo_1="Metais Alcalinos"
grupo_2="Metais Alcalino-Terrosos"
grupo_3a4="Metais de Transição"
grupo_13="Boro"
grupo_14="Grupo do Carbono"
grupo_15="Grupo do Nitrogênio"
grupo_16="Calcogênios"
grupo_17="Halogênios"
grupo_18="Gases Nobres"
grupo_lantanideos="Lantanideos"
grupo_actinideos="Actinideos"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x600")
        self.title("Consultor de Tabela Periódica")
    
app=App()
app.mainloop()