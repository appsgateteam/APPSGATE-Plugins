# -*- coding: utf-8 -*-
import werkzeug
import json
import pytz
from datetime import datetime, time

from odoo import fields, http, _
from odoo.http import request


class CarServices(http.Controller):

    @http.route(['/car/selection'], type='http', auth="public", website=True)
    def car_selection(self, **post):
        order = request.website.sale_get_order()
        cars = request.env['fleet.vehicle.model'].sudo().search([])
        brands = request.env['fleet.vehicle.model.brand'].sudo().search([])
        values = {'cars': cars, 'brands': brands, 'order': order}
        return request.render("ki_car_services.template_car_selection", values)

    @http.route(['/car/services'], type='http', auth="public", website=True)
    def car_services(self, **kw):
        car_id = int(kw.get('car_id', 0))
        if car_id:
            request.session['car_id'] = car_id

        car_id = request.session['car_id']

        products = request.env['product.template'].sudo().search([
            ('is_car_service', '=', True),
            '|',
            ('vehical_ids', 'in', car_id),
            ('vehical_ids', '=', False)
        ])
        values = {
            'products': products,
            'car_id': car_id
        }
        return request.render("ki_car_services.template_car_services", values)

    @http.route([
        '''/car/add/service/<int:product>'''
    ], type='http', auth="public", website=True)
    def add_car(self, product=None, **post):
        order = request.website.sale_get_order(force_create=1)
        if order.state != 'draft':
            request.website.sale_reset()
            return {}
        product = request.env['product.template'].sudo().browse(int(product))
        product_id = product.product_variant_id.id
        order._cart_update(
            product_id=int(product_id),
            add_qty=1,
            set_qty=1,
            product_custom_attribute_values=None,
            no_variant_attribute_values=None
        )
        order.sudo().write({'car_id' : int(post.get('car_id', 0))})
        return request.redirect("/car/services")

    @http.route(['/car/service/process'],
        type='http',auth="public", website=True)
    def car_services_process(self, **kw):
        order = request.website.sale_get_order(force_create=1)
        if not order.order_line.filtered(lambda i: i.product_id.is_car_service):
            car_id = int(kw.get('car_id', 0))
            if car_id:
                request.session['car_id'] = car_id
    
            car_id = request.session['car_id']
    
            products = request.env['product.template'].sudo().search([
                ('is_car_service', '=', True),
                '|',
                ('vehical_ids', 'in', car_id),
                ('vehical_ids', '=', False)
            ])
            values = {
                'products': products,
                'car_id': car_id,
                'error_code': 1
            }
            return request.render("ki_car_services.template_car_services", values)
        slots = request.env['service.time.slot'].sudo().search([])
        values = {
            'slots': slots,
            'current_date': fields.Date.today()
        }
        return request.render(
            "ki_car_services.template_car_services_date_select", values
        )

    @http.route(['/car/services/process/cart'],
        type='http', auth="public", website=True)
    def car_services_process_cart(self, **kw):
        if not kw.get('service_schedule_date', False) or not kw.get('slot_select', False):
            slots = request.env['service.time.slot'].sudo().search([])
            values = {
                'slots': slots,
                'error_code': 1,
                'current_date': fields.Date.today()
            }
            values.update(kw)
            return request.render(
                "ki_car_services.template_car_services_date_select", values
            )

        if not kw.get('pickup_address', False) and kw.get('pickup', False):
            slots = request.env['service.time.slot'].sudo().search([])
            values = {
                'slots': slots,
                'error_code': 2,
                'current_date': fields.Date.today()
            }
            values.update(kw)
            return request.render(
                "ki_car_services.template_car_services_date_select", values
            )

        vals = {}

        if kw.get('pickup', False):
            vals.update({'is_pick_up': True})
        else:
            vals.update({'is_pick_up': False})

        service_schedule_date = kw.get('service_schedule_date', False)
        slot = kw.get('slot_select', 0)
        date_deadline = datetime.strptime(service_schedule_date, "%Y-%m-%d")
        date_start = datetime.combine(
            date_deadline, time(int(float(slot)), 00)
        )
        user_tz = request.env.user.tz or 'UTC'
        local_tz = pytz.timezone(user_tz)
        date_with_tz = local_tz.localize(date_start, is_dst=None)
        date_in_utc = date_with_tz.astimezone(pytz.utc)
        vals.update({
            'service_schedule_date': date_in_utc.strftime("%Y-%m-%d %H:%M:S")
        })
        if kw.get('car_number', False):
            vals.update({'car_number': kw.get('car_number', False)})
        if kw.get('note', False):
            vals.update({'note': kw['note']})
        if kw.get('pickup_address', False):
            vals.update({'pickup_address': kw['pickup_address']})

        order = request.website.sale_get_order(force_create=1)
        order.sudo().write(vals)
        return request.redirect('/shop/cart')

