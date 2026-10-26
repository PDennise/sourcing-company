from django.db import models


class Inquiry(models.Model):
    class Kind(models.TextChoices):
        CONTACT = "contact", "General contact"
        CONSULTATION = "consultation", "Schedule a consultation"
        RFP = "rfp", "Submit an RFP"

    kind = models.CharField(max_length=20, choices=Kind.choices)
    name = models.CharField(max_length=120)
    company = models.CharField(max_length=160, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=40, blank=True)
    country = models.CharField(max_length=80, blank=True)
    industry = models.CharField(max_length=80, blank=True)
    product_interest = models.CharField(max_length=160, blank=True)
    volume = models.CharField(max_length=80, blank=True)
    preferred_date = models.DateField(null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.get_kind_display()} — {self.name} ({self.email})"
