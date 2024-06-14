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



