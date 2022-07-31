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


    def move_card(self, solved):
        new_box = self.box + 1 if solved else BOXES[0]

        if new_box in BOXES:
            self.box = new_box
            self.save

        return self

    
    class Meta:
        ordering = ['-date_created']
        verbose_name = 'card'
        verbose_name_plural = 'cards'