from django import forms

from .models import Inquiry


FIELD_SETS = {
    Inquiry.Kind.CONTACT: ["name", "company", "email", "phone", "country", "message"],
    Inquiry.Kind.CONSULTATION: [
        "name",
        "company",
        "email",
        "phone",
        "country",
        "preferred_date",
        "message",
    ],
    Inquiry.Kind.RFP: [
        "name",
        "company",
        "email",
        "phone",
        "country",
        "industry",
        "product_interest",
        "volume",
        "message",
    ],
}

REQUIRED_BY_KIND = {
    Inquiry.Kind.CONTACT: {"name", "email", "message"},
    Inquiry.Kind.CONSULTATION: {"name", "company", "email", "preferred_date", "message"},
    Inquiry.Kind.RFP: {"name", "email", "industry", "product_interest", "volume", "message"},
}


class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = [
            "name",
            "company",
            "email",
            "phone",
            "country",
            "industry",
            "product_interest",
            "volume",
            "preferred_date",
            "message",
        ]
        widgets = {
            "preferred_date": forms.DateInput(attrs={"type": "date"}),
            "message": forms.Textarea(attrs={"rows": 5}),
        }

    def __init__(self, *args, kind=Inquiry.Kind.CONTACT, extra_fields=None, **kwargs):
        super().__init__(*args, **kwargs)
        keep = FIELD_SETS.get(kind, FIELD_SETS[Inquiry.Kind.CONTACT])
        required = REQUIRED_BY_KIND.get(kind, REQUIRED_BY_KIND[Inquiry.Kind.CONTACT])

        for name in list(self.fields):
            if name not in keep:
                self.fields.pop(name)

        if kind == Inquiry.Kind.RFP and "industry" in self.fields:
            self.fields["industry"].widget = forms.Select(
                choices=[
                    ("", "Select an industry"),
                    ("led", "LED panels & lighting"),
                    ("construction", "Construction products"),
                    ("custom", "Custom sourcing"),
                ]
            )

        for name, field in self.fields.items():
            field.required = name in required
            css = "form-select" if isinstance(field.widget, forms.Select) else "form-control"
            field.widget.attrs["class"] = css
            field.widget.attrs.setdefault("placeholder", field.label)
