from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse

# Create your views here.

def hey_view(request: HttpRequest, name: str) -> HttpResponse:
  return HttpResponse(f'Hey, {name}!')

def age_in_view(request: HttpRequest, end: int, birthyear: int) -> HttpResponse:
  age = end - birthyear
  return HttpResponse(f'{age}')

def order_total_view(request: HttpRequest, burgers: int, fries: int, drinks: int) -> HttpResponse:
  burgers_price = 4.50 * burgers
  fries_price = 1.50 * fries
  drinks_price = 1.00 * drinks

  total = burgers_price + fries_price + drinks_price
  return HttpResponse(f'Order Total: {total:.2f}$')