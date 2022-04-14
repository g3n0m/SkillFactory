from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    post = "PS"
    news = "NW"
    TYPE = [
        (post, "Статья"),
        (news, "Новость"),
    ]
    author = models.ForeignKey('accounts.Author', on_delete=models.CASCADE)
    type = models.CharField(
        max_length=2,
        choices=TYPE,
        default=post
    )
    create_time = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through="PostCategory")
    header = models.CharField(
        max_length=124,
        default='Заголовок отсутвует'
    )
    text = models.TextField(default='Текст отсутствует')
    rating = models.FloatField(default=0.0)

    def like(self):
        self.rating += 1

    def dislike(self):
        self.rating -= 1

    @property
    def preview(self):
        return f'{self.text[:128]} ...'

    def __str__(self):
        return f'{self.author} \t {self.preview}'

    def get_absolute_url(self):
        return f'/news/{self.id}'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(default='')
    datetime = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField(default=0.0)

    def like(self):
        self.rating += 1

    def dislike(self):
        self.rating -= 1
