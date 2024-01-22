from django.test import SimpleTestCase
from django.urls import reverse, resolve
from Taskboard.views import all_task, task_detail, createTask, export_pdf, export_excel, assignTask, doneTask


class TestUrls(SimpleTestCase):

    def test_all_task_url_is_resolved(self):
        url = reverse('Taskboard:all_task')
        self.assertEquals(resolve(url).func, all_task)

    def test_task_detail_url_is_resolved(self):
        url = reverse('Taskboard:task_detail', args=[2])
        self.assertEquals(resolve(url).func, task_detail)

    def test_createTask_url_is_resolved(self):
        url = reverse('Taskboard:createTask')
        self.assertEquals(resolve(url).func, createTask)

    def test_export_pdf_url_is_resolved(self):
        url = reverse('Taskboard:export_pdf')
        self.assertEquals(resolve(url).func, export_pdf)

    def test_export_excel_url_is_resolved(self):
        url = reverse('Taskboard:export_excel')
        self.assertEquals(resolve(url).func, export_excel)

    def test_assignTask_url_is_resolved(self):
        url = reverse('Taskboard:assignTask', args=[2])
        self.assertEquals(resolve(url).func, assignTask)

    def test_doneTask_url_is_resolved(self):
        url = reverse('Taskboard:doneTask', args=[2])
        self.assertEquals(resolve(url).func, doneTask)
