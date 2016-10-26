# -*- encoding: utf-8 -*-
###############################################################################
#                                                                             #
# Copyright (C) 2015 Trustcode - www.trustcode.com.br                         #
#                                                                             #
# This program is free software: you can redistribute it and/or modify        #
# it under the terms of the GNU Affero General Public License as published by #
# the Free Software Foundation, either version 3 of the License, or           #
# (at your option) any later version.                                         #
#                                                                             #
# This program is distributed in the hope that it will be useful,             #
# but WITHOUT ANY WARRANTY; without even the implied warranty of              #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
# GNU General Public License for more details.                                #
#                                                                             #
# You should have received a copy of the GNU General Public License           #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.       #
###############################################################################

{
    'name': 'Base Module - HGSOFT',
    'summary': """Base Module for HGSOFT""",
    'version': '8.0.1.0.0',
    'category': 'Tools',
    'author': 'HGSOFT',
    'license': 'AGPL-3',
    'website': 'http://www.hgsoft.com.br',
    'contributors': ['Alexsandro Haag <alex@hgsoft.com.br>'],
    'depends': [
        'base', 'web'
    ],
    'data': [
        'views/module_view.xml',
        'views/hgsoft_base.xml',
        'data/base_data.xml',
        'views/res_partner_view.xml'
    ],
    'application': True,
    'auto_install': True
}
