import random
from fastapi import FastAPI
from pydantic import BaseModel

class MergeSortRequest(BaseModel):
    documento: list

class MergeSortResponse(BaseModel):
    sorted_document: list

app = FastAPI()

@app.get("/")

def root():

    return {
        "Servicio": "Estructuras de datos"
    }

@app.post("/merge-sort")
def merge_sort(request: MergeSortRequest):
    documento = request.documento
    sorted_document = merge_sort_recursive(documento)
    return {"sorted_document": sorted_document}

def merge_sort_recursive(documento):
    if len(documento) <= 1:
        return documento

    medio = len(documento) // 2
    izquierda = merge_sort_recursive(documento[:medio])
    derecha = merge_sort_recursive(documento[medio:])

    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    while izquierda and derecha:
        if izquierda[0] < derecha[0]:
            resultado.append(izquierda.pop(0))
        else:
            resultado.append(derecha.pop(0))
    resultado.extend(izquierda)
    resultado.extend(derecha)
    return resultado