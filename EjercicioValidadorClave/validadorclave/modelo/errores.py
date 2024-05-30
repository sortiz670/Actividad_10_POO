class ErrorValidacion(Exception):
    pass

class NoTieneLetraMayusculaError(ErrorValidacion):
    pass

class NoTieneLetraMinusculaError(ErrorValidacion):
    pass

class NoTieneNumeroError(ErrorValidacion):
    pass

class NoTieneCaracterEspecialError(ErrorValidacion):
    pass

class NoCumpleLongitudMinimaError(ErrorValidacion):
    pass

class NoTienePalabraSecretaError(ErrorValidacion):
    pass
