from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import Items,Bids
from .forms import ReviewForm,ItemsForm,SearchForm,DeleteForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.utils.text import slugify
from datetime import timedelta
from django.utils import timezone
def user_is_admin(user):
    return user.is_authenticated and user.is_superuser

@login_required
def index(request):
    item=Items.objects.all()   
    val=False
    user = request.user
    if user_is_admin(user):
        val=True 
    return render(request,"all.html",{
        "items":item,
        "x":val,
        "user": user
    })

@login_required
def bid(request,slug):
    book=get_object_or_404(Items,slug=slug)
    if request.method == 'POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            bid=Bids()
            increment = form.cleaned_data['bid']
            if increment>0:
                user = request.user 
                if user==book.highest:
                    return redirect("all")
                bid.item=book.slug
                bid.name=user
                book.bid+=increment
                bid.bid=book.bid
                bid.save()
                book.highest=user
                book.save()
            return redirect("all")        
    else:
        form=ReviewForm()
    bids=Bids.objects.filter(item=slug).order_by('-timestamp')
    return render(request,"bid.html",{
        "book":book,
        "form":form,
        "bids":bids
    })

@user_passes_test(user_is_admin)
def add(request):
    if request.method == 'POST':
        form = ItemsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("all")
    else:
        form = ItemsForm()
    return render(request, "add.html", {
        "form": form
    })

@login_required
def detail(request, slug):
    time=timezone.now()
    book=get_object_or_404(Items,slug=slug)
    bid=get_object_or_404(Bids,item=slug)
    if time - bid.timestamp > timedelta(hours=3):
        form=ReviewForm()
        return render(request,"detail.html",{
                "book":book,
                "bids":bid,
                "sold":True
                })
    if request.method == 'POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            increment = form.cleaned_data['bid']
            if increment>0:
                user = request.user 
                if user==book.highest:
                    return redirect("all")
                bid.name=user
                if increment>book.bid:
                    book.bid=increment
                else:
                    book.bid+=increment
                bid.bid=book.bid
                bid.save()
                book.highest=user
                book.save()
            return redirect("all")        
    else:
        form=ReviewForm()
    bids=Bids.objects.filter(item=slug).order_by('-timestamp')
    return render(request,"detail.html",{
        "book":book,
        "form":form,
        "bids":bids,
        "sold":False
    })

@user_passes_test(user_is_admin)
def search(request):
    employees = Items.objects.all()
    form = SearchForm(request.GET)
    if form.is_valid():
        title = form.cleaned_data.get('title')
        if title:
            employees = employees.filter(title__icontains=title)

    return render(request, "search.html", {
        "employees": employees,
        "form": form
    })

@user_passes_test(user_is_admin)
def delete(request):
    value=False
    employees = Items.objects.all()
    form = DeleteForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['title']
        s=slugify(name)
        item=Items.objects.get(title=name)
        bid=Bids.objects.get(item=s)
        item.delete()
        bid.delete()
        value=True
        return redirect("all")
    return render(request,"delete.html",{
        "form":form,
        "value":value
    })