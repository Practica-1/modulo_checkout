from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = "sale.order"

    invoice_type = fields.Selection([
        ('boleta', 'Boleta'),
        ('factura', 'Factura'),
    ], string="Tipo de Factura")

    full_name = fields.Char(string="Nombre y Apellidos")
    rut = fields.Char(string="RUT")
    email = fields.Char(string="Correo Electrónico")
    phone = fields.Char(string="Teléfono")
    delivery_method = fields.Selection([
        ('domicilio', 'Domicilio'),
        ('sucursal', 'Retiro en Sucursal'),
    ], string="Método de Entrega")
    region_envio = fields.Char(string="Región de Envío")
    direccion = fields.Char(string="Dirección de Envío")
    recibe_nombre = fields.Char(string="Nombre del Receptor")
    recibe_telefono = fields.Char(string="Teléfono del Receptor")
    notas = fields.Text(string="Notas del Pedido")
