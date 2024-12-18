from django.shortcuts import render, redirect 
from django.contrib.auth.models import User
from django.contrib import messages

from tiendapp.models import Customer, OrderDetail, Product

def v_sign_up(request):
    return render(request, 'tiendapp/sign_up.html')

def v_sign_up_create(request):
    if request.method == "POST":
        data = request.POST.copy()
        print('>>>>>>>>>>>>>', data)

        print("Creando un cliente: ")
        nuevo_user = User.objects.filter(username = data["email"]).first()
        if nuevo_user is not None:
            messages.error(request, 'El email ya esta registrado en la pagina.')
            # incluir mensaje de 'tu cuenta ya existe'
            return redirect('/sign_up')
        
        if nuevo_user is None:
            ### INICIO DE LA CREACION DE UN USUARIO
            nuevo_user = User()
            nuevo_user.first_name = data["first_name"]
            nuevo_user.last_name = data["last_name"]
            nuevo_user.username = data["email"]
            nuevo_user.is_active = True
            nuevo_user.save() # Almacena en base de datos al usuario

            nuevo_user.set_password("123456") # Definir contrasena
            nuevo_user.save()
            messages.success(request, 'La creacion de la cuenta fue satisfactoria.')
            ### FIN DE LA CREACION DE UN USUARIO

        print("Enlanzar el user al customer: ")
        nuevo_customer = Customer.objects.filter(user = nuevo_user).first()
        if nuevo_customer is None:
            nuevo_customer = Customer()
            nuevo_customer.user = nuevo_user # Enlace
            nuevo_customer.billing_address = data["billing_address"]
            nuevo_customer.shipping_address = "Av. Libertad 3434. Concepcion."
            nuevo_customer.phone = data["phone"]
            nuevo_customer.save()

            return redirect('/sign_in')
        
    return redirect('/')


def v_sign_in(request):
    from django.contrib.auth import authenticate, login

    if request.method == 'POST':
        data = request.POST.copy()
        username = data['username']
        password = data['password']

        usuario_valido = authenticate(request, username = username,
                                      password = password)
        
        if usuario_valido is not None:
            login(request, usuario_valido)
            messages.success(request, 'La sesion se inicio correctamente.')
            return redirect('/')
        else:
            messages.error(request, 'Tu usuario o contrasenia no coinciden.')
            #incluir mensaje de error

    return render(request, 'tiendapp/sign_in.html')

def v_sign_out(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('/')


