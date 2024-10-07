# app/main.py
from fastapi import FastAPI
from .routers import personas, tripulaciones, pilotos, copilotos, sobrecargos, vuelos, terminales, aeropuertos, vehiculos_aereos, aviones, avionetas, helicopteros, pasajeros, equipajes, boletos

app = FastAPI()

# Incluir los routers
app.include_router(personas.router, prefix="/api/v1/personas", tags=["personas"])
app.include_router(tripulaciones.router, prefix="/api/v1/tripulaciones", tags=["tripulaciones"])
app.include_router(pilotos.router, prefix="/api/v1/pilotos", tags=["pilotos"])
app.include_router(copilotos.router, prefix="/api/v1/copilotos", tags=["copilotos"])
app.include_router(sobrecargos.router, prefix="/api/v1/sobrecargos", tags=["sobrecargos"])
app.include_router(vuelos.router, prefix="/api/v1/vuelos", tags=["vuelos"])
app.include_router(terminales.router, prefix="/api/v1/terminales", tags=["terminales"])
app.include_router(aeropuertos.router, prefix="/api/v1/aeropuertos", tags=["aeropuertos"])
app.include_router(vehiculos_aereos.router, prefix="/api/v1/vehiculos_aereos", tags=["vehiculos_aereos"])
app.include_router(aviones.router, prefix="/api/v1/aviones", tags=["aviones"])
app.include_router(avionetas.router, prefix="/api/v1/avionetas", tags=["avionetas"])
app.include_router(helicopteros.router, prefix="/api/v1/helicopteros", tags=["helicopteros"])
app.include_router(pasajeros.router, prefix="/api/v1/pasajeros", tags=["pasajeros"])
app.include_router(equipajes.router, prefix="/api/v1/equipajes", tags=["equipajes"])
app.include_router(boletos.router, prefix="/api/v1/boletos", tags=["boletos"])