## Chapter 17 Using Applets As Servlet Front Ends

## Listing 17.2 ParallelSearches.html

&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Frameset//EN"&gt;

```
<HTML> <HEAD> <TITLE>Parallel Search Engine Results</TITLE> </HEAD> <FRAMESET ROWS="120,*"> <FRAME SRC="SearchAppletFrame.html" SCROLLING="NO"> <FRAMESET COLS="*,*,*"> <FRAME SRC="GoogleResultsFrame.html" NAME="results0"> <FRAME SRC="InfoseekResultsFrame.html" NAME="results1"> <FRAME SRC="LycosResultsFrame.html" NAME="results2"> </FRAMESET> </FRAMESET>
```

## Listing 17.3 SearchAppletFrame.html

&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"&gt; &lt;HTML&gt; &lt;HEAD&gt; &lt;TITLE&gt;Search Applet Frame&lt;/TITLE&gt; &lt;/HEAD&gt; &lt;BODY BGCOLOR="WHITE"&gt; &lt;CENTER&gt; &lt;APPLET CODE="SearchApplet.class" WIDTH=600 HEIGHT=100&gt; &lt;B&gt;This example requires a Java-enabled browser.&lt;/B&gt; &lt;/APPLET&gt; &lt;/CENTER&gt; &lt;/BODY&gt; &lt;/HTML&gt;

## 17.3 Sending Data with GET and Processing the Results Directly (HTTP Tunneling)

In the previous example, an applet instructs the browser to display the output of a server-side program in a particular frame. Using the browser to display results  is  a  reasonable  approach  when working with existing services, since

## 17.3 Sending Data with GET and Processing the Results Directly

most CGI programs are already set up to return HTML documents. However, if you are developing both the client and the server sides of the process, it  seems a bit wasteful to always send back an entire HTML document; in some cases, it would be nice to simply return data to an applet that is already running. The applet could then present the data in a graph or some other custom display. This approach is sometimes known as HTTP tunneling since a custom communication protocol is embedded within HTTP: proxies, encryption, server redirection, connections through firewalls, and all.

There are two main variations to this approach. Both make use of the URLConnection class to open an input stream from a URL. The difference lies in the  type  of  stream  they  use.  The  first  option  is  to  use  a BufferedInputStream or  some  other low-level stream that lets you read binary or ASCII data from an arbitrary server-side program. That approach is covered in the first  subsection.  The  second  option  is  to  use  an ObjectInputStream to directly read high-level data structures. That approach, covered in the second subsection, is available only when the server-side program is also written in the Java programming language.

## Reading Binary or ASCII Data

An applet can read the content sent by the server by first creating a URLConnection derived from the URL of the server-side program and then attaching  a BufferedInputStream to  it.  Seven  main  steps  are  required  to implement this approach on the client, as described below. I'm omitting the server-side  code  since  the  client  code  described  here  works  with  arbitrary server-side programs or static Web pages.

Note that many of the stream operations throw an IOException ,  so  the following statements need to be enclosed in a try / catch block.

## 1. Create a URL object referring to applet's home host. You

can pass an absolute URL string to the URL constructor (e.g., "http://host/path" ), but since browser security restrictions prohibit connections from applets to machines other than the home server, it makes more sense to build a URL based upon the hostname from which the applet was loaded.

```
URL currentPage = getCodeBase(); String protocol = currentPage.getProtocol(); String host = currentPage.getHost(); int port = currentPage.getPort(); String urlSuffix = "/servlet/SomeServlet"; URL dataURL = new URL(protocol, host, port, urlSuffix);
```

440

## Chapter 17 Using Applets As Servlet Front Ends

- 2. Create a URLConnection object. The openConnection method of URL returns a URLConnection object. This object will be used to obtain streams with which to communicate.
- URLConnection connection = dataURL.openConnection();
- 3. Instruct the browser not to cache the URL data. The first thing you do with the URLConnection object is to specify that the browser not cache it. This guarantees that you get a fresh result each time.

