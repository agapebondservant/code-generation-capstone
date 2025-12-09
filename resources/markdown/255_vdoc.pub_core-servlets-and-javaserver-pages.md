## Appendix A Servlet and JSP Quick Reference

## Including Static or Dynamic Content

- · Basic usage:

response.setContentType("text/html"); PrintWriter out = response.getWriter(); out.println("..."); RequestDispatcher dispatcher = getServletContext().getRequestDispatcher("/path/resource"); dispatcher.include(request, response); out.println("...");

- · JSP equivalent is jsp:include , not the JSP include directive.

## Forwarding Requests from JSP Pages

- · &lt;jsp:forward page="Relative URL" /&gt;

## A.16 Using HTML Forms

## The FORM Element

- · Usual form:

&lt;FORM ACTION="URL" ...&gt; ... &lt;/FORM&gt;

- · Attributes: ACTION (required), METHOD , ENCTYPE , TARGET , ONSUBMIT , ONRESET , ACCEPT , ACCEPT-CHARSET

## Textfields

- · Usual form: &lt;INPUT TYPE="TEXT" NAME="..." ...&gt;

(no end tag)

- · Attributes: NAME (required), VALUE , SIZE , MAXLENGTH , ONCHANGE , ONSELECT , ONFOCUS , ONBLUR , ONKEYDOWN , ONKEYPRESS , ONKEYUP
- · Different browsers have different rules regarding the situations where pressing Enter in a textfield submits the form. So, include a button or image map that submits the form explicitly.

## Password Fields

- · Usual form: &lt;INPUT TYPE="PASSWORD" NAME="..." ...&gt; (no end tag)
- · Attributes: NAME (required), VALUE , SIZE , MAXLENGTH , ONCHANGE , ONSELECT , ONFOCUS , ONBLUR , ONKEYDOWN , ONKEYPRESS , ONKEYUP
- · Always use POST with forms that contain password fields.

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.