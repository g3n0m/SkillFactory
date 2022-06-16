from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.shortcuts import redirect
from django.template.loader import render_to_string

from .models import Post
from .views import send_mail

@receiver(m2m_changed, sender=Post.postCategories.through)
def notify_users_post(sender, instance, **kwargs):
    send_mail(instance)


#отправка нового письма категории подписчикам без использования celery
#@receiver(m2m_changed, sender=Post.postCategories.through)
#def notify_users_post(sender, instance, **kwargs):
#    global subscriber
#    sub_text = instance.main_part
#    for category in instance.postCategories.all():
#        for subscriber in category.subscribers.all():
#            #проверка для удобства
#            #print('*********', subscriber.email, '**********')
#            #print()
#
#             #print('Адресат:', subscriber.email)
#            html_content = render_to_string(
#                'news/mail.html', {'post': instance, 'text': sub_text[:50], 'category': category.article_text})
#
#            msg = EmailMultiAlternatives(
#                subject=f'Здравствуй, {subscriber.username}. Новая статья в вашем разделе!',
#                from_email='silverbackstrela@yandex.ru',
#                to=[subscriber.email]
#            )
#
#            msg.attach_alternative(html_content, 'text/html')
#
            # вывод в консоль для удобства
            #print()
            #print(html_content)
            #print()

            # блокировать отправку писем, если в этом нет необходимости во избежании бана
            #msg.send()

#        return redirect('/news/')