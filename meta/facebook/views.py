
from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
from .models import *
from django.contrib.auth.hashers import make_password, check_password


def index(request):

    if request.method == "POST":
        product_id = request.POST.get('cartid')
        remove = request.POST.get('minus')
        cart_id = request.session.get('cart')
        print(cart_id)
        if cart_id:
            quantity = cart_id.get(product_id)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart_id.pop(product_id)
                    else:
                        cart_id[product_id] = quantity - 1
                else:
                    cart_id[product_id] = quantity + 1
            else:
                #
                cart_id[product_id] = 1
        else:
            cart_id = {}
            cart_id[product_id] = 1

        request.session['cart'] = cart_id

    cate = category.objects.all()
    cat_id = request.GET.get('category')

    if cat_id:
        products = product.objects.filter(category_id=cat_id)
    else:
        products = product.objects.all()

    context = {
        'cat': cate,
        'pro': products,

    }
    return render(request, 'home.html', context)


def signup(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        mno = request.POST.get('mobile')
        email = request.POST.get('email')
        passw = request.POST.get('pwd')
        gender = request.POST.get('gender')

        save_info = user_regis(
            first_name=fname, last_name=lname, mobile_no=mno, email=email, password=make_password(passw),  gender=gender)
        save_info.save()

        print(fname, lname, mno, email, passw)

        return HttpResponse("success")


def contact(request):
    return render(request, 'contact.html')


def login(request):
    if request.method == "POST":
        emailid = request.POST.get('email')
        passwd = request.POST.get('pwd')
        fetch_info = user_regis.objects.get(email=emailid)
        if check_password(passwd, fetch_info.password):
            request.session['name'] = fetch_info.first_name
            request.session['customer_id'] = fetch_info.id
            request.session['email'] = fetch_info.email
            return redirect('home')

        else:
            return HttpResponse("you have entered wrong password")

        return HttpResponse("login success")


def logout(request):
    print("------------------------")
    if request.method == 'POST':
        request.session.clear()
        return redirect('home')


def cartinfo(request):

    try:
        ids = list(request.session.get('cart').keys())
        cart_obj = product.objects.filter(id__in=ids)
        return render(request, 'cart.html', {'cart_obj': cart_obj})
    except:
        print("ok")

    return render(request, 'cart.html')


def checkout(request):

    if request.method == "POST":
        address = request.POST.get("address")
        mobile = request.POST.get("mobile")
        customer = request.session.get('customer_id')
        cart = request.session.get('cart')
        products = product.objects.filter(id__in=list(cart.keys()))
        if not customer:
            return HttpResponse("please login")
        for pro in products:
            save_ord_dtl = order(
                product=pro,
                customer=user_regis(id=customer),
                quantity=cart.get(str(pro.id)),
                address=address,
                mobile=mobile,
                price=pro.price
            )
            save_ord_dtl.save()
        request.session['cart'] = {}

        return redirect('cart')


def order_dtl(request):

    customer_id = request.session.get('customer_id')
    fetch_order = order.objects.filter(customer = customer_id)
    tp = 0
    for i in fetch_order:
        tp = tp+(i.price * i.quantity)
    

    return render(request, 'order.html', {'fetch_order_dtl': fetch_order,'tp':tp})
