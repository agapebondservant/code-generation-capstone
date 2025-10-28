## Chapter 8 Handling Cookies

Figure 8-3 Result of visiting the ShowCookies servlet within an hour of visiting SetCookies in a different browser session.

<!-- image -->

## 8.5 Basic Cookie Utilities

This section presents some simple but useful utilities for dealing with cookies.

## Finding Cookies with Specified Names

Listing 8.3 shows a section of ServletUtilities.java that simplifies the retrieval of a cookie or cookie value, given a cookie name. The getCookieValue method loops through the array of available Cookie objects, returning the value of any Cookie whose name matches the input. If there is no match, the  designated  default  value  is  returned.  So,  for  example,  my  typical approach for dealing with cookies is as follows:

```
Cookie[] cookies = request.getCookies(); String color = ServletUtilities.getCookieValue(cookies, "color", "black"); String font = ServletUtilities.getCookieValue(cookies, "font", "Arial");
```

The getCookie method also loops through the array comparing names, but returns the actual Cookie object instead of just the value. That method is for  cases  when you want to do something with the Cookie other  than  just read its value.