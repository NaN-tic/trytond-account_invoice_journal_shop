from trytond.pool import PoolMeta
from trytond.model import fields


class Invoice(metaclass=PoolMeta):
    __name__ = 'account.invoice'

    @fields.depends('shop', 'journal')
    def on_change_type(self):
        super(Invoice, self).on_change_type()
        if self.type == 'out' and self.shop and self.shop.journal_revenue:
            self.journal = self.shop.journal_revenue
        elif self.type == 'in' and self.shop and self.shop.journal_expense:
            self.journal = self.shop.journal_expense
