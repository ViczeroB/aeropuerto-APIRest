from sqlalchemy.orm import Session
from . import models, schemas

# Persona CRUD
def get_persona(db: Session, persona_id: int):
    return db.query(models.Persona).filter(models.Persona.id_persona == persona_id).first()

def create_persona(db: Session, persona: schemas.PersonaCreate):
    db_persona = models.Persona(**persona.dict())
    db.add(db_persona)
    db.commit()
    db.refresh(db_persona)
    return db_persona

# Tripulacion CRUD
def get_tripulacion(db: Session, tripulacion_id: int):
    return db.query(models.Tripulacion).filter(models.Tripulacion.id_tripulacion == tripulacion_id).first()

def create_tripulacion(db: Session, tripulacion: schemas.TripulacionCreate):
    db_tripulacion = models.Tripulacion(**tripulacion.dict())
    db.add(db_tripulacion)
    db.commit()
    db.refresh(db_tripulacion)
    return db_tripulacion

# Piloto CRUD
def get_piloto(db: Session, piloto_id: int):
    return db.query(models.Piloto).filter(models.Piloto.id_piloto == piloto_id).first()

def create_piloto(db: Session, piloto: schemas.PilotoCreate):
    db_piloto = models.Piloto(**piloto.dict())
    db.add(db_piloto)
    db.commit()
    db.refresh(db_piloto)
    return db_piloto

# Copiloto CRUD
def get_copiloto(db: Session, copiloto_id: int):
    return db.query(models.Copiloto).filter(models.Copiloto.id_copiloto == copiloto_id).first()

def create_copiloto(db: Session, copiloto: schemas.CopilotoCreate):
    db_copiloto = models.Copiloto(**copiloto.dict())
    db.add(db_copiloto)
    db.commit()
    db.refresh(db_copiloto)
    return db_copiloto

# Sobrecargo CRUD
def get_sobrecargo(db: Session, sobrecargo_id: int):
    return db.query(models.Sobrecargo).filter(models.Sobrecargo.id_sobrecargo == sobrecargo_id).first()

def create_sobrecargo(db: Session, sobrecargo: schemas.SobrecargoCreate):
    db_sobrecargo = models.Sobrecargo(**sobrecargo.dict())
    db.add(db_sobrecargo)
    db.commit()
    db.refresh(db_sobrecargo)
    return db_sobrecargo

# Vuelo CRUD
def get_vuelo(db: Session, vuelo_id: int):
    return db.query(models.Vuelo).filter(models.Vuelo.id_vuelo == vuelo_id).first()

def create_vuelo(db: Session, vuelo: schemas.VueloCreate):
    db_vuelo = models.Vuelo(**vuelo.dict())
    db.add(db_vuelo)
    db.commit()
    db.refresh(db_vuelo)
    return db_vuelo

# Terminal CRUD
def get_terminal(db: Session, terminal_id: int):
    return db.query(models.Terminal).filter(models.Terminal.id_terminal == terminal_id).first()

def create_terminal(db: Session, terminal: schemas.TerminalCreate):
    db_terminal = models.Terminal(**terminal.dict())
    db.add(db_terminal)
    db.commit()
    db.refresh(db_terminal)
    return db_terminal

# Aeropuerto CRUD
def get_aeropuerto(db: Session, aeropuerto_id: int):
    return db.query(models.Aeropuerto).filter(models.Aeropuerto.id_aeropuerto == aeropuerto_id).first()

def create_aeropuerto(db: Session, aeropuerto: schemas.AeropuertoCreate):
    db_aeropuerto = models.Aeropuerto(**aeropuerto.dict())
    db.add(db_aeropuerto)
    db.commit()
    db.refresh(db_aeropuerto)
    return db_aeropuerto

# VehiculoAereo CRUD
def get_vehiculo_aereo(db: Session, vehiculo_aereo_id: int):
    return db.query(models.VehiculoAereo).filter(models.VehiculoAereo.id_vehiculo_aereo == vehiculo_aereo_id).first()

def create_vehiculo_aereo(db: Session, vehiculo_aereo: schemas.VehiculoAereoCreate):
    db_vehiculo_aereo = models.VehiculoAereo(**vehiculo_aereo.dict())
    db.add(db_vehiculo_aereo)
    db.commit()
    db.refresh(db_vehiculo_aereo)
    return db_vehiculo_aereo

# Avion CRUD
def get_avion(db: Session, avion_id: int):
    return db.query(models.Avion).filter(models.Avion.id_avion == avion_id).first()

def create_avion(db: Session, avion: schemas.AvionCreate):
    db_avion = models.Avion(**avion.dict())
    db.add(db_avion)
    db.commit()
    db.refresh(db_avion)
    return db_avion

# Avioneta CRUD
def get_avioneta(db: Session, avioneta_id: int):
    return db.query(models.Avioneta).filter(models.Avioneta.id_avioneta == avioneta_id).first()

def create_avioneta(db: Session, avioneta: schemas.AvionetaCreate):
    db_avioneta = models.Avioneta(**avioneta.dict())
    db.add(db_avioneta)
    db.commit()
    db.refresh(db_avioneta)
    return db_avioneta

# Helicoptero CRUD
def get_helicoptero(db: Session, helicoptero_id: int):
    return db.query(models.Helicoptero).filter(models.Helicoptero.id_helicoptero == helicoptero_id).first()

def create_helicoptero(db: Session, helicoptero: schemas.HelicopteroCreate):
    db_helicoptero = models.Helicoptero(**helicoptero.dict())
    db.add(db_helicoptero)
    db.commit()
    db.refresh(db_helicoptero)
    return db_helicoptero

# Pasajero CRUD
def get_pasajero(db: Session, pasajero_id: int):
    return db.query(models.Pasajero).filter(models.Pasajero.id_pasajero == pasajero_id).first()

def create_pasajero(db: Session, pasajero: schemas.PasajeroCreate):
    db_pasajero = models.Pasajero(**pasajero.dict())
    db.add(db_pasajero)
    db.commit()
    db.refresh(db_pasajero)
    return db_pasajero

# Equipaje CRUD
def get_equipaje(db: Session, equipaje_id: int):
    return db.query(models.Equipaje).filter(models.Equipaje.id_equipaje == equipaje_id).first()

def create_equipaje(db: Session, equipaje: schemas.EquipajeCreate):
    db_equipaje = models.Equipaje(**equipaje.dict())
    db.add(db_equipaje)
    db.commit()
    db.refresh(db_equipaje)
    return db_equipaje

# Boleto CRUD
def get_boleto(db: Session, boleto_id: int):
    return db.query(models.Boleto).filter(models.Boleto.id_boleto == boleto_id).first()

def create_boleto(db: Session, boleto: schemas.BoletoCreate):
    db_boleto = models.Boleto(**boleto.dict())
    db.add(db_boleto)
    db.commit()
    db.refresh(db_boleto)
    return db_boleto