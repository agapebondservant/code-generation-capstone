## Chapter 16 Using HTML Forms

## 16.2 The FORM Element

HTML forms allow you to create a set of data input elements associated with a particular URL. Each of these elements is typically given a name and has a value based on the original HTML or user input. When the form is submitted,  the  names and values of all active elements are collected into a string with = between each name and value and with &amp; between each name/value pair. This string is then transmitted to the URL designated by the FORM element. The string is either appended to the URL after a question mark or sent on a separate line after the HTTP request headers and a blank line, depending on whether GET or POST is used as the submission method. This section covers the FORM element itself, used primarily to designate the URL and to choose the submission method. The following sections cover the various user interface controls that can be used within forms.

HTML Element: &lt;FORM ACTION="URL" ...&gt; ... &lt;/FORM&gt; ,

Attributes: ACTION (required), METHOD , ENCTYPE , TARGET , ONSUBMIT ONRESET , ACCEPT , ACCEPT-CHARSET

The FORM element creates an area for data input elements and designates the URL to which any collected data will be transmitted. For example:

&lt;FORM ACTION="http://some.isp.com/servlet/SomeServlet"&gt; FORM input elements and regular HTML &lt;/FORM&gt;

The rest of this section explains the attributes that apply to the FORM element: ACTION , METHOD , ENCTYPE , TARGET , ONSUBMIT , ONRESET , ACCEPT , and ACCEPT-CHARSET . Note that I am not discussing attributes like STYLE , CLASS , and LANG that apply to general HTML elements, but only those that are specific to the FORM element.

## ACTION

The ACTION attribute specifies the URL of the servlet or CGI program that will process the FORM data (e.g., http://cgi.whitehouse.gov/ bin/schedule-fund-raiser ) or an email address where the FORM data will be sent (e.g., mailto:audit@irs.gov ). Some ISPs do not allow ordinary users to create servlets or CGI programs, or they charge extra for this privilege. In such a case, sending the data by email is a convenient option when you create pages that need to collect data but

## 16.2 The FORM Element

not return results (e.g., for accepting orders for products). You must use the POST method (see METHOD in the following subsection) when using a mailto URL.

## METHOD

The METHOD attribute specifies how the data will be transmitted to the HTTP server. When GET is used, the data is appended to the end of the designated URL after a question mark. For an example, see Section 16.1 (How HTML Forms Transmit Data). GET is the default and is also the method that is used when a browser requests a normal URL. When POST is used, the data is sent on a separate line.

The advantages of using the GET method are twofold: the method is simple; and with servlets that use GET , users can access those servlets for testing and debugging without creating a form, simply by entering a URL with the proper data appended. On the other hand, due to URL size restrictions on some browsers, GET requests have limits on the amount of data that can be appended, whereas POST requests do not. Another disadvantage of GET is that most browsers show the URL, including the attached data string, in an address field at the top of the browser. This display makes GET inappropriate for sending sensitive data if your computer is in a relatively public place.

## ENCTYPE

This attribute specifies the way in which the data will be encoded before being transmitted. The default is application/x-www-form-urlencoded , which means that the client converts each space into a plus sign (+) and every other nonalphanumeric character into a percent sign (%) followed by the two hexadecimal digits representing that character (e.g., in ASCII or ISO Latin-1). Those transformations are in addition to placing an equal sign ( = ) between entry names and values and an ampersand ( &amp; ) between entries.

For example, Figure 16-5 shows a version of the GetForm.html page (Listing 16.1) where ' Marty (Java Hacker?) ' is entered for the first name. As can be seen in Figure 16-6, this entry gets sent as ' Marty+%28Java+Hacker%3F%29 '. That's because spaces become plus signs, 28 is the ASCII value (in hex) for a left parenthesis, 3F is the ASCII value of a question mark, and 29 is a right parenthesis.

## Chapter 16 Using HTML Forms

Figure 16-5 Customized result of GetForm.html .

<!-- image -->

Figure 16-6 HTTP request sent by Internet Explorer 5.0 when submitting GetForm.html with the data shown in Figure 16-5.

<!-- image -->

## 16.2 The FORM Element

Most recent browsers support an additional ENCTYPE of multipart/ form-data . This encoding transmits each of the fields as separate parts of a MIME-compatible document and automatically uses POST to submit them. This encoding sometimes makes it easier for the server-side program to handle complex data and is required when using file upload controls to send entire documents (see Section 16.7). For example, Listing 16.3 shows a form that differs from GetForm.html (Listing 16.1) only in that

&lt;FORM ACTION="http://localhost:8088/SomeProgram"&gt;

## has been changed to

&lt;FORM ACTION="http://localhost:8088/SomeProgram" ENCTYPE="multipart/form-data"&gt;

Figures 16-7 and 16-8 show the results.

## Listing 16.3 MultipartForm.html

&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"&gt;

&lt;HTML&gt;

&lt;HEAD&gt;

&lt;TITLE&gt;Using ENCTYPE="multipart/form-data"&lt;/TITLE&gt; &lt;/HEAD&gt;

&lt;BODY BGCOLOR="#FDF5E6"&gt;

&lt;H2 ALIGN="CENTER"&gt;Using ENCTYPE="multipart/form-data"&lt;/H2&gt;

&lt;FORM ACTION="http://localhost:8088/SomeProgram"

## ENCTYPE="multipart/form-data" &gt;

&lt;CENTER&gt;

First name:

&lt;INPUT TYPE="TEXT" NAME="firstName" VALUE="Joe"&gt;&lt;BR&gt;

Last name:

&lt;INPUT TYPE="TEXT" NAME="lastName" VALUE="Hacker"&gt;&lt;P&gt;

&lt;INPUT TYPE="SUBMIT"&gt;

&lt;/CENTER&gt;

&lt;/FORM&gt;

&lt;/BODY&gt;

&lt;/HTML&gt;

## Chapter 16 Using HTML Forms

Figure 16-7 Initial result of MultipartForm.html .

<!-- image -->

HTTP request sent by Netscape 4.7 when submitting

<!-- image -->

Figure 16-8 MultipartForm.html .

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.