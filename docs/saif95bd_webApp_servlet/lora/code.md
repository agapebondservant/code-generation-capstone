<#Summary>
This is the expected criteria for your final answer: The code for a complete backend NodeJS implementation and frontend React  application, with test suites and a README for setup instructions. All code should align with the requirements and technical specifications provided in the spec.
</#Summary>

<#Components>
1. Backend (NodeJS):
   - RESTful API using Express.js
   - Services, data models, and business logic from the spec
2. Frontend (React):
   - Responsive UI components from the spec
3. Testing:
   - Backend: Unit tests for services/controllers/utility functions using Jest
   - Frontend: Unit tests for React components using Jest/React Testing Library
   - Mocking database calls, external API requests, dependencies
   - Aim for 70%+ code coverage
</#Components>

<#Domain>
- **reg** class (backend):
  - Fields: id (long), firstName (String), lastName (String), middleName (String), birth (Date)
  - Simple entity with primary key generation
</#Domain>
<#Summary>
This is the expected criteria for your final answer: The code for a complete backend NodeJS implementation and frontend React  application, with test suites and a README for setup instructions. All code should align with the requirements and technical specifications provided in the spec.
</#Summary>

<#Components>
1. Backend (NodeJS):
   - RESTful API using Express.js
   - Services, data models, and business logic from the spec
2. Frontend (React):
   - Responsive UI components from the spec
3. Testing:
   - Backend: Unit tests for services/controllers/utility functions using Jest
   - Frontend: Unit tests for React components using Jest/React Testing Library
   - Mocking database calls, external API requests, dependencies
   - Aim for 70%+ code coverage
</#Components>

<#Domain>
- **reg** class (backend):
  - Fields: id (long), firstName (String), lastName (String), middleName (String), birth (Date)
  - Simple entity with primary key generation
</#Domain>
<#Summary>
This is the expected criteria for your final answer: The code for a complete backend NodeJS implementation and frontend React  application, with test suites and a README for setup instructions. All code should align with the requirements and technical specifications provided in the spec.
</#Summary>

<#Components>
1. Backend (NodeJS):
   - RESTful API using Express.js
   - Services, data models, and business logic from the spec
2. Frontend (React):
   - Responsive UI components from the spec
3. Testing:
   - Backend: Unit tests for services/controllers/utility functions using Jest
   - Frontend: Unit tests for React components using Jest/React Testing Library
   - Mocking database calls, external API requests, dependencies
   - Aim for 70%+ code coverage
</#Components>
<#Backend>
```javascript
// package.json (dependencies)

{
  "name": "studentApp",
  "version": "1.0.0",
  "description": "",
  "main": "server.js",
  "scripts": {
    "start": "node server.js",
    "test": "jest"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "cors": "^2.8.5",
    "express": "^4.17.1",
    "helmet": "^5.2.0",
    "jest": "^26.6.3",
    "jest-mock-redis": "^3.2.1",
    "monk": "^5.0.1",
    "nodemon": "^2.0.6",
    "shortid": "^2.3.8"
  }
}

// server.js

const express = require('express');
const helmet = require('helmet');
const cors = require('cors');
const Monk = require('monk');
const { reg, regUtil } = require('./regUtil');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(helmet());
app.use(cors());
app.use(express.json());

// Routes
app.post('/insert', async (req, res) => {
  try {
    const { id, firstName, lastName, middleName, birth } = req.body;
    const student = reg.create(id, firstName, lastName, middleName, birth);
    await regUtil.saveStudent(student);
    res.status(201).json(student);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

app.post('/search', async (req, res) => {
  try {
    const { search } = req.body;
    const students = await regUtil.getStudents(search);
    res.json(students);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```  
