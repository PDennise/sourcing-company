from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import InquiryForm
from .models import Inquiry


def _save_inquiry(request, kind, extra_fields, template_name, page_title, intro):
    form = InquiryForm(
        request.POST or None,
        kind=kind,
        extra_fields=extra_fields,
    )
    if request.method == "POST" and form.is_valid():
        inquiry = form.save(commit=False)
        inquiry.kind = kind
        inquiry.save()
        send_mail(
            subject=f"New {inquiry.get_kind_display()} from {inquiry.name}",
            message=(
                f"Name: {inquiry.name}\n"
                f"Company: {inquiry.company}\n"
                f"Email: {inquiry.email}\n"
                f"Phone: {inquiry.phone}\n"
                f"Country: {inquiry.country}\n"
                f"Industry: {inquiry.industry}\n"
                f"Product: {inquiry.product_interest}\n"
                f"Volume: {inquiry.volume}\n"
                f"Preferred date: {inquiry.preferred_date}\n\n"
                f"{inquiry.message}"
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.INQUIRY_NOTIFY_EMAIL],
            fail_silently=True,
        )
        return redirect(f"{reverse('thank_you')}?kind={kind}")
    return render(
        request,
        template_name,
        {
            "form": form,
            "page_title": page_title,
            "intro": intro,
        },
    )


def home(request):
    return render(request, "website/home.html")


def services(request):
    return render(request, "website/services.html")


def industries(request):
    return render(request, "website/industries.html")


def about(request):
    return render(request, "website/about.html")


def contact(request):
    return _save_inquiry(
        request,
        Inquiry.Kind.CONTACT,
        extra_fields=["company", "phone", "country"],
        template_name="website/contact.html",
        page_title="Get in Touch",
        intro="Tell us what you need from Turkey. We typically reply within one business day.",
    )


def consultation(request):
    return _save_inquiry(
        request,
        Inquiry.Kind.CONSULTATION,
        extra_fields=["company", "phone", "country", "preferred_date"],
        template_name="website/form_page.html",
        page_title="Schedule a Consultation",
        intro="Book a short call with our team to review specs, target markets, and factory options.",
    )


def rfp(request):
    return _save_inquiry(
        request,
        Inquiry.Kind.RFP,
        extra_fields=["company", "phone", "country", "industry", "product_interest", "volume"],
        template_name="website/form_page.html",
        page_title="Submit an RFP",
        intro="Share volumes, specs, and destination so we can match you with vetted Turkish manufacturers.",
    )


def thank_you(request):
    kind = request.GET.get("kind", "contact")
    return render(request, "website/thank_you.html", {"kind": kind})


def privacy(request):
    return render(request, "website/legal.html", {"page_title": "Privacy Policy"})


def terms(request):
    return render(request, "website/legal.html", {"page_title": "Terms of Service"})
