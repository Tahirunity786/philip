from django.http import HttpResponse
from django.shortcuts import redirect, render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate
from employee.models import hr_emps

# from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth import logout, login

# from employee.models import CustomUser
import traceback

# User = get_user_model()


def login_view(request):
    if request.method == "POST":
        try:
            username = request.POST.get("ID")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)  # Log the user in

                # Store the username in the session for later retrieval
                request.session['temp_username'] = username

                return redirect("Ehome")
            else:
                return redirect("Login")
        except Exception as e:
            # If an exception occurs, capture and display the traceback
            trace = traceback.format_exc()
            return HttpResponse(f"An error occurred: {e}<br>Traceback:<br>{trace}")
    else:
        return render(request, "employee/page-singin.html")

def register(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        empID = request.POST.get("empID")
        pass1 = request.POST.get("pass")
        pass2 = request.POST.get("pass2")

        if pass1 == pass2 and empID.isdigit():
            # Check if the username (empID) is already taken
            if not User.objects.filter(username=empID).exists():
                if len(pass1) > 8:
                    try:
                        user = User.objects.create_user(
                            first_name=fname,
                            last_name=lname,
                            username=empID,
                            password=pass1,
                        )
                        user.save()
                        messages.success(request, "User registered successfully.")
                        return redirect(
                            "Login"
                        )  # Redirect to your login page after registration
                    except Exception as e:
                        return HttpResponse(e)
                else:
                    messages.error(request, "Password must be 8 character.")
            else:
                messages.error(
                    request, "Username is already taken. Please choose a different one."
                )
        else:
            messages.error(request, "Passwords do not match.")

    # If it's a GET request or there was an error, render the registration page.
    return render(request, "employee/register.html")


@login_required(login_url="/mega-soft/e-login-view")
def index(request):
    return render(request, "employee/index.html")


@login_required(login_url="/mega-soft/e-login-view")
def insight(request):
    # print(r)
    return render(request, "employee/insight.html")


@login_required(login_url="/mega-soft/e-login-view")
def birthday(request):
    return render(request, "employee/birthday.html")


@login_required(login_url="/mega-soft/e-login-view")
def holiday(request):
    return render(request, "employee/holiday.html")


def giudeline(request):
    return render(request, "employee/guideline.html")


def announcement(request):
    return render(request, "employee/announcements.html")


def news(request):
    return render(request, "employee/new.html")


def newsletter(request):
    return render(request, "employee/newletter.html")


@login_required(login_url="/mega-soft/e-login-view")
def payslip(request):
    return render(request, "employee/payslip.html")


# WORKING
@login_required(login_url="/mega-soft/e-login-view")
def profile(request):
    if request.user.is_authenticated:
        emp_crd = hr_emps.objects.get(user=request.user.id)

        content = {"info": emp_crd}
    return render(request, "employee/profile.html", content)


@login_required(login_url="/mega-soft/e-login-view")
def attendance(request):
    if request.user.is_authenticated:
        emp_crd = hr_emps.objects.get(user=request.user.id)

        content = {"info": emp_crd}
    return render(request, "employee/m-attendance.html", content)


@login_required(login_url="/mega-soft/e-login-view")
def attendance_summary(request):
    return render(request, "employee/attendance.html")


@login_required(login_url="/mega-soft/e-login-view")
def settings(request):
    return render(request, "employee/settings.html")


@login_required(login_url="/mega-soft/e-login-view")
def support(request):
    return render(request, "employee/contact.html")


def logout_view(request):
    logout(request)

    return redirect("Login")

def lock_view(request):
    try:
        if request.method == "POST":
            # Retrieve the locked username from the session
            # locked_user_info = request.session.get('locked_user')
            locked_user_info = request.session['temp_username']
            print("This is locked_user",locked_user_info)
            if locked_user_info:
                locked_username = locked_user_info.get('username')

                password = request.POST.get('password')
                
                user = authenticate(request, username=locked_username, password=password)

                if user:
                    login(request, user)
                    # Remove user information from the session after successful login
                    request.session.pop('locked_user', None)
                    return redirect('Ehome')
                else:
                    return redirect('Login')
            else:
                # Handle the case where locked_user information is not available
                return HttpResponse("Locked user information not found.")
        else:
            # Log out the user and render the 'employee/page-unlock.html' template
            if request.user.is_authenticated:
                logout(request)
            return render(request, 'employee/page-unlock.html')

    except Exception as e:
        # If an exception occurs, capture and display the traceback
        trace = traceback.format_exc()
        return HttpResponse(f"An error occurred: {e}<br>Traceback:<br>{trace}")