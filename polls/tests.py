from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
import datetime
from .models import Question

def create_question(question_text, days):
	time=timzone.now()+datetime.timedelta(days=days)
	return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionIndexViewTests(TestCase):
	response=self.client.get(reverse('polls:index'))
	self.assertEqual(response.status_code, 200)
	self.assertContains(response, "No polls are available.")
	self.assertQuerysetEqual(response.context['latest_question_list'], [])

class QuestionModelTests(TestCase):
	def test_was_published_recently_with_future_question(self):
		time=timezone.now()+datetime.timedelta(days=30)
		future_question=Question(pub_date=time)
		self.assertIs(future_question.was_published_recently(), False)
	def test_was_published_recently_with_old_question(self):
		time=timezone.now()-datetime.timedelta(days=1, seconds=1)
		future_question=Question(pub_date=time)
		self.assertIs(future_question.was_published_recently(), False)
	def test_was_published_recently_with_recent_question(self):
		time=timezone.now()-datetime.timedelta(hours=23, minutes=59, seconds=59)
		future_question=Question(pub_date=time)
		self.assertIs(future_question.was_published_recently(), True)