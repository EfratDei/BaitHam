from django.test import SimpleTestCase
from django.urls import reverse, resolve
from Donations.views import donates_form, Thankyou, export_pdf, export_excel


class TestUrls(SimpleTestCase):

    def test_donates_form_url_is_resolved(self):
        url = reverse('Donations:new')
        self.assertEquals(resolve(url).func, donates_form)

    def test_Thankyou_url_is_resolved(self):
        url = reverse('Donations:Thankyou')
        self.assertEquals(resolve(url).func, Thankyou)

    def test_export_pdf_url_is_resolved(self):
        url = reverse('Donations:export_pdf')
        self.assertEquals(resolve(url).func, export_pdf)

    def test_export_excel_url_is_resolved(self):
        url = reverse('Donations:export_excel')
        self.assertEquals(resolve(url).func, export_excel)
