odoo.define('custom_checkout.checkout_form', function (require) {
    "use strict";

    var publicWidget = require('web.public.widget');

    publicWidget.registry.CheckoutForm = publicWidget.Widget.extend({
        selector: '#custom_checkout',
        events: {
            'change #tipo_documento': '_onChangeTipoDocumento',
            'change #tipo_entrega': '_onChangeTipoEntrega',
        },

        _onChangeTipoDocumento: function (ev) {
            var tipo = $(ev.currentTarget).val();
            if (tipo === "boleta") {
                $("#boleta_fields").show();
                $("#factura_fields").hide();
            } else {
                $("#boleta_fields").hide();
                $("#factura_fields").show();
            }
        },

        _onChangeTipoEntrega: function (ev) {
            var tipo = $(ev.currentTarget).val();
            if (tipo === "domicilio") {
                $("#domicilio_fields").show();
                $("#sucursal_fields").hide();
            } else {
                $("#domicilio_fields").hide();
                $("#sucursal_fields").show();
            }
        }
    });
});
