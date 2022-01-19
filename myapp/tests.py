from django.test import TestCase
from django.urls import reverse
from myapp import views

# class ViewsTestCase(TestCase):
#     def test_index_loads_properly(self):
#         """The index page loads properly"""
#         response = self.client.get('localhost:8000')
#         self.assertEqual(response.status_code, 200)

class HomePageTests(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, '<h1>Homepage</h1>')

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')


# git checkout -b new-ci-workflow
# git push origin new-ci-workflow
# https://www.atlassian.com/git/tutorials/making-a-pull-request
# https://learndjango.com/tutorials/django-testing-tutorial
# new branch
# git checkout -b new-ci-workflow
# git push origin new-ci-workflow
# git push --set-upstream origin new-ci-workflow
# git branch --set-upstream-to=origin/<branch> new-ci-workflow