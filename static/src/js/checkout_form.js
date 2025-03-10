/** @odoo-module **/

odoo.define('custom_checkout', function (require) {
    "use strict";

    var publicWidget = require('web.public.widget');

    publicWidget.registry.CustomCheckout = publicWidget.Widget.extend({
        selector: '#custom_checkout',

        events: {
            'change #tipo_documento': '_onTipoDocumentoChange',
        },

        start: function () {
            this._super.apply(this, arguments);
            this._toggleFields();
        },

        _onTipoDocumentoChange: function () {
            this._toggleFields();
        },

        _toggleFields: function () {
            let tipoDocumento = this.$('#tipo_documento').val();

            if (tipoDocumento === 'boleta') {
                this.$('#boleta_fields').show();
                this.$('#factura_fields').hide();
            } else {
                this.$('#boleta_fields').hide();
                this.$('#factura_fields').show();
            }
        }
    });

    return publicWidget.registry.CustomCheckout;
});
