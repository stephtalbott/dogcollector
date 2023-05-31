from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dog
from .forms import FeedingForm

# define the home view 
def home(request):
    # include an .html file extension - unlike when rendering EJS templates
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', {
        'dogs': dogs
    })

def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    feeding_form = FeedingForm()
    return render(request, 'dogs/detail.html', {
        'dog': dog, 'feeding_form': feeding_form
    })

class DogCreate(CreateView):
    model = Dog
    fields = '__all__' 

class DogUpdate(UpdateView):
    model = Dog
    fields = ['breed', 'description', 'age']

class DogDelete(DeleteView):
    model = Dog
    success_url = '/dogs'

def add_feeding(request, dog_id):
    form = FeedingForm(request.POST)
    # validate the form 
    if form.is_valid():
        # don't save the form to the db without a dog_id assigned 
        # a feeding has to belong to a dog!
        new_feeding = form.save(commit=False)
        new_feeding.dog_id = dog_id 
        new_feeding.save()
    return redirect('detail', dog_id=dog_id)