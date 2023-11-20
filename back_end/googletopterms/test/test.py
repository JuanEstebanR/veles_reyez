"""
    This file contains the tests for the API
"""
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from googletopterms.models import queries, comment
from django.contrib.auth.models import User


class UserTests(APITestCase):

    def setUp(self):
        """
        Create a user for the tests
        """
        url = reverse('register')
        data = {'username': 'JulianGomez',
                'password': 'secretPassword'}
        self.client.post(url, data, format='json')

    def test_create_user(self):
        """
        Ensure we can create a new user object
        """
        url = reverse('register')
        data = {'username': 'johndoe',
                'password': 'secretPassword'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username='johndoe').exists())
        """
            Ensure we can't create a new user object with
            existing username
        """
        data = {'username': 'JulianGomez',
                'password': 'secretPassword'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['username'][0],
                         'A user with that username already exists.')

    def test_login_user(self):
        """
        Ensure we can log in with a valid user
        """
        url = reverse('login')
        data = {
            'username': 'JulianGomez',
            'password': 'secretPassword'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user'], 'JulianGomez')
        """
        Ensure we cannot login with a non-existing user
        """
        url = reverse('login')
        data = {
            'username': 'johndoe',
            'password': 'secretPassword'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['message'], 'invalid Credentials')


class QueryTest(APITestCase):
    def setUp(self):
        """
        Create a user for the tests
        """
        url = reverse('register')
        data = {'username': 'JulianGomez',
                'password': 'secretPassword'}
        self.client.post(url, data, format='json')

    def test_create_query(self):
        """
        Ensure we can create a new query object
        """
        data = {
            'name': 'query1',
            'description': 'query description',
            'rawQuery': 'SELECT id, name FROM table_name',
            'relatedTo': 'table_name',
            'public': True,
            'comments': []
        }
        url = reverse('query_create', kwargs={
            'username': 'JulianGomez'})
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(queries.objects.filter(name='query1').exists())
        self.assertEqual(response.data['name'], 'query1')
        self.assertEqual(response.data['username'], 'JulianGomez')

    def test_get_queries_community(self):
        """
        Ensure we can't get a list of queries if database is empty
        """
        url = reverse('community_queries')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

        data_public = {
            'name': 'query1',
            'description': 'query description',
            'rawQuery': 'SELECT id, name FROM table_name',
            'relatedTo': 'table_name',
            'public': True,
            'comments': []
        }
        url = reverse('query_create', kwargs={'username': 'JulianGomez'})
        self.client.post(url, data_public, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data_private = {
            'name': 'query2',
            'description': 'query description2',
            'rawQuery': 'SELECT id, name FROM table_name',
            'relatedTo': 'table_name',
            'public': False,
            'comments': []
        }
        self.client.post(url, data_private, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        url = reverse('community_queries')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'query1')

        data_public_2 = {
            'name': 'query3',
            'description': 'query description3',
            'rawQuery': 'SELECT id, name FROM table_name',
            'relatedTo': 'table_name',
            'public': True,
            'comments': []
        }
        url = reverse('query_create', kwargs={'username': 'JulianGomez'})
        self.client.post(url, data_public_2, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        url = reverse('community_queries')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], 'query3')


class CommentsTest(APITestCase):
    def setUp(self):
        """
        Create a user for the tests
        """
        url = reverse('register')
        data = {'username': 'JulianGomez',
                'password': 'secretPassword'}
        self.client.post(url, data, format='json')
        query_data = {
            'name': 'query1',
            'description': 'query description',
            'rawQuery': 'SELECT id, name FROM table_name',
            'relatedTo': 'table_name',
            'public': True,
            'comments': []
        }
        url = reverse('query_create', kwargs={
            'username': 'JulianGomez'})
        self.client.post(url, query_data, format='json')

    def test_create_comment(self):
        """
        Ensure we can create a new comment object
        """
        comment_data = {
            'comment': 'This is a comment',
            'user': 'JulianGomez'
        }
        url = reverse('query_comment', kwargs={'pk': 1})
        response = self.client.post(url, comment_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(comment.objects.filter(query_id=1).exists())

        url = reverse('my_queries', kwargs={'username': 'JulianGomez'})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data[0]['comments']), 1)
        self.assertEqual(response.data[0]['comments'][0]['comment'],
                         'This is a comment')


class GoogleApiTest(APITestCase):

    def test_top_25_terms_and_rising(self):
        """
            Ensure we can get the top 25 terms
        """
        url = reverse('top_25_terms')
        data = {'interval': 2, 'table_name': 'top_terms'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 25)

        data = {'interval':3, 'table_name': 'top_rising_terms'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['term'], "duane martin")

    def test_top_25_international_terms(self):
        """
            Ensure we can get the top 25 international terms
        """
        url = reverse('International_top_terms')
        data = {'interval': 2, 'table_name': 'international_top_terms',
                'country_name': 'Colombia'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 25)

