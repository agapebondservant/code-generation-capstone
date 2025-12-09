Chapter 7 Generating the Server Response: HTTP Response Headers

## 7.5 Using Servlets to Generate GIF Images

Although servlets often generate HTML output, they certainly don't always do so. For example, Section 11.2 (The contentType Attribute) shows a JSP page (which gets translated into a servlet) that builds Excel spreadsheets and returns them to the client. Here, I'll show you how to generate GIF images.

First,  let  me  summarize  the  two  main  steps  servlets  have  to  perform  in order to build multimedia content. First, they have to set the Content-Type response  header  by  using  the setContentType method  of HttpServletResponse .  Second, they have to send the output in the appropriate format. This format varies among document types, of course, but in most cases you use send binary data, not strings as with HTML documents. Consequently, servlets  will  usually  get  the  raw  output  stream  by  using  the getOutputStream method,  rather  than  getting  a PrintWriter by  using getWriter . Putting these two points together, servlets that generate non-HTML content usually have a section of their doGet or doPost method that looks like this:

```
response.setContentType("type/subtype"); OutputStream out = response.getOutputStream();
```

Those are  the  two  general  steps  required  to  build  non-HTML  content. Next, let's look at the specific steps required to generate GIF images.

## 1. Create an Image .

You create an Image object by using the createImage method of the Component class. Since server-side programs should not actually open any windows on the screen, they need to explicitly tell the system to create a native window system object, a process that normally occurs automatically when a window pops up. The addNotify method accomplishes this task. Putting this all together, here is the normal process:

```
Frame f = new Frame(); f.addNotify(); int width = ...; int height = ...; Image img = f.createImage(width, height);
```

## 2. Draw into the Image .

You accomplish this task by calling the Image ' s getGraphics method and then using the resultant Graphics object in the usual manner. For example, with JDK 1.1, you would use various draw Xxx and fill Xxx methods of Graphics to draw images, strings, and shapes onto the Image . With the Java 2 platform, you would cast the Graphics object to Graphics2D , then make use of Java2D's much richer set of drawing operations, coordinate transformations, font settings, and fill patterns to perform the drawing. Here is a simple example:

```
Graphics g = img.getGraphics(); g.fillRect(...); g.drawString(...);
```

## 3. Set the Content-Type response header.

As already discussed, you use the setContentType method of HttpServletResponse for this task. The MIME type for GIF images is image/gif .

response.setContentType("image/gif");

## 4. Get an output stream.

As discussed previously, if you are sending binary data, you should call the getOutputStream method of HttpServletResponse rather than the getWriter method.

OutputStream out = response.getOutputStream();

## 5. Send the Image in GIF format to the output stream.

Accomplishing this task yourself requires quite a bit of work. Fortunately, there are several existing classes that perform this operation. One of the most popular ones is Jef Poskanzer's GifEncoder class, available free from http://www.acme.com/java/ . Here is how you would use this class to send an Image in GIF format:

```
try { new GifEncoder(img, out).encode(); } catch(IOException ioe) { // Error message }
```

Listings  7.8  and  7.9  show  a  servlet  that  reads message , fontName ,  and fontSize parameters and uses them to create a GIF image showing the mes-

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 7.5 Using Servlets to Generate GIF Images

## Chapter 7 Generating the Server Response: HTTP Response Headers

sage in the designated face and size, with a gray, oblique shadowed version of the message shown behind the main string. This operation makes use of several facilities available only in the Java 2 platform. First, it makes use of any font that is installed on the server system, rather than limiting itself to the standard names ( Serif , SansSerif , Monospaced , Dialog ,  and DialogInput ) available to JDK 1.1 programs.

Second, it uses the translate , scale , and shear transformations to create the shadowed version of the main message. Consequently, the servlet will run only in servlet engines running on the Java 2 platform. You would expect this to be the case with engines supporting the servlet 2.2 specification, since that is the servlet version stipulated in J2EE.

Even if you are using a server that supports only version 2.1, you should still use the Java 2 platform if you can, since it tends to be significantly more efficient for server-side tasks. However, many servlet 2.1 engines come preconfigured to use JDK 1.1, and changing the Java version is not always simple.  So,  for  example,  Tomcat  and  the  JSWDK  automatically  make  use  of whichever version of Java is first in your PATH , but the Java Web Server uses a bundled version of JDK 1.1.

