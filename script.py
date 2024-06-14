import json, requests, datetime, random, time




# génerer aléatoirement des kpis (json)
# faire un appel post sur l'api en fournissant le Json généré 
# attendre 5 secondes 
# repeter à l'infini 

def generate_random_kpi():
    return {
        "timestamp": datetime.datetime.now().isoformat(),
        "occup": random.uniform(0, 1),
        "cont_nb_per_s": random.randint(0, 100),
        "main_nb_per_s": random.randint(0, 100),
        "purity_nb_per_s": random.uniform(0, 1),
        "purity_mass_g_per_s": random.uniform(0, 1),
        "augmented_image_path": "path/to/augmented/image",
        "raw_image_path": "path/to/raw/image",
        "tag_Aluminium_nb_per_s": random.randint(0, 100),
        "tag_Aluminium_mass_g_per_s": random.randint(0, 100),
        "tag_Barquettes_Multicouches_nb_per_s": random.randint(0, 100),
        "tag_Barquettes_Multicouches_mass_g_per_s": random.randint(0, 100),
        "tag_ELA_nb_per_s": random.randint(0, 100),
        "tag_ELA_mass_g_per_s": random.randint(0, 100),
        "tag_EMR_nb_per_s": random.randint(0, 100),
        "tag_EMR_mass_g_per_s": random.randint(0, 100),
        "tag_Films_non_valorisable_nb_per_s": random.randint(0, 100),
        "tag_Films_non_valorisable_mass_g_per_s": random.randint(0, 100),
        "tag_Films_plastiques_PE_nb_per_s": random.randint(0, 100),
        "tag_Films_plastiques_PE_mass_g_per_s": random.randint(0, 100),
        "tag_Films_plastiques_PP_nb_per_s": random.randint(0, 100),
        "tag_Films_plastiques_PP_mass_g_per_s": random.randint(0, 100),
        "tag_Gros_de_magasin_nb_per_s": random.randint(0, 100),
        "tag_Gros_de_magasin_mass_g_per_s": random.randint(0, 100),
        "tag_Inconnus_nb_per_s": random.randint(0, 100),
        "tag_Inconnus_mass_g_per_s": random.randint(0, 100),
        "tag_JRM_nb_per_s": random.randint(0, 100),
        "tag_JRM_mass_g_per_s": random.randint(0, 100),
        "tag_PE_PP_Barquette_nb_per_s": random.randint(0, 100),
        "tag_PE_PP_Barquette_mass_g_per_s": random.randint(0, 100),
        "tag_PE_PP_Bouteille_nb_per_s": random.randint(0, 100),
        "tag_PE_PP_Bouteille_mass_g_per_s": random.randint(0, 100),
        "tag_PET_C_Barquettes_Pots_nb_per_s": random.randint(0, 100),
        "tag_PET_C_Barquettes_Pots_mass_g_per_s": random.randint(0, 100),
        "tag_PET_C_Bouteilles_Flacon_nb_per_s": random.randint(0, 100),
        "tag_PET_C_Bouteilles_Flacon_mass_g_per_s": random.randint(0, 100),
        "tag_PET_F_Barquettes_Pots_nb_per_s": random.randint(0, 100),
        "tag_PET_F_Barquettes_Pots_mass_g_per_s": random.randint(0, 100),
        "tag_PET_F_Bouteilles_Flacon_nb_per_s": random.randint(0, 100),
        "tag_PET_F_Bouteilles_Flacon_mass_g_per_s": random.randint(0, 100),
        "tag_PET_F_Opaques_nb_per_s": random.randint(0, 100),
        "tag_PET_F_Opaques_mass_g_per_s": random.randint(0, 100),
        "tag_PS_nb_per_s": random.randint(0, 100),
        "tag_PS_mass_g_per_s": random.randint(0, 100),
        "tag_PSE_nb_per_s": random.randint(0, 100),
        "tag_PSE_mass_g_per_s": random.randint(0, 100),
        "tag_Refus_emballage_nb_per_s": random.randint(0, 100),
        "tag_Refus_emballage_mass_g_per_s": random.randint(0, 100),
        "tag_Vrai_refus_nb_per_s": random.randint(0, 100),
        "tag_Vrai_refus_mass_g_per_s": random.randint(0, 100),
        "tag_Acier_nb_per_s": random.randint(0, 100),
        "tag_Acier_mass_g_per_s": random.randint(0, 100)
    }

def send_rand_kpi():
    url = "http://127.0.0.1:8000/addKPI"
    while True:
        kpi = generate_random_kpi()
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json"
        }
        response = requests.post(url, json=kpi, headers=headers)
            
    
        time.sleep(5) 

#send_rand_kpi()
#print(requests.get("http://127.0.0.1:8000/getKPI").text).
print(requests.get("http://127.0.0.1:8000/lastImage").text)
