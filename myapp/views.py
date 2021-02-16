from django.shortcuts import redirect, render
from .models import File
from .forms import FileForm
from django.db import models
import os
import re
from django.http import HttpResponse
from .process import *

def main(request):
    message = ''
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)

        if form.is_valid():
            request.FILES['docfile'].name = request.POST['type'] +"_" + request.FILES['docfile'].name
            newdoc = File(docfile=request.FILES['docfile'], kind=request.POST['type'], file_name=request.FILES['docfile'].name)
            if os.path.exists(newdoc.docfile.path):
                os.remove(newdoc.docfile.path)
                File.objects.filter(kind=request.POST['type'], file_name=request.FILES['docfile'].name).delete()

            newdoc.save()
            return redirect('main')
        
        else:
            message = 'The form is not valid. Fix the following error:'
    
    else:
        form = FileForm()

    documents = File.objects.all()
    namespaces = [document for document in documents if document.kind == "DATABASE"]
    column_references = [document for document in documents if document.kind == "SCHEMA"]
    data_points = [document for document in documents if document.kind == "DATA"]

    data = {
        'namespaces': namespaces,
        'column_references': column_references, 
        'data_points': data_points, 
        'form': form, 
        'enabled_link_data_button': namespaces and column_references and data_points,
        }

    return render(request, 'list.html', data)


def delete_file(request, file_name):
    file =  File.objects.filter(file_name=file_name).first()
    os.remove(file.docfile.path)
    file.delete()
    
    response = redirect('/')
    return response


def link_data(request):
    files = File.objects.all()
    
    database_df = create_data_frame(kind="DATABASE", files=files, separator=";")
    schema_df = create_data_frame(kind="SCHEMA", files=files, separator=",")
    data_df = create_data_frame(kind="DATA", files=files, separator=",")

    link_data_frames(database_df, schema_df, data_df)
  
    response = HttpResponse(open('media/rezult.zip', 'rb'), content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename=results.zip'
    return response