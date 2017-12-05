# -*- coding: utf-8 -*-
# Copyright (C) 2015 Matmoz d.o.o. (<http://www.matmoz.si>).
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openerp import api, models, fields


class ProjectTask (models.Model):
    _name = 'project.task'
    _inherit = 'project.task'

    change_id = fields.Many2one(
        comodel_name='change.management.change',
        string='Request',
        readonly=False,
        help="Task is an action on a change identified by this label."
    )


class ProjectProject (models.Model):
    _name = 'project.project'
    _inherit = 'project.project'

    change_ids = fields.One2many(
        comodel_name='change.management.change',
        inverse_name='project_id',
        string='Project changes'
    )

    change_count = fields.Integer(
        compute='_compute_change_count', type='integer'
    )

    @api.depends('change_ids')
    def _compute_change_count(self):
        for record in self:
            record.change_count = len(record.change_ids)
