from django.contrib import admin
from .models import HQ, Brigade, Unit, PDFSubmission, BrigadeReport


admin.site.register(HQ)
admin.site.register(Brigade)
admin.site.register(Unit)
admin.site.register(PDFSubmission)
admin.site.register(BrigadeReport)

# Register your models here.
