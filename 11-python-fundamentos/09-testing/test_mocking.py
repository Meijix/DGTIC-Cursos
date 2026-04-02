"""
Mocking — Simular Dependencias Externas
==========================================
El mocking reemplaza partes reales del sistema con objetos simulados.
Es esencial cuando tu codigo depende de servicios externos (APIs,
bases de datos, sistema de archivos, hora actual).

Ejecutar estos tests:
    pytest test_mocking.py -v
"""

import pytest
from unittest.mock import Mock, MagicMock, patch, call


# ============================================================
# MODULO A TESTEAR — Funciones que dependen de cosas externas
# ============================================================

import urllib.request
import json


def obtener_clima(ciudad):
    """
    Consulta el clima de una ciudad usando wttr.in.
    Esta funcion DEPENDE de internet — necesitamos mockearla en tests.
    """
    url = f"https://wttr.in/{ciudad}?format=j1"
    respuesta = urllib.request.urlopen(url)
    datos = json.loads(respuesta.read())
    temp = datos["current_condition"][0]["temp_C"]
    return {"ciudad": ciudad, "temperatura": int(temp)}


def enviar_notificacion(usuario, mensaje, servicio_email):
    """
    Envia una notificacion por email.
    Recibe el servicio de email como parametro (inyeccion de dependencia).
    """
    if not usuario.get("email"):
        raise ValueError("El usuario no tiene email")

    resultado = servicio_email.enviar(
        destinatario=usuario["email"],
        asunto="Notificacion",
        cuerpo=mensaje,
    )
    return resultado


def procesar_pedido(pedido, db, logger):
    """
    Procesa un pedido usando una base de datos y un logger.
    Ambos seran mockeados en los tests.
    """
    logger.info(f"Procesando pedido #{pedido['id']}")

    producto = db.obtener_producto(pedido["producto_id"])
    if not producto:
        logger.error(f"Producto {pedido['producto_id']} no encontrado")
        return False

    if producto["stock"] < pedido["cantidad"]:
        logger.warning("Stock insuficiente")
        return False

    db.reducir_stock(pedido["producto_id"], pedido["cantidad"])
    db.guardar_pedido(pedido)
    logger.info(f"Pedido #{pedido['id']} procesado exitosamente")
    return True


# ============================================================
# 1. MOCK BASICO — Objeto que acepta cualquier llamada
# ============================================================

class TestMockBasico:
    """Demostrar el uso basico de Mock."""

    def test_mock_acepta_cualquier_metodo(self):
        """Un Mock acepta cualquier atributo o metodo."""
        mock = Mock()

        # Llamar metodos que no existen — no lanza error
        mock.metodo_inventado()
        mock.otro_metodo(1, 2, 3)
        mock.atributo.sub_atributo.metodo()

        # Todo retorna otro Mock por defecto
        resultado = mock.algo()
        assert isinstance(resultado, Mock)

    def test_mock_con_return_value(self):
        """Configurar lo que retorna un Mock."""
        mock = Mock()
        mock.obtener_datos.return_value = {"nombre": "Ana", "edad": 25}

        resultado = mock.obtener_datos()
        assert resultado["nombre"] == "Ana"
        assert resultado["edad"] == 25

    def test_mock_con_side_effect(self):
        """side_effect permite definir comportamiento dinamico."""
        mock = Mock()

        # side_effect con excepcion — el mock lanza un error
        mock.conectar.side_effect = ConnectionError("Sin conexion")
        with pytest.raises(ConnectionError, match="Sin conexion"):
            mock.conectar()

        # side_effect con funcion — logica personalizada
        mock.calcular.side_effect = lambda x: x ** 2
        assert mock.calcular(5) == 25

        # side_effect con lista — retorna valores en secuencia
        mock.siguiente.side_effect = [1, 2, 3]
        assert mock.siguiente() == 1
        assert mock.siguiente() == 2
        assert mock.siguiente() == 3

    def test_mock_verificar_llamadas(self):
        """Verificar COMO se llamo un mock (espia)."""
        mock = Mock()
        mock.guardar("datos", formato="json")

        # Verificar que se llamo
        mock.guardar.assert_called()
        mock.guardar.assert_called_once()
        mock.guardar.assert_called_with("datos", formato="json")

        # Verificar numero de llamadas
        assert mock.guardar.call_count == 1

        # Verificar argumentos
        args, kwargs = mock.guardar.call_args
        assert args == ("datos",)
        assert kwargs == {"formato": "json"}


# ============================================================
# 2. MAGICMOCK — Mock con metodos magicos
# ============================================================

class TestMagicMock:
    """MagicMock soporta metodos magicos como __len__, __iter__."""

    def test_magic_mock_len(self):
        """MagicMock puede simular __len__."""
        mock = MagicMock()
        mock.__len__.return_value = 5
        assert len(mock) == 5

    def test_magic_mock_iter(self):
        """MagicMock puede simular __iter__."""
        mock = MagicMock()
        mock.__iter__.return_value = iter([1, 2, 3])
        assert list(mock) == [1, 2, 3]

    def test_magic_mock_context_manager(self):
        """MagicMock puede simular un context manager."""
        mock = MagicMock()
        mock.__enter__.return_value = "recurso"

        with mock as r:
            assert r == "recurso"