```java
// App.java (JUnit test)

import com.example.RegApp;
import com.example.data.reg.RegUtil;
import com.example.models.reg.Reg;
import org.junit.jupiter.api.*;
import org.mockito.*;

import java.util.*;

import static org.mockito.Mockito.*;

@Test
public class AppTest {

  @Mock
  private RegUtil regUtil;

  @Test
  public void testReg() {
    Reg reg = Reg.builder()
        .id(1L)
        .firstName("John")
        .lastName("Doe")
        .middleName("A")
        .birth(new Date())
        .build();

    when(regUtil.saveStudent(reg)).thenReturn(reg);

    Reg actual = RegApp.regUtil.saveStudent(reg);

    assertEquals(reg.getId(), actual.getId());
    assertEquals(reg.getFirstName(), actual.getFirstName());
    assertEquals(reg.getLastName(), actual.getLastName());
    assertEquals(reg.getMiddleName(), actual.getMiddleName());
    assertEquals(reg.getBirth(), actual.getBirth());
  }
}
```
```javascript
// AppTest.js (React test)

import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import App from './App';

test('renders Learn React', () => {
  const { getByText } = render(<App />);
  const linkElement = getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});
```
```javascript
// StudentSearch.test.js (React test)

import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import StudentSearch from './StudentSearch';

test('renders search input and displays students', async () => {
  render(<StudentSearch />);

  fireEvent.change(screen.getByPlaceholder('Search by name'), { target: { value: 'John' } });
  fireEvent.submit(screen.getByRole('form'));

  await waitFor(() => screen.getByRole('listbox')).then(
    () => expect(screen.getByRole('listbox')).toBeInTheDocument(),
    () => fail('Listbox not rendered'),
  );
});
```
```markdown
# Student Management Application

## Overview
This application is a basic web application using Java, JSP, and Hibernate. It allows users to manage student records with features for inserting, searching, and sorting students.

---

### Backend Requirements

1. **NodeJS RESTful API**
   - Implement services and business logic based on the provided specifications.
   - Use Express.js for the API.

2. **Frontend Requirements**
   - Develop React components following the design specifications.
   - Ensure the application is responsive.

### Testing
- **Backend**: Write JUnit tests for services/controllers using mock objects.
- **Frontend**: Write Jest/React Testing Library tests for components.

### Running the Application
1. Clone the repository.
2. Run `npm install` to install dependencies.
3. For NodeJS: `npm start` to start the server.
4. Access the frontend at the specified URL.

### Dependency Management
- Ensure all dependencies are listed in the `package.json` file.

---

*Backend: Application logic written in NodeJS/Express.js with JUnit tests for validation.*
*Frontend: User interface built in React following specifications.*
```

<#Backend>
```javascript
// package.json (dependencies)

{
  "name": "studentApp",
  "version": "1.0.0",
  "description": "",
  "main": "server.js",
  "scripts": {
    "start": "node server.js",
    "test": "jest"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "cors": "^2.8.5",
    "express": "^4.17.1",
    "helmet": "^5.2.0",
    "jest": "^26.6.3",
    "jest-mock-redis": "^3.2.1",
    "monk": "^5.0.1",
    "nodemon": "^2.0.6",
    "shortid": "^2.3.8"
  }
}

// server.js

const express = require('express');
const helmet = require('helmet');
const cors = require('cors');
const Monk = require('monk');
const { reg, regUtil } = require('./regUtil');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(helmet());
app.use(cors());
app.use(express.json());

// Routes
app.post('/insert', async (req, res) => {
  try {
    const { id, firstName, lastName, middleName, birth } = req.body;
    const student = reg.create(id, firstName, lastName, middleName, birth);
    await regUtil.saveStudent(student);
    res.status(201).json(student);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

app.post('/search', async (req, res) => {
  try {
    const { search } = req.body;
    const students = await regUtil.getStudents(search);
    res.json(students);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```
