from django import template

from cards.models import BOXES, CardModel

register = template.library

@register.inclusion_tag('cards/box_links.html')
def boxes_as_links():
    boxes = []
    for box_num in BOXES:
        card_count = CardModel.objects.filter(box=box_num).count()
        boxes.append({
            'number': box_num,
            'card_count': card_count
        })

    return {'boxes': boxes}
    # return boxes