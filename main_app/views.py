from django.shortcuts import render
dogs = [
  {'name': 'Opal', 'breed': 'German Shorthair Pointer-Australian Shepherd Mix', 'description': 'sassy snuggler', 'age': 3},
  {'name': 'Scout', 'breed': 'German Shepherd-Lab Mix', 'description': 'iron stomach protector/vacuum', 'age': 6},
]

# define the home view 
def home(request):
    # include an .html file extension - unlike when rendering EJS templates
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    return render(request, 'dogs/index.html', {
        'dogs': dogs
    })