from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from logging import getLogger

_logger = getLogger(__name__)

class ReportGeneratorPreviewWizard(models.TransientModel):
    _name = "reportgenerator.preview.wizard"
    _description = "Report Generator Preview Wizard"

    res_id = fields.Integer(
        string="Resource ID"
    )

    file = fields.Binary(
        string="File"
    )

    @api.onchange('res_id')
    def _onchange_res_id(self):
        if self.res_id > 0:
            report_id = self.env['reportgenerator.report'].browse(self.env.context.get("default_report_id"))
            self.file = report_id.generate_report(self.res_id)['content']