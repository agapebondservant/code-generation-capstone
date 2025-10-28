## Appendix A Servlet and JSP Quick Reference

## · application

Means that, in addition to being bound to a local variable, bean will be stored in shared ServletContext available through predefined application variable or by a call to getServletContext() .

## · session

Means that, in addition to being bound to a local variable, bean will be stored in HttpSession object associated with current request, where it can be retrieved with getValue .

## · request

Signifies that, in addition to being bound to a local variable, bean object should be placed in ServletRequest object for duration of current request, where it is available by means of the getAttribute method.

## Conditional Bean Creation

- · A jsp:useBean element results in a new bean being instantiated only if no bean with the same id and scope can be found. If a bean with the same id and scope is found, the preexisting bean is simply bound to the variable referenced by id .
- · You can make jsp:setProperty statements conditional on new bean creation:

&lt;jsp:useBean ...&gt; statements &lt;/jsp:useBean&gt;

## A.14 Creating Custom JSP Tag Libraries

## The Tag Handler Class

- · Implement Tag interface by extending TagSupport (no tag body or tag body included verbatim) or BodyTagSupport (tag body is manipulated).
- · doStartTag : code to run at beginning of tag
- · doEndTag : code to run at end of tag
- · doAfterBody : code to process tag body