from pydantic import BaseModel
from typing import Optional, List
from datetime import date

class PersonaBase(BaseModel):
    nombre: str
    apellido: str
    fecha_nacimiento: date
    genero: str

class PersonaCreate(PersonaBase):
    pass

class Persona(PersonaBase):
    id_persona: int

    class Config:
        orm_mode = True

class TripulacionBase(BaseModel):
    antiguedad: int
    turno: str
    horas_vuelo: float
    nombre: str
    apellido: str
    fecha_nacimiento: date
    genero: str

class TripulacionCreate(TripulacionBase):
    persona_id: int

class Tripulacion(TripulacionBase):
    id_tripulacion: int
    persona: Persona

    class Config:
        orm_mode = True

class PilotoBase(BaseModel):
    rango: str
    licencia: str
    tipo_aeronave: str

class PilotoCreate(PilotoBase):
    tripulacion_id: int

class Piloto(PilotoBase):
    id_piloto: int
    tripulacion: Tripulacion

    class Config:
        orm_mode = True

class CopilotoBase(BaseModel):
    rango: str
    tiempo_ser_piloto: int

class CopilotoCreate(CopilotoBase):
    tripulacion_id: int

class Copiloto(CopilotoBase):
    id_copiloto: int
    tripulacion: Tripulacion

    class Config:
        orm_mode = True

class SobrecargoBase(BaseModel):
    idiomas: str
    certificado: str

class SobrecargoCreate(SobrecargoBase):
    tripulacion_id: int

class Sobrecargo(SobrecargoBase):
    id_sobrecargo: int
    tripulacion: Tripulacion

    class Config:
        orm_mode = True

class VueloBase(BaseModel):
    origen: str
    destino: str
    duracion: float
    fecha_salida: date
    fecha_llegada: date

class VueloCreate(VueloBase):
    tripulacion_id: int
    terminal_id: int
    vehiculo_aereo_id: int

class Vuelo(VueloBase):
    id_vuelo: int
    tripulacion: Tripulacion
    terminal: 'Terminal'
    vehiculo_aereo: 'VehiculoAereo'

    class Config:
        orm_mode = True

class TerminalBase(BaseModel):
    capacidad: int
    disponibilidad: bool

class TerminalCreate(TerminalBase):
    aeropuerto_id: int

class Terminal(TerminalBase):
    id_terminal: int
    aeropuerto: 'Aeropuerto'
    vuelos: List[Vuelo] = []

    class Config:
        orm_mode = True

class AeropuertoBase(BaseModel):
    nombre: str
    numero_pistas: int
    tipo_aviones: str

class AeropuertoCreate(AeropuertoBase):
    pass

class Aeropuerto(AeropuertoBase):
    id_aeropuerto: int
    terminales: List[Terminal] = []

    class Config:
        orm_mode = True

class VehiculoAereoBase(BaseModel):
    modelo: str
    numero_serie: str
    capacidad: int
    color: str
    estado: str
    antiguedad: int
    horas_vuelo: float
    tiene_llantas: bool
    capacidad_tanque: float
    distancia_recorrida: float

class VehiculoAereoCreate(VehiculoAereoBase):
    pass

class VehiculoAereo(VehiculoAereoBase):
    id_vehiculo_aereo: int
    vuelos: List[Vuelo] = []

    class Config:
        orm_mode = True

class AvionBase(BaseModel):
    aerolinea: str
    tipo_motor: str
    numero_puertas: int
    tipo_avion: str

class AvionCreate(AvionBase):
    vehiculo_aereo_id: int

class Avion(AvionBase):
    id_avion: int
    vehiculo_aereo: VehiculoAereo

    class Config:
        orm_mode = True

class AvionetaBase(BaseModel):
    numero_motores: int
    tipo_pista: str
    tipo_avioneta: str

class AvionetaCreate(AvionetaBase):
    vehiculo_aereo_id: int

class Avioneta(AvionetaBase):
    id_avioneta: int
    vehiculo_aereo: VehiculoAereo

    class Config:
        orm_mode = True

class HelicopteroBase(BaseModel):
    tipo_helicoptero: str
    numero_helices: int

class HelicopteroCreate(HelicopteroBase):
    vehiculo_aereo_id: int

class Helicoptero(HelicopteroBase):
    id_helicoptero: int
    vehiculo_aereo: VehiculoAereo

    class Config:
        orm_mode = True

class PasajeroBase(BaseModel):
    nombre: str
    apellido: str
    direccion: str
    fecha_nacimiento: date
    nacionalidad: str

class PasajeroCreate(PasajeroBase):
    persona_id: int

class Pasajero(PasajeroBase):
    id_pasajero: int
    persona: Persona
    equipajes: List['Equipaje'] = []
    boletos: List['Boleto'] = []

    class Config:
        orm_mode = True

class EquipajeBase(BaseModel):
    peso: float
    altura: float
    ancho: float
    tipo_equipaje: str

class EquipajeCreate(EquipajeBase):
    pasajero_id: int

class Equipaje(EquipajeBase):
    id_equipaje: int
    pasajero: Pasajero

    class Config:
        orm_mode = True

class BoletoBase(BaseModel):
    asiento: str
    costo: float

class BoletoCreate(BoletoBase):
    pasajero_id: int
    vuelo_id: int

class Boleto(BoletoBase):
    id_boleto: int
    pasajero: Pasajero
    vuelo: Vuelo

    class Config:
        orm_mode = True