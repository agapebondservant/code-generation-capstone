## 12. Read the result.

The specific details will depend on what type of data the server sends. Here is an example that does something with each line sent by the server:

String line;

while((line = in.readLine()) != null) {

doSomethingWith(line);

}

## Bypassing the HTTP Server

Applets can talk directly to servers on their home host, using any of:

- · Raw sockets
- · Sockets with object streams
- • JDBC
- • RMI
- · Other network protocols

## A.17 Using Applets As Servlet Front Ends

- 7. Put the data into the buffer. For form data, use print . For
- 8. Set the Content-Length header. This header is required for POST data, even though it is unused with GET requests. connection.setRequestProperty ("Content-Length", String.valueOf(byteStream.size()));
- 9. Set the Content-Type header. Netscape uses multipart/form-data by default, but regular form data requires a setting of application/x-www-form-urlencoded , which is the default with Internet Explorer. So, for portability you should set this value explicitly when sending regular form data. The value is irrelevant when you are sending serialized data.

```
high-level serialized objects, use writeObject . String val1 = URLEncoder.encode(someVal1); String val2 = URLEncoder.encode(someVal2); String data = "param1=" + val1 + "&param2=" + val2; // Note '&' out.print(data); // Note print, not println out.flush(); // Necessary since no println used
```

connection.setRequestProperty

("Content-Type", "application/x-www-form-urlencoded");

## 10. Send the real data.

byteStream.writeTo(connection.getOutputStream());

- 11. Open an input stream. You typically use a BufferedReader for ASCII or binary data and an ObjectInputStream for serialized Java objects.

BufferedReader in =

new BufferedReader(new InputStreamReader

(connection.getInputStream()));