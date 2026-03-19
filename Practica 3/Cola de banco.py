from collections import deque

class GestorSaldos:
    def __init__(self, saldo_inicial: int, cantidad_cuentas: int):
        self.saldos = deque([saldo_inicial] * cantidad_cuentas)
        self.historial = deque()

    def es_vacio(self) -> bool:
        return not self.saldos

    def _procesar_transaccion(self, monto: int, es_deposito: bool):
        """Método privado para manejar la lógica común de mover saldos."""
        if self.es_vacio():
            return
        saldo_actual = self.saldos.popleft()
        self.historial.append(saldo_actual)
        nuevo_saldo = saldo_actual + monto if es_deposito else saldo_actual - monto
        self.saldos.append(nuevo_saldo)

    def retirar(self, monto: int):
        self._procesar_transaccion(monto, es_deposito=False)

    def depositar(self, monto: int):
        self._procesar_transaccion(monto, es_deposito=True)

    def limpiar_historial(self):
        self.historial.clear()

banco = GestorSaldos(saldo_inicial=1000, cantidad_cuentas=5)

print("¿Está vacío?", banco.es_vacio())

monto_retiro = 500
for _ in range(5):
    banco.retirar(monto_retiro)

print("Historial (antes del retiro):", list(banco.historial))

banco.limpiar_historial()

monto_deposito = 300
for _ in range(5):
    banco.depositar(monto_deposito)

print("Historial (antes del depósito):", list(banco.historial))
print("Saldos finales: ", list(banco.saldos))