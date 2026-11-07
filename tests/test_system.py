import pytest
from core.base import PaymentMethod
from core.registry import buat_metode


def test_payment_method_is_abstract():
    """Memastikan Abstract Base Class PaymentMethod tidak dapat diinstansiasi langsung."""
    with pytest.raises(TypeError):
        PaymentMethod("Test Abstract")  # type: ignore


def test_unknown_plugin_raises_keyerror():
    """Memastikan mengambil plugin yang tidak terdaftar memunculkan KeyError."""
    with pytest.raises(KeyError):
        buat_metode("plugin_ngawur_yang_tidak_ada")