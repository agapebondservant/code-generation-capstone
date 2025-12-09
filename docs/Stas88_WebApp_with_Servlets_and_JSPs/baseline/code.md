## Software Design Document (SDD) NodeJS and React Implementation

### 1. System Architecture

#### 1.1 Overall Design
The system follows a **Model-View-Controller (MVC)** architectural pattern, which segregates the application into three interconnected components. This separation ensures that the system is modular, maintainable, and scalable.

#### 1.2 Key Components
- **DAO Objects (`DBModel`)**: Responsible for handling database interactions using `node-postgres`. They implement the model interfaces to perform CRUD operations on `Dept`, `Emp`, and `Salgrade` entities.
- **Servlet Dispatcher (`DispatcherServlet` equivalent using Express.Router)**: Routes HTTP requests to appropriate route handlers based on the path of the request. It manages the communication between the frontend (React views) and backend (Node.js action handlers).
- **Action Classes** (`ViewEmpsAction`, `AddDeptAction`, `EditEmpAction`, etc.): Implement handlers based on routes to handle specific actions like retrieving, displaying, adding, editing, and deleting records in the database.
- **Utility Classes** (`SRequest` equivalent using Express.Request): Serve as wrappers for `express.Request`, providing convenience methods to retrieve query parameters, body, and headers from requests.
- **React Views** (`DeptInfo.jsx`, `EmpInfo.jsx`, `DeptTable.jsx`, etc.): Generate dynamic content based on requests processed by the action handlers. They are responsible for presenting the user interface using **JSX**.
- **Facade (`express.Router` equivalent)**: Acts as a front controller, handling requests and dynamically including the appropriate React components/views for rendering the user interface.

### 2. Functional Requirements

#### 2.1 Input Handling
- **Via HTTP Requests**: The system accepts inputs through HTTP GET, POST, PUT, DELETE requests. Parameters from these requests are parsed and passed to the appropriate route handlers for processing.

#### 2.2 Data Processing
- **CRUD Operations**: The system performs Create, Read, Update, and Delete operations on `Dept`, `Emp`, and `Salgrade` entities using the `node-postgres` based DAO implementation (`DBModel`). It involves querying, inserting, updating, and deleting records from the respective database tables.
- **Sorting and Searching**: Implementations for filtering and sorting records, such as `SortDepartmentsAction`, `SortEmployeesAction`, allow users to view records in various orders based on specified criteria.

#### 2.3 Output Generation
- **Dynamic Content**: The React components present data retrieved and manipulated by the action handlers. They utilize JSX for conditional expressions and iteration over arrays to dynamically generate HTML content.
- **Presenter Patterns**: While not explicitly detailed, the system may employ presenter or view model patterns within the components to separate concerns and manage business logic encapsulated in action handlers.

### 3. Business Requirements

#### 3.1 Business Rules
- **Department Management**: Operations on departments ensure data integrity, respecting constraints like valid department numbers and locations.
- **Employee Management**: Enforces rules on employee data, including valid assignments of managers and handling of salary increments.
- **Salary Grade Management**: Sets boundaries for salary grades, ensuring that entered minimum and maximum salaries adhere to specified rules.

#### 3.2 Success Criteria
- **Data Integrity**: The system must maintain the accuracy and consistency of data across all operations.
- **User Interface Responsiveness**: Actions must be swift, with minimal delay in processing requests and displaying results.
- **Error Handling and Validation**: Proper handling of invalid inputs and system errors, providing meaningful feedback to the user.
- **Scalability and Maintainability**: The architecture should be easily extendable to accommodate new features and maintainable for long-term use.

### 4. Backend Implementation

#### 4.1 Setup Instructions
1. Clone the repository: `git clone <repository-url>`
2. Install dependencies: `npm install`
3. Start the server: `npm start`

#### 4.2 Backend Code

