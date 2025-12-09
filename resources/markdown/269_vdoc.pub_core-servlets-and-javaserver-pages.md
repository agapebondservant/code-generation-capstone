## A.17 Using Applets As Servlet Front Ends

## File Upload Controls

- · Usual form:
- &lt;INPUT TYPE="FILE" ...&gt; (no end tag)
- · Attributes: NAME (required), VALUE (ignored), SIZE , MAXLENGTH , ACCEPT , ONCHANGE , ONSELECT , ONFOCUS , ONBLUR (nonstandard)
- · Use an ENCTYPE of multipart/form-data in the FORM declaration.

## Server-Side Image Maps

- · Usual form:
- &lt;INPUT TYPE="IMAGE" ...&gt; (no end tag)
- · Attributes: NAME (required), SRC , ALIGN
- · You can also provide an ISMAP attribute to a standard IMG element that is inside an &lt;A HREF...&gt; element.

## Hidden Fields

- · Usual form:
- &lt;INPUT TYPE="HIDDEN" NAME="..." VALUE="..."&gt; (no end tag)
- · Attributes: NAME (required), VALUE

## Internet Explorer Features

- · FIELDSET (with LEGEND): groups controls
- · TABINDEX : controls tabbing order
- · Both capabilities are part of HTML 4.0 spec; neither is supported by Netscape 4.

## A.17 Using Applets As Servlet Front Ends

## Sending Data with GET and Displaying the Resultant Page

```
String someData = name1 + "=" + URLEncoder.encode(val1) + "&" + name2 + "=" + URLEncoder.encode(val2) + "&" + ... nameN + "=" + URLEncoder.encode(valN); try { URL programURL = new URL(baseURL + "?" + someData); getAppletContext().showDocument(programURL); } catch(MalformedURLException mue) { ... }
```

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

<!-- image -->