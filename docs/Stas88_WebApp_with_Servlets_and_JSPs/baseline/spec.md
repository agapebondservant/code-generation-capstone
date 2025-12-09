# Software Design Document (SDD)

## 1. System Architecture

### Overall Design
The system follows a **Model-View-Controller (MVC)** architectural pattern, which segregates the application into three interconnected components. This separation ensures that the system is modular, maintainable, and scalable.

### Key Components
- **DAO Objects (`DBModel`)**: Responsible for handling database interactions using JDBC. They implement the model interfaces to perform CRUD operations on `Dept`, `Emp`, and `Salgrade` entities.
- **Servlet Dispatcher (`DispatcherServlet`)**: Routes HTTP requests to appropriate servlet actions based on the path of the request. It manages the communication between the frontend (JSP views) and backend (action classes).
- **Action Classes** (`ViewEmpsAction`, `AddDeptAction`, `EditEmpAction`, etc.): Implement the `IAction` interface to handle specific actions like retrieving, displaying, adding, editing, and deleting records in the database.
- **Utility Classes** (`SRequest`): Serve as wrappers for `HttpServletRequest`, providing convenience methods to retrieve parameter values from requests.
- **JSP Views** (`DeptInfo.jsp`, `EmpInfo.jsp`, `DeptTable.jsp`, etc.): Generate dynamic content based on requests processed by the action classes. They are responsible for presenting the user interface.
- **Facade (`DispatcherServlet`)**: Acts as a front controller, handling requests and dynamically including the appropriate JSP views for rendering the user interface.

## 2. Functional Requirements

### Input Handling
- **Via HTTP Requests**: The system accepts inputs through HTTP GET and POST requests. Parameters from these requests are parsed and passed to the appropriate action objects for processing.

### Data Processing
- **CRUD Operations**: The system performs Create, Read, Update, and Delete operations on `Dept`, `Emp`, and `Salgrade` entities using the JDBC-based DAO implementation (`DBModel`). It involves querying, inserting, updating, and deleting records from the respective database tables.
- **Sorting and Searching**: Implementations for filtering and sorting records, such as `SortDepartmentsAction` and `SortEmployeesAction`, allow users to view records in various orders based on specified criteria.

### Output Generation
- **Dynamic Content**: The JSP views present data retrieved and manipulated by the action classes. They utilize JSTL for conditional expressions and iteration over collections to dynamically generate HTML content.
- **Presenter Patterns**: While not explicitly detailed, the system may employ presenter or view model patterns within the JSP pages to separate concerns and manage business logic encapsulated in action classes.

## 3. Business Requirements

### Business Rules
- **Department Management**: Operations on departments ensure data integrity, respecting constraints like valid department numbers and locations.
- **Employee Management**: Enforces rules on employee data, including valid assignments of managers and handling of salary increments.
- **Salary Grade Management**: Sets boundaries for salary grades, ensuring that entered minimum and maximum salaries adhere to specified rules.

### Success Criteria
- **Data Integrity**: The system must maintain the accuracy and consistency of data across all operations.
- **User Interface Responsiveness**: Actions must be swift, with minimal delay in processing requests and displaying results.
- **Error Handling and Validation**: Proper handling of invalid inputs and system errors, providing meaningful feedback to the user.
- **Scalability and Maintainability**: The architecture should be easily extendable to accommodate new features and maintainable for long-term use.

This Software Design Document outlines the universal aspects of the application's design, focusing on the MVC pattern, the roles of different components, and the functional and business requirements essential for the system's operation. The design emphasizes modularity and maintainability, ensuring that the system can be effectively developed, deployed, and scaled across various programming languages and frameworks, adhering to the outlined architecture and requirements.