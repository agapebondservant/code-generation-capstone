<# Instructions>
Beginning of specification from prior document. Additional details required for formatting the final answer to capture all necessary elements for code production.
<#> - **Inputs**
****
**Input Handling:**
- Users prepare content pages with HTML and JSP fragments, annotating areas where content can be substituted using placeholders. 
- Master templates define these placeholders as accessible through JSP tags.
****

**Output Handling:**
- Upon request, the system assembles the final rendered page by combining the master template with the dynamically provided content, respecting the specified parameters and structure.
<#> - **Business Rules**
****
**Business Rules:**
- Content modified outside the master template should override or supplement the master's designated regions without disrupting the overall layout. 
- Parameters passed via JSP tags should influence content presentation, leveraging predefined scopes and defaults.
****

**Success Criteria:**
- The system enables seamless integration of distinct content elements into a unified layout without breaking semantic HTML or CSS flow. 
- Content authors can effectively use the layout tags to structure pages, demonstrating ease of use and anticipate required adjustments. 
- Applications built using this framework can be styled and updated independently of the content layout logic.
<inputs>
<#> - **Test Requirements**
****

**Backend Tests:**
1. Write unit tests for all services, controllers, and utility functions. 
2. Use a mock testing framework like Jest (or Mocha/Chai) as the testing framework. Mock database calls, external API requests, and dependencies. 
3. Aim for high code coverage (70%+ minimum). 

**Frontend Tests:**
1. Write unit tests for the React components. 
2. Use a mock testing framework like Jest and React Testing Library as the testing framework. 
3. Aim for high code coverage (70+% minimum).
<#> - **Error handling**
****

**Sandwitch Operation:**
- Ensure that when UX error states are triggered the app should show an error alert placeholder section that is within the main layout break. 
*Displays an error message within the main layout placeholder if the content retrieval fails or an invalid parameter is passed.*
****



### MasterTag
```java
/*@Tag(description="Show body of master page with placeholders for ParamaterTag content.", requestColumn="body", commentColumn="comment")*/
public class MasterTag extends JSPUIMasterTag {

    private List<String> bodyList = new ArrayList<>();

    @Subscribe
    public void setBody(JSPPlaceholderTag bodyTag) throws JspException {
        for(JSPBodyContentHelper bh : bodyTag.getCompostiteList()) {
            bodyList.add(0, bh.getBody());
        }
    }


    @Override
    public void setMasterPage(PrintStreamWriter writer) throws JspException {
        MasterTag masterTag = super.getMasterPageWriter(bodyList, commentList);
        writer.write("<html>");
        writer.write("<head>");
        writer.write("<title>");
        writer.write((String) getAttribute("title"));
        writer.write("</title>");
        writer.write("<meta name=\"REPLACETHISWITHPARTIALSSECTION\" content=\"%PLACE%\" />");
        writer.write("<style type=\"text/css\">");
        writer.write("  body {background: #F76893; font-family: consolas, monospace;}");
        writer.write("</style>");
        writer.write("</head>");
        writer.write("<body>");
        writer.write("<div id=\"PLACEHOLDER\" class=\"MAIN_BODY\">%PLACE%</div>");
        writer.write("<div id=\"JSP_BODY\" class=\"PAGE_CONTENT\">%BODY%</div>");
        writer.write("</body>");
        writer.write("</html>");
    }
}
```
```<ENTITY></ENTITY>```  
**JSPHelper**
```java
public class JSPHelper {
    private String codeTagTemplate




```### Reaction Sheet
```java
public class ReactionSheet extends SimpleTagSupport {

    public void setDirection(String direction) {
        this.direction = direction;
    }

    public void setPage(String page) {
        this.page = page;
    }

    @Override
    public void doTag() throws JspException {
        // TODO: Implement page reaction logic
    }
    
    private String page;
    private String direction;
}
```


