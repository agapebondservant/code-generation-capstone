## XML Syntax

- · Usual syntax:

&lt;%@ page attribute =" value " %&gt; &lt;%@ page import="java.util.*" %&gt;

- · XML equivalent:

&lt;jsp:directive.page attribute =" value " /&gt; &lt;jsp:directive.page import="java.util.*" /&gt;

## A.12Including Files and Applets in JSP Documents

## Including Files at Page Translation Time

- · &lt;%@ include file="Relative URL" %&gt;
- · Changing included file does not necessarily cause retranslation of JSP document. You have to manually change JSP document or update its modification date. Convenient way:

&lt;%-- Navbar.jsp modified 3/1/00 --%&gt;

&lt;%@ include file="Navbar.jsp" %&gt;

## Including Files at Request Time

- · &lt;jsp:include page="Relative URL" flush="true" /&gt;
- · Servlets can use include method of RequestDispatcher to accomplish similar result. See Section 15.3.
- · Because of a bug, you must use .html or .htm extensions for included files used with the Java Web Server.

## Applets for the Java Plug-In: Simple Case

- · Regular form:

&lt;APPLET CODE="MyApplet.class" WIDTH=475 HEIGHT=350&gt;

&lt;/APPLET&gt;

- · JSP form for Java Plug-in:

&lt;jsp:plugin type="applet"

code="MyApplet.class"

width="475" height="350"&gt;

&lt;/jsp:plugin&gt;

## Attributes of jsp:plugin

All  attribute  names  are  case  sensitive;  all  attribute  values  require  single  or double quotes.

- · type : for applets, this attribute should have a value of applet .

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## A.12 Including Files and Applets in JSP Documents