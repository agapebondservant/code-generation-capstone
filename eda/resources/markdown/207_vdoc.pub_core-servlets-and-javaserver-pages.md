## A.9 Session Tracking

- · getDomain/setDomain : lets you specify domain to which cookie applies. Current host must be part of domain specified.
- · getMaxAge/setMaxAge : gets/sets the cookie expiration time (in seconds). If you fail to set this, cookie applies to current browsing session only. See LongLivedCookie helper class (Section 8.5).
- · getName/setName : gets/sets the cookie name. For new cookies, you supply name to constructor, not to setName . For incoming cookie array, you use getName to find the cookie of interest.
- · getPath/setPath : gets/sets the path to which cookie applies. If unspecified, cookie applies to URLs that are within or below directory containing current page.
- · getSecure/setSecure : gets/sets flag indicating whether cookie should apply only to SSL connections or to all connections.
- · getValue/setValue : gets/sets value associated with cookie. For new cookies, you supply value to constructor, not to setValue . For incoming cookie array, you use getName to find the cookie of interest, then call getValue on the result.
- · getVersion/setVersion : gets/sets the cookie protocol version. Version 0 is the default; stick with that until browsers start supporting version 1.

## A.9 Session Tracking

## Looking Up Session Information: getValue

HttpSession session = request.getSession(true);

ShoppingCart cart =

(ShoppingCart)session.getValue("shoppingCart"); if (cart == null) { // No cart already in session cart = new ShoppingCart(); session.putValue("shoppingCart", cart);

}

doSomethingWith(cart);

## Associating Information with a Session: putValue

```
HttpSession session = request.getSession(true); session.putValue("referringPage", request.getHeader("Referer")); ShoppingCart cart = (ShoppingCart)session.getValue("previousItems"); if (cart == null) { // No cart already in session cart = new ShoppingCart(); session.putValue("previousItems", cart); } String itemID = request.getParameter("itemID"); if (itemID != null) { cart.addItem(Catalog.getItem(itemID)); }
```

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.