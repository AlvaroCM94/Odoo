# -*- coding: utf-8 -*-

from odoo import models, fields, api

class libros_libros(models.Model):
    _name = 'libros.libros'
    _description = 'libros.libros'

    name = fields.Char(string="Título")
    autor = fields.Many2one("libros.autores",string="Autor",required=True,ondelete="cascade")
    stock = fields.Integer(string="Stock")
    genero = fields.Char(string="Género")
    editorial = fields.Many2one("res.partner",string="Editorial",required=True,ondelete="cascade")

class libros_autores(models.Model):
    _name = 'libros.autores'
    _description = 'libros.autores'

    name = fields.Char(string="Nombre")
    edad = fields.Integer(string="Edad")
    imagen = fields.Binary(string="Imagen")
    libros = fields.One2many("libros.libros","autor",string="Libros")
    

class libros_clientes(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    libros = fields.One2many("libros.libros","editorial",string="Editorial")