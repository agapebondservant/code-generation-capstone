<!-- image -->

ne of the main motivations for building Web pages dynamically is so that the result can be based upon user input. This chapter shows you how to access that input. O

## 3.1 The Role of Form Data

If you've ever used a search engine, visited an on-line bookstore, tracked stocks  on  the  Web,  or  asked  a  Web-based  site  for  quotes  on plane tickets, you've probably seen funny-looking URLs like http://host/path?user=Marty+Hall&amp;origin=bwi&amp;dest=lax . The part after the question mark (i.e., user=Marty+Hall&amp;origin= bwi&amp;dest=lax ) is known as form data (or query data ) and is the most common way to  get  information  from  a  Web  page  to  a  server-side  program. Form data can be attached to the end of the URL after a question mark (as above), for GET requests, or sent to the server on a separate line, for POST requests.  If  you're  not  familiar  with  HTML  forms,  Chapter  16  (Using HTML Forms) gives details on how to build forms that collect and transmit data of this sort.

Extracting the needed information from this form data is traditionally one of the most tedious parts of CGI programming. First of all, you have to read