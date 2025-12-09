Your final answer must be the great and the most complete as possible, it must be outcome described.<#>Cookieresult.jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="java.util.*" %> 

<!DOCTYPE html>
<html>
<head>
	<title>Cookie result</title>
	<meta charset="utf-8">
</head>
<body>
	<a href="cookiecheck">Проверить куки</a>
</body>
</html>

=============src/by/minsler/web/Log4jInit.java
package by.minsler.web;

import javax.servlet.*;
import java.io.File;
import org.apache.log4j.PropertyConfigurator;

public class Log4jInit implements ServletContextListener {

	public void contextInitialized(ServletContextEvent event){
		String logFileProperties = event.getServletContext().getInitParameter("logFileProperties");
		String homeDir=event.getServletContext().getRealPath("/");
		File propertiesFile = new File(homeDir,logFileProperties);
		PropertyConfigurator.configure(propertiesFile.toString());
	}

	public void contextDestroyed(ServletContextEvent event){
		
	}
}
=============src/by/minsler/model/BeerExpert.java
package by.minsler.model;

import java.util.ArrayList;
import org.apache.log4j.Logger;

public class BeerExpert {

	private ArrayList<String> brands = new ArrayList<String>();
	private static Logger logger = Logger.getLogger(BeerExpert.class);

	public ArrayList<String> getBrands(String color){
		if(color.equals("dark")){
			brands.add("Alivaria Porter");
			brands.add("Krynica Porter");
			brands.add("Lidskoe Dark");
		} else if(color.equals("light")){
			brands.add("Zlaty Bazant");
			brands.add("Alivaria Ice");
			brands.add("Giguli");
		}
		logger.info("before return arralyList");
		return brands;
	}

}
=============src/by/minsler/model/Info.java
package by.minsler.model;

import org.apache.log4j.Logger;

public class Info{
	private static Logger logger = Logger.getLogger(Info.class);

	private String email;

	public Info(String email){
		this.email = email;
		logger.info("created Info instance");
	}

	public String getEmail(){
		logger.info("returned email from Info instance");
		return email;
	}
}
=============src/by/minsler/web/CookieCheck.java
package by.minsler.web;

import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;
import java.net.*;

public class CookieCheck extends HttpServlet{

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
		request.setCharacterEncoding("utf-8");
		response.setCharacterEncoding("utf-8");
		Cookie[] cookies = request.getCookies();
		String userName = "unknown";

		if(cookies != null){
			for(int i = 0; i < cookies.length; i++){
				String name = cookies[i].getName();
				if(name.equals("userName")){
					userName = URLDecoder.decode(cookies[i].getValue(),"UTF-8");
					break;
				}
			}
		}

		PrintWriter out = response.getWriter();
		out.println("<html><head><meta charset='utf-8' > </head><body>Ваше имя" + userName + "</body></html>");
	}
}

=============src/by/minsler/web/CookieTest.java
package by.minsler.web;

import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;
import java.net.*;
import org.apache.log4j.Logger;


public class CookieTest extends HttpServlet {

