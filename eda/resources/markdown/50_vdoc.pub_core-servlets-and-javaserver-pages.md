## Chapter 3 Handling the Client Request: Form Data

Figure 3-2 Output of ThreeParams servlet.

<!-- image -->

## 3.4 Example: Reading All Parameters

The previous example extracted parameter values from the form data based upon  prespecified  parameter  names.  It  also  assumed  that  each  parameter had  exactly  one  value.  Here's  an  example  that  looks  up all the  parameter names that are sent and puts their values in a table. It highlights parameters that have missing values as well as ones that have multiple values.

First, the servlet looks up all the parameter names by the getParameterNames method of HttpServletRequest . This method returns an Enumeration that  contains  the  parameter  names  in  an  unspecified  order.  Next,  the servlet  loops  down  the Enumeration in  the  standard  manner,  using hasMoreElements to  determine  when to  stop and  using nextElement to  get each entry. Since nextElement returns an Object , the servlet casts the result to a String and passes that to getParameterValues ,  yielding an array of strings. If that array is one entry long and contains only an empty string, then the parameter had no values and the servlet generates an italicized 'No Value' entry. If the array is more than one entry long, then the parameter had multiple values and the values are displayed in a bulleted list. Otherwise, the one main value is placed into the table unmodified. The source code for the servlet is shown in Listing 3.3, while Listing 3.4 shows the HTML code for a front end that can be used to try the servlet out. Figures 3-3 and 3-4 show the result of the HTML front end and the servlet, respectively.

## 3.4 Example: Reading All Parameters

Notice  that  the  servlet  uses  a doPost method  that  simply  calls doGet . That's because I want it to be able to handle both GET and POST requests. This approach is a good standard practice if you want HTML interfaces to have some flexibility in how they send data to the servlet. See the discussion of the service method in Section 2.6 (The Servlet Life Cycle) for a discussion of why having doPost call doGet (or vice versa) is preferable to overriding service directly.  The  HTML  form  from  Listing  3.4  uses POST ,  as should all forms  that  have  password  fields  (if  you  don't  know  why,  see Chapter 16). However, the ShowParameters servlet is not specific to that particular  front  end,  so  the  source  code  archive  site  at www.coreservlets.com includes a similar HTML form that uses GET for you to experiment with.

## Listing 3.3 ShowParameters.java

```
package coreservlets; import java.io.*; import javax.servlet.*; import javax.servlet.http.*; import java.util.*; public class ShowParameters extends HttpServlet { public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException { response.setContentType("text/html"); PrintWriter out = response.getWriter(); String title = "Reading All Request Parameters"; out.println(ServletUtilities.headWithTitle(title) + "<BODY BGCOLOR=\"#FDF5E6\">\n" + "<H1 ALIGN=CENTER>" + title + "</H1>\n" + "<TABLE BORDER=1 ALIGN=CENTER>\n" + "<TR BGCOLOR=\"#FFAD00\">\n" + "<TH>Parameter Name<TH>Parameter Value(s)"); Enumeration paramNames = request.getParameterNames() ; while(paramNames.hasMoreElements()) { String paramName = (String)paramNames.nextElement(); out.print("<TR><TD>" + paramName + "\n<TD>"); String[] paramValues = request.getParameterValues(paramName) ; if (paramValues.length == 1) { String paramValue = paramValues[0]; if (paramValue.length() == 0) out.println("<I>No Value</I>");
```

## 72

## Chapter 3 Handling the Client Request: Form Data

## else out.println(paramValue); } else { out.println("&lt;UL&gt;"); for(int i=0; i&lt;paramValues.length; i++) { out.println("&lt;LI&gt;" + paramValues[i]); } out.println("&lt;/UL&gt;"); } } out.println("&lt;/TABLE&gt;\n&lt;/BODY&gt;&lt;/HTML&gt;"); } public void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException { doGet(request, response); } } Listing 3.3 ShowParameters.java (continued)

## Listing 3.4 ShowParametersPostForm.html

&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"&gt; &lt;HTML&gt; &lt;HEAD&gt; &lt;TITLE&gt;A Sample FORM using POST&lt;/TITLE&gt; &lt;/HEAD&gt; &lt;BODY BGCOLOR="#FDF5E6"&gt; &lt;H1 ALIGN="CENTER"&gt;A Sample FORM using POST&lt;/H1&gt; &lt;FORM ACTION="/servlet/coreservlets.ShowParameters" METHOD="POST" &gt; Item Number: &lt;INPUT TYPE="TEXT" NAME="itemNum"&gt;&lt;BR&gt; Quantity: &lt;INPUT TYPE="TEXT" NAME="quantity"&gt;&lt;BR&gt; Price Each: &lt;INPUT TYPE="TEXT" NAME="price" VALUE="$"&gt;&lt;BR&gt; &lt;HR&gt; First Name: &lt;INPUT TYPE="TEXT" NAME="firstName"&gt;&lt;BR&gt; Last Name: &lt;INPUT TYPE="TEXT" NAME="lastName"&gt;&lt;BR&gt; Middle Initial: &lt;INPUT TYPE="TEXT" NAME="initial"&gt;&lt;BR&gt; Shipping Address: &lt;TEXTAREA NAME="address" ROWS=3 COLS=40&gt;&lt;/TEXTAREA&gt;&lt;BR&gt; Credit Card:&lt;BR&gt; &amp;nbsp;&amp;nbsp;&lt;INPUT TYPE="RADIO" NAME="cardType" VALUE="Visa"&gt;Visa&lt;BR&gt; &amp;nbsp;&amp;nbsp;&lt;INPUT TYPE="RADIO" NAME="cardType" VALUE="Master Card"&gt;Master Card&lt;BR&gt;

## 3.4 Example: Reading All Parameters

## Listing 3.4 ShowParametersPostForm.html (continued)

```
&nbsp;&nbsp;<INPUT TYPE="RADIO" NAME="cardType" VALUE="Amex">American Express<BR> &nbsp;&nbsp;<INPUT TYPE="RADIO" NAME="cardType" VALUE="Discover">Discover<BR> &nbsp;&nbsp;<INPUT TYPE="RADIO" NAME="cardType" VALUE="Java SmartCard">Java SmartCard<BR> Credit Card Number: <INPUT TYPE="PASSWORD" NAME="cardNum"><BR> Repeat Credit Card Number: <INPUT TYPE="PASSWORD" NAME="cardNum"><BR><BR> <CENTER> <INPUT TYPE="SUBMIT" VALUE="Submit Order"> </CENTER>
```

&lt;/FORM&gt;

&lt;/BODY&gt;

&lt;/HTML&gt;

Figure 3-3 HTML front end that collects data for ShowParameters servlet.

<!-- image -->

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.