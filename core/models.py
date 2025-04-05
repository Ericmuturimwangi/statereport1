from django.db import models
from django.contrib.auth.models import User

class HQ(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__ (self):
        return self.user.username
    
class Brigade(models.Model):
    name = models.CharField(max_length=100)
    hq = models.ForeignKey(HQ, on_delete=models.CASCADE)
    account = models.OneToOneField(User, on_delete=models.CASCADE)

    def __Str__(self):
        return self.name
    
class Unit(models.Model):
    name = models.CharField(max_length=100)
    brigade = models.ForeignKey(Brigade, on_delete=models.CASCADE)

    def __Str__(self):
        return self.name
    
class PDFSubmission(models.Model):

    class SubmissionStatus(models.TextChoices):
        PENDING= 'PENDING', 'Pending'
        IN_BRIGADE ='IN_BRIGADE', 'In Brigade'
        IN_HQ = 'IN_HQ', 'In HQ'
        COMPLETED ='COMPLETED', 'Completed'


    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    date = models.DateField()
    file = models.FileField(upload_to='unit_pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=SubmissionStatus.choices,
        default = SubmissionStatus.PENDING,
    )

    def __str__(self):
        return f"Submission by {self.unit.name} on {self.date}"
    
class BrigadeReport(models.Model):
    brigade = models.ForeignKey(Brigade, on_delete=models.CASCADE)
    date = models.DateField()
    compiled_file = models.FileField(upload_to='brigade_reports/')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report for {self.brigade.name} on {self.date}"

