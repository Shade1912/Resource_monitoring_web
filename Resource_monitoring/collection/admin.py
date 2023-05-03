from django.contrib import admin
from baseapp.models import alerts,session_data, group_privileges, user_extra_details,userlogs,drug_template,device, probe

# Register your models here.
admin.site.register(alerts)
admin.site.register(session_data)
admin.site.register(group_privileges)
admin.site.register(user_extra_details)
admin.site.register(userlogs)
admin.site.register(drug_template)
admin.site.register(device)
admin.site.register(probe)