Listing 7.10 shows an HTML form used as a front end to the servlet. Figures 7-5 through 7-8 show some possible results. Just to simplify experimentation,  Listing  7.11  presents  an  interactive  application  that  lets  you  specify the message, font name, and font size on the command line, popping up a JFrame that  shows the same image as the servlet would return. Figure 7-9 shows one typical result.

## Listing 7.8 ShadowedText.java

```
package coreservlets; import java.io.*; import javax.servlet.*; import javax.servlet.http.*; import java.awt.*; /** Servlet that generates GIF images representing *  a designated message with an oblique shadowed *  version behind it. *  <P> *  <B>Only runs on servers that support Java 2, since *  it relies on Java2D to build the images.</B> */ public class ShadowedText extends HttpServlet { public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException { String message = request.getParameter("message"); if ((message == null) || (message.length() == 0)) {
```

## 7.5 Using Servlets to Generate GIF Images

## String fontSizeString = request.getParameter("fontSize"); Listing 7.8 ShadowedText.java (continued)

```
message = "Missing 'message' parameter"; } String fontName = request.getParameter("fontName"); if (fontName == null) { fontName = "Serif"; } int fontSize; try { fontSize = Integer.parseInt(fontSizeString); } catch(NumberFormatException nfe) { fontSize = 90; } response.setContentType("image/gif"); OutputStream out = response.getOutputStream(); Image messageImage = MessageImage.makeMessageImage(message, fontName, fontSize); MessageImage.sendAsGIF(messageImage, out); } /** Allow form to send data via either GET or POST. */ public void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException { doGet(request, response); } }
```

## Listing 7.9 MessageImage.java

package coreservlets;

```
import java.awt.*; import java.awt.geom.*; import java.io.*;
```

import Acme.JPM.Encoders.GifEncoder;

/** Utilities for building images showing shadowed messages.

- *  Includes a routine that uses Jef Poskanzer's GifEncoder
- *  to return the result as a GIF.
- *  &lt;P&gt;
- *  &lt;B&gt;Does not run in JDK 1.1, since it relies on Java2D
- *  to build the images.&lt;/B&gt;
- *  &lt;P&gt;

*/

<!-- image -->

## 172 Chapter 7 Generating the Server Response: HTTP Response Headers

## Listing 7.9 MessageImage.java (continued)

