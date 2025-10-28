## 16.9 Hidden Fields

Hidden fields do not affect the appearance of the page that is presented to the user. Instead, they store fixed names and values that are sent unchanged to  the  server,  regardless  of  user  input.  Hidden  fields  are  typically  used  for three purposes.

First, they are one method of tracking users as they move around within a site (see Section 9.1, 'The Need for Session Tracking'). Servlet authors typically  rely  on  the  servlet  session  tracking  API  (Section  9.2)  rather  than attempting to implement session tracking at this low level.

Second, hidden fields are used to provide predefined input to a server-side program when a variety of static HTML pages act as front ends to the same program on the server. For example, an on-line store might pay commissions to  people who  refer  customers  to their  site.  In  this  scenario,  the  referring page  could  let  visitors  search  the  store's  catalog  by  means  of  a  form,  but embed a hidden field listing its referral ID.

Third, hidden fields are used to store contextual information in pages that are dynamically generated. For example, in the order confirmation page of the on-line store developed in Section 9.4, each row in the table corresponds to a particular item being ordered (see Figure 9-6). The user can modify the number of items ordered, but there is no visible form element that stores the item ID. So, a hidden form is used (see Listing 9.5).

## HTML Element: &lt;INPUT TYPE="HIDDEN" NAME="..." VALUE="..."&gt; (No End Tag)

Attributes: NAME (required), VALUE

This element stores a name and a value, but no graphical element is created in the browser. The name/value pair is added to the form data when the form is submitted. For instance, with the following example, itemID=hall001 will always get sent with the form data.

&lt;INPUT TYPE="HIDDEN" NAME="itemID" VALUE="hall001"&gt;

Note that the term 'hidden' does not mean that the field cannot be discovered by the user, since it is clearly visible in the HTML source. Because there is no reliable way to 'hide' the HTML that generates a page, authors are cautioned not to use hidden fields to embed passwords or other sensitive information.

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.