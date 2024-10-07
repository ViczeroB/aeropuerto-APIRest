from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float, Boolean
from sqlalchemy.orm import relationship
from .database import Base

class Persona(Base):
    __tablename__ = 'personas'
    id_persona = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    apellido = Column(String, index=True)
    fecha_nacimiento = Column(Date)
    genero = Column(String)
    # Relaciones
    tripulacion = relationship("Tripulacion", back_populates="persona")
    pasajero = relationship("Pasajero", back_populates="persona")

class Tripulacion(Base):
    __tablename__ = 'tripulaciones'
    id_tripulacion = Column(Integer, primary_key=True, index=True)
    antiguedad = Column(Integer)
    turno = Column(String)
    horas_vuelo = Column(Float)
    nombre = Column(String)
    apellido = Column(String)
    fecha_nacimiento = Column(Date)
    genero = Column(String)
    # Relaciones
    persona_id = Column(Integer, ForeignKey('personas.id_persona'))
    persona = relationship("Persona", back_populates="tripulacion")
    vuelos = relationship("Vuelo", back_populates="tripulacion")
    piloto = relationship("Piloto", back_populates="tripulacion")
    copiloto = relationship("Copiloto", back_populates="tripulacion")
    sobrecargo = relationship("Sobrecargo", back_populates="tripulacion")

class Piloto(Base):
    __tablename__ = 'pilotos'
    id_piloto = Column(Integer, primary_key=True, index=True)
    rango = Column(String)
    licencia = Column(String)
    tipo_aeronave = Column(String)
    # Relaciones
    tripulacion_id = Column(Integer, ForeignKey('tripulaciones.id_tripulacion'))
    tripulacion = relationship("Tripulacion", back_populates="piloto")

class Copiloto(Base):
    __tablename__ = 'copilotos'
    id_copiloto = Column(Integer, primary_key=True, index=True)
    rango = Column(String)
    tiempo_ser_piloto = Column(Integer)
    # Relaciones
    tripulacion_id = Column(Integer, ForeignKey('tripulaciones.id_tripulacion'))
    tripulacion = relationship("Tripulacion", back_populates="copiloto")

class Sobrecargo(Base):
    __tablename__ = 'sobrecargos'
    id_sobrecargo = Column(Integer, primary_key=True, index=True)
    idiomas = Column(String)
    certificado = Column(String)
    # Relaciones
    tripulacion_id = Column(Integer, ForeignKey('tripulaciones.id_tripulacion'))
    tripulacion = relationship("Tripulacion", back_populates="sobrecargo")

class Vuelo(Base):
    __tablename__ = 'vuelos'
    id_vuelo = Column(Integer, primary_key=True, index=True)
    origen = Column(String)
    destino = Column(String)
    duracion = Column(Float)
    fecha_salida = Column(Date)
    fecha_llegada = Column(Date)
    # Relaciones
    tripulacion_id = Column(Integer, ForeignKey('tripulaciones.id_tripulacion'))
    tripulacion = relationship("Tripulacion", back_populates="vuelos")
    terminal_id = Column(Integer, ForeignKey('terminales.id_terminal'))
    terminal = relationship("Terminal", back_populates="vuelos")
    vehiculo_aereo_id = Column(Integer, ForeignKey('vehiculos_aereos.id_vehiculo_aereo'))
    vehiculo_aereo = relationship("VehiculoAereo", back_populates="vuelos")
    boletos = relationship("Boleto", back_populates="vuelo")

class Terminal(Base):
    __tablename__ = 'terminales'
    id_terminal = Column(Integer, primary_key=True, index=True)
    capacidad = Column(Integer)
    disponibilidad = Column(Boolean)
    # Relaciones
    vuelos = relationship("Vuelo", back_populates="terminal")
    aeropuerto_id = Column(Integer, ForeignKey('aeropuertos.id_aeropuerto'))
    aeropuerto = relationship("Aeropuerto", back_populates="terminales")

