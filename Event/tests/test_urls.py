import unittest
from django.urls import reverse, resolve

from Event.views import all_events, createEvent, deleteEvent, Event_detail


class TestUrls(unittest.TestCase):
    def test_all_events_url_is_resolved(self):
        url = reverse('Event:all_events')
        self.assertEqual(resolve(url).func, all_events)

    def test_createEvent_url_is_resolved(self):
        url = reverse('Event:createEvent')
        self.assertEqual(resolve(url).func, createEvent)

    def test_deleteEvent_url_is_resolved(self):
        url = reverse('Event:deleteEvent', args=[2])
        self.assertEqual(resolve(url).func, deleteEvent)

    def test_Event_detail_url_is_resolved(self):
        url = reverse('Event:Event_detail',args=[2])
        self.assertEqual(resolve(url).func, Event_detail)
