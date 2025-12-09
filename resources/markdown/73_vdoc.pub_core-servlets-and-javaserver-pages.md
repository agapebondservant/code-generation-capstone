- ' Prentice Hall and Sun Microsystems. Personal use only; do not redistribute.

Chapter

<!-- image -->

ookies are small bits of textual information that a Web server sends to a browser and that the browser returns unchanged when later visiting the same Web site or domain. By letting the server read information it  sent  the  client  previously,  the  site  can  provide  visitors  with  a  number  of conveniences such as presenting the site the way the visitor previously customized it or  letting  identifiable  visitors  in  without  their  having  to  enter  a password. Most browsers avoid caching documents associated with cookies, so the site can return different content each time. C

This chapter discusses how to explicitly set and read cookies from within servlets, and the next chapter shows you how to use the servlet session tracking API (which can use cookies behind the scenes) to keep track of users as they move around to different pages within your site.

## 8.1 Benefits of Cookies

This section summarizes four typical ways in which cookies can add value to your site.

## Chapter 8 Handling Cookies

## Identifying a User During an E-commerce Session

Many on-line stores use a 'shopping cart' metaphor in which the user selects an  item,  adds  it  to  his  shopping  cart,  then  continues  shopping.  Since  the HTTP connection is usually closed  after  each  page  is  sent,  when  the  user selects a new item to add to the cart, how does the store know that it is the same  user  that  put  the  previous  item  in  the  cart?  Persistent  (keep-alive) HTTP connections (see Section 7.4) do not solve this problem, since persistent connections generally apply only to requests made very close together in time,  as  when  a  browser  asks  for  the  images  associated  with  a  Web  page. Besides, many servers and browsers lack support for persistent connections. Cookies, however, can solve this problem. In fact, this capability is so useful that servlets have an API specifically for session tracking, and servlet authors don't  need  to  manipulate  cookies  directly  to  take  advantage  of  it.  Session tracking is discussed in Chapter 9.

## Avoiding Username and Password

Many large sites require you to register in order to use their services, but it is inconvenient to remember and enter the username and password each time you visit. Cookies are a good alternative for low-security sites. When a user registers, a cookie containing a unique user ID is sent to him. When the client reconnects at a later date, the user ID is returned, the server looks it up, determines  it  belongs  to  a  registered  user,  and  permits  access  without  an explicit  username  and  password.  The  site  may  also  remember  the  user's address, credit card number, and so forth, thus simplifying later transactions.

## Customizing a Site

Many 'portal' sites let you customize the look of the main page. They might let  you  pick  which  weather  report  you  want  to  see,  what  stock  and  sports results you care about, how search results should be displayed, and so forth. Since it would be inconvenient for you to have to set up your page each time you visit their site, they use cookies to remember what you wanted. For simple  settings,  this  customization  could  be  accomplished by storing the  page settings directly in the cookies. Section 8.6 gives an example of this. For more complex customization, however, the site just sends the client a unique identifier  and  keeps  a  server-side  database  that  associates  identifiers  with  page settings.