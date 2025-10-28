is

## 11.12 XML Syntax for Directives

## 11.12 XML Syntax for Directives

JSP permits you to use an alternative XML-compatible syntax for directives. These constructs take the following form:

&lt;jsp:directive. directiveType attribute =" value " /&gt;

For example, the XML equivalent of

&lt;%@ page import="java.util.*" %&gt;

&lt;jsp:directive.page import="java.util.*" /&gt;