"""
Excepciones Personalizadas en Python
=======================================
Crea tus propias excepciones cuando las excepciones built-in no
describen bien el error de tu dominio. Esto hace que el codigo
sea mas legible y el manejo de errores mas preciso.

Ejecuta este archivo:
    python excepciones_custom.py
"""

# ============================================================
# 1. EXCEPCION PERSONALIZADA BASICA
# ============================================================

# La forma mas simple: heredar de Exception y nada mas.
# El nombre descriptivo ya aporta valor.

class EdadInvalidaError(Exception):
    """Se lanza cuando la edad no es un valor aceptable."""
    pass

print("=== Excepcion basica ===\n")

def verificar_edad(edad):
    if not isinstance(edad, (int, float)):
        raise TypeError(f"La edad debe ser numerica, recibio {type(edad).__name__}")
    if edad < 0 or edad > 150:
        raise EdadInvalidaError(f"Edad fuera de rango: {edad}")
    return True

try:
    verificar_edad(-5)
except EdadInvalidaError as e:
    print(f"Capturado EdadInvalidaError: {e}")

# ============================================================
# 2. EXCEPCION CON ATRIBUTOS ADICIONALES
# ============================================================

class ErrorDeValidacion(Exception):
    """
    Excepcion con atributos extra para dar contexto.
    Incluye el campo que fallo, el valor recibido y un mensaje.
    """

    def __init__(self, campo, valor, mensaje="Valor invalido"):
        self.campo = campo
        self.valor = valor
        self.mensaje = mensaje
        # Llamar a super().__init__ con un mensaje completo
        super().__init__(f"[{campo}] {mensaje} (recibio: {valor!r})")

print("\n=== Excepcion con atributos ===\n")

def validar_email(email):
    if not isinstance(email, str):
        raise ErrorDeValidacion("email", email, "Debe ser un string")
    if "@" not in email:
        raise ErrorDeValidacion("email", email, "Falta el simbolo @")
    if "." not in email.split("@")[1]:
        raise ErrorDeValidacion("email", email, "Dominio invalido")
    return True

for email_test in ["usuario@correo.com", "sin_arroba", 12345]:
    try:
        validar_email(email_test)
        print(f"  '{email_test}' es valido")
    except ErrorDeValidacion as e:
        # Accedemos a los atributos especificos
        print(f"  Campo: {e.campo}, Valor: {e.valor!r}, Mensaje: {e.mensaje}")

# ============================================================
# 3. JERARQUIA DE EXCEPCIONES
# ============================================================

# Es buena practica crear una excepcion BASE para tu aplicacion.
# Las demas heredan de ella. Asi puedes capturar TODAS las de tu app
# con un solo except, o ser mas especifico.

class ErrorBancario(Exception):
    """Excepcion base para todos los errores del sistema bancario."""
    pass

class SaldoInsuficienteError(ErrorBancario):
    """Se lanza cuando no hay fondos suficientes."""

    def __init__(self, cuenta, saldo_actual, monto_solicitado):
        self.cuenta = cuenta
        self.saldo_actual = saldo_actual
        self.monto_solicitado = monto_solicitado
        self.faltante = monto_solicitado - saldo_actual
        super().__init__(
            f"Cuenta {cuenta}: saldo ${saldo_actual:.2f}, "
            f"se requieren ${monto_solicitado:.2f} "
            f"(faltan ${self.faltante:.2f})"
        )

class CuentaNoEncontradaError(ErrorBancario):
    """Se lanza cuando la cuenta no existe."""

    def __init__(self, cuenta_id):
        self.cuenta_id = cuenta_id
        super().__init__(f"Cuenta '{cuenta_id}' no encontrada")

class MontoInvalidoError(ErrorBancario):
    """Se lanza cuando el monto no es valido."""

    def __init__(self, monto, razon="Monto debe ser positivo"):
        self.monto = monto
        self.razon = razon
        super().__init__(f"Monto invalido: ${monto} ({razon})")

# --- Simulacion de un banco simple ---

class BancoSimple:
    """Banco que demuestra el uso de excepciones personalizadas."""

    def __init__(self):
        self.cuentas = {}

    def crear_cuenta(self, cuenta_id, saldo_inicial=0):
        if saldo_inicial < 0:
            raise MontoInvalidoError(saldo_inicial, "Saldo inicial negativo")
        self.cuentas[cuenta_id] = saldo_inicial
        return saldo_inicial

    def consultar_saldo(self, cuenta_id):
        if cuenta_id not in self.cuentas:
            raise CuentaNoEncontradaError(cuenta_id)
        return self.cuentas[cuenta_id]

    def retirar(self, cuenta_id, monto):
        if monto <= 0:
            raise MontoInvalidoError(monto)

        saldo = self.consultar_saldo(cuenta_id)  # Puede lanzar CuentaNoEncontradaError

        if monto > saldo:
            raise SaldoInsuficienteError(cuenta_id, saldo, monto)

        self.cuentas[cuenta_id] -= monto
        return self.cuentas[cuenta_id]

print("\n=== Jerarquia de excepciones bancarias ===\n")

banco = BancoSimple()
banco.crear_cuenta("001", 1000)
banco.crear_cuenta("002", 500)

# Caso 1: operacion exitosa
try:
    nuevo_saldo = banco.retirar("001", 200)
    print(f"Retiro exitoso. Nuevo saldo: ${nuevo_saldo:.2f}")
except ErrorBancario as e:
    print(f"Error: {e}")

# Caso 2: saldo insuficiente
try:
    banco.retirar("002", 999)
except SaldoInsuficienteError as e:
    print(f"Saldo insuficiente: faltan ${e.faltante:.2f}")

# Caso 3: cuenta no existe
try:
    banco.retirar("999", 100)
except CuentaNoEncontradaError as e:
    print(f"Cuenta no encontrada: {e.cuenta_id}")

# Caso 4: capturar CUALQUIER error bancario con la base
try:
    banco.retirar("001", -50)
except ErrorBancario as e:
    # Captura MontoInvalidoError porque hereda de ErrorBancario
    print(f"Error bancario generico: {type(e).__name__}: {e}")

# ============================================================
# 4. VERIFICAR LA JERARQUIA
# ============================================================

print("\n=== Verificacion de jerarquia ===\n")

error = SaldoInsuficienteError("001", 100, 500)
print(f"Es SaldoInsuficienteError: {isinstance(error, SaldoInsuficienteError)}")
print(f"Es ErrorBancario: {isinstance(error, ErrorBancario)}")
print(f"Es Exception: {isinstance(error, Exception)}")

# Esto permite manejar errores a diferentes niveles de granularidad:
# - except SaldoInsuficienteError:  → manejo especifico
# - except ErrorBancario:           → manejo de cualquier error bancario
# - except Exception:               → manejo generico

print("""
=== BUENAS PRACTICAS ===

1. Hereda de Exception (nunca de BaseException).
2. Crea una excepcion BASE para tu aplicacion/modulo.
3. Nombres descriptivos terminados en Error o Exception.
4. Agrega atributos utiles (__init__ con datos de contexto).
5. Siempre llama a super().__init__() con un mensaje claro.
6. Documenta cuando y por que se lanza cada excepcion.
""")
