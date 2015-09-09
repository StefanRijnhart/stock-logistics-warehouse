# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Josse Colpaert
#    Copyright 2015 Odoo SA
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Stock Forecast Report',
    'version': '1.0',
    'author': 'Odoo SA,Odoo Community Association (OCA)',
    'category': 'Warehouse',
    'license': 'AGPL-3',
    'website': 'https://github.com/OCA/stock-logistics-warehouse',
    'depends': ['stock'],
    'data': [
        'report/report_stock_forecast.xml',
        'security/ir.model.access.csv',
    ],
}
