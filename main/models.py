from django.db import models

class Writers(models.Model):
    name = models.CharField('имя и фимилия', max_length=25,)
    surname = models.CharField('фамилия на английском',max_length=20, primary_key=True)
    photo = models.ImageField('фото', upload_to='img/')
    description = models.CharField('краткое описание', max_length=100)
    full_description = models.TextField('полное описание')
    back = models.ImageField('задник', upload_to='img/', default='')
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Писатель'
        verbose_name_plural = 'Писатели'

class FAQ(models.Model):
    question = models.CharField('вопрос', max_length=150)
    answer = models.TextField('ответ')

    def __str__(self) -> str:
        return self.question
    
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

class Feedback(models.Model):
    feedback = models.TextField('вопрос/отзыв')

    def __str__(self) -> str:
        return self.feedback
    
    class Meta:
        verbose_name = 'Вопрос/отзыв'
        verbose_name_plural = 'Вопросы/отзывы'