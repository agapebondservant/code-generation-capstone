## Chapter 11 The JSP page Directive: Structuring Generated Servlets

Servers can use a larger buffer than you specify, but not a smaller one. For example, &lt;%@  page  buffer="32kb"  %&gt; means  the  document  content should be buffered and not sent to the client until at least 32 kilobytes have been accumulated or the page is completed. The default buffer size is server specific, but must be at least 8 kilobytes. Be cautious about turning off buffering; doing so requires JSP entries that set headers or status codes to appear at the top of the file, before any HTML content.

## 11.6 The autoflush Attribute

The autoflush attribute controls whether the output buffer should be automatically  flushed  when  it  is  full  or  whether  an  exception  should  be  raised when the buffer overflows. Use of this attribute takes one of the following two forms:

```
<%@ page autoflush="true" %> <%-- Default --%> <%@ page autoflush="false" %>
```

A value of false is illegal when also using buffer="none" .

## 11.7 The extends Attribute

The extends attribute indicates the superclass of the servlet that will be generated for the JSP page and takes the following form:

&lt;%@ page extends=" package.class " %&gt;

Use this attribute with extreme caution since the server may be using a custom superclass already.

## 11.8 The info Attribute

The info attribute defines a string that can be retrieved from the servlet by means  of  the getServletInfo method.  Use  of info takes  the  following form:

&lt;%@ page info=" Some Message " %&gt;