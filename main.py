from fastapi import FastAPI,HTTPException 
from pydantic import BaseModel #to check the data type in a class
from pydantic import Field #to give a default value to a field
from typing import Optional, List #for optional data 
from uuid import UUID, uuid4 # to generate hast
import uvicorn
from datetime import datetime

class CuentaUsuario():
    def __init__(self, numero, nombre, saldo, NumerosContacto):
        self.numero = numero
        self.nombre = nombre
        self.saldo = saldo
        self.NumerosContacto = NumerosContacto

    def historialOperaciones(self):
        return [op.getOperacion() for op in Operaciones if op.origen == self or op.Destino == self]

    def existeContacto(self,numero:str)->bool:
        return numero in self.NumerosContacto
    
    def transferir(self,destino,valor: int)->bool:
        if self.saldo >= valor and self.existeContacto(destino.numero):
            self.saldo -= valor
            destino.saldo += valor
            Operaciones.append(Operacion(self,destino,valor))
            return True
        
    def listarContactos(self):
        result = []
        for contacto in self.NumerosContacto:
            c = [c for c in BD if c.numero == contacto][0]
            result.append({c.numero, c.nombre})
        return result

BD: List[CuentaUsuario] = [] 
BD.append(CuentaUsuario(numero="21345", nombre="Arnaldo",saldo=200,NumerosContacto=["123","456"]))#
BD.append(CuentaUsuario(numero="123", nombre="Luisa",saldo=400,NumerosContacto=["456"]))
BD.append(CuentaUsuario(numero="456", nombre="Andrea",saldo=300,NumerosContacto=["21345"]))
class Operacion():
    def __init__(self, origen:CuentaUsuario, Destino: CuentaUsuario, Valor):
        self.origen = origen
        self.Destino = Destino
        self.Valor = Valor
        self.fecha = datetime.now()

    def getOperacion(self): 
        return {"origen": self.origen.numero, "Destino": self.Destino.numero, "Valor": self.Valor, "fecha": self.fecha}

Operaciones: List[Operacion] = [] 
app = FastAPI() 
@app.get("/")
def main():
    return {"message": "Examen Final : Billetera Virtual"}


@app.get("/billetera/contactos/minumero/{numero}")
def obtain(numero:int):
    try:
        cuenta = [c for c in BD if c.numero == str(numero)][0]
        data = cuenta.listarContactos()
        return {"message":data}
    except:
        return {"message": "Cuenta no encontrada"}

@app.get("/billetera/historial/minumero/{numero}")
def historial_operaciones(numero:int):
        try:
            cuenta = [c for c in BD if c.numero == str(numero)][0]
            data = cuenta.historialOperaciones()
            return {"message": "Historial de operaciones", "data": data}
        except:
            return {"message": "Cuenta no encontrada"}
        
@app.post("/billetera/pagar/minumero/{numero}/numerodestino/{destino}/valor/{valor}")
def pagar(numero:int,destino:int,valor:int):
        try:
            cuenta = [c for c in BD if c.numero == str(numero)][0]
            cuentaDestino = [c for c in BD if c.numero == str(destino)][0]
            print("here")
            if cuenta.transferir(cuentaDestino,valor):
                return {"message": "Pago exitoso"}
            else:
                return {"message": "Pago fallido"}
        except:
            return {"message": "Cuenta no encontrada"}


if __name__ == "__main__":
    
    uvicorn.run(app, host="127.0.0.1", port=8000)
    

    