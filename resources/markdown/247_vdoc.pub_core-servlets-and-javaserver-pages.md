## Appendix A Servlet and JSP Quick Reference

## Optionally Including the Tag Body

- · Tag handler :

Return EVAL\_BODY\_INCLUDE or SKIP\_BODY at different times, depending on value of request time parameter.

## Manipulating the Tag Body

- · Tag handler :

You should extend BodyTagSupport , implement doAfterBody . Call getBodyContent to get BodyContent object describing tag body. BodyContent has three key methods: getEnclosingWriter , getReader , and getString . Return SKIP\_BODY from doAfterBody .

## Including or Manipulating the Tag Body Multiple Times

- · Tag handler :

To process body again, return EVAL\_BODY\_TAG from doAfterBody . To finish, return SKIP\_BODY .

## Using Nested Tags

- · Tag handler :

Nested tags can use findAncestorWithClass to find the tag in which they are nested. Place data in field of enclosing tag.

- · Tag Library Descriptor:

Declare all tags separately, regardless of nesting structure in real page.

## A.15 Integrating Servlets and JSP

## Big Picture

- · Servlet handles initial request, reads parameters, cookies, session information, etc.
- · Servlet then does whatever computations and database lookups are needed.
- · Servlet then stores data in beans.
- · Servlet forwards request to one of many possible JSP pages to present final result.
- · JSP page extracts needed values from beans.