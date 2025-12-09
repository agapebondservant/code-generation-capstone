<!-- image -->

his chapter discusses using HTML forms as front ends to servlets or other server-side programs. These forms provide simple and reliable user interface controls to collect data from the user and transmit it to the servlet. The following chapter discusses the use of applets as servlet front ends. Using applets in this role requires considerably more effort and has some security limitations. However, it permits a much richer user interface and can support significantly more efficient and flexible network communication. T

To use forms, you'll need to know where to place regular HTML files in order to make them accessible to the Web server. This location varies from server to server, but with the JSWDK and Tomcat, you place an HTML file in install\_dir /webpages/path/file.html and then access it via http://localhost/path/file.html (replace localhost with  the  real hostname if running remotely).

## 16.1 How HTML Forms Transmit Data

HTML forms let  you  create  a  variety  of  user  interface  controls  to  collect input on a Web page. Each of the controls typically has a name and a value, where the name is specified in the HTML and the value comes either from the HTML or by means of user input. The entire form is associated with the

## Chapter 16 Using HTML Forms

URL of a program that will process the data, and when the user submits the form (usually by pressing a button), the names and values of the controls are sent to the designated URL as a string of the form

Name1=Value1&amp;Name2=Value2...Name N =Value N

This string can be sent to the designated program in one of two ways. The first, which uses the HTTP GET method, appends the string to the end of the specified URL, after a question mark. The second way data can be sent is by the  HTTP POST method.  Here,  the POST request  line,  the  HTTP  request headers, and a blank line are first sent to the server, and then the data string is sent on the following line.

For example,  Listing 16.1 (HTML code) and Figure 16-1 (typical result) show a simple form with two textfields. The HTML elements that make up this form are discussed in detail in the rest of this chapter, but for now note a couple of things. First, observe that one text field has a name of firstName and the other has a name of lastName . Second, note that the GUI controls are considered text-level (inline) elements, so you need to use explicit HTML formatting to make sure that the controls appear next to the text describing them. Finally, notice  that  the FORM element  designates http://localhost:8088/SomeProgram as the URL to which the data will be sent.

Before submitting the form, I start a server program called EchoServer on port 8088 of my local machine. EchoServer , shown in Section 16.12, is a mini 'Web server' used for debugging. No matter what URL is specified and what data is sent to it, it merely returns a Web page showing all the HTTP information sent by the browser. As shown in Figure 16-2, when the form is submitted  with Joe in  the  first  textfield  and Hacker in  the  second,  the browser simply requests the URL http://localhost:8088/SomeProgram?firstName=Joe&amp;lastName=Hacker .  Listing  16.2  (HTML  code) and Figure 16-3 (typical result) show a variation that uses POST instead  of GET .  As  shown in Figure 16-4, submitting the form with textfield values of Joe and Hacker results  in  the  line firstName=Joe&amp;lastName=Hacker being sent to the browser on a separate line after the HTTP request headers and a blank line.

That's  the  general  idea  behind  HTML  forms:  GUI  controls  gather  data from the user, each control has a name and a value, and a string containing all the  name/value  pairs  is  sent  to  the  server  when  the  form  is  submitted. Extracting the names and values on the server is straightforward in servlets: that was covered in Chapter 3 (Handling the Client Request: Form Data). The remainder of this chapter covers options in setting up forms and the various GUI controls you can put in them.

## Listing 16.1 GetForm.html

```
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"> <HTML> <HEAD> <TITLE>A Sample Form Using GET</TITLE> </HEAD> <BODY BGCOLOR="#FDF5E6"> <H2 ALIGN="CENTER">A Sample Form Using GET</H2> <FORM ACTION="http://localhost:8088/SomeProgram"> <CENTER> First name: <INPUT TYPE="TEXT" NAME="firstName" VALUE="Joe"><BR> Last name: <INPUT TYPE="TEXT" NAME="lastName" VALUE="Hacker"><P> <INPUT TYPE="SUBMIT"> <!-- Press this button to submit form --> </CENTER> </FORM> </BODY> </HTML>
```

Figure 16-1 Initial result of GetForm.html .

<!-- image -->

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 16.1 How HTML Forms Transmit Data

## Chapter 16 Using HTML Forms

Figure 16-2 HTTP request sent by Netscape 4.7 when submitting GetForm.html .

<!-- image -->

## Listing 16.2 PostForm.html

```
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"> <HTML> <HEAD> <TITLE>A Sample Form Using POST</TITLE> </HEAD> <BODY BGCOLOR="#FDF5E6"> <H2 ALIGN="CENTER">A Sample Form Using POST</H2> <FORM ACTION="http://localhost:8088/SomeProgram" METHOD="POST" > <CENTER> First name: <INPUT TYPE="TEXT" NAME="firstName" VALUE="Joe"><BR> Last name: <INPUT TYPE="TEXT" NAME="lastName" VALUE="Hacker"><P> <INPUT TYPE="SUBMIT"> </CENTER> </FORM> </BODY> </HTML>
```

## 16.1 How HTML Forms Transmit Data

Figure 16-3 Initial result of PostForm.html .

<!-- image -->

Figure 16-4 HTTP request sent by Netscape 4.7 when submitting PostForm.html .

<!-- image -->

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

<!-- image -->