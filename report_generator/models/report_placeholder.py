from odoo import models, fields

class ReportGeneratorReportPlaceholder(models.Model):
    _name = "reportgenerator.report.placeholder"
    _description = "Report Generator Placeholder"
    
    name = fields.Char(
        string="Name",
        required=True
    )
    
    report_id = fields.Many2one(
        comodel_name="reportgenerator.report",
        string="Related report"
    )
    
    text_field = fields.Char(
        string="Code",
        required=True
    )
    
    text_size = fields.Integer(
        string="Font size",
        required=True
    )
    
    text_color = fields.Char(
        string="Color",
        required=True
    )
     
    text_font_id = fields.Many2one(
        comodel_name="reportgenerator.report.placeholder.font",
        string="Font",
        required=True
    )
    
    text_alignment = fields.Selection(
        selection=[
            ('left', 'Left'),
            ('right', 'Right'),
            ('center', 'Center'),
        ],
        string="Alignment",
        required=True,
        default="left"
    )
    
    page = fields.Integer(
        string="Page",
        required=True,
        default=1
    )
    
    position_x = fields.Integer(
        string="Position X",
        required=True
    )
    
    position_y = fields.Integer(
        string="Position Y",
        required=True
    )
