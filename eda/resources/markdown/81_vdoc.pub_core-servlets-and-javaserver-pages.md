## 9.2 The Session Tracking API

the user has disabled them. However, it has most of the same problems as cookies, namely, that the server-side program has a lot of straightforward but tedious processing to do. In addition, you have to be very careful that every URL that references your site and is returned to the user (even by indirect means  like Location fields  in  server  redirects)  has  the  extra  information appended. And, if the user leaves the session and comes back via a bookmark or link, the session information can be lost.

## Hidden Form Fields

HTML forms can have an entry that looks like the following:

&lt;INPUT TYPE="HIDDEN" NAME="session" VALUE="..."&gt;

This entry means that, when the form is submitted, the specified name and value  are  included  in  the GET or POST data.  For  details,  see  Section  16.9 (Hidden Fields). This hidden field can be used to store information about the session but it has the major disadvantage that it only works if every page is dynamically generated.

## Session Tracking in Servlets

Servlets  provide  an  outstanding  technical  solution:  the HttpSession API. This high-level interface is built on top of cookies or URL-rewriting. In fact, most  servers  use  cookies  if  the  browser  supports  them,  but  automatically revert to URL-rewriting when cookies are unsupported or explicitly disabled. But,  the  servlet  author  doesn't  need  to  bother  with  many  of  the  details, doesn't have to explicitly manipulate cookies or information appended to the URL, and is automatically given a convenient place to store arbitrary objects that are associated with each session.

## 9.2 The Session Tracking API

Using sessions in servlets is straightforward and involves looking up the session object associated with the current request, creating a new session object when  necessary,  looking  up  information  associated  with  a  session,  storing information in a session, and discarding completed or  abandoned sessions. Finally,  if  you  return  any  URLs  to  the  clients  that  reference  your  site  and URL-rewriting is being used, you need to attach the session information to the URLs.

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## Chapter 9 Session Tracking

## Looking Up the HttpSession Object Associated with the Current Request

You look up the HttpSession object by calling the getSession method of HttpServletRequest .  Behind  the  scenes,  the  system  extracts  a  user  ID from a cookie or attached URL data, then uses that as a key into a table of previously created HttpSession objects. But this is all done transparently to the programmer: you just call getSession . If getSession returns null , this means that the user is not already participating in a session, so you can create a new session. Creating a new session in this case is so commonly done that there is an option to automatically create a new session if one doesn't already exist. Just pass true to getSession .  Thus, your first step usually looks like this:

HttpSession session = request.getSession(true);

If you care whether the session existed previously or is newly created, you can use isNew to check.

## Looking Up Information Associated with a Session

HttpSession objects live on the server; they're just automatically associated with the client by a behind-the-scenes mechanism like cookies or URL-rewriting. These session objects have a built-in data structure that lets you store any number of keys and associated values. In version 2.1 and earlier of the servlet API, you use session.getValue("attribute") to look up a previously stored value. The return type is Object , so you have to do a typecast to whatever more specific type of data was associated with that attribute name in the session. The return value is null if there is no such attribute, so you need to check for null before calling methods on objects associated with sessions.

In version 2.2 of the servlet API, getValue is deprecated in favor of getAttribute because of the better naming match with setAttribute (in version 2.1 the match for getValue is putValue , not setValue ). Nevertheless, since  not  all  commercial  servlet  engines  yet  support  version  2.2,  I'll  use getValue in my examples.

Here's  a  representative  example,  assuming ShoppingCart is  some  class you've defined to store information on items being purchased (for an implementation, see Section 9.4 (An  On-Line  Store Using a Shopping Cart and Session Tracking)).

## 9.2 The Session Tracking API

```
HttpSession session = request.getSession(true); ShoppingCart cart = (ShoppingCart)session.getValue("shoppingCart"); if (cart == null) { // No cart already in session cart = new ShoppingCart(); session.putValue("shoppingCart", cart); } doSomethingWith(cart);
```

In most cases, you have a specific attribute name in mind and want to find the value (if any) already associated with that name. However, you can also discover all the attribute names in a given session by calling getValueNames , which returns an array of strings. This method is your only option for finding attribute names in version 2.1, but in servlet engines supporting version 2.2 of the servlet specification, you can use getAttributeNames . That method is more consistent in that it returns an Enumeration , just like the getHeaderNames and getParameterNames methods of HttpServletRequest .

Although the data that was explicitly associated with a session is the part you  care  most  about,  there  are  some  other  pieces  of  information  that  are sometimes useful as well. Here is a summary of the methods available in the HttpSession class.

## public Object getValue(String name) public Object getAttribute(String name)

These methods extract a previously stored value from a session object. They return null if there is no value associated with the given name. Use getValue in version 2.1 of the servlet API. Version 2.2 supports both methods, but getAttribute is preferred and getValue is deprecated.

## public void putValue(String name, Object value) public void setAttribute(String name, Object value)

These methods associate a value with a name. Use putValue with version 2.1 servlets and either setAttribute (preferred) or putValue (deprecated) with version 2.2 servlets. If the object supplied to putValue or setAttribute implements the HttpSessionBindingListener interface, the object's valueBound method is called after it is stored in the session. Similarly, if the previous value implements HttpSessionBindingListener , its valueUnbound method is called.

## public void removeValue(String name) public void removeAttribute(String name)

