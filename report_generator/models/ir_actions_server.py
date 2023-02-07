from odoo import models, fields

class IrActionsServer(models.Model):
    _inherit = 'ir.actions.server'

    reportgenerator_report_id = fields.Many2one(
        comodel_name="reportgenerator.report",
        string="Related Report"
    )