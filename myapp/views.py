from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Book, Admin


# Create your views here.
def index(request):
    return render(request, 'index.html')


def admin_login(request):
    if request.method == "POST":
        admin_email = request.POST['admin_email']
        admin_password = request.POST['admin_password']

        if admin_email and admin_password:
            if Admin.objects.filter(email=admin_email).exists() and Admin.objects.filter(password=admin_password).exists():
                messages.info(request, 'Successfully Login')
                return redirect('home')
            else:
                messages.info(request, 'Invalid Credential')
                return redirect('admin_login')
        else:
            return render(request, 'admin_login.html')
    else:
        return render(request, 'admin_login.html')


def admin_register(request):
    if request.method == "POST":
        add_admin_email = request.POST.get('admin_email')
        add_admin_password = request.POST.get('admin_password')
        repassword = request.POST.get('repassword')


        if add_admin_email and add_admin_password and repassword:
            if add_admin_password == repassword:
                # check Admin Already exist...
                if Admin.objects.filter(email=add_admin_email).exists():
                    messages.info(request, 'Email id Already exist')
                    return redirect('admin_login')
                else:
                    admin = Admin()
                    admin.email = add_admin_email
                    admin.password = add_admin_password
                    admin.save()
                    messages.info(request, 'Admin Added Successfully')
                    return redirect('admin_login')
            else:
                messages.info(request, 'password not match')
                return redirect('admin_register')
        else:
            messages.info(request, "Please enter empty field")
            return redirect('admin_register')
    else:
        return render(request, 'admin_register.html')


def admin_list(request):
    admins = Admin.objects.all()
    return render(request, 'admin_list.html', {'admins': admins})


def delete_admin(request):
    id = request.GET['id']
    if id:
        admin = Admin.objects.filter(id=id)
        admin.delete()
        return redirect('admin_list')
    else:
        admins = Admin.objects.all()
        return render(request, 'admin_list.html', {'admins': admins})


def add_book(request):
    if request.method == "POST":
        book_name = request.POST['book_name']
        author_name = request.POST['author_name']
        date = request.POST['date']
        if book_name and author_name and date:
            if Book.objects.filter(book_name=book_name).exists():
                messages.info(request, 'Book Already exist')
                return redirect('add_book')
            else:
                obj = Book()
                obj.book_name = book_name
                obj.author_name = author_name
                obj.date = date
                obj.save();
                return redirect('add_book')
        else:
            books = Book.objects.all()
            return render(request, 'add_book.html', {'books': books})
    else:
        books = Book.objects.all()
        return render(request, 'add_book.html', {'books': books})


def edit_book(request):
    id = request.GET['id']
    if request.method == "POST":
        book = Book.objects.get(id=id)
        book.book_name = request.POST['book_name']
        book.author_name = request.POST['author_name']
        book.save()
        return redirect('add_book')

    elif request.method == "GET":
        if id:
            book = Book.objects.filter(id=id)
            return render(request, 'edit_book.html', {'books': book})
        else:
            books = Book.objects.all()
            return render(request, 'add_book.html', {'books': books})


def delete_book(request):
    id = request.GET['id']
    if id:
        book = Book.objects.filter(id=id)
        book.delete()
        return redirect('add_book')
    else:
        books = Book.objects.all()
        return render(request, 'add_book.html', {'books': books})


def all_books(request):
    books = Book.objects.all()
    return render(request, 'all_books.html', {'books': books})