These methods remove any values associated with the designated name. If the value being removed implements HttpSessionBindingLis-

## Chapter 9 Session Tracking

tener , its valueUnbound method is called. With version 2.1 servlets, use removeValue . In version 2.2, removeAttribute is preferred, but removeValue is still supported (albeit deprecated) for backward compatibility.

## public String[] getValueNames() public Enumeration getAttributeNames()

These methods return the names of all attributes in the session. Use getValueNames in version 2.1 of the servlet specification. In version 2.2, getValueNames is supported but deprecated; use getAttributeNames instead.

## public String getId()

This method returns the unique identifier generated for each session. It is sometimes used as the key name when only a single value is associated with a session, or when information about sessions is being logged.

## public boolean isNew()

This method returns true if the client (browser) has never seen the session, usually because it was just created rather than being referenced by an incoming client request. It returns false for preexisting sessions.

## public long getCreationTime()

This method returns the time in milliseconds since midnight, January 1, 1970 (GMT) at which the session was first built. To get a value useful for printing out, pass the value to the Date constructor or the setTimeInMillis method of GregorianCalendar .

## public long getLastAccessedTime()

This method returns the time in milliseconds since midnight, January 1, 1970 (GMT) at which the session was last sent from the client.

## public int getMaxInactiveInterval() public void setMaxInactiveInterval(int seconds)

These methods get or set the amount of time, in seconds, that a session should go without access before being automatically invalidated. A negative value indicates that the session should never time out. Note that the time out is maintained on the server and is not the same as the cookie expiration date, which is sent to the client.

## public void invalidate()

This method invalidates the session and unbinds all objects associated with it.

## Associating Information with a Session

As discussed in the previous section, you read information associated with a session  by  using getValue (in  version  2.1  of  the  servlet  specification)  or getAttribute (in  version 2.2 ). To specify information in version 2.1 servlets, you use putValue , supplying a key and a value. Use setAttribute in version 2.2. This is a more consistent name because it uses the get / set notation  of  JavaBeans.  To  let  your  values  perform  side  effects  when  they  are stored in a session, simply have the object you are associating with the session implement the HttpSessionBindingListener interface.  Now,  every  time putValue or setAttribute is called on one of those objects, its valueBound method is called immediately afterward.

Be aware that putValue and setAttribute replace any previous values; if you want to remove a value without supplying a replacement, use removeValue in  version 2.1 and removeAttribute in  version 2.2. These methods trigger  the valueUnbound method  of  any  values  that  implement HttpSessionBindingListener .  Sometimes  you  just  want  to  replace  previous values; see the referringPage entry in the example below for an example. Other times,  you want  to  retrieve  a  previous  value and  augment  it;  for  an example,  see  the previousItems entry  below.  This  example  assumes  a ShoppingCart class with an addItem method to store items being ordered, and a Catalog class with a static getItem method that returns an item, given an item identifier. For an implementation, see Section 9.4 (An On-Line Store Using a Shopping Cart and Session Tracking).

HttpSession session = request.getSession(true);

```
session.putValue("referringPage", request.getHeader("Referer")); ShoppingCart cart = (ShoppingCart)session.getValue("previousItems"); if (cart == null) { // No cart already in session cart = new ShoppingCart(); session.putValue("previousItems", cart); } String itemID = request.getParameter("itemID"); if (itemID != null) { cart.addItem(Catalog.getItem(itemID)); }
```

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 9.2 The Session Tracking API

## Chapter 9 Session Tracking

## Terminating Sessions

Sessions  will  automatically  become  inactive  when  the  amount  of  time between client accesses exceeds the interval specified by getMaxInactiveInterval .  When  this  happens,  any  objects  bound  to  the HttpSession object  automatically  get  unbound.  When  this  happens,  your attached  objects will  automatically  be  notified  if  they  implement  the HttpSessionBindingListener interface.

Rather than waiting for sessions to time out, you can explicitly deactivate a session through the use of the session's invalidate method.

## Encoding URLs Sent to the Client

If you are using URL-rewriting for session tracking and you send a URL that references your site to the client, you need to explicitly add on the session data. Since the servlet will automatically switch to URL-rewriting when cookies aren't supported by the client, you should routinely encode all URLs that reference your site. There are two possible places you might use URLs that refer to your own site. The first is when the URLs are embedded in the Web page that the servlet generates. These URLs should be passed through the encodeURL method of HttpServletResponse . The method will determine if URL-rewriting is currently in use and append the session information only if necessary. The URL is returned unchanged otherwise.

## Here's an example:

String originalURL = someRelativeOrAbsoluteURL; String encodedURL = response.encodeURL(originalURL); out.println("&lt;A HREF=\"" + encodedURL + "\"&gt;...&lt;/A&gt;");

The second place you might use a URL that refers to your own site is in a sendRedirect call (i.e., placed into the Location response header). In this second situation, there are different rules for determining if session information needs to be attached, so you cannot use encodeURL . Fortunately, HttpServletResponse supplies an encodeRedirectURL method to handle that case. Here's an example:

String originalURL = someURL; // Relative URL OK in version 2.2 String encodedURL = response.encodeRedirectURL(originalURL); response.sendRedirect(encodedURL);

Since you often don't know if your servlet will later become part of a series of pages that use session tracking, it is good practice for servlets to plan ahead and encode URLs that reference their site.