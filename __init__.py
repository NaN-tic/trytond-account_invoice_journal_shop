# This file is part account_invoice_journal_shop module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import shop
from . import invoice
from . import sale


def register():
    module = 'account_invoice_journal_shop'
    Pool.register(
        invoice.Invoice,
        sale.Sale,
        shop.Shop,
        module=module, type_='model')
