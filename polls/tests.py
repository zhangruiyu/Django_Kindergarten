import datetime

from django.test import TestCase
from django.utils import timezone
from polls.models import Question


class QuestionMethodTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() 应该对 pub_date 字段值是将来的那些问题返回 False。
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)


def test_was_published_recently_with_old_question(self):
    """
    对于 pub_date 在一天以前的 Question，was_published_recently() 应该返回 False。
    """
    time = timezone.now() - datetime.timedelta(days=30)
    old_question = Question(pub_date=time)
    self.assertEqual(old_question.was_published_recently(), False)


def test_was_published_recently_with_recent_question(self):
    """
    对于 pub_date 在一天之内的 Question，was_published_recently() 应该返回 True。
    """
    time = timezone.now() - datetime.timedelta(hours=1)
    recent_question = Question(pub_date=time)
    self.assertEqual(recent_question.was_published_recently(), True)
