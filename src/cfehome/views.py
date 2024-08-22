from django.http import HttpResponse

from visits.models import PageVisit


def home_page_view(request, *args, **kwargs):
    query = PageVisit.objects.all()
    print(query)
    return HttpResponse("<h1>Hello World</h1>")
