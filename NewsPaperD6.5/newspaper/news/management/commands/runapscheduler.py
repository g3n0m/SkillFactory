import logging

from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.mail import EmailMultiAlternatives
from django.core.management.base import BaseCommand
from django.template.loader import render_to_string
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution

from datetime import datetime as date_time

from news.models import Category, Post


logger = logging.getLogger(__name__)


def news_sender():
    for category in Category.objects.all():

        news_from_each_category = []
        # определение номера прошлой недели
        week_number_last = date_time.now().isocalendar()[1] - 1

        # добавляем в список статьи прошлой недели
        for news in Post.objects.filter(id=category.id, datetime__week=week_number_last).values('pk',
                                                                                    'headline',
                                                                                    'datetime',
                                                                                    'category_Type'):
            date_format = news.get("datetime").strftime("%m/%d/%Y")
            new = (f' http://127.0.0.1:8000/news/{news.get("pk")}, {news.get("headline")}, '
                   f'Категория: {news.get("category_Type")}, Дата создания: {date_format}')
            news_from_each_category.append(new)

        # для удобства проверки
        #print(news_from_each_category)
        #print()
        #print('+++++++++++++++++++++++++++++', category.article_text, '++++++++++++++++++++++++++++++++++++++++++++')
        #print()
        #print("Письма будут отправлены подписчикам категории:", category.article_text, '( id:', category.id, ')')

        subscribers = category.subscribers.all()

        # цикл для вывода инфы в консоль об адресах подписчиков, для удобства и тестов
        #print('по следующим адресам email: ')
        #for qaz in subscribers:
        #    print(qaz.email)
        #print()

        #формирование письма
        for subscriber in subscribers:
            # для удобства в консоль добавляем вывод
            #print('____________________________', subscriber.email, '___________________________________')
            #print()
            #print('Письмо, отправленное по адресу: ', subscriber.email)
            html_content = render_to_string(
                'news/mail_sender.html', {'user': subscriber,
                                     'text': news_from_each_category,
                                     'category_name': category.article_text,
                                     'week_number_last': week_number_last})
            msg = EmailMultiAlternatives(
                subject=f'Здравствуй, {subscriber.username}, новые статьи за прошлую неделю в вашем разделе!',
                from_email='silverbackstrela@yandex.ru',
                to=[subscriber.email]
            )
            msg.attach_alternative(html_content, 'text/html')
            #print()
            # для удобства в консоль выводим содержимое нашего письма для проверки
            #print(html_content)

            # Чтобы запустить реальную рассылку нужно раскоментить нижнюю строчку
            msg.send()


def delete_old_job_executions(max_age=604_800):
    DjangoJobExecution.objects.delete_old_job_executions(max_age)

class Command(BaseCommand):
    help = "Runs apscheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            news_sender,

            #для проверки будем отправлять письма каждые 20 секунд
            #trigger=CronTrigger(second="*/20"),

            # отправляем письма подписчикам в понедельник в 9 утра
            trigger=CronTrigger(day_of_week="mon", hour="08", minute="00"),

            id="news_sender",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'news_sender'.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info(
            "Added weekly job: 'delete_old_job_executions'."
        )

        try:
            logger.info("Starting scheduler")
            print('Starting scheduler...')
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            print('Stopping scheduler...')
            logger.info("Scheduler shut down successfully!")
