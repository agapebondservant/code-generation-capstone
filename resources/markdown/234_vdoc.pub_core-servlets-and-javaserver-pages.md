## A.13 Using JavaBeans with JSP

code="MyApplet.class"

width="475" height="350"&gt;

## &lt;jsp:fallback&gt;

&lt;B&gt;Error: this example requires Java.&lt;/B&gt; &lt;/jsp:fallback&gt;

&lt;/jsp:plugin&gt;

- · The Java Web Server does not properly handle jsp:fallback .

## A.13 Using JavaBeans with JSP

## Basic Requirements for Class to be a Bean

- 1. Have a zero-argument (empty) constructor.
- 2. Have no public instance variables (fields).
- 3. Access persistent values through methods called get Xxx (or is Xxx ) and set Xxx .

## Basic Bean Use

- · &lt;jsp:useBean id="name" class="package.Class" /&gt;
- · &lt;jsp:getProperty name="name" property="property" /&gt;
- · &lt;jsp:setProperty name="name" property="property" value="value" /&gt;

The value attribute can take a JSP expression.

## Associating Properties with Request Parameters

- · Individual properties:
- · Automatic type conversion: for primitive types, performed according to valueOf method of wrapper class.
- · All properties:

&lt;jsp:setProperty

name="entry"

property="numItems"

param="numItems" /&gt;

&lt;jsp:setProperty name="entry" property="*" /&gt;

## Sharing Beans: The scope Attribute of jsp:useBean

Examples of sharing beans given in Chapter 15.

- · page

Default value. Indicates that, in addition to being bound to a local variable, bean object should be placed in PageContext object for duration of current request.

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.