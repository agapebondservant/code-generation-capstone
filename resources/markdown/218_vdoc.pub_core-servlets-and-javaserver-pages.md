## Appendix A Servlet and JSP Quick Reference

## The session Attribute

- · &lt;%@ page session="true" %&gt; &lt;%!-- Default --%&gt;
- · &lt;%@ page session="false" %&gt;

## The buffer Attribute

- · &lt;%@ page buffer="sizekb" %&gt;
- · &lt;%@ page buffer="none" %&gt;
- · Servers can use a larger buffer than you specify, but not a smaller one. For example, &lt;%@ page buffer="32kb" %&gt; means the document content should be buffered and not sent to the client until at least 32 kilobytes have been accumulated or the page is completed.

## The autoflush Attribute

- · &lt;%@ page autoflush="true" %&gt; &lt;%!-- Default --%&gt;
- · &lt;%@ page autoflush="false" %&gt;
- · A value of false is illegal when buffer="none" is also used.

## The extends Attribute

- · &lt;%@ page extends="package.class" %&gt;

## The info Attribute

- · &lt;%@ page info="Some Message" %&gt;

## The errorPage Attribute

- · &lt;%@ page errorPage="Relative URL" %&gt;
- · The exception thrown will be automatically available to the designated error page by means of the exception variable. See Listings 11.5 and 11.6 for examples.

## The isErrorPage Attribute

- · &lt;%@ page isErrorPage="true" %&gt;
- · &lt;%@ page isErrorPage="false" %&gt; &lt;%!-- Default --%&gt;
- · See Listings 11.5 and 11.6 for examples.

## The language Attribute

- · &lt;%@ page language="cobol" %&gt;
- · For now, don't bother with this attribute since java is both the default and the only legal choice.