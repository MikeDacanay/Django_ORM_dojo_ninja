# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Books(models.Model):
	name = models.CharField(max_length=255)
	desc = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True) 
	updated_at = models.DateTimeField(auto_now = True) 

class Authors(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	book = models.ManyToManyField(Books, related_name="authors")
	email = models.CharField(max_length=255)
	notes = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)