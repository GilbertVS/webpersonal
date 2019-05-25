from django.contrib import admin
from .models import Project
from .models import Curssos
from .models import Inscripcions

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
# Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(Curssos)
admin.site.register(Inscripcions)
