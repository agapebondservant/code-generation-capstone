## 1.3 JavaServer Pages

100-element array then write into the 999th 'element,' which is really some random part of program memory. So programmers who forget to do this check themselves open their system up to deliberate or accidental buffer overflow attacks. Servlets suffer from neither of these problems. Even if a servlet executes a remote system call to invoke a program on the local operating system, it does not use a shell to do so. And of course array bounds checking  and  other  memory  protection features  are  a  central part  of the Java programming language.

## Inexpensive

There are a number of free or very inexpensive Web servers available that are good for 'personal' use or low-volume Web sites. However, with the major exception of Apache, which is free, most commercial-quality Web servers are relatively expensive. Nevertheless, once you have a Web server, no matter its cost, adding servlet support to it (if it doesn't come preconfigured to support servlets) costs very little extra. This is in contrast to many of the other CGI alternatives, which require a significant initial investment to purchase a proprietary package.

## 1.3 JavaServer Pages

JavaServer Pages (JSP) technology enables you to mix regular, static HTML with  dynamically  generated  content  from  servlets.  Many  Web  pages  that are built by CGI programs are primarily static, with the parts that change limited  to  a  few  small  locations.  For  example,  the  initial  page  at  most on-line stores is the same for all visitors, except for a small welcome message  giving  the  visitor's  name  if  it  is  known.  But  most  CGI  variations, including  servlets,  make  you  generate  the  entire  page  via  your  program, even though most of it is always the same. JSP lets you create the two parts separately. Listing 1.1 gives an example. Most of the page consists of regular HTML, which is passed to the visitor unchanged. Parts that are generated dynamically are marked with special HTML-like tags and mixed right into the page.

9