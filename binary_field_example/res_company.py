# -*- coding: utf-8 -*-
###############################################################################
#
#   Module for OpenERP
#   Copyright (C) 2013 Akretion (http://www.akretion.com).
#   @author Sébastien BEAU <sebastien.beau@akretion.com>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from openerp import models, fields


class ResCompany(models.Model):
    _inherit = 'res.company'

    binary_test = fields.BinaryField('Test Binary')
    binary_test_ori = fields.Binary('Test Binary Ori')
#    image_test = fields.ImageField('Test Image')
#    image_test_resize = fields.ImageField(
#            'Test Image small',
#            resize_based_on='image_test',
#            height=64,
#            width=64,
#            )