<#> - **Technologies**
****
I need to get familiar with Java Spring, Node.js, Express.js, and Spring Data JPA. For frontend, I will use React JS or React Native and TypeScript. Testing frameworks should include Jest and Mocha/Chai for Javascript testing, with jest-mock, mocks for simulating dependencies and DB etc. Need clear README instructions covering backend startup scripts, frontend serve commands, database setup, and integration steps.
<#> - **Framework Selection**
****
The core framework recommendation is Maven for Java projects setup and managing similar JS. Jest will be replacing Chai for script automation but Mocha remains viable alternative for backend if needed to be consistent with multi language testing strategies.
<#> - **Package & Version Requirements**
For the JSP module, Dropwizard spring javadfseved JSP repository access via artifacts required Maven coordinates. WebSocket Plus library.FileUploader binary feature packages managed by same Maven Cocoon serializer dependencies. Java UI must reference compatible version for core services usage - Jakarta EE doubles.
The package naming convention dictates: _core-jva-web-app-v2.fitools.launch[sprintf("%s.%s", Release, MasterVersion)]_ and use versioning strategy pattern to manage external plugins compatibility with version X.Y.Z.
JavaScript UI bundles: _react-boostrap-chart-template-utils-Jest[mask_] emerging unique identifiers from bundled file NameMask classes under appropriate module-Identifier naming strategy such!=-RCAPickl
```<Reaction Sheet>
```
<br>An overview of the structure and functionalities identified from the provided specifications needs to be accurately captured in the<br>final integration requirements.<br>
```
```<#> - **Architecture Diagram**
****
```java
1. Implement RESTful API using Spring Boot:
   ```java
   @RestController
   @RequestMapping("/api/master")
   public class MasterController {
       private final MasterTag masterTag;

       public MasterController(MasterTag masterTag) {
           this.masterTag = masterTag;
       }

       @GetMapping("/layout")
       public String getLayout(@RequestParam String template) {
           return masterTag.populateTemplate(template);
       }
   }
   ```
2. Set up database with Spring Data JPA connections in `application.properties`.
3. Create ER diagram for data models representing `MasterTag`, `ParameterTag`, and `Content`.
4. Design JUnit tests for service layer with JPA repository mocks.
5. Develop documentation site for deployment instructions in Maven format utilizing Javadoc JSP template formats.
<#> - **Readme Setup Documentation**
****
Document the setup instructions using Markdown including:
1. Development environment setup steps for Java and NodeJS.
2. Database schema creation via SQL scripts located in `/db/scripts`.
3. Build commands for backend and frontend.
4. Development server commands for React components and Spring Boot API.
5. Deployment procedures for UAT environment frh.
<#> - **Styling Guide**
****
Global styles should utilize Google Fonts API. Include buttons within components that trigger event alerts based on props. Replace placeholders in CSS within `<style>` tags when rendering dynamic content.
***<style>***  
*jsp-table-layout { width:auto;overflow:hidden;}<br>[comment] { display:block;}</style>***  
***  
```javascript
*import React from 'react';
*import { RenderTagContent, RenderBody } from './LayoutComponents';
***  
```  
```css
```<#> - **Unit Testing**
****
**Backend:**
- Write JUnit tests for all `MasterTag` implementations to ensure correct evaluation of placeholders with `@Test`.
- Manage templates with JSP directives (`$JSPDirectiveTag`) for dynamic replacement logic.<br>**Frontend:**
- Use Jest snapshot testing to validate UI markup structures against controlled component states using `render` from React Testing Library.<br>
<#> - **Documentation**
****
Include:
- Sample JSP page demonstrating master template usage with dynamic content replacement using `<jsp:param>`.
- Example REST endpoint demonstration in OpenAPI specification format.
- Metrics page showcasing `<metrics>` tags mapping to internal counters within project.<br>**Dependency Management Screenshots:**
- Include screenshots of Maven dependencies bar in IDE context for quick reference.<br>
```<#> - **Sprint Overview**
****
**Product Increment Push**: Handle rezoning exc {\
PRIORITY>HIGH[][]\
BUDGET>2023-09-02T23:59:59')


### Concepts
#### Master Templates
Lay the foundational structured overlay of UI components enabling modular parts integration with semantic spacing and unique identifiers.
#### Parameter Tags
Provide modularity leveraging JSP directives `<![CDATA[...]]>` for technical scope demarcation within master pages ensuring content robustness.
#### Action Methods
Strategize action method templates for dynamic UI states transition controls against managed state exchange patterns supporting responsive role adaptations.
#### Content Injection
Manage placeholders `<content-placeholder name="body">` structured declaratively defined by `ParameterTag` for webhook driven UI content augmentation design patterns.
#### Placeholders and Replacements
Integrate runtime content within structured `<div id="PLACEHOLDER">` layers facilitating peak dynamic re-render latencies without disrupting layout continuity requirements.
**End of Specification**  
<#> - **Metrics**
****
Metrics collections: 
- `/metrics` endpoint mirroring `/body` URI payload specifications.
- Naming standards for metrics instances match respective `ValueTag` placeholders encapsulating encapsulate endpoint identifier along servlet path components naming methodology.
-LAST CONTENT
    
```<#> - **Task Instructions**
****
Read the content of the specified spec document and write the code for a complete NodeJS and React application based on the provided specification. The code should include both backend and frontend components with comprehensive unit testing using mock objects. Backend Requirements (NodeJS):
1. Write the code for a RESTful API using Express.js or your preferred NodeJS framework.  2. Follow the services, data models, and business logic defined in the spec. Do NOT just develop a generic application.

Frontend Requirements (React):
1. Write the code for responsive UI components in React. 2. Develop the components according to the design specifications in the spec. Do NOT just develop a generic application. 
```