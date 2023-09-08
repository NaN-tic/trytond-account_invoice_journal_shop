from trytond.pool import PoolMeta
from trytond.model import fields
from trytond.pyson import Eval


class Shop(metaclass=PoolMeta):
    __name__ = 'sale.shop'

    logo = fields.Binary('Logo')
    email = fields.Char('E-mail')
    phone = fields.Char('Phone')

    journal_revenue = fields.Many2One(
        'account.journal', 'Account Journal Revenue',
        domain=[
            ('type', '=', 'revenue'),
            ],
        context={
            'company': Eval('company'),
            },
        depends=['company'])
    journal_expense = fields.Many2One(
        'account.journal', 'Account Journal Expense',
        domain=[
            ('type', '=', 'expense'),
            ],
        context={
            'company': Eval('company'),
            },
        depends=['company'])
