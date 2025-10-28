## 8.3 The Servlet Cookie API

## 8.3 The Servlet Cookie API

To send cookies to the client, a servlet should create one or more cookies with designated  names  and  values  with new  Cookie(name,  value) ,  set  any optional attributes with cookie.set Xxx (readable later by cookie.get Xxx ), and insert the cookies into the response headers with response.addCookie(cookie) .  To  read incoming cookies, a servlet should call request.getCookies ,  which returns an array of Cookie objects corresponding to the cookies the browser has associated with your site (this is null if there are no cookies in the request). In most cases, the servlet loops down this array until it finds the one whose name ( getName ) matches the name it had in mind, then calls getValue on that Cookie to see the value associated with that name. Each of these topics is discussed in more detail in the following sections.

## Creating Cookies

You  create  a  cookie  by  calling  the Cookie constructor,  which  takes  two strings:  the  cookie  name  and  the  cookie  value.  Neither  the  name  nor  the value should contain white space or any of the following characters:

```
[ ] ( ) = , " / ? @ : ;
```

## Cookie Attributes

Before adding the cookie to the outgoing headers, you can set various characteristics of the cookie by using one of the following set Xxx methods, where Xxx is  the name of the attribute you want to specify. Each set Xxx method has a corresponding get Xxx method to retrieve the attribute value. Except for name and value, the cookie attributes apply only to outgoing cookies from the server to the client; they aren't set on cookies that come from the browser to the server. See Appendix A (Servlet and JSP Quick Reference) for a summarized version of this information.

## public String getComment() public void setComment(String comment)

These methods look up or specify a comment associated with the cookie. With version 0 cookies (see the upcoming subsection on

## Chapter 8 Handling Cookies

getVersion and setVersion ), the comment is used purely for informational purposes on the server; it is not sent to the client.

## public String getDomain() public void setDomain(String domainPattern)

These methods get or set the domain to which the cookie applies. Normally, the browser only returns cookies to the exact same hostname that sent them. You can use setDomain method to instruct the browser to return them to other hosts within the same domain. To prevent servers setting cookies that apply to hosts outside their domain, the domain specified is required to start with a dot (e.g., .prenhall.com ), and must contain two dots for noncountry domains like .com , .edu and .gov ; and three dots for country domains like .co.uk and .edu.es . For instance, cookies sent from a servlet at bali.vacations.com would not normally get sent by the browser to pages at mexico.vacations.com . If the site wanted this to happen, the servlets could specify cookie.setDomain(".vacations.com") .

## public int getMaxAge() public void setMaxAge(int lifetime)

These methods tell how much time (in seconds) should elapse before the cookie expires. A negative value, which is the default, indicates that the cookie will last only for the current session (i.e., until the user quits the browser) and will not be stored on disk. See the LongLivedCookie class (Listing 8.4), which defines a subclass of Cookie with a maximum age automatically set one year in the future. Specifying a value of 0 instructs the browser to delete the cookie.

## public String getName() public void setName(String cookieName)

This pair of methods gets or sets the name of the cookie. The name and the value are the two pieces you virtually always care about. However, since the name is supplied to the Cookie constructor, you rarely need to call setName . On the other hand, getName is used on almost every cookie received on the server. Since the getCookies method of HttpServletRequest returns an array of Cookie objects, it is common to loop down this array, calling getName until you have a particular name, then check the value with getValue . For an encapsulation of this process, see the getCookieValue method shown in Listing 8.3.

## public String getPath() public void setPath(String path)

These methods get or set the path to which the cookie applies. If you don't specify a path, the browser returns the cookie only to URLs in or below the directory containing the page that sent the cookie. For example, if the server sent the cookie from http://ecommerce.site.com/toys/ specials.html , the browser would send the cookie back when connecting to http://ecommerce.site.com/toys/bikes/beginners.html , but not to http://ecommerce.site.com/cds/classical.html . The setPath method can be used to specify something more general. For example, someCookie.setPath("/") specifies that all pages on the server should receive the cookie. The path specified must include the current page; that is, you may specify a more general path than the default, but not a more specific one. So, for example, a servlet at http://host/store/cust-service/request could specify a path of /store/ (since /store/ includes /store/cust-service/ ) but not a path of /store/cust-service/returns/ (since this directory does not include /store/cust-service/ ).

## public boolean getSecure() public void setSecure(boolean secureFlag)

This pair of methods gets or sets the boolean value indicating whether the cookie should only be sent over encrypted (i.e., SSL) connections. The default is false ; the cookie should apply to all connections.

## public String getValue() public void setValue(String cookieValue)

The getValue method looks up the value associated with the cookie; the setValue method specifies it. Again, the name and the value are the two parts of a cookie that you almost always care about, although in a few cases, a name is used as a boolean flag and its value is ignored (i.e., the existence of a cookie with the designated name is all that matters).

## public int getVersion() public void setVersion(int version)

These methods get/set the cookie protocol version the cookie complies with. Version 0, the default, follows the original Netscape specification (http://www.netscape.com/newsref/std/cookie\_spec.html ). Version 1, not yet widely supported, adheres to RFC 2109 (retrieve RFCs from the archive sites listed at http://www.rfc-editor.org/ ).

## 8.3 The Servlet Cookie API