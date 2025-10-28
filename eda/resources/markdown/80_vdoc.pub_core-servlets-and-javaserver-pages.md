' Prentice Hall and Sun Microsystems. Personal use only; do not redistribute.

<!-- image -->

his chapter shows you how to use the servlet session tracking API to keep track of visitors as they move around at your site. T

## 9.1 The Need for Session Tracking

HTTP is a 'stateless' protocol: each time a  client retrieves a Web page, it opens a separate connection to the Web server, and the server does not automatically maintain contextual information about a client. Even with servers that  support  persistent  (keep-alive)  HTTP  connections  and  keep  a  socket open for multiple client requests that occur close together in time (see Section 7.4), there is no built-in support for maintaining contextual information. This lack of context causes a number of difficulties. For example, when clients at an on-line store add an  item to their shopping carts,  how  does the server know what's already in them? Similarly, when clients decide to proceed to  checkout, how can the server determine which previously created shopping carts are theirs?

There are three typical solutions to this problem: cookies, URL-rewriting, and hidden form fields.

## Chapter 9 Session Tracking

## Cookies

You can use HTTP cookies to store information about a shopping session, and each subsequent connection can look up the current session and then extract information  about that  session  from  some  location  on  the  server  machine. For example, a servlet could do something like the following:

```
String sessionID = makeUniqueString(); Hashtable sessionInfo = new Hashtable(); Hashtable globalTable = findTableStoringSessions(); globalTable.put(sessionID, sessionInfo); Cookie sessionCookie = new Cookie("JSESSIONID", sessionID); sessionCookie.setPath("/"); response.addCookie(sessionCookie);
```

Then, in later requests the server could use the globalTable hash table to associate a session ID from the JSESSIONID cookie  with the sessionInfo hash table of data associated with that particular session. This is an excellent solution and is the most widely used approach for session handling. Still, it would be nice to have a higher-level API that handles some of these details. Even though servlets have a high-level and easy-to-use interface to cookies (see Chapter 8), a number of relatively tedious details still need to be handled in this case:

- · Extracting the cookie that stores the session identifier from the other cookies (there may be many cookies, after all)
- · Setting an appropriate expiration time for the cookie (sessions that are inactive for 24 hours probably should be reset)
- · Associating the hash tables with each request
- · Generating the unique session identifiers

Besides, due to real and perceived privacy concerns over cookies (see Section 8.2), some users disable them. So, it would be nice to have alternative implementation approaches in addition to a higher-level protocol.

## URL-Rewriting

With this approach, the client appends some extra data on the end of each URL that  identifies  the  session,  and  the  server  associates  that  identifier with data it has stored about that session. For example, with http://host/path/file.html;jsessionid=1234 , the session information is attached as jsessionid=1234 .  This is also an excellent solution, and even has the advantage that it works when browsers don't support cookies or when