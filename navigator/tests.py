from django.test import TestCase

class NavigatorTest(TestCase):

    def test_use_correct_template(self):
        response = self.client.get('/navigator/')
        self.assertTemplateUsed(response, 'navigator.html')

    def test_passes_list_with_5_items_when_search_term_is_provided(self):
        response = self.client.get('/navigator/?search_term=arrow')
        self.assertEqual(type(response.context['repositories']), list)
        self.assertEqual(len(response.context['repositories']), 5)

    def test_passes_no_list_when_search_term_is_not_provided(self):
        response = self.client.get('/navigator/')
        self.assertEqual(response.context['repositories'], None)

