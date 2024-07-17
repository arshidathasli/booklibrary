from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from book_app.models import Book
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from .models import Cart, CartItem, Orders, OrderItems
from django.contrib.auth.decorators import login_required

from accounts.models import UserProfile
from django.contrib.auth.models import User


def listBook(request):
    books = Book.objects.all()
    paginator = Paginator(books, 4)
    page_number = request.GET.get("page")

    try:
        page = paginator.get_page(page_number)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return render(request, "user/userlistbook.html", {"books": books, "page": page})


def detailsview(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, "user/userdetailsview.html", {"book": book})


def Search_book(request):
    query = request.GET.get("q")
    books = []

    if query:
        books = Book.objects.filter(
            Q(title__icontains=query) | Q(author__name__icontains=query)
        )

    context = {"books": books, "query": query}
    return render(request, "user/usersearch.html", context)


def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    user1 = User.objects.get(username=request.user)
    user = UserProfile.objects.get(user=user1)
    cart, created = Cart.objects.get_or_create(user=user)

    if book.quantity > 0:
        cart_item, item_created = CartItem.objects.get_or_create(cart=cart, book=book)

        if not item_created:
            cart_item.quantity += 1
        else:
            cart_item.quantity = 1
        cart_item.save()

    return redirect("viewcart")


def view_cart(request):
    # print(f"Request.user: {request.user}")
    user = User.objects.get(username=request.user)
    user = UserProfile.objects.get(user=user)
    cart, created = Cart.objects.get_or_create(user=user)
    cart_items = cart.cartitem_set.all()
    total_price = sum(item.book.price * item.quantity for item in cart_items)
    total_items = cart_items.count()

    context = {
        "cart_items": cart_items,
        "total_price": total_price,
        "total_items": total_items,
    }

    return render(request, "user/cart.html", context)


def increase_quantity(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    if cart_item.quantity < cart_item.book.quantity:

        cart_item.quantity += 1
        cart_item.save()
    return redirect("viewcart")


def decrease_quantity(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    if cart_item.quantity > 1:

        cart_item.quantity -= 1
        cart_item.save()
    return redirect("viewcart")


def remove_from_cart(request, item_id):

    try:
        cart_item = CartItem.objects.get(id=item_id)
        cart_item.delete()

    except cart_item.DoesNotExist:
        pass

    return redirect("viewcart")


def view_orders(request):
    # user_profile = get_object_or_404(UserProfile, user=request.user)
    user = User.objects.get(username=request.user)
    user_profile = UserProfile.objects.get(user=user)
    orders = ""

    orders = Orders.objects.filter(user=user_profile)
    context = {"orders": orders}
    print(f"Orders: {orders}")

    return render(request, "user/order.html", context)


def place_order_cod(request):
    user1 = User.objects.get(username=request.user)
    user_profile = UserProfile.objects.get(user=user1)
    print(f"Reached inside try")
    cart = get_object_or_404(Cart, user=user_profile)
    cart_items = CartItem.objects.filter(cart=cart)
    print(f"Reached after cart_items")
    if cart_items.exists():
        print(f"Reached inside cart_items: {cart_items}")
        total_amount = sum(item.book.price * item.quantity for item in cart_items)
        order = Orders.objects.create(user=user_profile, amount=total_amount)
        for item in cart_items:
            print(f"Item: {item}")
            OrderItems.objects.create(
                order=order, book=item.book, quantity=item.quantity
            )
            item.book.quantity -= item.quantity
            item.book.save()
            if item.quantity > 0:
                item.quantity = 0
                item.save()
            else:
                item.delete()

        messages.success(request, "Order placed successfully!")
        cart_items.delete()
        return redirect("orders")
    else:
        messages.error(request, "Your cart is empty.")
        return redirect("viewcart")
