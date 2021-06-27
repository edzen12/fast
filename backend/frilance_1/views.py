from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    response = Response({
        'pay_image': reverse('pay_image-list', request=request, format=format),
        'service': reverse('service-list', request=request, format=format),
        'social': reverse('social-list', request=request, format=format),
        'reviews': reverse('reviews-list', request=request, format=format),
        'tarif': reverse('tarif-list', request=request, format=format),
        'linkprice': reverse('linkprice-list', request=request, format=format),
        'form': reverse('form-list', request=request, format=format),
    })
    return response
