# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 FactorLibre (http://www.factorlibre.com)
#                  Hugo Santos <hugo.santos@factorlibre.com>
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
from openerp import models, fields


class DHLCountryService(models.Model):
    _name = 'dhl.country.service'

    country_id = fields.Many2one('res.country', 'Country', required=True)
    service_name = fields.Char('Service Name', required=True)
    service_code = fields.Char('Service Code')
    service_number = fields.Char('Service Code No.', required=True)


class DHLZipcodeFacility(models.Model):
    _name = 'dhl.zipcode.facility'

    zipcode = fields.Char('Zipcode', required=True, select=True)
    facility_name = fields.Char('Facility Name', required=True)
    facility_code = fields.Char('Facility Code', required=True)
