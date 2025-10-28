## Appendix A Servlet and JSP Quick Reference

## JavaScript Buttons

- · Usual form:

&lt;INPUT TYPE="BUTTON" ...&gt; (no end tag)

- · Attributes: NAME , VALUE , ONCLICK , ONDBLCLICK , ONFOCUS , ONBLUR

## Alternative JavaScript Buttons

- · Usual form:
- &lt;/BUTTON&gt;
- · Attributes: NAME , VALUE , ONCLICK , ONDBLCLICK , ONFOCUS , ONBLUR
- · Internet Explorer only.

```
<BUTTON TYPE="BUTTON" ...> HTML Markup
```

## Check Boxes

- · Usual form:

&lt;INPUT TYPE="CHECKBOX" NAME="..." ...&gt; (no end tag)

- · Attributes: NAME (required), VALUE , CHECKED , ONCLICK , ONFOCUS , ONBLUR
- · Name/value transmitted only if check box is checked.

## Radio Buttons

- · Usual form: &lt;INPUT TYPE="RADIO" NAME="..." VALUE="..." ...&gt;

(no end tag)

- · Attributes: NAME (required), VALUE (required), CHECKED , ONCLICK , ONFOCUS , ONBLUR
- · You indicate a group of radio buttons by providing all of them with the same NAME .

## Combo Boxes

- · Usual form:
- &lt;/SELECT&gt;
- · SELECT Attributes: NAME (required), SIZE , MULTIPLE , ONCLICK , ONFOCUS , ONBLUR , ONCHANGE

```
<SELECT NAME="Name" ...>
```

```
<OPTION VALUE="Value1">Choice 1 Text <OPTION VALUE="Value2">Choice 2 Text ... <OPTION VALUE="ValueN">Choice N Text
```

VALUE

- · OPTION Attributes: SELECTED ,

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.