## How to create CSV output

To output CSV using django, you can use either python csv library or django template system.

### 1. Using Python CSV library
Python's standard library comes with a csv module that allows for working with csv files.

- First, set up an app and basic urls.
- Then we add a view to return an CSV file as response (index view)

Notable points:
- In index view, we create a django <b>HttpResponse</b> object.<br><b>content_type</b> header is set to '<b>text/csv</b>'.<br>
It indicates the format of the document provided by the current url.<br>
Should be set a [MIME Type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/MIME_types), e.g. text/csv.

- [Content-Disposition](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Disposition)</b>.<br>
Header that tells the browser how to proceed with the content of the response.<br>
Set to '<b>attachment</b>' to indicate that this file should be downloaded.

- The <b>writer()</b> function from python's csv module expects a file-like object (any file-like object that implements <b>write()</b> method).<br><b>io</b> module uses this method to write data into an object (a file, buffer or stream).<br>

- The <b>writerow.writer()</b> function object accepts a row (An iterable of strings/numbers).

- If the content you're writing into the file contains characters such as quote or double quotes, there is no need for manually escaping them.

### 2. Large CSV outputs
In case of larger csv outputs, it is recommended to use <b>StreamingHttpResponse</b> to prevent load balancers from dropping a timed-out connection when server was trying to generate the response.

- Take a look at <b>stream_csv</b> view.
- Client will receive the file chunk by chunk and write it into the disk (as a temp file at first) in the correct order.

### 3. Using django's template system
This approach will pass a list of items to template and renders it.<br>
Django's official Howto uses txt file (other <b>text-based</b> formats are also acceptable).<br>
- Look at template_csv view.
- I also attempted to try other formats.
- One important thing here is the rendering of special characters such as a quote character.<br>
In these cases, you can either use the <b>|addslashes</b> template flag or if you know that your data is safe you can turn off the autoescape (or use the <b>|safe</b> flag)
