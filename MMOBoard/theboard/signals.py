from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.models import User

from .models import Comment, UserProfile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=Comment)
def comment_notify(sender, instance, created, **kwargs): 
    if instance.approved_comment:
        subject = f'{instance.author}, ваш коммент опубликован'
        body = f'Уважаемый {instance.author}, коммент от {instance.date_added.strftime("%d-%m-%Y")} к публикации "{instance.post.title}" от {instance.post.author} опубликован.'
        email = instance.author.email

    if not instance.approved_comment:
        subject = f'{instance.author}, ваш коммент был отклонен'
        body = f'Уважаемый {instance.author}, коммент от {instance.date_added.strftime("%d-%m-%Y")} к публикации "{instance.post.title}" от {instance.post.author} был отклонен.'
        email = instance.author.email

    if created:
        subject = f'Уважаемый {instance.post.author}, новый коммент от {instance.author} к вашей публикации "{instance.post.title}"'
        body = f'Уважаемый {instance.post.author}, вы получили коммент к вашей публикации "{instance.post.title}" от {instance.author}, {instance.date_added.strftime("%d-%m-%Y %H:%M")}'
        email = instance.post.author.email

    msg = EmailMultiAlternatives(
        subject=subject,
        body=body,
        from_email='g3n0mskilled@yandex.ru',
        to=[email]
    )
    
    html_content = render_to_string(
        'theboard/comment_created.html',
        {
            'comment': instance,
            'body': body
        }
    )

    msg.attach_alternative(html_content, "text/html")

    msg.send()


@receiver(post_delete, sender=Comment)
def delete_comment_notify(sender, instance, **kwargs): 
    subject = f'{instance.author}, коммент был удален'
    body = f'Добрый день, {instance.author}! Ваш коммент от {instance.date_added.strftime("%d-%m-%Y")} к публикации "{instance.post.title}" от {instance.post.author} был удален.'
    email = instance.author.email

    msg = EmailMultiAlternatives(
        subject=subject,
        body=body,
        from_email='g3n0mskilled@yandex.ru',
        to=[email]
    )
    
    html_content = render_to_string(
        'theboard/comment_created.html',
        {
            'comment': instance,
            'body': body
        }
    )

    msg.attach_alternative(html_content, "text/html")

    msg.send()


@receiver(post_save, sender=User)
def profile_notify(sender, instance, created, **kwargs):
    subject = f'Добрый день, {instance.username}! Настройки профиля на сайте MMORPG Board были изменены!'
    body = f'Добрый день, {instance.username}! Настройки профиля на сайте MMORPG Board были изменены!'
    email = instance.email

    print(subject)
    print('--------------- \\ --------------')

    msg = EmailMultiAlternatives(
        subject=subject,
        body=body,
        from_email='g3n0mskilled@yandex.ru',
        to=[email]
    )
    
    html_content = render_to_string(
        'theboard/profile_email.html',
        {
            'userprofile': instance.userprofile,
            'body': body
        }
    )

    msg.attach_alternative(html_content, "text/html")

    msg.send()
