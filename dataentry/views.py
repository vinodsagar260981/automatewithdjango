from django.shortcuts import render, redirect
from .utils import get_all_custom_models
from uploads.models import Upload
from django.conf import settings
from django.core.management import call_command
from django.contrib import messages

# Create your views here.
def import_data(request):
    if request.method == 'POST':
        file_path = request.FILES.get('file_path')
        model_name =request.POST.get('model_name')
        # print(file_path)
        # print(model_name)
        #store the file inside the upload model
        upload = Upload.objects.create(file=file_path, model_name=model_name)

        #construct full path
        relative_path = str(upload.file.url)
        base_path = str(settings.BASE_DIR)
        full_path =base_path + relative_path 
        # print(full_path)

        #trigger the importdata command from management
        try:
            call_command('importdata', full_path, model_name)
            messages.success(request, "Data imported successfully")
        except Exception as e:
            messages.error(request, str(e))

        return redirect('import_data')
    else:
        custom_models = get_all_custom_models()
        context = {
            'custom_models': custom_models,
        }
    return render(request, 'dataentry/dataentry.html', context)