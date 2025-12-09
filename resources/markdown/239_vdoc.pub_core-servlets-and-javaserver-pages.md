## A.14 Creating Custom JSP Tag Libraries

## The Tag Library Descriptor File

- · Within taglib element, contains tag element for each tag handler.
- E.g.:

&lt;tag&gt;

&lt;name&gt;prime&lt;/name&gt;

&lt;tagclass&gt;coreservlets.tags.PrimeTag&lt;/tagclass&gt;

- &lt;info&gt;Outputs a random N-digit prime.&lt;/info&gt;
- &lt;bodycontent&gt;EMPTY&lt;/bodycontent&gt;
- &lt;attribute&gt;

&lt;name&gt;length&lt;/name&gt;

&lt;required&gt;false&lt;/required&gt;

- &lt;/attribute&gt;

&lt;/tag&gt;

## The JSP File

- · &lt;%@ taglib uri="some-taglib.tld" prefix=" prefix " %&gt;
- · &lt;prefix:tagname /&gt;
- · &lt;prefix:tagname&gt;body&lt;/prefix:tagname&gt;

## Assigning Attributes to Tags

- · Tag handler :

Implements setXxx for each attribute xxx .

- · Tag Library Descriptor:

&lt;tag&gt;

...

&lt;attribute&gt;

&lt;name&gt;length&lt;/name&gt;

&lt;required&gt;false&lt;/required&gt;

&lt;rtexprvalue&gt;true&lt;/rtexprvalue&gt; &lt;%-- sometimes --%&gt;

- &lt;/attribute&gt;
- &lt;/tag&gt;

## Including the Tag Body

- · Tag handler :

You should return EVAL\_BODY\_INCLUDE instead of SKIP\_BODY from doStartTag .

- · Tag Library Descriptor:
- &lt;tag&gt;

...

- &lt;bodycontent&gt;JSP&lt;/bodycontent&gt;

&lt;/tag&gt;

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

<!-- image -->