# Software Design Document (SDD)
## Cricket Club Management System

---

## 1. System Architecture

### Overall Design
The system follows a layered architecture pattern that separates concerns into three distinct tiers:

- **Presentation Layer:** Manages user interface elements and user interactions through web pages
- **Application Layer:** Processes business logic and coordinates data flow between the presentation and data layers
- **Data Access Layer:** Handles all database operations and data persistence

This modular design promotes maintainability, scalability, and clear separation of responsibilities across components.

### Key Components

**Presentation Components:**
- **index:** Navigation interface providing access to primary system functions
- **insert:** Form interface for capturing new member information
- **search:** Form interface for querying member records by last name

**Application Components:**
- **regServlet:** Central request handler that routes search queries and data submissions
- **regInsert:** Processes member data submissions and coordinates with data access utilities
- **regSearchAll:** Manages member search operations and result retrieval

**Domain Model:**
- **reg:** Represents a cricket club member entity with properties including first name, middle name, last name, and date of birth

**Utility Components:**
- **regUtil:** Data access utility providing methods for database operations including data retrieval, insertion, and updates

---

## 2. Functional Requirements

### Input Handling
The system accepts user input through two primary interfaces:

1. **Member Registration:** Captures member details (first name, middle name, last name, date of birth) through a structured form
2. **Member Search:** Accepts last name as a search parameter through a query form

### Data Processing

**Member Registration Process:**
- Validates incoming member data from the registration form
- Invokes the data utility to persist member information to the database
- Returns confirmation of successful registration

**Member Search Process:**
- Receives last name search criteria
- Queries the database through the data utility to retrieve matching member records
- Compiles search results for presentation

**Core Data Operations:**
- **getData:** Retrieves individual member record by last name
- **getAllData:** Fetches all member records matching a last name
- **saveData:** Persists new member information to the database
- **updateData:** Modifies existing member records

### Output Generation

**Registration Confirmation:**
Upon successful member data insertion, the system returns the user to the registration interface with a success notification confirming the operation.

**Search Results:**
Search operations generate a results view displaying all members matching the provided last name, presenting relevant member details in a structured format.

---

## 3. Business Requirements

### Business Rules

1. **Member Registration:** The system must allow authorized users to register new cricket club members with complete and validated information
2. **Member Search:** Users must be able to search and retrieve member records using last name as the primary search criterion
3. **Data Validation:** All member information must be validated before persistence to ensure data integrity
4. **Unique Identification:** Each member record must be uniquely identifiable within the system

### Success Criteria

1. **Data Accuracy:** New member records are stored accurately with all provided information preserved correctly in the database
2. **Search Precision:** Search functionality returns accurate results matching the last name criteria with 100% accuracy
3. **System Reliability:** The system successfully processes member registration and search requests without errors
4. **Response Time:** Search and registration operations complete within acceptable timeframes for optimal user experience
5. **Data Integrity:** All database operations maintain referential integrity and prevent data corruption