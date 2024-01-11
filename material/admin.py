from django.contrib import admin
from material.models import Material, MaterialAmpliado, MaterialBraille

# Register your models here.

class MaterialAdmin(admin.ModelAdmin):
    pass

class MaterialAmpliadoAdmin(admin.ModelAdmin):
    pass

class MaterialBrailleAdmin(admin.ModelAdmin):
    pass

admin.site.register(MaterialBraille, MaterialBrailleAdmin)
admin.site.register(MaterialAmpliado, MaterialAmpliadoAdmin)
admin.site.register(Material, MaterialAdmin)


