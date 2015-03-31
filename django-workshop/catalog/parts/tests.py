from __future__ import absolute_import

from django.test import TestCase
from django.core.urlresolvers import reverse

from . import models


# Create your tests here.

class PartsTest(TestCase):
    def setUp(self):
        # best practice: use fixtures to generate data
        part = models.CarParts()
        part.name = 'shifter'
        part.slug = 'part_1'
        part.year = 1666
        part.save()

    def test_create_part(self):
        data = {
            'name': 'door',
            'slug': 'part_2',
            'year': 1996
        }

        url = reverse('index')
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

        part = models.CarParts.objects.get(slug='part_2')
        self.assertEqual(part.year, 1996)

    def test_index_page(self):
        url = reverse('index')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn('parts index', response.content)

    def test_future_year(self):
        url = reverse('by_year', kwargs={'year': 2020})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)

    def test_past_year(self):
        url = reverse('by_year', kwargs={'year': 1666})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn('1666', response.content)
