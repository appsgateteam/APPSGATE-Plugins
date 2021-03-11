# -*- coding: utf-8 -*-
# Part of Kiran Infosoft. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.depends(
        'order_line',
        'order_line.product_id',
        'order_line.product_id.service_type_ids'
    )
    def _compute_car_services(self):
        for rec in self:
            rec.car_service_ids = self.order_line.mapped(
                'product_id'
            ).mapped('service_type_ids')

    car_id = fields.Many2one(
        'fleet.vehicle.model',
        string="Car",
    )
    car_number = fields.Char(
        string="Car Number",
        copy=False
    )
    is_pick_up = fields.Boolean(
        string="Pick Up?",
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
        compute="_compute_car_services",
    )


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def _timesheet_create_task_prepare_values(self, project):
        vals = super(
            SaleOrderLine, self
        )._timesheet_create_task_prepare_values(project)
        if self.order_id.car_id:
            vals.update({
                'car_id': self.order_id.car_id.id,
                'car_number': self.order_id.car_number,
                'is_pick_up': self.order_id.is_pick_up,
                'service_schedule_date': self.order_id.service_schedule_date,
                'pickup_address': self.order_id.pickup_address,
                'car_service_ids': [
                    (4, i.id) for i in self.order_id.car_service_ids
                ]
            })
        return vals
