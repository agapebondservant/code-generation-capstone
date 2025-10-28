## Chapter 16 Using HTML Forms

## 16.8 Server-Side Image Maps

In  HTML,  an  element  called MAP lets  you  associate  URLs  with  various regions of an image; then, when the image is clicked in one of the designated regions,  the  browser  loads  the  appropriate  URL.  This  form  of  mapping  is known as a client-side image map , since the determination of which URL to contact is made on the client and no server-side program is involved. HTML also supports server-side image maps that can be used within HTML forms. With such maps, an image is drawn, and when the user clicks on it, the coordinates of the click are sent to a server-side program.

Client-side  image  maps  are  simpler  and  more  efficient  than  server-side ones and should be used when all you want to do is associate a fixed set of URLs  with  some  predefined  image  regions.  However,  server-side  image maps are appropriate if the URL needs to be computed (e.g,. for weather maps),  the  regions  change  frequently,  or  other  form  data  needs  to  be included with the request. This section discusses  two  approaches to server-side image maps.

## IMAGE-Standard Server-Side Image Maps

The usual way to create server-side image maps is by means of an &lt;INPUT TYPE="IMAGE" ...&gt; element inside a form.

HTML Element: &lt;INPUT TYPE="IMAGE" ...&gt; (No End Tag) Attributes: NAME (required), SRC , ALIGN

This  element  displays  an  image  that,  when  clicked,  sends  the  form  to  the servlet  or  other  server-side  program  specified  by  the  enclosing  form's ACTION . The name itself is not sent; instead, name .x= xpos and name .y= ypos are transmitted, where xpos and ypos are the coordinates of the mouse click relative to the upper-left corner of the image.

## NAME

The NAME attribute identifies the textfield when the form is submitted.

## SRC

SRC designates the URL of the associated image.

## ALIGN

The ALIGN attribute has the same options ( TOP , MIDDLE , BOTTOM , LEFT , RIGHT ) and default ( BOTTOM ) as the ALIGN attribute of the IMG element and is used in the same way.

Listing 16.5 shows a simple example, where the form's ACTION specifies the EchoServer developed in Section 16.12. Figures 16-21 and 16-22 show the results before and after the image is clicked.

## Listing 16.5 ImageMap.html

```
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"> <HTML> <HEAD> <TITLE>The IMAGE Input Control</TITLE> </HEAD> <BODY> <H1 ALIGN="CENTER">The IMAGE Input Control</H1> Which island is Java? Click and see if you are correct. <FORM ACTION="http://localhost:8088/GeographyTester"> <INPUT TYPE="IMAGE" NAME="map" SRC="images/indonesia.gif"> </FORM> Of course, image maps can be implemented <B>in</B> Java as well. :-) </BODY> </HTML>
```

## 16.8 Server-Side Image Maps

## Chapter 16 Using HTML Forms

Figure 16-21 An IMAGE input control with NAME="map" .

<!-- image -->

Figure 16-22 Clicking on the image at (305, 280) submits the form and adds map.x=305&amp;map.y=280 to the form data.

<!-- image -->

## 16.8 Server-Side Image Maps

## ISMAP-Alternative Server-Side Image Maps

ISMAP is an optional attribute of the IMG element and can be used in a similar  manner to the &lt;INPUT  TYPE="IMAGE"  ...&gt; FORM entry. ISMAP is  not actually a FORM element at all, but can still be used for simple connections to servlets or CGI programs. If an image with ISMAP is  inside a hypertext link, then clicking on the image results in the coordinates of the click being sent to the specified URL. Coordinates are separated by commas and are specified in pixels relative to the top-left corner of the image.

For instance, Listing 16.6 embeds an image that uses the ISMAP attribute inside a hypertext link to http://localhost:8088/ChipTester , which is answered  by  the  mini  HTTP  server  developed  in  Section  16.12.  Figure 16-23 shows the initial result, which is identical to what would have been shown had the ISMAP attribute  been  omitted.  However, when the mouse button is pressed 271 pixels to the right and 184 pixels below the top-left corner  of  the  image,  the  browser  requests  the  URL http://localhost:8088/ChipTester?271,184 (as is shown in Figure 16-24).

If a server-side image map is used simply to select among a static set of destination URLs, then a client-side MAP element is a much better option because the server doesn't have to be contacted just to decide which URL applies.  If  the  image  map  is  intended  to  be  mixed  with  other  input  elements,  then  the IMAGE input  type  is  preferred  instead.  However,  for  a stand-alone image map where the URL associated with a region changes frequently  or  requires  calculation,  an  image  with ISMAP is  a  reasonable choice.

## Listing 16.6 IsMap.html

&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"&gt; &lt;HTML&gt; &lt;HEAD&gt; &lt;TITLE&gt;The ISMAP Attribute&lt;/TITLE&gt; &lt;/HEAD&gt; &lt;BODY&gt; &lt;H1 ALIGN="CENTER"&gt;The ISMAP Attribute&lt;/H1&gt; &lt;H2&gt;Select a pin:&lt;/H2&gt; &lt;A HREF="http://localhost:8088/ChipTester"&gt; &lt;IMG SRC="images/chip.gif" WIDTH=495 HEIGHT=200 ALT="Chip" BORDER=0 ISMAP&gt;&lt;/A&gt;

&lt;/BODY&gt;

&lt;/HTML&gt;

## Chapter 16 Using HTML Forms

Figure 16-23 Setting the ISMAP attribute of an IMG element inside a hypertext link changes what happens when the image is selected.

<!-- image -->

Figure 16-24 When an ISMAP image is selected, the coordinates of the selection are transmitted with the URL.

<!-- image -->