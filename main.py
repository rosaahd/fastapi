from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Articulo(BaseModel):
    id: int
    titulo: str
    autor: str
    contenido: str
    creado: str
    categoria: str

articulos = [
    Articulo(id=1, titulo="Explorando la Inteligencia Artificial", autor="Marta Sánchez",
             contenido="Este artículo proporciona una visión general sobre el desarrollo y el futuro potencial de la inteligencia artificial en diversas industrias.",
             creado="2024-04-10", categoria="Tecnología"),
    Articulo(id=2, titulo="Impresionismo: Un Movimiento que Cambió el Arte", autor="Roberto Núñez",
             contenido="Análisis del movimiento impresionista y su impacto duradero en las técnicas y percepciones artísticas.",
             creado="2024-04-12", categoria="Arte"),
    Articulo(id=3, titulo="Avances en la Energía Renovable", autor="Juana Fernández",
             contenido="Exploración de las últimas tecnologías en energía renovable y su impacto en la reducción de la huella de carbono global.",
             creado="2024-04-15", categoria="Ciencia"),
    Articulo(id=4, titulo="Nutrición y Salud en el Siglo XXI", autor="Susana Ramírez",
             contenido="Este artículo discute las tendencias modernas en nutrición y cómo estas están influenciando la salud general de la población.",
             creado="2024-04-20", categoria="Salud")
]



@app.post("/articulos/", response_model=Articulo)
def crear_articulo(articulo: Articulo):
    articulos.append(articulo)
    return articulo


@app.get("/articulos/", response_model=List[Articulo])
def leer_articulos():
    return articulos

@app.get("/articulos/{articulo_id}", response_model=Articulo)
def get_by_id(articulo_id: int):
    for index, articulo in enumerate(articulos):
        if articulo.id == articulo_id:
            return articulo
    raise HTTPException(status_code=404, detail="Artículo no encontrado")

@app.put("/articulos/{articulo_id}", response_model=Articulo)
def modificar_articulo(articulo_id: int, articulo: Articulo):
    for index, art in enumerate(articulos):
        if art.id == articulo_id:
            articulos[index] = articulo
            return articulo
    raise HTTPException(status_code=404, detail="Artículo no encontrado")

@app.delete("/articulos/{articulo_id}")
def delete_by_id(articulo_id: int):
    for index, articulo in enumerate(articulos):
        if articulo.id == articulo_id:
            articulos.pop(index)
            return articulos