from django.shortcuts import render
from .utility import *
from .forms import *


from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages



# home page
def index(request):
    template_name = 'index.html'
    context = {}
    return render(request, template_name, context)

# crop image
@csrf_exempt
def cropImage(request):
    template_name = 'crop-image.html'
    form = None
    if request.method == 'POST':
        pass

    context = {
        "form": form
    }
    return render(request, template_name, context)

import json
@csrf_exempt
def uploadImage(request):
    pass
    # fs = FileSystemStorage()
    # try:
    #     if request.method == 'POST':files
    #         printStar()
    #         file_obj = request.FILES.get('cropped_image')
    #         print(type(file_obj))
    #         file_name = 'email_cover_image.png'


    #         print("file_obj: ", file_obj)
    #         print("file_name: ", file_name)
    #         f = file_obj
    #         with open(f.name, 'wb+') as destination:
    #             for chunk in f.chunks():
    #                 destination.write(chunk)


    #         # filename = fs.save(file_name, file_obj)
    #         # file_path = fs.url(filename)
    #         printStar()

    #         return JsonResponse({
    #             'status': 'success',
    #             'message': 'Image Uploaded Successfully',
    #             'url': file_path
    #         })
    # except Exception as E:
    #     print(E)
    # return JsonResponse({
    #     'status': 'failed',
    #     'message': 'failed_to_upload_image'
    # })

########################################################



# class ImageCropper(View):
#     def get(self, request):
#         return render(request, 'crop-image.html')


# @csrf_exempt
# def uploadImage(request):
#     fs = FileSystemStorage()
#     try:
#         if request.FILES.get('cropped_image'):
#             file_obj = request.FILES['cropped_image']
#             file_name = 'email_cover_image.png'
#             filename = fs.save(file_name, file_obj)
#             file_path = fs.url(filename)
#             return JsonResponse({
#                 'status': 'success',
#                 'message': 'Image Uploaded Successfully',
#                 'url': file_path
#             })
#     except Exception as E:
#         print(E)
#     return JsonResponse({
#         'status': 'failed',
#         'message': 'failed_to_upload_image'
#     })

import base64
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import base64
@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        printStar()
        image = request.FILES['image_file']
        print(image)
        printStar()

        
        return JsonResponse({'message': 'File uploaded successfully.'})
    else:
        return JsonResponse({'error': 'Invalid request.'})


from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
 
@csrf_exempt
def temp(request):
    template_name = 'temp.html'
    form = None
    if request.method == 'POST':
        pass

    context = {
        "form": form
    }
    return render(request, template_name, context)


@csrf_exempt
def temp1(request):
    fs = FileSystemStorage()
    try:
        if request.FILES.get('cropped_image'):
            file_obj = request.FILES['cropped_image']
            file_name = 'crop_image.png'
            filename = fs.save(file_name, file_obj)
            file_path = fs.url(filename)
            return JsonResponse({
                'status': 'success',
                'message': 'Image Uploaded Successfully',
                'url': file_path
            })
    except Exception as E:
        print(E)
    return JsonResponse({
        'status': 'failed',
        'message': 'failed_to_upload_image'
    })