public class MessageImage {

- /** Creates an Image of a string with an oblique
- *  shadow behind it. Used by the ShadowedText servlet
- *  and the ShadowedTextFrame desktop application.

*/

public static Image makeMessageImage(String message,

```
String fontName, int fontSize) { Frame f = new Frame(); // Connect to native screen resource for image creation. f.addNotify(); // Make sure Java knows about local font names. GraphicsEnvironment env = GraphicsEnvironment.getLocalGraphicsEnvironment(); env.getAvailableFontFamilyNames(); Font font = new Font(fontName, Font.PLAIN, fontSize); FontMetrics metrics = f.getFontMetrics(font); int messageWidth = metrics.stringWidth(message); int baselineX = messageWidth/10; int width = messageWidth+2*(baselineX + fontSize); int height = fontSize*7/2; int baselineY = height*8/10; Image messageImage = f.createImage(width, height); Graphics2D g2d = (Graphics2D)messageImage.getGraphics(); g2d.setFont(font); g2d.translate(baselineX, baselineY); g2d.setPaint(Color.lightGray); AffineTransform origTransform = g2d.getTransform(); g2d.shear(-0.95, 0); g2d.scale(1, 3); g2d.drawString(message, 0, 0); g2d.setTransform(origTransform); g2d.setPaint(Color.black); g2d.drawString(message, 0, 0); return(messageImage); } /** Uses GifEncoder to send the Image down output stream *  in GIF89A format. See http://www.acme.com/java/ for *  the GifEncoder class. */ public static void sendAsGIF(Image image, OutputStream out) {
```

```
try { new GifEncoder(image, out).encode(); } catch(IOException ioe) { System.err.println("Error outputting GIF: " + ioe); } } }
```

## 7.5 Using Servlets to Generate GIF Images

## Listing 7.10 ShadowedText.html

&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"&gt;

&lt;HTML&gt;

&lt;HEAD&gt;

&lt;TITLE&gt;GIF Generation Service&lt;/TITLE&gt;

&lt;/HEAD&gt;

## &lt;BODY BGCOLOR="#FDF5E6"&gt;

&lt;H1 ALIGN="CENTER"&gt;GIF Generation Service&lt;/H1&gt; Welcome to the &lt;I&gt;free&lt;/I&gt; trial edition of our GIF generation service. Enter a message, a font name, and a font size below, then submit the form. You will be returned a GIF image showing the message in the designated font, with an oblique "shadow" of the message behind it. Once you get an image you are satisfied with, right click on it (or click while holding down the SHIFT key) to save it to your local disk.

&lt;P&gt;

The server is currently on Windows, so the font name must be either a standard Java font name (e.g., Serif, SansSerif, or Monospaced) or a Windows font name (e.g., Arial Black). Unrecognized font names will revert to Serif.

## &lt;FORM ACTION="/servlet/coreservlets.ShadowedText" &gt;

&lt;CENTER&gt;

Message:

&lt;INPUT TYPE="TEXT" NAME="message"&gt;&lt;BR&gt;

Font name:

&lt;INPUT TYPE="TEXT" NAME="fontName" VALUE="Serif"&gt;&lt;BR&gt;

Font size:

&lt;INPUT TYPE="TEXT" NAME="fontSize" VALUE="90"&gt;&lt;BR&gt;&lt;BR&gt;

&lt;Input TYPE="SUBMIT" VALUE="Build Image"&gt;

&lt;/CENTER&gt;

## &lt;/FORM&gt;

&lt;/BODY&gt;

&lt;/HTML&gt;

## Chapter 7 Generating the Server Response: HTTP Response Headers

Figure 7-5 Front end to ShadowedText servlet.

<!-- image -->

Figure 7-6 Using the GIF-generation servlet to build the logo for a children's books Web site. (Result of submitting the form shown in Figure 7-5).

<!-- image -->

## 7.5 Using Servlets to Generate GIF Images

<!-- image -->

Figure 7-7 Using the GIF-generation servlet to build the title image for a site describing a local theater company.

<!-- image -->

Figure 7-8 Using the GIF-generation servlet to build an image for a page advertising a local carnival.

<!-- image -->

## 176

## Chapter 7 Generating the Server Response: HTTP Response Headers

## Listing 7.11 ShadowedTextFrame.java

```
package coreservlets; import java.awt.*; import javax.swing.*; import java.awt.geom.*; /** Interactive interface to MessageImage class. *  Enter message, font name, and font size on the command *  line. Requires Java2. */ public class ShadowedTextFrame extends JPanel { private Image messageImage; public static void main(String[] args) { String message = "Shadowed Text"; if (args.length > 0) { message = args[0]; } String fontName = "Serif"; if (args.length > 1) { fontName = args[1]; } int fontSize = 90; if (args.length > 2) { try { fontSize = Integer.parseInt(args[2]); } catch(NumberFormatException nfe) {} } JFrame frame = new JFrame("Shadowed Text"); frame.addWindowListener(new ExitListener()); JPanel panel = new ShadowedTextFrame(message, fontName, fontSize); frame.setContentPane(panel); frame.pack(); frame.setVisible(true); } public ShadowedTextFrame(String message, String fontName, int fontSize) { messageImage = MessageImage.makeMessageImage(message, fontName, fontSize); int width = messageImage.getWidth(this); int height = messageImage.getHeight(this); setPreferredSize(new Dimension(width, height)); }
```

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 7.5 Using Servlets to Generate GIF Images

## Listing 7.11 ShadowedTextFrame.java (continued)

```
public void paintComponent(Graphics g) { super.paintComponent(g); g.drawImage(messageImage, 0, 0, this); } }
```

## Listing 7.12 ExitListener.java

```
package coreservlets; import java.awt.*; import java.awt.event.*; /** A listener that you attach to the top-level Frame or JFrame * of your application, so quitting the frame exits the app. */ public class ExitListener extends WindowAdapter { public void windowClosing(WindowEvent event) { System.exit(0); } }
```

<!-- image -->

Figure 7-9 ShadowedTextFrame application when invoked with ' java coreservlets.ShadowedTextFrame "Tom's Tools" Haettenschweiler

100 '.

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

<!-- image -->