## Chapter Generating the Server Response: HTTPStatus Codes

<!-- image -->

## Topics in This Chapter

- · The purpose of HTTP status codes
- · The way to specify status codes from servlets
- · The meaning of each of the HTTP 1.1 status code values
- · A servlet that uses status codes to redirect users to other sites and to report errors

Chapter

<!-- image -->

hen a Web server responds to a request from a browser or other Web client, the response typically consists of a status line, some response  headers,  a  blank  line,  and  the  document.  Here  is  a minimal example: W

HTTP/1.1 200 OK

Content-Type: text/plain

Hello World

The status line consists of the HTTP version ( HTTP/1.1 in  the  example above), a status code (an integer; 200 in the above example), and a very short message corresponding to the status code ( OK in the example). In most cases, all of the headers are optional except for Content-Type , which specifies the MIME type of the document that follows. Although most responses contain a document,  some  don't.  For  example,  responses  to HEAD requests  should never include a document, and there are a variety of status codes that essentially indicate failure and either don't include a document or include only a short error message document.

Servlets can perform a variety of important tasks by manipulating the status line and the response headers. For example, they can forward the user to other sites; indicate that the attached document is an image, Adobe Acrobat file, or HTML file; tell the user that a password is required to access the document; and so forth. This chapter discusses the various status codes and what