from pydantic import BaseModel, Field, validator
import datetime
from typing import Dict, Optional, List


list_of_matters = [
    "Aluminium",
    "Barquettes Multicouches",
    "ELA",
    "EMR",
    "Films non valorisable",
    "Films plastiques PE",
    "Films plastiques PP",
    "Gros de magasin",
    "Inconnus",
    "JRM",
    "PE/PP Barquette",
    "PE/PP Bouteille",
    "PET C Barquettes & Pots",
    "PET C Bouteilles & Flacon",
    "PET F Barquettes & Pots",
    "PET F Bouteilles & Flacon",
    "PET F Opaques",
    "PS",
    "PSE",
    "Refus emballage",
    "Vrai refus",
    "Acier"
]

class Kpi(BaseModel):
    timestamp: datetime.datetime
    occup: float = Field(..., ge=0, le=1)
    cont_nb_per_s: int
    main_nb_per_s: int
    purity_nb_per_s: float = Field(..., ge=0, le=1)
    purity_mass_g_per_s: float = Field(..., ge=0, le=1)
    augmented_image_path: str
    raw_image_path: str
    tag_Aluminium_nb_per_s: int
    tag_Aluminium_mass_g_per_s: int
    tag_Barquettes_Multicouches_nb_per_s: int
    tag_Barquettes_Multicouches_mass_g_per_s: int
    tag_ELA_nb_per_s: int
    tag_ELA_mass_g_per_s: int
    tag_EMR_nb_per_s: int
    tag_EMR_mass_g_per_s: int
    tag_Films_non_valorisable_nb_per_s: int
    tag_Films_non_valorisable_mass_g_per_s: int
    tag_Films_plastiques_PE_nb_per_s: int
    tag_Films_plastiques_PE_mass_g_per_s: int
    tag_Films_plastiques_PP_nb_per_s: int
    tag_Films_plastiques_PP_mass_g_per_s: int
    tag_Gros_de_magasin_nb_per_s: int
    tag_Gros_de_magasin_mass_g_per_s: int
    tag_Inconnus_nb_per_s: int
    tag_Inconnus_mass_g_per_s: int
    tag_JRM_nb_per_s: int
    tag_JRM_mass_g_per_s: int
    tag_PE_PP_Barquette_nb_per_s: int
    tag_PE_PP_Barquette_mass_g_per_s: int
    tag_PE_PP_Bouteille_nb_per_s: int
    tag_PE_PP_Bouteille_mass_g_per_s: int
    tag_PET_C_Barquettes_Pots_nb_per_s: int
    tag_PET_C_Barquettes_Pots_mass_g_per_s: int
    tag_PET_C_Bouteilles_Flacon_nb_per_s: int
    tag_PET_C_Bouteilles_Flacon_mass_g_per_s: int
    tag_PET_F_Barquettes_Pots_nb_per_s: int
    tag_PET_F_Barquettes_Pots_mass_g_per_s: int
    tag_PET_F_Bouteilles_Flacon_nb_per_s: int
    tag_PET_F_Bouteilles_Flacon_mass_g_per_s: int
    tag_PET_F_Opaques_nb_per_s: int
    tag_PET_F_Opaques_mass_g_per_s: int
    tag_PS_nb_per_s: int
    tag_PS_mass_g_per_s: int
    tag_PSE_nb_per_s: int
    tag_PSE_mass_g_per_s: int
    tag_Refus_emballage_nb_per_s: int
    tag_Refus_emballage_mass_g_per_s: int
    tag_Vrai_refus_nb_per_s: int
    tag_Vrai_refus_mass_g_per_s: int
    tag_Acier_nb_per_s: int
    tag_Acier_mass_g_per_s: int







class ImagePaths(BaseModel):
    augmented_image_path: str
    raw_image_path: str


