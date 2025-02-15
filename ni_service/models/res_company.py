#  Copyright (c) 2024 NSTDA
from odoo import fields, models


class Company(models.Model):
    _inherit = "res.company"

    service_calendar_id = fields.Many2one(
        "resource.calendar",
        help="Default service resource calendar",
        domain="[('company_id', '=', id)]",
    )
    service_attendance_ids = fields.Many2many(
        "resource.calendar.attendance",
        help="Default service resource calendar",
        domain="[('calendar_id', '=', service_calendar_id)]",
    )
