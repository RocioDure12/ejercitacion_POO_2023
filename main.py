from fastapi import FastAPI
from typing import Union

app = FastAPI()


@app.get("/api/proveedores")
def read_proveedores():
    return [
        {
            "nombre":"JUAN SRL"
        },
        {
            "nombre":"KUKELINA SOFT"
        }
    ]

