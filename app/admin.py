from django.contrib import admin
from app.models import EMP
from app.models import Department
from app.models import Country
from app.models import Capital
# Register your models here.
admin.site.register(Department)
admin.site.register(EMP)
admin.site.register(Country)
admin.site.register(Capital)
