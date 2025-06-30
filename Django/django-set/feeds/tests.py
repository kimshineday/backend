from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Feed
from users.models import User

class FeedAPITestCase(APITestCase):
    # 각 테스트 메서드가 실행되는지 확인
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='xptmxm@00')

        self.feed1 = Feed.objects.create(user=self.user, title = 'Title1')
        self.feed2 = Feed.objects.create(user=self.user, title = 'Title1')
    def test_get_all_feeds(self):
        url = reverse('all_feeds')
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual((len(res.date), 2))

    def test_get_feed_detail(self):
        url = reverse('feed_detail', kwargs={'feed_id':1})
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        """
        print('test res.data', res.data)
        #.test res.data {'id:1, 'user': OrderedDict({'username': 'testuser', 'email':'', 'is_superuser': False}), 'review_set': [], 'created_at': '날짜', 'updated_at': '날짜', 'title': 'Title 1', 'content':''}
        """
        #self.assertEqual(len(res.data), 2)
        self.assertEqual(res.data['content'], self.feed1.content)

    def test_create_feed(self):
        self.client.login(username='testuser', password='password')

        url = reverse('all_feeds')
        data = {'content':'New Feed', 'title':'New Title'}
        res = self.client.post(url, data)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Feed.objects.count(), 3) # 게시글 수가 3개


        self.assertEqual(Feed.objects.latest('id').content, 'New Feed') # 가장 최신 글

# 디테일하게 생각을 하고 설계를 할 필요가 있다.