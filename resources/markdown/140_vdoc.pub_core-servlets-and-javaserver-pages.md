## Chapter 16 Using HTML Forms

## 16.10 Grouping Controls

HTML 4.0 defines the FIELDSET element, with an associated LEGEND ,  that can be used to visually group controls within a form. This capability is quite useful but is supported only by Internet Explorer. Hopefully, Netscape version 5 will add support for this element. In the meantime, you should reserve use  of  this  element  to  intranet  applications  where  all  your  users  are  using Internet Explorer.

<!-- image -->

## Core Warning

As of version 4.7, Netscape does not support the FIELDSET element.

## HTML Element: &lt;FIELDSET&gt;

Attributes: None.

This element is used as a container to enclose controls and, optionally, a LEGEND element. It has no attributes beyond the universal ones for style sheets, language, and so forth. Listing 16.7 gives an example, with the result shown in Figure 16-25.

Figure 16-25 The FIELDSET element lets you visually group related controls.

<!-- image -->

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## Listing 16.7 Fieldset.html

&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"&gt;

&lt;HTML&gt;

&lt;HEAD&gt;

&lt;TITLE&gt;Grouping Controls in Internet Explorer&lt;/TITLE&gt; &lt;/HEAD&gt;

&lt;BODY BGCOLOR="#FDF5E6"&gt;

&lt;H2 ALIGN="CENTER"&gt;Grouping Controls in Internet Explorer&lt;/H2&gt;

&lt;FORM ACTION="http://localhost:8088/SomeProgram"&gt;

## &lt;FIELDSET&gt;

## &lt;LEGEND&gt;Group One&lt;/LEGEND&gt;

Field 1A: &lt;INPUT TYPE="TEXT" NAME="field1A" VALUE="Field A"&gt;&lt;BR&gt;

Field 1B: &lt;INPUT TYPE="TEXT" NAME="field1B" VALUE="Field B"&gt;&lt;BR&gt;

Field 1C: &lt;INPUT TYPE="TEXT" NAME="field1C" VALUE="Field C"&gt;&lt;BR&gt;

&lt;/FIELDSET&gt;

## &lt;FIELDSET&gt;

## &lt;LEGEND ALIGN="RIGHT"&gt;Group Two&lt;/LEGEND&gt;

Field 2A: &lt;INPUT TYPE="TEXT" NAME="field2A" VALUE="Field A"&gt;&lt;BR&gt;

Field 2B: &lt;INPUT TYPE="TEXT" NAME="field2B" VALUE="Field B"&gt;&lt;BR&gt;

Field 2C: &lt;INPUT TYPE="TEXT" NAME="field2C" VALUE="Field C"&gt;&lt;BR&gt;

## &lt;/FIELDSET&gt;

&lt;/FORM&gt;

&lt;/BODY&gt;

&lt;/HTML&gt;

## HTML Element: &lt;LEGEND&gt;

Attributes:

ALIGN

This element, legal only within an enclosing FIELDSET , places a label on the etched border that is drawn around the group of controls.

## ALIGN

This attribute controls the position of the label. Legal values are TOP , BOTTOM , LEFT , and RIGHT , with TOP being the default. In Figure 16-25, the first group has the default legend alignment, and the second group stipulates ALIGN="RIGHT" . In HTML, style sheets are often a better way to control element alignment, since they permit a single change to be propagated to multiple places.

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 16.10 Grouping Controls