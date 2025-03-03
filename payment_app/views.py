import stripe
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY

def buy_item(request, id):
    item = get_object_or_404(Item, id=id)
    
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': item.currency,
                'product_data': {'name': item.name},
                'unit_amount': int(item.price * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url="http://localhost:8000/success/",
        cancel_url="http://localhost:8000/cancel/",
    )
    print(session)
    return JsonResponse({'id': session.id})

def item_detail(request, id):
    item = get_object_or_404(Item, id=id)
    # print(item)
    return render(request, 'item_detail.html', {'item': item, 'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY})

