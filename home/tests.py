from django.test import TestCase

class TestDisplayViews(TestCase):

    def test_display_all_view(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")

    def test_display_all_view(self):
        page = self.client.get("/about")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "about.html")

    def test_display_all_view(self):
        page = self.client.get("/contact")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "contact.html")

    def test_display_all_view(self):
        page = self.client.get("/FAQ")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "faq.html")

    def test_display_all_view(self):
        page = self.client.get("/how-to")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "how-to.html")

    def test_display_all_view(self):
        page = self.client.get("/shipping")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "shipping.html")