# ============================================================
# 3. MOCK CON INYECCION DE DEPENDENCIAS
# ============================================================

class TestEnviarNotificacion:
    """Testear funciones pasando mocks como argumentos."""

    def test_enviar_exitoso(self):
        """Simula un envio de email exitoso."""
        # ARRANGE
        usuario = {"nombre": "Ana", "email": "ana@test.com"}
        mensaje = "Tu pedido fue enviado"
        servicio_mock = Mock()
        servicio_mock.enviar.return_value = {"status": "enviado", "id": "123"}

        # ACT
        resultado = enviar_notificacion(usuario, mensaje, servicio_mock)

        # ASSERT
        assert resultado["status"] == "enviado"
        servicio_mock.enviar.assert_called_once_with(
            destinatario="ana@test.com",
            asunto="Notificacion",
            cuerpo="Tu pedido fue enviado",
        )

    def test_enviar_sin_email_lanza_error(self):
        """Verifica que falla si el usuario no tiene email."""
        usuario = {"nombre": "Luis"}
        servicio_mock = Mock()

        with pytest.raises(ValueError, match="no tiene email"):
            enviar_notificacion(usuario, "mensaje", servicio_mock)

        # El servicio NUNCA debio ser llamado
        servicio_mock.enviar.assert_not_called()


# ============================================================
# 4. PATCH — Reemplazar objetos temporalmente
# ============================================================

class TestPatch:
    """
    patch() reemplaza un objeto en el lugar donde se USA
    (no donde se define). Es crucial entender la diferencia.
    """

    @patch("urllib.request.urlopen")
    def test_obtener_clima_con_patch_decorador(self, mock_urlopen):
        """
        @patch como decorador: reemplaza urlopen durante el test.
        El mock se pasa como argumento EXTRA al metodo de test.
        """
        # Configurar la respuesta simulada
        respuesta_simulada = Mock()
        respuesta_simulada.read.return_value = json.dumps({
            "current_condition": [{"temp_C": "22"}]
        }).encode()
        mock_urlopen.return_value = respuesta_simulada

        # Ejecutar
        resultado = obtener_clima("Mexico")

        # Verificar
        assert resultado["ciudad"] == "Mexico"
        assert resultado["temperatura"] == 22
        mock_urlopen.assert_called_once()

    def test_obtener_clima_con_patch_context_manager(self):
        """
        patch como context manager: mas explicito sobre el alcance.
        """
        with patch("urllib.request.urlopen") as mock_urlopen:
            respuesta_simulada = Mock()
            respuesta_simulada.read.return_value = json.dumps({
                "current_condition": [{"temp_C": "15"}]
            }).encode()
            mock_urlopen.return_value = respuesta_simulada

            resultado = obtener_clima("Bogota")
            assert resultado["temperatura"] == 15

        # Fuera del 'with', urlopen vuelve a ser el original


# ============================================================
# 5. EJEMPLO COMPLEJO: MULTIPLES MOCKS
# ============================================================

class TestProcesarPedido:
    """Testear una funcion con multiples dependencias mockeadas."""

    def test_pedido_exitoso(self):
        """Pedido se procesa cuando hay stock suficiente."""
        # ARRANGE
        pedido = {"id": 1, "producto_id": "LAPTOP", "cantidad": 2}

        db_mock = Mock()
        db_mock.obtener_producto.return_value = {
            "id": "LAPTOP", "nombre": "Laptop", "stock": 10
        }
        logger_mock = Mock()

        # ACT
        resultado = procesar_pedido(pedido, db_mock, logger_mock)

        # ASSERT
        assert resultado is True
        db_mock.reducir_stock.assert_called_once_with("LAPTOP", 2)
        db_mock.guardar_pedido.assert_called_once_with(pedido)

    def test_pedido_producto_no_encontrado(self):
        """Pedido falla cuando el producto no existe."""
        pedido = {"id": 2, "producto_id": "NADA", "cantidad": 1}

        db_mock = Mock()
        db_mock.obtener_producto.return_value = None
        logger_mock = Mock()

        resultado = procesar_pedido(pedido, db_mock, logger_mock)

        assert resultado is False
        logger_mock.error.assert_called_once()
        db_mock.guardar_pedido.assert_not_called()

    def test_pedido_sin_stock(self):
        """Pedido falla cuando no hay stock suficiente."""
        pedido = {"id": 3, "producto_id": "MOUSE", "cantidad": 100}

        db_mock = Mock()
        db_mock.obtener_producto.return_value = {
            "id": "MOUSE", "nombre": "Mouse", "stock": 5
        }
        logger_mock = Mock()

        resultado = procesar_pedido(pedido, db_mock, logger_mock)

        assert resultado is False
        logger_mock.warning.assert_called_once()
        db_mock.reducir_stock.assert_not_called()
