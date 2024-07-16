from main import CuentaUsuario, Operacion, BD, pagar

import pytest

@pytest.mark.parametrize(
    "Usuario", #parameter value
    [
        (CuentaUsuario(numero="21345", nombre="Arnaldo",saldo=200,NumerosContacto=["123","456"])),
        (CuentaUsuario(numero="456", nombre="Andrea",saldo=300,NumerosContacto=["21345"])),
        (CuentaUsuario(numero="123", nombre="Luisa",saldo=400,NumerosContacto=["456"]))
    ]
)


# Caso de prueba: Validamos la creacion de un usuario
def test_exists(Usuario:CuentaUsuario):
    resp = [c for c in BD if c.numero == Usuario.numero]
    assert len(resp) ==1

@pytest.mark.parametrize(
    "Usuario", #parameter value
    [
        (CuentaUsuario(numero="21345", nombre="Arnaldo",saldo=200,NumerosContacto=["123","456"])),
        (CuentaUsuario(numero="123", nombre="Luisa",saldo=400,NumerosContacto=["456"]))
    ]
)

# Caso de prueba: Valimos el listado de contactos
def test_listarContactos(Usuario:CuentaUsuario):
    resp = [c for c in BD if c.numero == Usuario.numero][0]
    assert len(resp.NumerosContacto) == 1
    


@pytest.mark.parametrize(
    "Usuario,Destino,Valor", #parameter value
    [
        (CuentaUsuario(numero="21345", nombre="Arnaldo",saldo=200,NumerosContacto=["123","456"]), CuentaUsuario(numero="456", nombre="Andrea",saldo=300,NumerosContacto=["21345"]), 5),
        (CuentaUsuario(numero="21345", nombre="Arnaldo",saldo=200,NumerosContacto=["123","456"]), CuentaUsuario(numero="456", nombre="Andrea",saldo=300,NumerosContacto=["21345"]), 10)
    ]
)

# Caso de prueba: Validamos la transferencia de dinero
def test_transferir(Usuario:CuentaUsuario, Destino:CuentaUsuario, Valor:int):

    assert Usuario.transferir(Destino, Valor) == True

    # Caso de error: El saldo restante no cumple con el valor de la transferencia
    assert Usuario.saldo == 195
    # Caso de error: El saldo restante no cumple con el valor de la transferencia
    assert Destino.saldo == 305
