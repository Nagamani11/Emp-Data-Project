from django.shortcuts import render
from .models import EmployeesData
def mainPage(request):
        return render(request, 'mainpage.html')
def add_emp(request):
    if request.method == 'GET':
        data = EmployeesData.objects.all()
        return render(request, 'add_emp.html')
    else:
        fname1 = request.POST.get('fname')
        lname1 = request.POST.get('lname')
        email1 = request.POST.get('email')
        mobile1 = request.POST.get('mobile')
        percentage1 = request.POST.get('percentage')
        year1 = request.POST.get('year')
        location1 = request.POST.get('location')
        college1 = request.POST.get('college')
        university1 = request.POST.get('university')
        EmployeesData(
            first_name = fname1,
            last_name = lname1,
            email = email1,
            mobile = mobile1,
            percentage = percentage1,
            year = year1,
            location = location1,
            college_name = college1,
            university = university1
        ).save()
        return render(request, 'mainpage.html')

def details_page(request):
    data = EmployeesData.objects.all()
    return render(request, 'detailspage.html',{'data':data})