```java
// App.java (JUnit test)

import com.example.RegApp;
import com.example.data.reg.RegUtil;
import com.example.models.reg.Reg;
import org.junit.jupiter.api.*;
import org.mockito.*;

import java.util.*;

import static org.mockito.Mockito.*;

@Test
public class AppTest {

  @Mock
  private RegUtil regUtil;

  @Test
  public void testReg() {
    Reg reg = Reg.builder()
        .id(1L)
        .firstName("John")
        .lastName("Doe")
        .middleName("A")
        .birth(new Date())
        .build();

    when(regUtil.saveStudent(reg)).thenReturn(reg);

    Reg actual = RegApp.regUtil.saveStudent(reg);

    assertEquals(reg.getId(), actual.getId());
    assertEquals(reg.getFirstName(), actual.getFirstName());
    assertEquals(reg.getLastName(), actual.getLastName());
    assertEquals(reg.getMiddleName(), actual.getMiddleName());
    assertEquals(reg.getBirth(), actual.getBirth());
  }
}
```
```javascript
// AppTest.js (React test)

import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import App from './App';

test('renders Learn React', () => {
  const { getByText } = render(<App />);
  const linkElement = getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});
```
```javascript
// StudentSearch.test.js (React test)

import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import StudentSearch from './StudentSearch';

test('renders search input and displays students', async () => {
  render(<StudentSearch />);

  fireEvent.change(screen.getByPlaceholder('Search by name'), { target: { value: 'John' } });
  fireEvent.submit(screen.getByRole('form'));

  await waitFor(() => screen.getByRole('listbox')).then(
    () => expect(screen.getByRole('listbox')).toBeInTheDocument(),
    () => fail('Listbox not rendered'),
  );
});
```
```markdown
# Student Management Application

## Overview
This application is a basic web application using Java, JSP, and Hibernate. It allows users to manage student records with features for inserting, searching, and sorting students.

---

### Backend Requirements

1. **NodeJS RESTful API**
   - Implement services and business logic based on the provided specifications.
   - Use Express.js for the API.

2. **Frontend Requirements**
   - Develop React components following the design specifications.
   - Ensure the application is responsive.

### Testing
- **Backend**: Write JUnit tests for services/controllers using mock objects.
- **Frontend**: Write Jest/React Testing Library tests for components.

### Running the Application
1. Clone the repository.
2. Run `npm install` to install dependencies.
3. For NodeJS: `npm start` to start the server.
4. Access the frontend at the specified URL.

### Dependency Management
- Ensure all dependencies are listed in the `package.json` file.

---

*Backend: Application logic written in NodeJS/Express.js with JUnit tests for validation.*
*Frontend: User interface built in React following specifications.*
</#Backend>
<#Frontend>
```javascript
// App.js

import React from 'react';
import StudentSearch from './StudentSearch';
import Insert from './Insert';

function App() {
  return (
    <div>
      <h1>Student Management App</h1>
      <StudentSearch />
      <Insert />
    </div>
  );
}

export default App;
```
```javascript
// StudentSearch.js

import React, { useState } from 'react';

function StudentSearch() {
  const [searchTerm, setSearchTerm] = useState('');

  return (
    <div>
      <input
        type="text"
        placeholder="Search by name"
        onChange={(e) => setSearchTerm(e.target.value)}
      />
      <form onSubmit={(e) => { e.preventDefault(); console.log(searchTerm); }}>
        <button type="submit">Search</button>
      </form>
    </div>
  );
}

export default StudentSearch;
```
```javascript
// Insert.js

function Insert() {
  return (
    <div>
      <h2>Add Student</h2>
      {/* Form to insert student would go here */}
    </div>
  );
}
```
```markdown
# Student Management Application

## Overview
This application is a basic web application using Java, JSP, and Hibernate. It allows users to manage student records with features for inserting, searching, and sorting students.

---

### Backend Requirements

1. **NodeJS RESTful API**
   - Implement services and business logic based on the provided specifications.
   - Use Express.js for the API.

2. **Frontend Requirements**
   - Develop React components following the design specifications.
   - Ensure the application is responsive.

### Testing
- **Backend**: Write JUnit tests for services/controllers using mock objects.
- **Frontend**: Write Jest/React Testing Library tests for components.

### Running the Application
1. Clone the repository.
2. Run `npm install` to install dependencies.
3. For NodeJS: `npm start` to start the server.
4. Access the frontend at the specified URL.

### Dependency Management
- Ensure all dependencies are listed in the `package.json` file.

---

*Backend: Application logic written in NodeJS/Express.js with JUnit tests for validation.*
*Frontend: User interface built in React following specifications.*
</#Frontend>
```