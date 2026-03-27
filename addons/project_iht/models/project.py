from odoo import models, fields

class ProjectProject(models.Model):
    _inherit = 'project.project'

    lokasi_proyek = fields.Text(string="Lokasi Proyek")
    source_aplikasi_pendukung = fields.Char(string="Source Aplikasi Pendukung")
    daftar_perkerja_remote = fields.Json(string="Daftar Pekerja Remote")