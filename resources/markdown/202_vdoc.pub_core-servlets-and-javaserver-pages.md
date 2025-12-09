## Appendix A Servlet and JSP Quick Reference

## A.8 Handling Cookies

## Typical Uses of Cookies

- · Identifying a user during an e-commerce session
- · Avoiding username and password
- · Customizing a site
- · Focusing advertising

## Problems with Cookies

- · It's a privacy problem, not a security problem.
- · Privacy problems include: servers can remember what you did in previous sessions; if you give out personal information, servers can link that information to your previous actions; servers can share cookie information through use of a cooperating third party like doubleclick.net (by each loading image off the third-party site); poorly designed sites could store sensitive information like credit card numbers directly in the cookie.

## General Usage

- · Sending cookie to browser (standard approach):
- · Sending cookie to browser (simplified approach):

```
Cookie c = new Cookie("name", "value"); c.setMaxAge(...); // Set other attributes. response.addCookie(c);
```

Use LongLivedCookie class (Section 8.5).

- · Reading cookies from browser (standard approach):
- · Reading cookies from browser (simplified approach):

```
Cookie[] cookies = response.getCookies(); for(int i=0; i<cookies.length; i++) { Cookie c = cookies[i]; if (c.getName().equals("someName")) { doSomethingWith(c); break; } }
```

Extract cookie or cookie value from cookie array by using ServletUtilities.getCookie or ServletUtilities.getCookieValue .

## Cookie Methods

- · getComment/setComment : gets/sets comment. Not supported in version 0 cookies (which is what most browsers now support).