from trytond.pool import PoolMeta
from trytond.model import fields
from trytond.pyson import Eval


class Shop(metaclass=PoolMeta):
    __name__ = 'sale.shop'

    journal_revenue = fields.Many2One(
        'account.journal', 'Account Journal Revenue',
        domain=[
            ('type', '=', 'revenue'),
            ],
        context={
            'company': Eval('company', -1),
            },
        depends=['company'])
    journal_expense = fields.Many2One(
        'account.journal', 'Account Journal Expense',
        domain=[
            ('type', '=', 'expense'),
            ],
        context={
            'company': Eval('company', -1),
            },
        depends=['company'])
