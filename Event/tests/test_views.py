from django.urls import reverse
from django.test import TestCase, Client
from Event.models import event


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.obj = event.objects.create(name='event number 1',
                                        date='2021-11-24',
                                        text='welcome to my event',
                                        image='default.png')

    def test_all_events_GET(self):
        response = self.client.get(reverse('Event:all_events'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Event/all_events.html')

    def test_Event_detail_GET(self):
        response = self.client.get(reverse('Event:Event_detail', args=[self.obj.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Event/event_detail.html')

    def test_create_event_GET(self):
        response = self.client.get(reverse('Event:createEvent'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Event/createEvent.html')

    def test_create_event_POST_Valid(self):
        event_count = event.objects.count()
        response = self.client.post(reverse('Event:createEvent'), {'name': 'event number 1',
                                                                   'date': '2021-11-24',
                                                                   'text': 'welcome to my event',
                                                                   'image': 'photo.png'})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(event.objects.count(), event_count + 1)

    def test_create_event_POST_Not_Valid(self):
        response = self.client.post(reverse('Event:createEvent'),
                                    {'name': 'event number 1',
                                     'date': '2021-11-24',
                                     'text': 'welcome to my event',
                                     'image': 'photo.png'})
        self.assertEqual(response.status_code, 302)

    def test_delete_event_GET(self):
        response = self.client.get(reverse('Event:deleteEvent', args=[self.obj.pk]))
        self.assertEqual(response.status_code, 302)

    def test_delete_event_POST(self):
        event_count = event.objects.count()
        response = self.client.get(reverse('Event:deleteEvent', args=[self.obj.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(event.objects.count(), event_count - 1)

