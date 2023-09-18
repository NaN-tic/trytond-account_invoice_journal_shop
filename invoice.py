from trytond.pool import PoolMeta
from trytond.model import fields


class Invoice(metaclass=PoolMeta):
    __name__ = 'account.invoice'

    @fields.depends('type', 'shop')
    def set_journal(self, pattern=None):
        super(Invoice, self).set_journal(pattern)
        if self.type == 'out' and self.shop and self.shop.journal_revenue:
            self.journal = self.shop.journal_revenue
        elif self.type == 'in' and self.shop and self.shop.journal_expense:
            self.journal = self.shop.journal_expense

    @fields.depends(methods=['on_change_type'])
    def on_change_shop(self):
        super().on_change_shop()
        self.on_change_type()
