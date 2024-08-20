from odoo import api, fields, models
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT


class ProductTemplate(models.Model):
    _inherit = "product.template"

    cluster = fields.Char()


