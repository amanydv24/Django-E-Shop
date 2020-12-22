from django.shortcuts import render, HttpResponse, redirect, \
    get_object_or_404, reverse
from django.contrib import messages
from django.conf import settings
from decimal import Decimal
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm



@csrf_exempt
def payment_done(request):
    return render(request, 'payment_done.html')
