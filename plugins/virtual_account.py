from core.base import PaymentMethod
from core.registry import register_plugin
from core.utils import buat_id


@register_plugin("va")
class VirtualAccount(PaymentMethod):
    BATAS_TRANSAKSI = 10_000_000

    def __init__(self, bank: str = "BCA", kadaluarsa_jam: int = 24):
        super().__init__(f"Virtual Account {bank}")
        self.kadaluarsa_jam = kadaluarsa_jam
        self.status = "menunggu"

    def biaya_admin(self, jumlah: float) -> float:
        return 4000.0

    def validasi(self, jumlah: float) -> bool:
        return jumlah <= self.BATAS_TRANSAKSI

    def bayar(self, jumlah: float) -> str:
        self.status = "dibayar"
        return buat_id("VA")