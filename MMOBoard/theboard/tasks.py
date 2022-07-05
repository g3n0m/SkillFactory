from celery import shared_task
import time

from django.core.mail import EmailMultiAlternatives, send_mail
from django.template.loader import render_to_string

import datetime as DT
from datetime import timedelta, date

from datetime import datetime, timezone

from .models import Post, UserProfile, User


@shared_task
def subscribe_confirmation_message(user_name, email):
    send_mail(
        subject=f'MMORPG Board: подписка на обновления.',
        message=f'Добрый день, {user_name}! Спасибьо что подписались на еженедельные обновления на портале MMORPG Board.',
        from_email='g3n0mskilled@yandex.ru',
        recipient_list=[f'{email}', ],
    )


@shared_task
def weekly_digest():
    week = timedelta(days=7)

    subscribers = User.objects.filter(userprofile__news_susbscribed=True)
    subscribers_emails = []
    for subscriber in subscribers:
        subscribers_emails.append(subscriber.email)

    posts = Post.objects.all()
    weekly_posts = []
    now = datetime.now(timezone.utc)

    for post in posts:
        time_delta = now - post.post_date        
        if time_delta < week:
            weekly_posts.append(post)
       
    # print(f'Кол-во публикаций: {len(weekly_posts)}')
    # print(subscribers_emails)
    # print(weekly_posts)
    # print('----------------   ---------------')
    # print('----------------   ---------------')

    if subscribers_emails:
        msg = EmailMultiAlternatives(
            subject=f'Новостной недельный дайджест с портала MMORPG BOARD.',
            body=f'Привет! Еженедельная подборка публикаций',
            from_email='g3n0mskilled@yandex.ru',
            to=subscribers_emails,
        )

        html_content = render_to_string(
            'theboard/weekly_digest.html',
            {
                'digest': weekly_posts,
            }
        )

        msg.attach_alternative(html_content, "text/html")

        msg.send()
