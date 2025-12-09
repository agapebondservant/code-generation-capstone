' Prentice Hall and Sun Microsystems. Personal use only; do not redistribute.

## Chapter The JSP page Directive: Structuring Generated Servlets

<!-- image -->

## Topics in This Chapter

- · The purpose of the page directive
- · Designating which classes are imported
- · Using custom classes
- · Specifying the MIME type of the page
- · Generating Excel documents
- · Controlling threading behavior
- · Participating in sessions
- · Setting the size and behavior of the output buffer
- · Designating pages to process JSP errors
- · XML-compatible syntax for directives

Home page for this book: http://www.coreservlets.com.

Home page for sequel: http://www.moreservlets.com.

Servlet and JSP training courses: http://courses.coreservlets.com.

<!-- image -->

JSP directive affects the overall structure of the servlet that results from the JSP page. The following templates show the two possible forms for directives. Single quotes can be substituted for the double quotes around the attribute values, but the quotation marks cannot be omitted  altogether.  To  obtain  quote  marks  within  an  attribute  value,  precede them with a back slash, using \' for ' and \" for " . A

```
<%@ directive attribute="value" %> <%@ directive attribute1="value1" attribute2="value2" ... attribute N ="value N " %>
```

In  JSP,  there  are  three  types  of  directives: page , include ,  and taglib . The page directive lets you control the structure of the servlet by importing classes, customizing the servlet superclass, setting the content type, and the like. A page directive can be placed anywhere within the document; its use is the topic of this chapter. The second directive, include , lets you insert a file into the servlet class at the time the JSP file is translated into a servlet. An include directive should be placed in the document at the point at which you want the file to be inserted; it is discussed in Chapter 12 (Including Files and Applets  in JSP  Documents) for inserting files into  JSP pages. JSP  1.1 introduces  a  third  directive, taglib ,  which  can  be  used  to  define  custom