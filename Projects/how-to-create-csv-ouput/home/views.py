import csv
from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    response = HttpResponse(
        content_type = 'text/csv',
        headers = {'Content-Disposition': "attachment; filename=my_csv_file.csv"},
    )

    writer = csv.writer(response)
    writer.writerow(["First row", "Foo", "Bar", "Baz"])
    writer.writerow(["Second row", "A", "B", "C", '"Testing"', "Here's a quote"])

    return response