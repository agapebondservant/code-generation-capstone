## Text Areas

- · Usual form:

&lt;TEXTAREA NAME="..." ROWS=xxx COLS=yyy&gt; ...

```
Some text
```

&lt;/TEXTAREA&gt;

- · Attributes: NAME (required), ROWS (required), COLS (required), WRAP (nonstandard), ONCHANGE , ONSELECT , ONFOCUS , ONBLUR , ONKEYDOWN , ONKEYPRESS , ONKEYUP
- · White space in initial text is maintained and HTML markup between start and end tags is taken literally, except for character entities such as &amp;lt; , &amp;copy; , and so forth.

## Submit Buttons

- · Usual form: &lt;INPUT TYPE="SUBMIT" ...&gt; (no end tag)
- · Attributes: NAME , VALUE , ONCLICK , ONDBLCLICK , ONFOCUS , ONBLUR
- · When a submit button is clicked, the form is sent to the servlet or other server-side program designated by the ACTION parameter of the FORM .

## Alternative Push Buttons

- · Usual form:

&lt;BUTTON TYPE="SUBMIT" ...&gt;

HTML Markup

- &lt;/BUTTON&gt;
- · Attributes: NAME , VALUE , ONCLICK , ONDBLCLICK , ONFOCUS , ONBLUR
- · Internet Explorer only.

## Reset Buttons

- · Usual form:

&lt;INPUT TYPE="RESET" ...&gt; (no end tag)

- · Attributes: VALUE , NAME , ONCLICK , ONDBLCLICK , ONFOCUS , ONBLUR Except for VALUE , attributes are only for use with JavaScript.

## Alternative Reset Buttons

- · Usual form:

&lt;BUTTON TYPE="RESET" ...&gt; HTML Markup &lt;/BUTTON&gt;

- · Attributes: VALUE , NAME , ONCLICK , ONDBLCLICK , ONFOCUS , ONBLUR
- · Internet Explorer only.

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## A.16 Using HTML Forms