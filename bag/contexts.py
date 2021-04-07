"""
Set the free gift threshold and 
product count etc.
"""

from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.FREE_GIFT_THRESHOLD:
        free_gift_delta = settings.FREE_GIFT_THRESHOLD - total
    else:
        free_gift_delta = 0

    grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'free_gift_delta': free_gift_delta,
        'free_gift_threshold': settings.FREE_GIFT_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
