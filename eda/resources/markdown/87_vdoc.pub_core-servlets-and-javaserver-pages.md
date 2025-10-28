## Chapter 10 JSP Scripting Elements

## 10.3 JSP Scriptlets

If you want to do something more complex than insert a simple expression, JSP  scriptlets  let  you  insert  arbitrary  code  into  the  servlet's \_jspService method (which is called by service ). Scriptlets have the following form:

&lt;% Java Code %&gt;

Scriptlets  have  access  to  the  same  automatically  defined  variables  as expressions ( request , response , session , out ,  etc.; see Section 10.5). So, for example, if you want output to appear in the resultant page, you would use the out variable, as in the following example.

&lt;% String queryData = request.getQueryString(); out.println("Attached GET data: " + queryData); %&gt;

In this particular instance, you could have accomplished the same effect more easily by using the following JSP expression:

Attached GET data: &lt;%= request.getQueryString() %&gt;

In general, however, scriptlets can perform a number of tasks that cannot be accomplished with expressions alone. These tasks include setting response headers and status codes, invoking side effects such as writing to the server log or updating a database, or executing code that contains loops, conditionals, or other complex constructs. For instance, the following snippet specifies that the current page is sent to the client as plain text, not as HTML (which is the default).

&lt;% response.setContentType("text/plain"); %&gt;

It is important to note that you can set response headers or status codes at various places within a JSP page, even though this capability appears to violate the rule that this type of response data needs to be specified before any document content is sent to the client. Setting headers and status codes is permitted because servlets that result from JSP pages use a special type of PrintWriter (of  the  more  specific  class JspWriter )  that  buffers  the document before sending it. This buffering behavior can be changed, however; see Section  11.6  for  a discussion  of  the autoflush attribute  of  the page directive.

## 10.3 JSP Scriptlets

As an example of executing code that is too complex for a JSP expression, Listing 10.2 presents a JSP page that uses the bgColor request parameter to set  the  background  color  of  the  page.  Some  results  are  shown  in  Figures 10-2, 10-3, and 10-4.

```
Listing 10.2 BGColor.jsp <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"> <HTML> <HEAD> <TITLE>Color Testing</TITLE> </HEAD> <% String bgColor = request.getParameter("bgColor"); boolean hasExplicitColor; if (bgColor != null) { hasExplicitColor = true; } else { hasExplicitColor = false; bgColor = "WHITE"; } %> <BODY BGCOLOR=" <%= bgColor %> "> <H2 ALIGN="CENTER">Color Testing</H2> <% if (hasExplicitColor) { out.println("You supplied an explicit background color of " + bgColor + "."); } else { out.println("Using default background color of WHITE. " + "Supply the bgColor request attribute to try " + "a standard color, an RRGGBB value, or to see " + "if your browser supports X11 color names."); } %> </BODY> </HTML>
```

## Chapter 10 JSP Scripting Elements

Figure 10-2 Default result of BGColor.jsp .

<!-- image -->

Figure 10-3 Result of BGColor.jsp when accessed with a bgColor parameter having the RGB value C0C0C0 .

<!-- image -->

## 10.3 JSP Scriptlets

Figure 10-4 Result of BGColor.jsp when accessed with a bgColor parameter having the X11 color value papayawhip .

<!-- image -->

## Using Scriptlets to Make Parts of the JSP File Conditional

Another use of scriptlets is to conditionally include standard HTML and JSP constructs. The key to this approach is the fact that code inside a scriptlet gets  inserted  into  the  resultant  servlet's \_jspService method  (called  by service ) exactly as written, and any static HTML (template text) before or after a scriptlet gets converted to print statements. This means that scriptlets  need  not  contain  complete  Java  statements,  and  blocks  left  open  can affect the static  HTML or JSP outside of the scriptlets. For example, consider the following JSP fragment containing mixed template text and scriptlets.

```
<% if (Math.random() < 0.5) { %> Have a <B>nice</B> day! <% } else { %> Have a <B>lousy</B> day! <% } %>
```