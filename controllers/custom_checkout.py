from odoo import http
from odoo.http import request

class CustomCheckout(http.Controller):

    @http.route(['/shop/checkout'], type='http', auth="public", website=True)
    def checkout(self, **kwargs):
        order = request.website.sale_get_order()
        if order:
            order.sudo().write({
                'invoice_type': kwargs.get('invoice_type'),
                'full_name': kwargs.get('full_name'),
                'rut': kwargs.get('rut'),
                'email': kwargs.get('email'),
                'phone': kwargs.get('phone'),
                'delivery_method': kwargs.get('delivery_method'),
                'region_envio': kwargs.get('region_envio'),
                'direccion': kwargs.get('direccion'),
                'recibe_nombre': kwargs.get('recibe_nombre'),
                'recibe_telefono': kwargs.get('recibe_telefono'),
                'notas': kwargs.get('notas'),
            })
        return request.redirect('/shop/payment')
