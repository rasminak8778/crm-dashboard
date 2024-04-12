# -*- coding: utf-8 -*-
from odoo import models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        """function defined to Once the quotation is confirmed move the related
        lead/opportunity to sales team stage."""
        res = super(SaleOrder, self).action_confirm()
        for order in self:
            if order.team_id and order.team_id.lead_state_id:
                opportunity = order.opportunity_id
                if opportunity.stage_id != order.team_id.lead_state_id:
                    opportunity.stage_id = order.team_id.lead_state_id
        return res
