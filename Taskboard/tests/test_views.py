from django.test import TestCase, Client
from django.urls import reverse
from Taskboard.models import list_task


class TestViews(TestCase):
    def setup(self):
        self.client = Client()
        self.obj = list_task.objects.create(
            name='task1',
            date='2019-14-21',
            text='Take Rexie to get vaccinated')

    def test_all_task_GET(self):
        response = self.client.get(reverse('Taskboard:all_task'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Taskboard/all_task.html')

    def test_task_detail_GET(self):
        obj = list_task.objects.create(
            date='2021-11-10',
            name='name'
        )
        response = self.client.get(reverse('Taskboard:task_detail', args=[obj.pk]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Taskboard/task_detail.html')
        self.assertTemplateUsed(response, 'adopter/Base.html')

    def test_createTask_GET(self):
        response = self.client.get(reverse('Taskboard:createTask'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Taskboard/createTask.html')

    def test_createTask_POST_Valid(self):
        task = list_task.objects.count()
        response = self.client.post(reverse('Taskboard:createTask'), {'date': '2021-11-10',
                                                                      'name': 'name',
                                                                      'text': 'description',
                                                                      'status': 'True'})

        self.assertEqual(response.status_code, 302)  # means redirection works
        self.assertEqual(list_task.objects.count(), task + 1)  # object created so expected true

    def test_createTask_POST_Not_Valid(self):
        response = self.client.post(reverse('Taskboard:createTask'), {'date': '2021-11-10',
                                                                      'name': '',  # fail here
                                                                      'text': '',
                                                                      'status': 'True'})



        self.assertEqual(response.status_code, 200)  # means bad form so we render
