## Appendix A Servlet and JSP Quick Reference

## Example Form

## ThreeParamsForm.html

&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"&gt;

&lt;HTML&gt;

&lt;HEAD&gt;

&lt;TITLE&gt;Collecting Three Parameters&lt;/TITLE&gt;

&lt;/HEAD&gt;

&lt;BODY BGCOLOR="#FDF5E6"&gt;

&lt;H1 ALIGN="CENTER"&gt;Collecting Three Parameters&lt;/H1&gt;

&lt;FORM ACTION="/servlet/coreservlets.ThreeParams" &gt;

First Parameter:  &lt;INPUT TYPE="TEXT"

NAME="param1" &gt;&lt;BR&gt;

Second Parameter: &lt;INPUT TYPE="TEXT"

NAME="param2" &gt;&lt;BR&gt;

Third Parameter:  &lt;INPUT TYPE="TEXT"

NAME="param3" &gt;&lt;BR&gt;

&lt;CENTER&gt;

&lt;INPUT TYPE="SUBMIT"&gt;

&lt;/CENTER&gt;

&lt;/FORM&gt;

&lt;/BODY&gt;

&lt;/HTML&gt;

## Filtering HTML-Specific Characters

- · Must replace &lt; , &gt; , " , &amp; with &amp;lt; , &amp;gt; , &amp;quot; , and &amp;amp; . Use ServletUtilities.filter(htmlString) for this substitution. See Section 3.6.

## A.4 Handling the Client Request: HTTP Request Headers

## Methods That Read Request Headers

These are all methods in HttpServletRequest .

- · public String getHeader(String headerName) Returns value of an arbitrary header. Returns null if header not in request.
- · public Enumeration getHeaders(String headerName) Returns values of all occurrences of header in request. 2.2 only.
- · public Enumeration getHeaderNames() Returns names of all headers in current request.

•

public long getDateHeader(String headerName)

Reads header that represents a date and converts it to Java date format (milliseconds since 1970).

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.