from django.db import models

NUM_BOXES = 5
BOXES = range(1, NUM_BOXES + 1)

class CardModel(models.Model):
    question = models.CharField(max_length=150)
    answer = models.CharField(max_length=150)
    box = models.IntegerField(choices=zip(BOXES, BOXES), default=BOXES[0])
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

    class Meta:
        ordering = ['-date_created']
        verbose_name = 'card'
        verbose_name_plural = 'cards'