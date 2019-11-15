# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.onchange('name')
    def _check_name_unique(self):
        if self.search([('name', '=ilike', self.name)]):
            return {
                'warning': {
                    'title': _('Name repeated'),
                    'message': _('There is a partner with the same name'),
                },
            }

    @api.onchange('vat')
    def _check_vat_unique(self):
        if self.search([('vat', '=', self.vat)]):
            return {
                'warning': {
                    'title': _('VAT repeated'),
                    'message': _('There is a partner with the same VAT'),
                },
            }
