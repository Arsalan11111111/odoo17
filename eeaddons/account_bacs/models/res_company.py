# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

from odoo.exceptions import ValidationError


class ResCompany(models.Model):
    _inherit = 'res.company'

    bacs_sun = fields.Char(string='Service User Number', help="Service user number of your company within BACS, given by the bank.")

    @api.constrains('bacs_sun')
    def validate_bacs_direct_credit_sun(self):
        for record in self:
            if not record.bacs_sun:
                continue

            if len(record.bacs_sun) != 6:
                raise ValidationError(_("The service user number must be 6 characters long."))

            if not record.bacs_sun.isdigit():
                raise ValidationError(_("The service user number must be numeric."))
