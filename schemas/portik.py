from models.portik import list_of_matters


def KpiEntity(db_item) -> dict:
    return {
            "timestamp": db_item["timestamp"],
            "occup": db_item["occup"],
            "cont_nb_per_s": db_item["cont_nb_per_s"],
            "main_nb_per_s": db_item["main_nb_per_s"],
            "purity_nb_per_s": db_item["purity_nb_per_s"],
            "purity_mass_g_per_s": db_item["purity_mass_g_per_s"],
            "augmented_image_path": db_item["augmented_image_path"],
            "raw_image_path": db_item["raw_image_path"],

            "tag_Aluminium_nb_per_s": db_item["tag_Aluminium_nb_per_s"],
            "tag_Aluminium_mass_g_per_s": db_item["tag_Aluminium_mass_g_per_s"],
            "tag_Barquettes_Multicouches_nb_per_s": db_item["tag_Barquettes_Multicouches_nb_per_s"],
            "tag_Barquettes_Multicouches_mass_g_per_s": db_item["tag_Barquettes_Multicouches_mass_g_per_s"],
            "tag_ELA_nb_per_s": db_item["tag_ELA_nb_per_s"],
            "tag_ELA_mass_g_per_s": db_item["tag_ELA_mass_g_per_s"],
            "tag_EMR_nb_per_s": db_item["tag_EMR_nb_per_s"],
            "tag_EMR_mass_g_per_s": db_item["tag_EMR_mass_g_per_s"],
            "tag_Films_non_valorisable_nb_per_s": db_item["tag_Films_non_valorisable_nb_per_s"],
            "tag_Films_non_valorisable_mass_g_per_s": db_item["tag_Films_non_valorisable_mass_g_per_s"],
            "tag_Films_plastiques_PE_nb_per_s": db_item["tag_Films_plastiques_PE_nb_per_s"],
            "tag_Films_plastiques_PE_mass_g_per_s": db_item["tag_Films_plastiques_PE_mass_g_per_s"],
            "tag_Films_plastiques_PP_nb_per_s": db_item["tag_Films_plastiques_PP_nb_per_s"],
            "tag_Films_plastiques_PP_mass_g_per_s": db_item["tag_Films_plastiques_PP_mass_g_per_s"],
            "tag_Gros_de_magasin_nb_per_s": db_item["tag_Gros_de_magasin_nb_per_s"],
            "tag_Gros_de_magasin_mass_g_per_s": db_item["tag_Gros_de_magasin_mass_g_per_s"],
            "tag_Inconnus_nb_per_s": db_item["tag_Inconnus_nb_per_s"],
            "tag_Inconnus_mass_g_per_s": db_item["tag_Inconnus_mass_g_per_s"],
            "tag_JRM_nb_per_s": db_item["tag_JRM_nb_per_s"],
            "tag_JRM_mass_g_per_s": db_item["tag_JRM_mass_g_per_s"],
            "tag_PE_PP_Barquette_nb_per_s": db_item["tag_PE_PP_Barquette_nb_per_s"],
            "tag_PE_PP_Barquette_mass_g_per_s": db_item["tag_PE_PP_Barquette_mass_g_per_s"],
            "tag_PE_PP_Bouteille_nb_per_s": db_item["tag_PE_PP_Bouteille_nb_per_s"],
            "tag_PE_PP_Bouteille_mass_g_per_s": db_item["tag_PE_PP_Bouteille_mass_g_per_s"],
            "tag_PET_C_Barquettes_Pots_nb_per_s": db_item["tag_PET_C_Barquettes_Pots_nb_per_s"],
            "tag_PET_C_Barquettes_Pots_mass_g_per_s": db_item["tag_PET_C_Barquettes_Pots_mass_g_per_s"],
            "tag_PET_C_Bouteilles_Flacon_nb_per_s": db_item["tag_PET_C_Bouteilles_Flacon_nb_per_s"],
            "tag_PET_C_Bouteilles_Flacon_mass_g_per_s": db_item["tag_PET_C_Bouteilles_Flacon_mass_g_per_s"],
            "tag_PET_F_Barquettes_Pots_nb_per_s": db_item["tag_PET_F_Barquettes_Pots_nb_per_s"],
            "tag_PET_F_Barquettes_Pots_mass_g_per_s": db_item["tag_PET_F_Barquettes_Pots_mass_g_per_s"],
            "tag_PET_F_Bouteilles_Flacon_nb_per_s": db_item["tag_PET_F_Bouteilles_Flacon_nb_per_s"],
            "tag_PET_F_Bouteilles_Flacon_mass_g_per_s": db_item["tag_PET_F_Bouteilles_Flacon_mass_g_per_s"],
            "tag_PET_F_Opaques_nb_per_s": db_item["tag_PET_F_Opaques_nb_per_s"],
            "tag_PET_F_Opaques_mass_g_per_s": db_item["tag_PET_F_Opaques_mass_g_per_s"],
            "tag_PS_nb_per_s": db_item["tag_PS_nb_per_s"],
            "tag_PS_mass_g_per_s": db_item["tag_PS_mass_g_per_s"],
            "tag_PSE_nb_per_s": db_item["tag_PSE_nb_per_s"],
            "tag_PSE_mass_g_per_s": db_item["tag_PSE_mass_g_per_s"],
            "tag_Refus_emballage_nb_per_s": db_item["tag_Refus_emballage_nb_per_s"],
            "tag_Refus_emballage_mass_g_per_s": db_item["tag_Refus_emballage_mass_g_per_s"],
            "tag_Vrai_refus_nb_per_s": db_item["tag_Vrai_refus_nb_per_s"],
            "tag_Vrai_refus_mass_g_per_s": db_item["tag_Vrai_refus_mass_g_per_s"],
            "tag_Acier_nb_per_s": db_item["tag_Acier_nb_per_s"],
            "tag_Acier_mass_g_per_s": db_item["tag_Acier_mass_g_per_s"]
}




def listOfKpiEntity(db_item_list) -> list:
    list_kpi_entity = []
    for item in db_item_list:
        list_kpi_entity.append(KpiEntity(item))
    return list_kpi_entity