import pytest
from validadorclave.modelo.validacion import ReglaValidacionGanimedes, ReglaValidacionCalisto
from validadorclave.modelo.validador import Validador
from validadorclave.modelo.errores import *

def test_validacion_ganimedes():
    regla = ReglaValidacionGanimedes()
    validador = Validador(regla)
    
    assert validador.es_valida("Aabc123@") == True
    
    with pytest.raises(ErrorLongitud):
        validador.es_valida("Aabc1@")
    
    with pytest.raises(ErrorMayuscula):
        validador.es_valida("abc123@")
    
    with pytest.raises(ErrorMinuscula):
        validador.es_valida("ABC123@")
    
    with pytest.raises(ErrorNumero):
        validador.es_valida("Abcdef@")
    
    with pytest.raises(ErrorCaracterEspecial):
        validador.es_valida("Abc12345")

def test_validacion_calisto():
    regla = ReglaValidacionCalisto()
    validador = Validador(regla)
    
    assert validador.es_valida("123calIStO") == True
    
    with pytest.raises(ErrorLongitud):
        validador.es_valida("123calI")
    
    with pytest.raises(ErrorNumero):
        validador.es_valida("calIStO")
    
    with pytest.raises(ErrorCalisto):
        validador.es_valida("123calisto")
    
    with pytest.raises(ErrorCalisto):
        validador.es_valida("123CALISTO")
