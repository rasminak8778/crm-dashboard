# -*- coding: utf-8 -*-
from odoo import fields, models


class SalesTeam(models.Model):
    _inherit = 'crm.team'

    lead_state_id = fields.Many2one('crm.stage',
                                    string='Lead State',
                                    help='Select any CRM Lead State')
