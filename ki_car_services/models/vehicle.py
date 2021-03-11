# -*- coding: utf-8 -*-
# Part of Kiran Infosoft. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class Vehicle(models.Model):
    _inherit = 'fleet.vehicle.model'

    @api.depends('service_order_ids')
    def _compute_service_order_count(self):
        for rec in self:
            rec.service_order_count = len(rec.service_order_ids)

    service_order_ids = fields.One2many(
        'sale.order',
        "car_id",
        string="Service Orders",
    )
    service_order_count = fields.Integer(
        string="Service Orders#",
        compute="_compute_service_order_count",
    )

    @api.multi
    def action_view_service_orders(self):
        act =self.env.ref('ki_car_services.action_service_orders')
        act_read = act.read([])[0]
        act_read['domain'] = [('car_id', '=', self.id)]
        return act_read

    @api.depends('service_order_ids')
    def _compute_service_task_count(self):
        for rec in self:
            rec.service_task_count = len(rec.service_task_ids)

    service_task_ids = fields.One2many(
        'project.task',
        "car_id",
        string="Service Tasks",
    )
    service_task_count = fields.Integer(
        string="Service Tasks#",
        compute="_compute_service_task_count",
    )

    @api.multi
    def action_view_service_tasks(self):
        act =self.env.ref('ki_car_services.action_view_service_tasks')
        act_read = act.read([])[0]
        act_read['domain'] = [('car_id', '=', self.id)]
        return act_read
