from odoo import models, fields

class libraryBooks(models.Model):
    _name = 'library.book'
    name = fields.Char('Title', required=True)
    date_release = fields.Date('Realease Date')
    author_ids = fields.Many2many(
        'res.partner',
        string='Authors'
    )
