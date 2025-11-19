## How to create PDF files
This how-to uses [ReportLab](https://pypi.org/project/reportlab/) to generate and return pdf files dynamically.
- Install reportlab:
```
> pip install reportlab
```

Reportlab's API works with file-like objects and Django's FileResponse also accepts file-like objects.

- Take a look at <b>download_pdf</b> view in <b>shop</b> app.<br>

<b>Key Points:</b><br>

- A very important one is ```buffer.seek(0)```.<br>
After writing into the pdf, the pointer will no longer be at the beginning.<br>
To return the pdf file as a response, it needs to be read from the <b>beginning</b> of the file.<br>
Without calling ```buffer.seek(0)```, response will be corrupted or empty.<br>
(Try it yourself, comment out buffer.seek(0) and see if you can successfully download the file, and if you did manage to download the file, you'll notice that its size is 0 bytes and cannot be opened.)

- The filename parameter of FileResponse will automatically set the MIME type to application/pdf.

- as_attachment=True will add 'attachment' to Content-Disposition header, propmting the client to save the file.
