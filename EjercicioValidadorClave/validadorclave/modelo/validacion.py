from abc import ABC, abstractmethod
from .errores import *

class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada: int):
        self._longitud_esperada = longitud_esperada

    def _validar_longitud(self, clave: str) -> bool:
        return len(clave) > self._longitud_esperada

    def _contiene_mayuscula(self, clave: str) -> bool:
        return any(c.isupper() for c in clave)

    def _contiene_minuscula(self, clave: str) -> bool:
        return any(c.islower() for c in clave)

    def _contiene_numero(self, clave: str) -> bool:
        return any(c.isdigit() for c in clave)

    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        pass

class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self):
        super().__init__(8)

    def contiene_caracter_especial(self, clave: str) -> bool:
        caracteres_especiales = '@_#$%'
        return any(c in caracteres_especiales for c in clave)

    def es_valida(self, clave: str) -> bool:
        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError("La clave no tiene la longitud mínima requerida.")
        if not self._contiene_mayuscula(clave):
            raise NoTieneLetraMayusculaError("La clave no contiene al menos una letra mayúscula.")
        if not self._contiene_minuscula(clave):
            raise NoTieneLetraMinusculaError("La clave no contiene al menos una letra minúscula.")
        if not self._contiene_numero(clave):
            raise NoTieneNumeroError("La clave no contiene al menos un número.")
        if not self.contiene_caracter_especial(clave):
            raise NoTieneCaracterEspecialError("La clave no contiene al menos un carácter especial.")
        return True

class ReglaValidacionCalisto(ReglaValidacion):
    def __init__(self):
        super().__init__(6)

    def contiene_calisto(self, clave: str) -> bool:
        index = clave.lower().find('calisto')
        if index == -1:
            return False
        substring = clave[index:index+7]
        mayusculas = sum(1 for c in substring if c.isupper())
        minusculas = sum(1 for c in substring if c.islower())
        return mayusculas >= 2 and mayusculas < 7 and minusculas > 0

    def es_valida(self, clave: str) -> bool:
        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError("La clave no tiene la longitud mínima requerida.")
        if not self._contiene_numero(clave):
            raise NoTieneNumeroError("La clave no contiene al menos un número.")
        if not self.contiene_calisto(clave):
            raise NoTienePalabraSecretaError("La clave no contiene la palabra 'calisto' con al menos dos letras mayúsculas y no todas.")
        return True
