## Chapter 17 Using Applets As Servlet Front Ends

That Uses Object Serialization and HTTP Tunneling) gives an example. In the third approach, covered in Section 17.6, the applet sends POST data to a servlet and then processes the results itself. Section 17.6 (An Applet That Sends  POST  Data)  gives  an  example.  Finally,  Section  17.7  serves  as  a reminder that an  applet  can bypass the HTTP  server altogether  and talk directly to a custom server program running on the applet's home machine.

This  chapter  assumes  that  you  already  have  some  familiarity  with  basic applets and focuses on the techniques to allow them to communicate with server-side programs. Readers who are unfamiliar with applets should consult a  general  introduction  to  the  Java  programming  language. Core  Web Programming or Core Java (both from Prentice Hall) are two good choices.

## 17.1 Sending Data with GET and Displaying the Resultant Page

The showDocument method  instructs  the  browser  to  display  a  particular URL. Recall that you can transmit GET data to a servlet or CGI program by appending it to the program's URL after a question mark (?). Thus, to send GET data from an applet, you simply need to append the data to the string from which the URL is built, then create the URL object and call showDocument in the normal manner. A basic template for doing this in applets follows, assuming that baseURL is  a  string  representing  the  URL  of  the  server-side program and that someData is the information to be sent with the request.

```
try { URL programURL = new URL(baseURL + "?" + someData); getAppletContext().showDocument(programURL); } catch(MalformedURLException mue) { ... }
```

However, when data is sent by a browser, it is URL encoded , which means that  spaces  are  converted  to  plus  signs  (+)  and  nonalphanumeric  characters into a percent sign (%) followed by the two hex digits representing that character, as discussed in Section 16.2 (The FORM Element). The preceding example assumes that someData has already been encoded properly and fails if it has not been. JDK 1.1 has a URLEncoder class with a static encode method that can perform this encoding. So, if an applet is contacting a server-side program that normally receives GET data from HTML forms, the applet needs to