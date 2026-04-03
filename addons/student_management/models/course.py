from odoo import models,fields

class Course(models.Model):
    _name = "course.course"
    _description = "Course"
    
    name = fields.Char(required=True)
    description = fields.Text()
    
    enrollment_ids = fields.One2many("course.enrollment", "course_id")