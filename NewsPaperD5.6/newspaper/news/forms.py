from django.forms import ModelForm, BooleanField # Импортируем true-false поле
from .models import Post
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group

# Создаём модельную форму
class PostForm(ModelForm):
    check_box = BooleanField(label='Ало, Галочка!')  # добавляем галочку, или же true-false поле

    # в класс мета как обычно надо написать модель по которой будет строится форма и нужные нам поля.
    # Мы уже делали что-то похожее с фильтрами.
    class Meta:
        model = Post
        fields = ['post_name', 'position', 'category', 'author', 'content', 'check_box']
        # не забываем включить галочку в поля иначе она не будет показываться на странице!


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        return user

