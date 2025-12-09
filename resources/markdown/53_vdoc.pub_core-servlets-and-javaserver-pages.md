' Prentice Hall and Sun Microsystems. Personal use only; do not redistribute.

## Chapter Handling the Client Request: HTTPRequest Headers

<!-- image -->

## Topics in This Chapter

- · Reading HTTP request headers from servlets
- · Building a table of all the request headers
- · The purpose of each of the HTTP 1.1 request headers
- · Reducing download times by compressing pages
- · Restricting access with password-protected servlets

Chapter

<!-- image -->

ne of the keys to creating effective servlets is understanding how to manipulate  the  HyperText  Transfer  Protocol  (HTTP).  Getting  a thorough grasp of this protocol is not an esoteric, theoretical topic, but rather a practical issue that can have an immediate impact on the performance and usability of your servlets. This chapter discusses the HTTP information  that  is  sent  from  the  browser  to  the  server  in  the  form  of  request headers. It explains each of the HTTP 1.1 request headers, summarizing how and why they would be used in a servlet.  The chapter  also  includes  three detailed examples: listing all request headers sent by the browser, reducing download time by encoding the Web page with gzip when appropriate, and establishing password-based access control for servlets. O

Note that  HTTP request headers are  distinct  from  the  form  data  discussed in the previous chapter. Form data results directly from user input and is sent as part of the URL for GET requests and on a separate line for POST requests. Request headers, on the other hand, are indirectly set by the browser and are sent immediately following the initial GET or POST request line.  For  instance,  the  following  example  shows  an  HTTP  request  that might  result  from  submitting a  book-search  request  to a servlet at http://www.somebookstore.com/search . The request includes the headers Accept , Accept-Encoding , Connection , Cookie , Host , Referer ,  and User-Agent , all of which might be important to the operation of the servlet, but none of which can be derived from the form data or deduced auto-