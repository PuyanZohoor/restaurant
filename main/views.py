from django.shortcuts import render
from django.contrib.auth import login, authenticate 
from .forms import TableForm 
from django.contrib import messages



def index_page(request):
    return render(request, 'index.html')

def menu_page(request):
    return render(request, 'menu.html')

def book_page(request):
    return render(request, 'book.html')

def about_page(request):
    return render(request, 'about.html')


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'SignUpPage.html', context = context)


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
            )
            if user:
                login(request, user)
                message = 'hello {user.username} you have been logged in!'
            else:
                message = 'Login Failed!'
    return render(request, 'LoginPage.html', {'message': message})


def logout_user(request):
    logout(request)
    return redirect('index.html')


def booking(request):
    if request.method == 'POST':
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
            if form.is_reserved:
                messages.error('the table is already taken!')
                return redirect('index.html')
            messages.success('the table reserved for you.')
            return redirect('index.html')
    else:
        form = TableForm()
    context = {'form': form}
    return render(request, 'book.html', context = context)
