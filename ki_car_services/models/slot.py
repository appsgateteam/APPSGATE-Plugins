# -*- coding: utf-8 -*-
# Part of Kiran Infosoft. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class ServiceTimeSlot(models.Model):
    _name = 'service.time.slot'

    name = fields.Float(
        string="Slot",
        readonly=True
    )
    active = fields.Boolean(
        string="Available For Service?"
    )
