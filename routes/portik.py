from fastapi import APIRouter, BackgroundTasks
from models.portik import Kpi
from config.db import connection
from schemas.portik import KpiEntity, listOfKpiEntity
import random, datetime
from motor.motor_asyncio import AsyncIOMotorClient
import asyncio
from config.db import connection

from models.portik import list_of_matters
from bson import ObjectId
portik_router = APIRouter()



@portik_router.get('/getKPI')
async def retrieve_last_KPI():
    '''
    description : récupère le dernier KPI créé,
    on récupèrera tout les champs exceptés les path des image raw et augmented
    '''
    last_kpi = KpiEntity(connection.local.portik.find_one(sort=[("timestamp", -1)]))
    if last_kpi:
        last_kpi.pop("augmented_image_path", None)
        last_kpi.pop("raw_image_path", None)
        return last_kpi
    return None

@portik_router.post('/addKPI')
async def add_KPI(kpi : Kpi):
    '''
    description : crée un KPI composé de 50 champs

    '''
    print("Requête reçue:", kpi)
    connection.local.portik.insert_one(dict(kpi))
    return listOfKpiEntity(connection.local.portik.find())


@portik_router.get('/lastImage')
async def get_image_path():
    '''
    récupère les path des images raw et augmented du dernier KPI créé en fonction de la dernière date de création
    retourne un KPI contenant seulement les paths des images
    '''
    last_kpi = KpiEntity(connection.local.portik.find_one(sort=[("timestamp", -1)]))

    if last_kpi:
        image_paths = extract_image_paths(last_kpi)
        return image_paths
    return None

def extract_image_paths(db_item):
    return {
        "augmented_image_path": db_item["augmented_image_path"],
        "raw_image_path": db_item["raw_image_path"]
    }

@portik_router.post("/kpi_generation")
async def start_kpi_generation(background_tasks: BackgroundTasks):
    background_tasks.add_task(generate_kpi_periodically)
    return {"message": "KPI generation started"}

async def generate_kpi_periodically():
    while True:
        # Génère un KPI
        kpi = generate_random_kpi()
        await listOfKpiEntity(connection.local.portik.insert_one(kpi))
        # Affiche le KPI généré (à des fins de débogage)
        print("Generated KPI:", kpi)
        # Attendez 60 secondes avant de générer un nouveau KPI
        await asyncio.sleep(1)


def generate_random_kpi():
    return {
        "timestamp": datetime.datetime.now(),
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