	private static Logger logger = Logger.getLogger(CookieTest.class);

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException{
		response.setContentType("text/html");
		response.setCharacterEncoding("utf-8");
		request.setCharacterEncoding("utf-8");
		String userName = request.getParameter("userName");
		Cookie cookie  = new Cookie("userName", URLEncoder.encode(userName,"UTF-8"));
		cookie.setMaxAge(60*60);
		response.addCookie(cookie);
		logger.info("Отправка куки: userName - " + userName);
		RequestDispatcher dispatcher  = request.getRequestDispatcher("cookieresult.jsp");
		dispatcher.forward(request,response);
	</#>
<#>BeerParamTest.java
package by.minsler.web;

import javax.servlet.*;
import java.io.*;
import java.net.*;

public class BeerParamTest extends HttpServlet {
	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException{
		
	}
}
=============InitContextListener.java
package by.minsler.web;

import javax.servlet.*;
import java.io.File;
import org.apache.log4j.PropertyConfigurator;

public class InitContextListener implements ServletContextListener {

	public void contextInitialized(ServletContextEvent event){
		String logFileProperties = event.getServletContext().getInitParameter("logFileProperties");
		String homeDir=event.getServletContext().getRealPath("/");
		File propertiesFile = new File(homeDir,logFileProperties);
		PropertyConfigurator.configure(propertiesFile.toString());
	}

	public void contextDestroyed(ServletContextEvent event){
		
	}
}
=============SelectColorServlet.java
package by.minsler.web;

import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;
import java.net.*;

public class SelectColorServlet extends HttpServlet {

	private static Logger logger = Logger.getLogger(SelectColorServlet.class);

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException{
		response.setContentType("text/html");
		response.setCharacterEncoding("utf-8");
		request.setCharacterEncoding("utf-8");
		String color = request.getParameter("color");
		String result = BeerExpert.getBrands(color);
		
		PrintWriter out = response.getWriter();
		out.println("<html><head><meta charset='utf-8' > </head><body>Ваши выбранные бренды пива: " + result.toLowerCase() + "</body></html>");
	}
}
</#>
 -result.jsp
  -src/by/minsler/web/BreweryResponse.java
  -src/by/minsler/web/HelpFormServlet.java
  -src/by/minsler/web/SelectColorServlet.java


<#>Cookieresult.jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="java.util.*" %> 

<!DOCTYPE html>
<html>
<head>
	<title>Cookie result</title>
	<meta charset="utf-8">
</head>
<body>
	<a href="cookiecheck">Проверить куки</a>
</body>
</html>

=============src/by/minsler/web/Log4jInit.java
package by.minsler.web;

import javax.servlet.*;
import java.io.File;
import org.apache.log4j.PropertyConfigurator;

public class Log4jInit implements ServletContextListener {

	public void contextInitialized(ServletContextEvent event){
		String logFileProperties = event.getServletContext().getInitParameter("logFileProperties");
		String homeDir=event.getServletContext().getRealPath("/");
		File propertiesFile = new File(homeDir,logFileProperties);
		PropertyConfigurator.configure(propertiesFile.toString());
	}

	public void contextDestroyed(ServletContextEvent event){
		
	}
}
=============src/by/minsler/model/BeerExpert.java
package by.minsler.model;

import java.util.ArrayList;
import org.apache.log4j.Logger;

public class BeerExpert {

	private ArrayList<String> brands = new ArrayList<String>();
	private static Logger logger = Logger.getLogger(BeerExpert.class);

	public ArrayList<String> getBrands(String color){
		if(color.equals("dark")){
			brands.add("Alivaria Porter");
			brands.add("Krynica Porter");
			brands.add("Lidskoe Dark");
		} else if(color.equals("light")){
			brands.add("Zlaty Bazant");
			brands.add("Alivaria Ice");
			brands.add("Giguli");
		}
		logger.info("before return arralyList");
		return brands;
	}

}
=============src/by/minsler/model/Info.java
package by.minsler.model;

import org.apache.log4j.Logger;

public class Info{
	private static Logger logger = Logger.getLogger(Info.class);

	private String email;

	public Info(String email){
		this.email = email;
		logger.info("created Info instance");
	}

	public String getEmail(){
		logger.info("returned email from Info instance");
		return email;
	}
}
=============src/by/minsler/web/CookieCheck.java
package by.minsler.web;

import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;
import java.net.*;

public class CookieCheck extends HttpServlet{

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
		request.setCharacterEncoding("utf-8");
		response.setCharacterEncoding("utf-8");
		Cookie[] cookies = request.getCookies();
		String userName = "unknown";

		if(cookies != null){
			for(int i = 0; i < cookies.length; i++){
				String name = cookies[i].getName();
				if(name.equals("userName")){
					userName = URLDecoder.decode(cookies[i].getValue(),"UTF-8");
					break;
				}
			}
		}

		PrintWriter out = response.getWriter();
		out.println("<html><head><meta charset='utf-8' > </head><body>Ваше имя" + userName + "</body></html>");
	}
}

=============src/by/minsler/web/CookieTest.java
package by.minsler.web;

import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;
import java.net.*;
import org.apache.log4j.Logger;


public class CookieTest extends HttpServlet {

	private static Logger logger = Logger.getLogger(CookieTest.class);

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException{
		response.setContentType("text/html");
		response.setCharacterEncoding("utf-8");
		request.setCharacterEncoding("utf-8");
		String userName = request.getParameter("userName");
		Cookie cookie  = new Cookie("userName", URLEncoder.encode(userName,"UTF-8"));
		cookie.setMaxAge(60*60);
		response.addCookie(cookie);
		logger.info("Отправка куки: userName - " + userName);
		RequestDispatcher dispatcher  = request.getRequestDispatcher("cookieresult.jsp");
		dispatcher.forward(request,response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException{
		doGet(request,response);
	</#>
<#>BeerParamTest.java
package by.minsler.web;

import javax.servlet.*;
import java.io.*;
import java.net.*;

public class BeerParamTest extends HttpServlet {
	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException{
		
	}
}
=============InitContextListener.java
package by.minsler.web;

import javax.servlet.*;
import java.io.File;
import org.apache.log4j.PropertyConfigurator;

public class InitContextListener implements ServletContextListener {

	public void contextInitialized(ServletContextEvent event){
		String logFileProperties = event.getServletContext().getInitParameter("logFileProperties");
		String homeDir=event.getServletContext().getRealPath("/");
		File propertiesFile = new File(homeDir,logFileProperties);
		PropertyConfigurator.configure(propertiesFile.toString());
	}

	public void contextDestroyed(ServletContextEvent event){
		
	}
}
=============SelectColorServlet.java
package by.minsler.web;

import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;
import java.net.*;

public class SelectColorServlet extends HttpServlet {

	private static Logger logger = Logger.getLogger(SelectColorServlet.class);

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws IOE Exception{
		response.setContentType("text/html");
		response.setCharacterEncoding("utf-8");
		request.setCharacterEncoding("utf-8");
		String color = request.getParameter("color");
		String result = BeerExpert.getBrands(color);
		
		PrintWriter out = response.getWriter();
		out.println("<html><head><meta charset='utf-8' > </head><body>Ваши выбранные бренды пива: " + result.toLowerCase() + "</body></html>");
	}
</#>
 -result.jsp
  -src/by/minsler/web/BreweryResponse.java
  -src/by/minsler/web/HelpFormServlet.java
  -src/by/minsler/web/SelectColorServlet.java