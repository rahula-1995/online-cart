from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from .models import product,Contact,Orders,OrderUpdate
import json

# Create your views here.
def index(request):

    catprods = product.objects.all()
    params={"product":catprods}

    return render(request, 'coronakit/index.html',params)

def about(request):

    return render(request, 'coronakit/about.html')

def cart(request):

    return render(request, 'coronakit/cart.html')

def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('firstName', '')
        email = request.POST.get('email', '')
        print("1"+email)
        address = request.POST.get('address', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone)
        order.save()
        id = order.order_id
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()

        return render(request, 'coronakit/confirm.html',{'id':id})

    return render(request, 'coronakit/checkout.html')

def contact(request):
    thank=False
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('number', '')
        desc = request.POST.get('message', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank=True
        return render(request, 'coronakit/contact-us.html',{'thank':thank})


    return render(request, 'coronakit/contact-us.html',{'thank':thank})

def gallery(request):

    return render(request, 'coronakit/gallery.html')

def account(request):
    response="Enter your order Id and Email and click Track Order to find details about your order!"
    if request.method == "POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)

            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                response=update[0].update_desc
                details=order[0].items_json
                kj=json.loads(details)
                price=kj[0:len(kj)-1]
                grandtotal=kj[-1]


                return render(request, 'coronakit/my-account.html',{'orders':price,'grandtotal':grandtotal,'response':response})
            else:
                return HttpResponse('{}')
        except Exception as e:
            print(e.__class__.__name__)
            return HttpResponse('sorry something went wrong')



    return render(request, 'coronakit/my-account.html',{'response':response})

def shop(request):

    return render(request, 'coronakit/shop.html')

def detailed(request):
    catprods1 = product.objects.all()
    params1 = {"product": catprods1}

    return render(request, 'coronakit/shop-detail.html',params1)

def wishlist(request):

    return render(request, 'coronakit/wishlist.html')
