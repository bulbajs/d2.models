# Создать двух пользователей
# (с помощью метода User.objects.create_user('username')).
# Создал 7 пользователей
# 2. Создать двух пользователей (с помощью метода User.objects.create_user('username')).
# 3. Создать два объекта модели Author, связанные с пользователями.
# 4. Добавить 4 категории в модель Category.
# 5. Добавить 2 статьи и 1 новость.
# 6. Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
# 7. Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).
# 8. Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
# 9. Обновить рейтинги пользователей.
# 10Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
# Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
# Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
from django.contrib.auth.models import User
from news.models import Author, Category

User.objects.create_user(username='bulba')
User.objects.create_user(username='psyduck')
User.objects.create_user(username='bulb')
User.objects.create_user(username='Dan')
User.objects.create_user(username='Bob')
User.objects.create_user(username='Bulba')
User.objects.create_user(username='Psyduck')
User.objects.create_user(username='artem')


# Создание пользователей

u1 = User.objects.get(pk=1)
Author.objects.create(authorUser=u1)
u3 = User.objects.get(pk=3)
Author.objects.create(authorUser=u3)
u6 = User.objects.get(pk=6)
Author.objects.create(authorUser=u6)
u7 = User.objects.get(pk=7)
Author.objects.create(authorUser=u7)

# Создание объектов модели Category

Category.objects.create(name = 'Sport')
Category.objects.create(name = 'Investing')
Category.objects.create(name = 'IT')
Category.objects.create(name = 'blog')