class Aeropuerto(Base):
    __tablename__ = 'aeropuertos'
    id_aeropuerto = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    numero_pistas = Column(Integer)
    tipo_aviones = Column(String)
    # Relaciones
    terminales = relationship("Terminal", back_populates="aeropuerto")

class VehiculoAereo(Base):
    __tablename__ = 'vehiculos_aereos'
    id_vehiculo_aereo = Column(Integer, primary_key=True, index=True)
    modelo = Column(String)
    numero_serie = Column(String)
    capacidad = Column(Integer)
    color = Column(String)
    estado = Column(String)
    antiguedad = Column(Integer)
    horas_vuelo = Column(Float)
    tiene_llantas = Column(Boolean)
    capacidad_tanque = Column(Float)
    distancia_recorrida = Column(Float)
    # Relaciones
    vuelos = relationship("Vuelo", back_populates="vehiculo_aereo")
    avion = relationship("Avion", back_populates="vehiculo_aereo")
    avioneta = relationship("Avioneta", back_populates="vehiculo_aereo")
    helicoptero = relationship("Helicoptero", back_populates="vehiculo_aereo")

class Avion(Base):
    __tablename__ = 'aviones'
    id_avion = Column(Integer, primary_key=True, index=True)
    aerolinea = Column(String)
    tipo_motor = Column(String)
    numero_puertas = Column(Integer)
    tipo_avion = Column(String)
    # Relaciones
    vehiculo_aereo_id = Column(Integer, ForeignKey('vehiculos_aereos.id_vehiculo_aereo'))
    vehiculo_aereo = relationship("VehiculoAereo", back_populates="avion")

class Avioneta(Base):
    __tablename__ = 'avionetas'
    id_avioneta = Column(Integer, primary_key=True, index=True)
    numero_motores = Column(Integer)
    tipo_pista = Column(String)
    tipo_avioneta = Column(String)
    # Relaciones
    vehiculo_aereo_id = Column(Integer, ForeignKey('vehiculos_aereos.id_vehiculo_aereo'))
    vehiculo_aereo = relationship("VehiculoAereo", back_populates="avioneta")

class Helicoptero(Base):
    __tablename__ = 'helicopteros'
    id_helicoptero = Column(Integer, primary_key=True, index=True)
    tipo_helicoptero = Column(String)
    numero_helices = Column(Integer)
    # Relaciones
    vehiculo_aereo_id = Column(Integer, ForeignKey('vehiculos_aereos.id_vehiculo_aereo'))
    vehiculo_aereo = relationship("VehiculoAereo", back_populates="helicoptero")

class Pasajero(Base):
    __tablename__ = 'pasajeros'
    id_pasajero = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    apellido = Column(String)
    direccion = Column(String)
    fecha_nacimiento = Column(Date)
    nacionalidad = Column(String)
    # Relaciones
    persona_id = Column(Integer, ForeignKey('personas.id_persona'))
    persona = relationship("Persona", back_populates="pasajero")
    equipajes = relationship("Equipaje", back_populates="pasajero")
    boletos = relationship("Boleto", back_populates="pasajero")

class Equipaje(Base):
    __tablename__ = 'equipajes'
    id_equipaje = Column(Integer, primary_key=True, index=True)
    peso = Column(Float)
    altura = Column(Float)
    ancho = Column(Float)
    tipo_equipaje = Column(String)
    # Relaciones
    pasajero_id = Column(Integer, ForeignKey('pasajeros.id_pasajero'))
    pasajero = relationship("Pasajero", back_populates="equipajes")

class Boleto(Base):
    __tablename__ = 'boletos'
    id_boleto = Column(Integer, primary_key=True, index=True)
    asiento = Column(String)
    costo = Column(Float)
    # Relaciones
    pasajero_id = Column(Integer, ForeignKey('pasajeros.id_pasajero'))
    pasajero = relationship("Pasajero", back_populates="boletos")
    vuelo_id = Column(Integer, ForeignKey('vuelos.id_vuelo'))
    vuelo = relationship("Vuelo", back_populates="boletos")