import json
from mendeleev import element

def tabela():
    tabela=[]
    for n in range (1,9): 
        atomo=element(n)
        neutrons = [iso.mass_number - atomo.atomic_number for iso in atomo.isotopes]
        dados={
            'nome_atomo': atomo.name,
            'sigla': atomo.symbol if atomo.symbol else '?',
            'numero_atomico':atomo.atomic_number if atomo.atomic_number else 0,
            'num_camadas':atomo.ec.max_n(),
            'num_valencia':atomo.nvalence(),
            'grupo':atomo.group_id,
            'max_neutrons':max(neutrons) if neutrons else 0,
            'min_neutrons':min(neutrons) if neutrons else 0,
        }
        
        tabela.append(dados)
    with open('tabela_periodica.json', 'w', encoding='utf-8') as f:
        json.dump(tabela, f, ensure_ascii=False, indent=4)

    print("Arquivo 'tabela_periodica.json' gerado com sucesso!")



tabela()