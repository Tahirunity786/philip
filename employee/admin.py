from django.contrib import admin
from employee.models import *


# class CustomUserAdmin(admin.ModelAdmin):
#     model=CustomUser

# admin.site.register(CustomUser, CustomUserAdmin)

# Register your models here.
admin.site.register(hr_mas_dept)
admin.site.register(hr_mas_grade)
admin.site.register(hr_mas_subdept)
admin.site.register(hr_mas_desig)
admin.site.register(hr_mas_cadre)
admin.site.register(hr_mas_section)
admin.site.register(hr_mas_subsection)
admin.site.register(hr_mas_division)
admin.site.register(hr_mas_costcentre)
admin.site.register(hr_mas_company)
admin.site.register(hr_emps)
admin.site.register(HrAttendata)
admin.site.register(HrUserlogs)
admin.site.register(Pbcatcol)
admin.site.register(Pbcatedt)
admin.site.register(Pbcatfmt)
admin.site.register(Pbcattbl)
admin.site.register(Pbcatvld)
admin.site.register(announcments)
# admin.site.register(hr_mas_cadre)
admin.site.register(hr_mas_org)
admin.site.register(hr_mas_loc)
admin.site.register(HrEmpsInfo)
