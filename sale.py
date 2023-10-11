from trytond.pool import PoolMeta

class Sale(metaclass=PoolMeta):
    __name__ = 'sale.sale'

    def _get_invoice_sale(self):
        invoice = super()._get_invoice_sale()
        invoice.on_change_type()
        return invoice
