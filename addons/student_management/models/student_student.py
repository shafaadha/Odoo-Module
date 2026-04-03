from odoo import models, fields, api
from odoo.exceptions import ValidationError

class StudentStudent(models.Model):
    _name = 'student.student'
    _description = 'Student Data'

    name = fields.Char(string="Name")
    age = fields.Integer()
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string="Gender")

    status = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed')
    ], default='draft')

    enrollment_ids = fields.One2many(
        "course.enrollment",
        "student_id",
        string="Enrollments"
    )   
    
    progress = fields.Float(compute="_compute_progress", store=True)

    total_course = fields.Integer(
        string='Total Courses',
        compute='_compute_total_course',
        store=True
    )
    

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('name'):
                vals['name'] = "Student Baru"
        return super().create(vals_list)

    @api.depends('enrollment_ids')
    def _compute_total_course(self):
        for rec in self:
            rec.total_course = len(rec.enrollment_ids)
            
    @api.depends('enrollment_ids.status')
    def _compute_progress(self):
        for rec in self:
            if not rec.enrollment_ids:
                rec.progress = 0
            else:
                done = len(rec.enrollment_ids.filtered(lambda x: x.status == 'done'))
                total = len(rec.enrollment_ids)
                rec.progress = (done / total) * 100

    @api.constrains('age')
    def _check_age(self):
        for rec in self:
            if not rec.age or rec.age < 18:
                raise ValidationError("Umur harus diatas 18 Tahun")
            
    @api.depends('status')
    def _compute_progress(self):
        for rec in self:
            if rec.status == 'draft':
                rec.progress = 0
            elif rec.status == 'ongoing':
                rec.progress = 50
            elif rec.status == 'done':
                rec.progress = 100
            
    def action_confirm_status(self):
        for rec in self:
            if not rec.age or rec.age < 18:
                raise ValidationError("Student harus berumur minimal 18 tahun untuk confirm status")
            rec.status = 'confirmed'
