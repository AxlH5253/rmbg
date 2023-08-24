from django.http import JsonResponse
from rest_framework.decorators import api_view
from PIL import Image
from .rmbg import remove_background

@api_view(['POST', 'GET'])
def upload_image(request, format=None):
    if(request.method == 'POST'):
        try:
            file_uploaded = request.FILES.get('file')
            input_image = Image.open(file_uploaded)
            output_image = remove_background(input_image)
            return JsonResponse({'status': 200, 'data': output_image, 'message': 'success'}, status=200)
        except Exception as e:
            return JsonResponse({'status': 500, 'message': e }, status=500)
    elif(request.method == 'GET'):
        return JsonResponse({'status': 200, 'message': 'success'}, status=200)
