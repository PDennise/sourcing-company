# Sourcing Consultant

B2B website for a Turkey-based sourcing consultancy connecting international buyers with manufacturers of LED panels and construction materials.

## Stack

- Python / Django
- HTML, CSS, JavaScript
- Bootstrap 5

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

Contact, consultation, and RFP forms save to the `Inquiry` model. Review them in Django admin after creating a superuser:

```bash
python manage.py createsuperuser
```
