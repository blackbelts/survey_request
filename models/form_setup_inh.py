# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, _


class Job1(models.Model):
    _inherit = "form.setup"

    # survey_id = fields.Many2one(
    #     'survey.survey', "Request Form",)
    #
    #
    # def action_print_survey(self):
    #     return self.survey_id.action_print_survey()
    #
    # def action_new_survey(self):
    #     self.ensure_one()
    #     survey = self.env['survey.survey'].create({
    #         'title': _("Request Form : %s") % self.name,
    #     })
    #     self.write({'survey_id': survey.id})
    #
    #     action = {
    #             'name': _('Survey'),
    #             'view_mode': 'form,tree',
    #             'res_model': 'survey.survey',
    #             'type': 'ir.actions.act_window',
    #             'context': {'form_view_initial_mode': 'edit'},
    #             'res_id': survey.id,
    #         }
    #
    #     return action
