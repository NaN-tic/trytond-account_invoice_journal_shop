from trytond.pool import PoolMeta

class Sale(metaclass=PoolMeta):
    __name__ = 'sale.sale'

    def _get_invoice(self):
        invoice = super()._get_invoice()
        invoice.on_change_type()
        return invoice
