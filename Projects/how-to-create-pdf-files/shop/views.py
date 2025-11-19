from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse, FileResponse

import io
from reportlab.pdfgen import canvas

# Create your views here.

def index(request):
    return render(request, "index.html", {})

def download_pdf(request: HttpRequest) -> FileResponse:

    buffer = io.BytesIO() # Create an in-memory buffer stream to store bytes (pdf data)

    p = canvas.Canvas(buffer, pagesize=(595.27, 841.89)) # Create a canvas (from reportlab)

    p.drawString(50, 750, "Hello World.") # Draw something to it

    p.showPage() # showPage() saves the current page

    p.save() # save() saves the file and closes the canvas

    buffer.seek(0) # set the pointer to beginning of the file
    
    return FileResponse(buffer, as_attachment=True, filename="hello.pdf")