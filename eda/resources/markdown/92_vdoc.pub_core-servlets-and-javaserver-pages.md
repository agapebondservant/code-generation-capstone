## 11.2 The contentType Attribute

Figure 11-1 ImportAttribute.jsp when first accessed.

<!-- image -->

Figure 11-2 ImportAttribute.jsp when accessed in a subsequent visit.

<!-- image -->

## 11.2 The contentType Attribute

The contentType attribute sets the Content-Type response header, indicating the MIME type of the document being sent to the client. For more information on MIME types, see Table 7.1 (Common MIME Types) in Section 7.2 (HTTP 1.1 Response Headers and Their Meaning).

<!-- image -->

## Chapter 11 The JSP page Directive: Structuring Generated Servlets

Use of the contentType attribute takes one of the following two forms:

&lt;%@ page contentType="MIME-Type" %&gt;

&lt;%@ page contentType="MIME-Type; charset=Character-Set" %&gt;

For example, the directive

&lt;%@ page contentType="text/plain" %&gt;

has the same effect as the scriptlet

&lt;% response.setContentType("text/plain"); %&gt;

Unlike regular servlets, where the default MIME type is text/plain , the default for JSP  pages  is text/html (with a default character set of ISO-8859-1 ).

## Generating Plain Text Documents

Listing 11.2 shows a document that appears to be HTML but has a contentType of text/plain . Strictly speaking, browsers are supposed to display the raw  HTML content in such a case, as shown in Netscape in Figure 11-3. Internet  Explorer,  however,  interprets  the  document  as  though  it  were  of type text/html , as shown in Figure 11-4.

## Listing 11.2 ContentType.jsp

&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"&gt; &lt;HTML&gt; &lt;HEAD&gt; &lt;TITLE&gt;The contentType Attribute&lt;/TITLE&gt; &lt;/HEAD&gt; &lt;BODY&gt; &lt;H2&gt;The contentType Attribute&lt;/H2&gt; &lt;%@ page contentType="text/plain" %&gt; This should be rendered as plain text, &lt;B&gt;not&lt;/B&gt; as HTML. &lt;/BODY&gt; &lt;/HTML&gt;

## 11.2 The contentType Attribute

<!-- image -->

Figure 11-3 For plain text documents, Netscape does not try to interpret HTML tags.

<!-- image -->

Figure 11-4 Internet Explorer interprets HTML tags in plain text documents.

<!-- image -->

Chapter 11 The JSP page Directive: Structuring Generated Servlets

## Generating Excel Spreadsheets

You can create simple Microsoft Excel spreadsheets by specifying application/vnd.ms-excel as  the  content  type  and  then  formatting  the  spreadsheet entries in one of two ways.

One way to format the content is to put rows on separate lines of the document and to use tabs between each of the columns. Listing 11.3 shows a simple example, and Figures 11-5 and 11-6 show the results of loading the page in Netscape on a system with Excel installed. Of course, in a real application, the  entries  would  probably  be  generated  dynamically,  perhaps  by  a  JSP expression or scriptlet that refers to database values that were accessed with JDBC (see Chapter 18).

## Listing 11.3 Excel.jsp

```
<%@ page contentType="application/vnd.ms-excel" %> <%-- Note that there are tabs, not spaces, between columns. --%> 1997 1998 1999 2000 2001 (Anticipated) 12.3 13.4 14.5 15.6 16.7
```

Figure 11-5 With the default browser settings, Netscape prompts you before allowing Excel content.

<!-- image -->

## 11.2 The contentType Attribute

Figure 11-6 Result of Excel.jsp on system that has Excel installed.

<!-- image -->

A second way to format Excel content is to use a normal HTML table, which recent versions of Excel can interpret properly as long as the page is marked  with  the  proper  MIME  type.  This  capability  suggests  a  simple method of returning either HTML or Excel content, depending on which the  user  prefers:  just  use  an  HTML  table  and  set  the  content  type  to application/vnd.ms-excel only if the user requests the results in Excel. Unfortunately, this approach brings to light a small deficiency in the page directive:  attribute  values cannot be computed at run time, nor can page directives be conditionally inserted as can template text. So, the following attempt results in Excel content regardless of the result of the checkUserRequest method.

```
<% boolean usingExcel = checkUserRequest(request); %> <% if (usingExcel) { %> <%@ page contentType="application/vnd.ms-excel" %> <% } %>
```

Fortunately, there is a simple solution to the problem of conditionally setting the content type: just use scriptlets and the normal servlet approach of response.setContentType , as in the following snippet:

```
<% String format = request.getParameter("format"); if ((format != null) && (format.equals("excel"))) { response.setContentType("application/vnd.ms-excel"); } %>
```

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## Chapter 11 The JSP page Directive: Structuring Generated Servlets

Listing 11.4 shows a page that uses this approach; Figures 11-7 and 11-8 show  the  results  in  Internet  Explorer.  Again,  in  a  real  application  the  data would almost  certainly  be  dynamically  generated.  For  example,  see  Section 18.3 (Some JDBC Utilities) for some very simple methods to create an HTML table (usable in HTML or as an Excel spreadsheet) from a database query.

```
Listing 11.4 ApplesAndOranges.jsp <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"> <HTML> <HEAD> <TITLE>Comparing Apples and Oranges</TITLE> <LINK REL=STYLESHEET HREF="JSP-Styles.css" TYPE="text/css"> </HEAD> <BODY> <CENTER> <H2>Comparing Apples and Oranges</H2> <% String format = request.getParameter("format"); if ((format != null) && (format.equals("excel"))) { response.setContentType("application/vnd.ms-excel"); } %> <TABLE BORDER=1> <TR><TH></TH><TH>Apples<TH>Oranges <TR><TH>First Quarter<TD>2307<TD>4706 <TR><TH>Second Quarter<TD>2982<TD>5104 <TR><TH>Third Quarter<TD>3011<TD>5220 <TR><TH>Fourth Quarter<TD>3055<TD>5287 </TABLE> </CENTER> </BODY> </HTML>
```

## 11.2 The contentType Attribute

<!-- image -->

Figure 11-7 The default result of ApplesAndOranges.jsp is HTML content.

<!-- image -->

Figure 11-8 Specifying format=excel for ApplesAndOranges.jsp results in Excel content.

<!-- image -->