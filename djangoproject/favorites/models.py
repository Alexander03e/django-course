from django.db import models


def serials(request):
    serials = Serials.objects.all()
    return render(request, "serials/object.html", {'serials': serials})
    
