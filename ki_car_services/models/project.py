# -*- coding: utf-8 -*-
# Part of Kiran Infosoft. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class ProjectTask(models.Model):
    _inherit = 'project.task'

    car_id = fields.Many2one(
        'fleet.vehicle.model',
        string="Car",
        copy=False
    )
    is_pick_up = fields.Boolean(
        string="Pick Up?",
        copy=False
    )
    car_number = fields.Char(
        string="Car Number",
        copy=False
    )
    service_schedule_date = fields.Datetime(
        string="Schedule Date",
        copy=False
    )
    pickup_address = fields.Text(
        string="Pickup Address",
        copy=False
    )
    car_service_ids = fields.Many2many(
        'fleet.service.type',
        string="Services",
        copy=False
    )