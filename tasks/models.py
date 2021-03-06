# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from thumbs import ImageWithThumbsField


from south.modelsinspector import add_introspection_rules
add_introspection_rules(
    [
        (
            (ImageWithThumbsField, ),
            [],
            {
                "verbose_name": ["verbose_name",{"default":None}],
                "name": ["name", {"default": None}],
                "width_field": ["width_field", {"default": None}],
                "height_field":["height_field", {"default": None}],
                "sizes": ["sizes", {"default": None}],
             },
         ),
     ],
["^thumbs\.ImageWithThumbsField",])

#from django.db.models import ImageWithThumbsField


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Категория')
    name = models.CharField(max_length=100, verbose_name='Категория транслитом')
    class Meta:
        verbose_name = 'категории'
        verbose_name_plural = 'категория'
    def __unicode__(self):
        return self.title

class Status(models.Model):
    status_name = models.CharField(max_length=30, verbose_name='Статус')
    class Meta:
        verbose_name='статусы'
        verbose_name_plural='Статус'
    def __unicode__(self):
        return self.status_name
    

class Tag(models.Model):
    title = models.CharField(max_length=100, verbose_name='Тег')
    name = models.CharField(max_length=100, verbose_name='Тег транслитом')
    class Meta:
        verbose_name = 'теги'
        verbose_name_plural = 'Тег'
    def __unicode__(self):
        return self.titlez

class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    end_date = models.DateTimeField(blank=True, verbose_name='До какого срока задача актуальна?', null=True)
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category, related_name='tasks')
    rate = models.IntegerField(verbose_name = 'Рейтинг', default=0)
    task_photo = ImageWithThumbsField(upload_to='task_photos', verbose_name='Фото', blank=True, null=True,sizes=((50, 50),(150, 150),))
    thumb_taskp_hoto = ImageWithThumbsField(upload_to='task_thumbs', verbose_name='Фото', blank=True,null=True, sizes=((50, 50),(150, 150),))
    status = models.IntegerField(default=1)
    class Meta:
        verbose_name = 'задачи'
        verbose_name_plural = 'Задача'
        def __unicode__(self):
            return self.title
            
class Answer(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    class Meta:
        verbose_name = 'отклики'
        verbose_name_plural = 'Отклик'
    def __unicode__(self):
        return self.content
        
class Profile(models.Model):
    user = models.ForeignKey(User, related_name='profile')
    avatar = models.ImageField(upload_to='avatars', blank=True)
    #karma
    end_tasks =  models.IntegerField(default=0)
    gevt_tasks = models.IntegerField(default=0)
    class Meta:
        verbose_name = 'профили пользователей'
        verbose_name_plural = 'Профиль пользователя'
    def __unicode__(self):
        return self.user.get_full_name()
        
        













