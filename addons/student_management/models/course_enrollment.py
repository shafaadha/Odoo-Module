from odoo import models, fields, api
from odoo.exceptions import ValidationError

class CourseEnrollment(models.Model):
    _name = "course.enrollment"
    _description = "Course Enrollment"

    student_id = fields.Many2one('student.student', required=True)
    course_id = fields.Many2one('course.course', required=True)

    status = fields.Selection([
        ('draft', 'Draft'),
        ('ongoing', 'Ongoing'),
        ('done', 'Done')
    ], default='draft')

    progress = fields.Float(
        compute="_compute_progress",
        store=True
    )
    
    @api.depends('status')
    def _compute_progress(self):
        for rec in self:
            if rec.status == 'draft':
                rec.progress = 0
            elif rec.status == 'ongoing':
                rec.progress = 50
            elif rec.status == 'done':
                rec.progress = 100
    
    @api.constrains('student_id', 'course_id')
    def _check_duplicate_enrollment(self):
        for rec in self:
            domain = [
                ('student_id', '=', rec.student_id.id),
                ('course_id', '=', rec.course_id.id),
                ('id', '!=', rec.id)
            ]
            if self.search_count(domain):
                raise ValidationError("Student sudah terdaftar di course ini!")
            
            
            
    def action_start(self):
        self.status = 'ongoing'

    def action_finish(self):
        self.status = 'done'