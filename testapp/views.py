from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from testapp.models import testdata
from testapp.forms import (SendDataForm,
                           sendDataModelForm,
                           UpdateForm)
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def first_view(request):
    # return HttpResponse("<h1>Hello World</h1>")
    data = {'name':'Millicent', 'age': 17, 'course':'android'}
    return render(request, 'testapp/index.html',data)

def savedata(request):
    if request.method == 'POST':
        data = testdata()
        data.studentName = request.POST.get('studentName')
        data.age = request.POST.get('age')
        data.course = request.POST.get('course')
        data.email = request.POST.get('email')
        data.save()
        messages.success(request, 'Data saved successfully')
        # return HttpResponse('Data saved')
        return redirect('display')
    else:
        return render(request, 'testapp/form.html')


def regularFormView(request):
    if request.method == 'POST':
        form = SendDataForm(request.POST)
        if form.is_valid():
            # create an object of the model to save to
            # print(form.email)
            data = testdata()
            data.studentName = form.cleaned_data['studentName']
            data.age = form.cleaned_data['age']
            data.course = form.cleaned_data['course']
            data.email = form.cleaned_data['email']
            data.save()
            messages.success(request, 'Data saved successfully')
            return redirect('display')
    else:
        form = SendDataForm()

    dict =  {'form': form}
    return render(request, 'testapp/forms2.html',dict)



def modelFormView(request):
    if request.method == 'POST':
        form = sendDataModelForm(request.POST)
        if form.is_valid():
            # data = form.save(commit=False)
            # data.age = 17
            # data.save()
            form.save()
            messages.success(request, 'Data saved successfully')
            # return HttpResponse('Your data was saved')
            return redirect('display')
    else:
        form = sendDataModelForm()

    dict = {'form': form}
    return render(request, 'testapp/forms3.html',dict)


@login_required
def retrieveData(request):
    data=testdata.objects.all()
    dict = {'data': data}
    return render(request, 'testapp/display.html',dict)


def update(request,data_id):
    data = get_object_or_404(testdata,id=data_id)
    if request.method == 'POST':
        form = UpdateForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data successfully updated')
            return redirect('display')

    else:
        form = UpdateForm(instance=data)

    dict = {'data':data,'form':form}
    return render(request,'testapp/update.html',dict )


def delete_data(request, data_id):
    testdata.objects.filter(id=data_id).delete()
    messages.info(request, 'Your data has been deleted')
    return redirect('display')


#http://127.0.0.1:8000/login/?next=/display/









