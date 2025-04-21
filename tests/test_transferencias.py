import pytest
from app.model_sim import interpretar

def test_transferencia_valida():
    entrada = "Transferir $500 a Juan"
    salida = interpretar(entrada)
    assert "éxito" in salida.lower()

def test_transferencia_sin_monto():
    entrada = "Transferir dinero a Pedro"
    salida = interpretar(entrada)
    assert "monto válido" in salida.lower()

def test_consulta_saldo():
    entrada = "¿Cuál es mi saldo?"
    salida = interpretar(entrada)
    assert "$" in salida

def test_input_invalido():
    entrada = "quiero pizza"
    salida = interpretar(entrada)
    assert "no entendí" in salida.lower()