from django import template

from cards.models import BOXES, CardModel

register = template.Library()

@register.inclusion_tag('cards/_box_links.html')
def boxes_as_links():
    boxes = []
    for box_num in BOXES:
        cards = CardModel.objects.filter(box=box_num)
        boxes.append({
            'number': box_num,
            'cards': cards
        })

    return {'boxes': boxes}
    # return boxes