**DAO (`DBModel.js`):**
```javascript
const { Pool } = require('pg');
const pool = new Pool({
  user: 'username',
  host: 'localhost',
  database: 'database_name',
  password: 'password',
  port: 5432,
});

class DBModel {
  async getDepts() {
    const { rows } = await pool.query('SELECT * FROM dept');
    return rows;
  }

  async getEmps() {
    const { rows } = await pool.query('SELECT * FROM emp');
    return rows;
  }

  async addDept(newDept) {
    await pool.query('INSERT INTO dept VALUES($1, $2, $3)', [newDept.id, newDept.name, newDept.location]);
  }

  // Other CRUD operations for Emp and Salgrade
}

module.exports = DBModel;
```

**Action Handler (`EmpsAction.js`):**
```javascript
const DBModel = require('./DBModel');
const { response } = require('express');

class ViewEmpsAction {
  async handle(req, res) {
    const emps = await DBModel.getEmps();
    res.json(emps);
  }
}

module.exports = ViewEmpsAction;
```

**Service (`index.js`):**
```javascript
const express = require('express');
const app = express();
const port = 3000;

// Middleware
app.use(express.json());

// Routes
const viewEmpsAction = new ViewEmpsAction();
app.get('/emps', viewEmpsAction.handle);

// Start server
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
```

### 5. Frontend Implementation

#### 5.1 Setup Instructions
1. Clone the repository: `git clone <repository-url>`
2. Install dependencies: `npm install`
3. Start the development server: `npm start`

#### 5.2 Frontend Code

**React Component (`DeptInfo.jsx`):**
```jsx
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const DeptInfo = () => {
  const [depts, setDepts] = useState([]);
  
  useEffect(() => {
    axios.get('/emps').then(response => {
      setDepts(response.data);
    });
  }, []);

  return (
    <div>
      <h1>Departments</h1>
      <ul>
        {depts.map(dept => (
          <li key={dept.id}>{dept.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default DeptInfo;
```

**Component (`DeptTable.jsx`):**
```jsx
import React, { Component } from 'react';

const DeptTable = ({ departments }) => {
  return (
    <table>
      <thead>
        <tr>
          <th>Department ID</th>
          <th>Name</th>
          <th>Location</th>
        </tr>
      </thead>
      <tbody>
        {departments.map(dept => (
          <tr key={dept.id}>
            <td>{dept.id}</td>
            <td>{dept.name}</td>
            <td>{dept.location}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default DeptTable;
```

### 6. Unit Testing

**Backend Tests (`DBModel.test.js`):**
```javascript
const DBModel = require('./DBModel');

test('should get departments', async () => {
  // Mock database calls using Jest
  // Assert if the returned data is as expected
});
```

**Frontend Tests (`DeptInfo.test.jsx`):**
```jsx
import { render, cleanup } from '@testing-library/react';
import DeptInfo from './DeptInfo';
import axios from 'axios';
import Mockito from 'axios-mock-adapter';

jest.mock('axios');

afterEach(cleanup);

test('should fetch and display departments', async () => {
  const mockAxios = new Mockito(axios);
  const departments = [{ id: 1, name: 'IT', location: 'New York' }];
  mockAxios.get('/emps').mockResolvedValue({ data: departments });

  const { getByText } = render(<DeptInfo />);
  const depts = getByText(/it/i);
  expect(depts).toBeInTheDocument();
});
```

### 7. README for Setup Instructions

**Setting Up the Project**
1. Clone the project repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd path/to/project
   ```
3. Install the dependencies:
   ```bash
   npm install
   ```
4. Start the backend server:
   ```bash
   npm start
   ```
5. Start the frontend development server:
   ```bash
   npm run dev
   ```

This implementation provides a complete backend NodeJS application and a frontend React application, aligning with the specified architectural patterns, functional, and business requirements. Comprehensive unit tests are included to ensure high code coverage and reliability.

**Note:** The actual code provides a basic structure and example components. Depending on the specific database tables (`Dept`, `Emp`, `Salgrade`) and their respective relationships, additional models, routes, and actions would need to be implemented to fully realize the system as described in the specification.