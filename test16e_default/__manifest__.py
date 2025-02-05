##############################################################################
#
#    Copyright (C) 2023  jeo Software  (http://www.jeosoft.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your optiogitn) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#   le agregamos esto
##############################################################################

{
    "name": "test16e",
    "version": "16.0.1.0.0",
    "category": "Tools",
    "summary": "Test for v16 EE",
    "author": "jeo Software",
    "website": "http://github.com/jobiols/cl-test",
    "license": "AGPL-3",
    "depends": [],
    "installable": True,
    # manifest version, if omitted it is backward compatible
    "env-ver": "2",
    # if Enterprise it installs in a different directory than community
    "odoo-license": "EE",
    # Config to write in odoo.conf
    "config_local": [
        "workers = 0",
        "admin_password = admin",
    ],
    "port": "8069",
    "git-repos": [
        "https://github.com/jobiols/cl-test.git -b 16.0e",

        "https://github.com/ingadhoc/account-financial-tools.git adhoc-account-financial-tools",
        "https://github.com/ingadhoc/account-payment.git adhoc-account-payment",
        "https://github.com/ingadhoc/odoo-argentina.git adhoc-odoo-argentina",
        "https://github.com/ingadhoc/argentina-sale.git adhoc-argentina-sale",
        "https://github.com/ingadhoc/account-invoicing.git adhoc-account-invoicing",
        "https://github.com/ingadhoc/odoo-argentina-ee.git adhoc-odoo-argentina-ee",
        "https://github.com/ingadhoc/stock.git adhoc-stock",
        "https://github.com/ingadhoc/aeroo_reports.git adhoc-aeroo_reports",
        "https://github.com/ingadhoc/sale.git adhoc-sale",

    ],
    # list of images to use in the form 'name image-url'
    "docker-images": [
        "odoo jobiols/odoo-ent:16.0e",
        "postgres postgres:14.13-alpine",
    ],
}
