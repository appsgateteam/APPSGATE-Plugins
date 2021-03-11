# -*- coding: utf-8 -*-
# Part of Kiran Infosoft. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class Product(models.Model):
    _inherit = 'product.template'

    is_car_service = fields.Boolean(
        string="Car Service",
        copy=False
    )
    vehical_ids = fields.Many2many(
        'fleet.vehicle.model',
        string="Cars",
    )
    service_type_ids = fields.Many2many(
        'fleet.service.type',
        string="Services",
    )