connection.setUseCaches(false);

- 4. Set any desired HTTP headers. If you want to set HTTP request headers (see Chapter 4), you can use setRequestProperty to do so.

connection.setRequestProperty("header", "value");

- 5. Create an input stream. There are a variety of appropriate streams, but a common one is BufferedReader . It is at the point where you create the input stream that the connection to the Web server is actually established behind the scenes.

BufferedReader in =

new BufferedReader(new InputStreamReader( connection.getInputStream()));

- 6. Read each line of the document. The HTTP specification stipulates that the server closes the connection when it is done. When the connection is closed, readLine returns null . So, simply read until you get null .

```
String line; while ((line = in.readLine()) != null) { doSomethingWith(line);
```

}

- 7. Close the input stream.

in.close();

## 17.3 Sending Data with GET and Processing the Results Directly

## Reading Serialized Data Structures

The approach shown in the previous subsection makes good sense when your  applet  is  talking  to  an  arbitrary  server-side  program  or  reading  the content of static Web pages. However, when an applet talks to a servlet, you  can  do  even  better.  Rather  than  sending  binary  or  ASCII  data,  the servlet can transmit arbitrary data structures by using the Java serialization mechanism. The applet can read this data in a single step by using readObject ; no long and tedious parsing is required. The steps required to implement  HTTP  tunneling  are  summarized  below.  Again,  note  that  the statements  need  to  be  enclosed  within  a try / catch block  in  your  actual applet.

## The Client Side

An applet needs to perform the following seven steps to read serialized data structures sent by a servlet. Only Steps 5 and 6 differ from what is required to read ASCII data. These steps are slightly simplified by the omission of the try / catch blocks.

- 1. Create a URL
- As before, since the URL must refer to the host from which the suffix and construct the rest of the URL automatically.
- object referring to the applet's home host. applet was loaded, it makes the most sense to specify a URL
- 2. Create a URLConnection object. The openConnection method of URL returns a URLConnection object. This object will be used to obtain streams with which to communicate.

```
URL currentPage = getCodeBase(); String protocol = currentPage.getProtocol(); String host = currentPage.getHost(); int port = currentPage.getPort(); String urlSuffix = "/servlet/SomeServlet"; URL dataURL = new URL(protocol, host, port, urlSuffix);
```

URLConnection connection = dataURL.openConnection();

- 3. Instruct the browser not to cache the URL data. The first thing you do with the URLConnection object is to specify that the browser not cache it. This guarantees that you get a fresh result each time.

connection.setUseCaches(false);

## Chapter 17 Using Applets As Servlet Front Ends

- 4. Set any desired HTTP headers. If you want to set HTTP request headers (see Chapter 4), you can use setRequestProperty to do so.

connection.setRequestProperty("header", "value");

- 5. Create an ObjectInputStream . The constructor for this class simply takes the raw input stream from the URLConnection . It is at the point where you create the input stream that the connection to the Web server is actually established.

ObjectInputStream in =

new ObjectInputStream(connection.getInputStream());

- 6. Read the data structure with readObject . The return type of readObject is Object , so you need to make a typecast to whatever more specific type the server actually sent.

SomeClass value = (SomeClass)in.readObject(); doSomethingWith(value);

- 7. Close the input stream.

in.close();

## The Server Side

A servlet needs to perform the following four steps to send serialized data structures to an applet. Assume that request and response are the HttpServletRequest and HttpServletResponse objects supplied to the doGet and doPost methods. Again, these steps are simplified slightly by the omission of the required try / catch blocks.

- 1. Specify that binary content is being sent. This task is accomplished by designating

application/x-java-serialized-object as the MIME type of the response. This is the standard MIME type for objects encoded with an ObjectOutputStream , although in practice, since the applet (not the browser) is reading the result, the MIME type is not very important. See the discussion of Content-Type in Section 7.2 (HTTP 1.1 Response Headers and Their Meaning) for more information on MIME types.

String contentType =

- "application/x-java-serialized-object";

response.setContentType(contentType);