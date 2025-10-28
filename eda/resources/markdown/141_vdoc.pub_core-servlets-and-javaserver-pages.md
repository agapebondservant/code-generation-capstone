## Chapter 16 Using HTML Forms

## 16.11 Controlling Tab Order

HTML 4.0 defines a TABINDEX attribute that can be used in any of the visual HTML elements. Its value is an integer, and it controls the order in which elements  receive  the  input  focus  when  the  TAB  key  is  pressed.  Unfortunately, however, it is supported only by Internet Explorer. Nevertheless, you can use TABINDEX even for pages that will be viewed by multiple browsers, as long as the designated tabbing order is a convenience to the user, not a necessity for proper operation of the page.

<!-- image -->

## Core Warning

As of version 4.7, Netscape does not support the TABINDEX attribute.

## Listing 16.8 Tabindex.html

&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"&gt;

&lt;HTML&gt;

&lt;HEAD&gt;

&lt;TITLE&gt;Controlling TAB Order&lt;/TITLE&gt;

&lt;/HEAD&gt;

&lt;BODY BGCOLOR="#FDF5E6"&gt;

&lt;H2 ALIGN="CENTER"&gt;Controlling TAB Order&lt;/H2&gt;

&lt;FORM ACTION="http://localhost:8088/SomeProgram"&gt;

Field 1 (first tab selection):

&lt;INPUT TYPE="TEXT" NAME="field1"

TABINDEX=1 &gt;&lt;BR&gt;

Field 2 (third tab selection):

&lt;INPUT TYPE="TEXT" NAME="field2"

TABINDEX=3 &gt;&lt;BR&gt;

Field 3 (second tab selection):

&lt;INPUT TYPE="TEXT" NAME="field3"

TABINDEX=2 &gt;&lt;BR&gt;

&lt;/FORM&gt;

&lt;/BODY&gt;

&lt;/HTML&gt;