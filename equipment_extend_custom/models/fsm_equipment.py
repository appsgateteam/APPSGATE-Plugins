# -*- coding: utf-8 -*-


from odoo import fields, models, api


class FSMEquipment(models.Model):
    _inherit = 'fsm.equipment'
    
    warranty_information_custom = fields.Char(
        string='Warranty Information',
        required=True,
        copy=False
    )
    warranty_date_custom = fields.Date(
        string='Warranty Date',
        required=True,
        copy=False   
    )
    warranty_service_provider_custom_id = fields.Many2one(
        'res.partner',
        string='Warranty Service Provider',
        required=True,
        copy=False,
    )
    manufacturer_custom = fields.Char(
        string='Manufacturer',
        copy=False,
        required=True,
    )
    record_brand_custom = fields.Char(
        string='Record Brand',
        copy=False,
        required=True,
    )
    model_number_custom = fields.Char(
        string='Model Number',
        copy=False,
        required=True,
    )
    serial_number_custom = fields.Char(
        string='Serial Number',
        copy=False,
        required=True,
    )
    received_date_custom = fields.Date(
        string='Received Date',
        required=True,
        copy=False   
    )
