# Software Design Document (SDD)

## 1. System Architecture

### Overall Design
The system implements a **centralized request-dispatch architecture** with clear separation of concerns. The design follows these principles:

- **Request Routing**: A central dispatcher component routes incoming requests to appropriate handlers based on URL patterns
- **Layered Architecture**: The system is organized into distinct layers:
  - **Presentation Layer**: Handles user interactions and request/response cycles
  - **Business Logic Layer**: Processes business rules and coordinates data operations
  - **Data Access Layer**: Manages data persistence and retrieval operations
- **Interface-Based Design**: Components communicate through well-defined interfaces, enabling loose coupling and flexibility
- **Stateless Processing**: Each request is processed independently, supporting scalability

### Key Components

| Component | Responsibility |
|-----------|---------------|
| **Request Dispatcher** | Routes incoming requests to appropriate action handlers based on URL mapping |
| **Action Handler Interface** | Defines the contract for all business operation handlers |
| **Action Handlers** | Execute specific business operations (add, find, edit, remove) for organizational entities |
| **Data Access Interface** | Defines the contract for data persistence operations |
| **Data Access Implementation** | Provides concrete implementation of data operations against the data store |
| **Domain Model** | Represents core business entities: Department, Employee, and Salary Grade |

**Domain Model Entities:**
- **Department (`Dept`)**: Represents organizational departments with unique identifiers and attributes
- **Employee (`Emp`)**: Represents staff members with employment details and departmental associations
- **Salary Grade (`SalGrade`)**: Defines compensation tiers with minimum and maximum salary ranges

## 2. Functional Requirements

### Input Handling
- The system accepts requests through URL-based routing, where each URL corresponds to a specific business operation
- Request parameters are extracted and validated from incoming requests
- The dispatcher analyzes the request path and instantiates the appropriate action handler

### Data Processing

**Request Processing Flow:**
1. The dispatcher receives an incoming request and identifies the target action handler
2. Request parameters are extracted and passed to the action handler
3. The action handler performs business logic operations, including:
   - Parameter validation and transformation
   - Invocation of data access operations to retrieve or modify data
   - Application of business rules and constraints
   - Preparation of response data

**Core Business Operations:**
- **Create Operations**: Add new departments, employees, or salary grades to the system
- **Retrieve Operations**: Find and fetch existing records based on search criteria
- **Update Operations**: Modify attributes of existing organizational entities
- **Delete Operations**: Remove records from the system while maintaining data integrity

### Output Generation
- Action handlers prepare results for presentation to the user
- Results are formatted and rendered through presentation templates
- The system provides feedback messages indicating operation success or failure
- Navigation options are presented to support workflow continuation

## 3. Business Requirements

### Business Rules

1. **Entity Uniqueness**
   - Department identifiers must be unique across the system
   - Employee identifiers must be unique across the system
   - No duplicate records are permitted during creation or update operations

2. **Organizational Hierarchy**
   - Employees must be associated with valid departments
   - Employees may have supervisor relationships with other employees
   - Supervisor relationships must maintain logical consistency within the organizational structure

3. **Compensation Constraints**
   - Salary grades define valid compensation ranges with minimum and maximum boundaries
   - Employee salaries must align with established salary grade definitions
   - Salary grade ranges must not overlap or create ambiguities

4. **Data Integrity**
   - All entity relationships must be maintained consistently
   - Deletion operations must consider dependent relationships
   - Updates must preserve referential integrity across entities

### Success Criteria

1. **Functional Completeness**
   - The system successfully executes all CRUD (Create, Read, Update, Delete) operations for departments, employees, and salary grades
   - All business rules are enforced consistently across operations

2. **Performance**
   - The system processes requests and updates organizational data in real-time
   - Database operations complete without degrading user experience

3. **Reliability**
   - Transaction failures are handled gracefully with appropriate rollback mechanisms
   - Data consistency and integrity are maintained even in error scenarios
   - The system provides clear error messages for failed operations

4. **Usability**
   - Users can navigate the system intuitively without technical expertise
   - Form submissions and data entry processes are straightforward
   - Operation results and system feedback are clearly communicated

5. **Maintainability**
   - The modular architecture allows for independent modification of components
   - New action handlers can be added without disrupting existing functionality
   - Business rules can be updated without requiring architectural changes