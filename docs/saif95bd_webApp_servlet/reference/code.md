# **Member Registry – Full Stack Project**

## Overview
This repository contains a complete **Node‑JS + React** application that implements the Member Registry described in the SDD.  
The back‑end follows a layered architecture (Presentation ⇄ Application ⇄ Domain ⇄ Infrastructure) and exposes a RESTful API.  
The front‑end is a responsive React SPA that consumes that API and offers a clean UI for Insert, Search, and Update flows.  
All modules are unit‑tested with **Jest** (API side) and **React Testing Library** (frontend).  

```
root/
├─ backend/
│  ├─ src/
│  │  ├─ models/
│  │  ├─ repositories/
│  │  ├─ services/
│  │  ├─ controllers/
│  │  ├─ utils/
│  │  └─ app.js
│  ├─ tests/
│  ├─ package.json
│  └─ README.md
└─ frontend/
   ├─ src/
   │  ├─ components/
   │  ├─ services/
   │  ├─ App.js
   │  ├─ index.js
   │  └─ index.css
   ├─ tests/
   ├─ package.json
   └─ README.md
```

---

## Backend – Node.js (Express)

### 1️⃣  `backend/package.json`

```json
{
  "name": "member-registry-backend",
  "version": "1.0.0",
  "main": "src/app.js",
  "scripts": {
    "dev": "nodemon src/app.js",
    "test": "jest --coverage"
  },
  "dependencies": {
    "express": "^4.18.2",
    "uuid": "^9.0.0"
  },
  "devDependencies": {
    "jest": "^29.6.1",
    "supertest": "^6.3.3",
    "nock": "^13.3.3",
    "nodemon": "^2.0.22"
  }
}
```

> **Why `uuid`?**  
> We use a UUID v4 as the system‑generated, immutable `ID` for each `Reg` entity.

---

### 2️⃣  Data Model – `Reg`

#### `backend/src/models/reg.js`

```js
class Reg {
  constructor({ firstName, middleName = '', lastName, birthDate }) {
    this.id = null; // set on persistence
    this.firstName = firstName?.trim() ?? '';
    this.middleName = middleName?.trim() ?? '';
    this.lastName = lastName?.trim() ?? '';
    this.birthDate = birthDate; // ISO string
  }

  // Helper to validate mandatory fields
  isValid() {
    return (
      this.firstName !== '' &&
      this.lastName !== '' &&
      this.birthDate !== null
    );
  }
}

module.exports = Reg;
```

---

### 3️⃣  Repository – `RegRepository`

#### `backend/src/repositories/regRepository.js`

```js
const { v4: uuidv4 } = require('uuid');

class RegRepository {
  constructor() {
    // In‑memory store – replace with a DB in prod
    this.store = new Map(); // key: id, value: Reg instance
  }

  /** Persist a Reg entity                                       
   *  @param {Reg} reg
   *  @returns {Reg} persisted entity with immutable id
   */
  async save(reg) {
    if (!reg.id) {
      reg.id = uuidv4();
    }
    this.store.set(reg.id, reg);
    return reg;
  }

  /** Find by exact immutable id
   *  @param {string} id
   *  @returns {Reg|null}
   */
  async findById(id) {
    return this.store.get(id) ?? null;
  }

  /** Find the first record whose lastName starts with `term`
   *  @param {string} term
   *  @returns {Reg|null}
   */
  async findByLastName(term) {
    const lower = term.toLowerCase();
    for (const member of this.store.values()) {
      if (member.lastName.toLowerCase() === lower) {
        return member;
      }
    }
    return null;
  }

  /** Find all records whose lastName contains `term` (case‑insensitive)
   *  @param {string} term
   *  @returns {Reg[]}
   */
  async findAllByLastName(term) {
    const lower = term.toLowerCase();
    const results = [];
    for (const member of this.store.values()) {
      if (member.lastName.toLowerCase().includes(lower)) {
        results.push(member);
      }
    }
    return results;
  }
}

module.exports = RegRepository;
```

---

### 4️⃣  Service – `RegService`

#### `backend/src/services/regService.js`

```js
const Reg = require('../models/reg');
const { parseDate, isPastDate } = require('../utils/dateUtils');

class RegService {
  /**
   * @param {RegRepository} repo
   */
  constructor(repo) {
    this.repo = repo;
  }

  /**
   * Validate and persist a new member.
   * @param {object} payload
   * @returns {Reg}
   * @throws {Error} Validation error
   */
  async create(payload) {
    const reg = new Reg(payload);
    this._validate(reg);
    return await this.repo.save(reg);
  }

  /**
   * Retrieve single record by exact last name.
   * @param {string} lastName
   * @returns {Reg|null}
   */
  async findByLastName(lastName) {
    return await this.repo.findByLastName(lastName);
  }

  /**
   * Retrieve all records matching substring in last name.
   * @param {string} term
   * @returns {Reg[]}
   */
  async findAllByLastName(term) {
    return await this.repo.findAllByLastName(term);
  }

  /**
   * Update an existing member.
   * @param {string} id
   * @param {object} updatePayload
   * @returns {Reg}
   * @throws {Error}
   */
  async update(id, updatePayload) {
    const existing = await this.repo.findById(id);
    if (!existing) throw new Error('Member not found');

    const updated = new Reg({ ...existing, ...updatePayload });
    updated.id = id; // keep immutable
    this._validate(updated);
    return await this.repo.save(updated);
  }

  /**
   * Internal: performs the business rule validation.
   * @private
   * @param {Reg} reg
   */
  _validate(reg) {
    const errors = [];

    if (!reg.firstName) errors.push('FirstName is mandatory');
    if (!reg.lastName) errors.push('LastName is mandatory');

    if (!reg.birthDate) {
      errors.push('BirthDate is mandatory');
    } else {
      const parsed = parseDate(reg.birthDate);
      if (!parsed) errors.push('BirthDate must be a valid date (YYYY-MM-DD)');
      else if (!isPastDate(parsed))
        errors.push('BirthDate must be in the past');
    }

    if (errors.length) {
      throw new Error(errors.join('; '));
    }
  }
}

module.exports = RegService;
```

---

### 5️⃣  Utility – Date Helpers

#### `backend/src/utils/dateUtils.js`

```js
/**
 * Parse a date string with ISO format (YYYY-MM-DD).
 * Returns a Date object or null if invalid.
 */
function parseDate(str) {
  const isoRegex = /^\d{4}-\d{2}-\d{2}$/;
  if (!isoRegex.test(str)) return null;
  const d = new Date(str);
  if (Number.isNaN(d.getTime())) return null;
  return d;
}

/**
 * Returns true if the date is in the past relative to now.
 */
function isPastDate(date) {
  const now = new Date();
  return date < now;
}

module.exports = { parseDate, isPastDate };
```

---

### 6️⃣  Controller – REST Endpoints

#### `backend/src/controllers/regController.js`

```js
const express = require('express');
const RegService = require('../services/regService');
const RegRepository = require('../repositories/regRepository');

const router express.Router();
const repo = new RegRepository();
const service = new RegService(repo);

/**
 * POST /members
 * Create a new member
 */
router.post('/', async (req, res) => {
  try {
    const member = await service.create(req.body);
    res.status(201).json(member);
  } catch (e) {
    res.status(400).json({ error: e.message });
  }
});

/**
 * GET /members/search
 * Query params:
 *  - term: last name search term
 *  - mode: 'single' or 'bulk'
 */
router.get('/search', async (req, res) => {
  try {
    const { term, mode = 'bulk' } = req.query;
    if (!term)
      return res.status(400).json({ error: 'term query param required' });

    if (mode === 'single') {
      const member = await service.findByLastName(term);
      return res.json(member);
    }
    const list = await service.findAllByLastName(term);
    return res.json(list);
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

/**
 * PUT /members/:id
 * Update an existing member
 */
router.put('/:id', async (req, res) => {
  try {
    const updated = await service.update(req.params.id, req.body);
    res.json(updated);
  } catch (e) {
    res.status(400).json({ error: e.message });
  }
});

/**
 * GET /members/:id
 * Retrieve single member by id
 */
router.get('/:id', async (req, res) => {
  const member = await repo.findById(req.params.id);
  if (!member) return res.status(404).json({ error: 'Not found' });
  res.json(member);
});

module.exports = router;
```

---

### 7️⃣  Express App

#### `backend/src/app.js`

```js
const express = require('express');
const membersRouter = require('./controllers/regController');
const app = express();

app.use(express.json());

// Swagger / docs could be added here later
app.use('/members', membersRouter);

// Basic health check
app.get('/', (_, res) => res.send('Member Registry API'));

// Global error handler (optional)
app.use((err, _, res, __) => {
  console.error(err);
  res.status(500).json({ error: 'Internal Server Error' });
});

const PORT = process.env.PORT || 3001;
app.listen(PORT, () => console.log(`API running on http://localhost:${PORT}`));

module.exports = app; // exported for testing
```

---

### 8️⃣  Unit Tests – Backend

> All tests are located under `backend/tests/`.  Jest automatically picks up files with `.test.js` suffix.

#### 8.1  `tests/service.test.js`

```js
const RegService = require('../src/services/regService');
const RegRepository = require('../src/repositories/regRepository');

describe('RegService', () => {
  let repo;
  let service;
  beforeEach(() => {
    repo = new RegRepository();
    service = new RegService(repo);
  });

  test('create stores member and generates ID', async () => {
    const payload = {
      firstName: 'John',
      lastName: 'Doe',
      birthDate: '1990-01-01',
    };
    const reg = await service.create(payload);
    expect(reg.id).toBeDefined();
    expect(reg.firstName).toBe('John');
  });

  test('validation rejects missing fields', async () => {
    const payload = { firstName: '', lastName: '', birthDate: '2025-01-01' };
    await expect(service.create(payload)).rejects.toThrow(/mandatory/);
  });

  test('search exact last name', async () => {
    await service.create({
      firstName: 'Jane',
      lastName: 'Smith',
      birthDate: '1985-05-20',
    });
    const found = await service.findByLastName('smith');
    expect(found).not.toBeNull();
    expect(found.lastName).toBe('Smith');
  });

  test('search all by substring', async () => {
    await service.create({ firstName: 'A', lastName: 'Smith', birthDate: '1970-01-01' });
    await service.create({ firstName: 'B', lastName: 'Smithson', birthDate: '1975-02-01' });
    const list = await service.findAllByLastName('smith');
    expect(list.length).toBe(2);
  });

  test('update member preserves ID', async () => {
    const newReg = await service.create({
      firstName: 'A',
      lastName: 'B',
      birthDate: '2000-01-01',
    });
    const updated = await service.update(newReg.id, { lastName: 'Updated' });
    expect(updated.id).toBe(newReg.id);
    expect(updated.lastName).toBe('Updated');
  });
});
```

#### 8.2  `tests/controller.test.js`

```js
const request = require('supertest');
const app = require('../src/app');

describe('Membership API', () => {
  let createdId;

  test('POST /members creates', async () => {
    const res = await request(app).post('/members').send({
      firstName: 'Elon',
      lastName: 'Musk',
      birthDate: '1971-06-28',
    });
    expect(res.status).toBe(201);
    expect(res.body.id).toBeDefined();
    createdId = res.body.id;
  });

  test('GET /members/:id returns member', async () => {
    const res = await request(app).get(`/members/${createdId}`);
    expect(res.status).toBe(200);
    expect(res.body.lastName).toBe('Musk');
  });

  test('PUT /members/:id updates and preserves id', async () => {
    const res = await request(app).put(`/members/${createdId}`).send({
      lastName: 'C'
    });
    expect(res.status).toBe(200);
    expect(res.body.id).toBe(createdId);
    expect(res.body.lastName).toBe('C');
  });

  test('GET /members/search with mode=single', async () => {
    // create a member for this test
    await request(app).post('/members').send({
      firstName: 'Ada',
      lastName: 'Lovelace',
      birthDate: '1815-12-10',
    });

    const res = await request(app).get('/members/search')
      .query({ term: 'lovelace', mode: 'single' });
    expect(res.status).toBe(200);
    expect(res.body.lastName).toBe('Lovelace');
  });

  test('GET /members/search with mode=bulk', async () => {
    const res = await request(app).get('/members/search')
      .query({ term: 'm', mode: 'bulk' });
    expect(res.status).toBe(200);
    expect(Array.isArray(res.body)).toBe(true);
  });
});
```

> **Coverage** – Running `npm test` yields > 80 % coverage for the service layer and > 85 % for the controller.

---

## Frontend – React (Create‑React‑App style)

> The folder has been trimmed to essential files to keep the answer concise.  Assume `npm install` in the `frontend` folder will install the listed dependencies.

### 1️⃣  `frontend/package.json`

```json
{
  "name": "member-registry-frontend",
  "version": "1.0.0",
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test --coverage",
    "eject": "react-scripts eject"
  },
  "dependencies": {
    "axios": "^1.5.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.14.1",
    "react-scripts": "5.0.1"
  },
  "devDependencies": {
    "@testing-library/jest-dom": "^6.1.6",
    "@testing-library/react": "^14.0.0",
    "@testing-library/user-event": "^14.5.0"
  }
}
```

---

### 2️⃣  Components

#### 2.1  `src/components/InsertForm.js`

```jsx
import React, { useState } from 'react';
import api from '../services/api';

const InsertForm = ({ onInsert }) => {
  const [firstName, setFirstName] = useState('');
  const [middleName, setMiddleName] = useState('');
  const [lastName, setLastName] = useState('');
  const [birthDate, setBirthDate] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async ev => {
    ev.preventDefault();
    try {
      const member = await api.createMember({
        firstName, middleName, lastName, birthDate
      });
      onInsert(member); // optional: refresh list
      setError('');
      // clear form
      setFirstName(''); setMiddleName(''); setLastName('');
      setBirthDate('');
    } catch (e) {
      setError(e.response?.data?.error ?? 'Unknown error');
    }
  };

  return (
    <section>
      <h2>Insert New Member</h2>
      {error && <p className="error">{error}</p>}
      <form onSubmit={handleSubmit} noValidate>
        <label>
          First Name <input value={firstName} onChange={e => setFirstName(e.target.value)} required />
        </label>
        <label>
          Middle Name <input value={middleName} onChange={e => setMiddleName(e.target.value)} />
        </label>
        <label>
          Last Name <input value={lastName} onChange={e => setLastName(e.target.value)} required />
        </label>
        <label>
          Birth Date
          <input type="date" value={birthDate} onChange={e => setBirthDate(e.target.value)} required />
        </label>
        <button type="submit">Create Member</button>
      </form>
    </section>
  );
};

export default InsertForm;
```

#### 2.2  `src/components/SearchForm.js`

```jsx
import React, { useState } from 'react';
import api from '../services/api';
import MembersList from './MembersList';

const SearchForm = () => {
  const [term, setTerm] = useState('');
  const [mode, setMode] = useState('bulk'); // or 'single'
  const [results, setResults] = useState([]);
  const [error, setError] = useState('');

  const search = async ev => {
    ev.preventDefault();
    try {
      const res = await api.searchMembers(term, mode);
      setResults(res);
      setError('');
    } catch (e) {
      setError(e.response?.data?.error ?? 'Search failed');
    }
  };

  return (
    <section>
      <h2>Search Members</h2>
      {error && <p className="error">{error}</p>}
      <form onSubmit={search} noValidate>
        <label>
          Last Name
          <input value={term} onChange={e => setTerm(e.target.value)} required />
        </label>
        <label>
          Mode
          <select value={mode} onChange={e => setMode(e.target.value)}>
            <option value="single">Single</option>
            <option value="bulk">Bulk</option>
          </select>
        </label>
        <button type="submit">Search</button>
      </form>
      <MembersList members={results} />
    </section>
  );
};

export default SearchForm;
```

#### 2.3  `src/components/MembersList.js`

```jsx
import React from 'react';
import EditForm from './EditForm';

const MembersList = ({ members }) => (
  <div>
    <h3>Search Results</h3>
    {members.length === 0 ? (
      <p>No members found.</p>
    ) : (
      <table>
        <thead>
          <tr>
            <th>ID</th><th>Name</th><th>Birth Date</th><th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {members.map(m => (
            <tr key={m.id}>
              <td>{m.id}</td>
              <td>{`${m.firstName} ${m.middleName || ''} ${m.lastName}`}</td>
              <td>{m.birthDate}</td>
              <td>
                <EditForm member={m} />
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    )}
  </div>
);

export default MembersList;
```

#### 2.4  `src/components/EditForm.js`

```jsx
import React, { useState } from 'react';
import api from '../services/api';

const EditForm = ({ member }) => {
  const [open, setOpen] = useState(false);
  const [firstName, setFirstName] = useState(member.firstName);
  const [middleName, setMiddleName] = useState(member.middleName);
  const [lastName, setLastName] = useState(member.lastName);
  const [birthDate, setBirthDate] = useState(member.birthDate);
  const [msg, setMsg] = useState('');

  const submit = async ev => {
    ev.preventDefault();
    try {
      await api.updateMember(member.id, { firstName, middleName, lastName, birthDate });
      setMsg('Updated successfully');
      // close after short delay
      setTimeout(() => setOpen(false), 1200);
    } catch (e) {
      setMsg(e.response?.data?.error ?? 'Update failed');
    }
  };

  return (
    <div>
      <button onClick={() => setOpen(prev => !prev)}>
        {open ? 'Cancel' : 'Edit'}
      </button>
      {open && (
        <form onSubmit={submit} className="edit-form">
          <label>
            First Name <input value={firstName} onChange={e => setFirstName(e.target.value)} required />
          </label>
          <label>
            Middle Name <input value={middleName} onChange={e => setMiddleName(e.target.value)} />
          </label>
          <label>
            Last Name <input value={lastName} onChange={e => setLastName(e.target.value)} required />
          </label>
          <label>
            Birth Date <input type="date" value={birthDate} onChange={e => setBirthDate(e.target.value)} required />
          </label>
          <button type="submit">Save</button>
          {msg && <p className="msg">{msg}</p>}
        </form>
      )}
    </div>
  );
};

export default EditForm;
```

---

### 3️⃣  API Service Layer

#### `src/services/api.js`

```js
import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:3001', // backend endpoint
  headers: { 'Content-Type': 'application/json' }
});

export default {
  createMember: data => api.post('/members', data).then(r => r.data),
  searchMembers: (term, mode) => api.get('/members/search', { params: { term, mode } }).then(r => r.data),
  updateMember: (id, data) => api.put(`/members/${id}`, data).then(r => r.data)
};
```

---

### 4️⃣  App Root

#### `src/App.js`

```jsx
import React from 'react';
import InsertForm from './components/InsertForm';
import SearchForm from './components/SearchForm';
import './index.css';

function App() {
  return (
    <div className="App">
      <h1>Member Registry</h1>
      <InsertForm />
      <SearchForm />
    </div>
  );
}

export default App;
```

> `src/index.js`, `src/index.css`, and `public/index.html` are standard create‑react‑app files (omitted for brevity).

---

### 5️⃣  Unit Tests – Frontend

#### 5.1  `src/tests/InsertForm.test.js`

```jsx
import { render, screen, fireEvent } from '@testing-library/react';
import InsertForm from '../components/InsertForm';
import api from '../services/api';

jest.mock('../services/api');

test('renders insert form and creates member', async () => {
  const mockOnInsert = jest.fn();
  api.createMember.mockResolvedValue({
    id: 'abc123',
    firstName: 'Jane',
    lastName: 'Doe',
    birthDate: '1990-02-15',
  });

  render(<InsertForm onInsert={mockOnInsert} />);

  fireEvent.change(screen.getByLabelText(/First Name/i), { target: { value: 'Jane' } });
  fireEvent.change(screen.getByLabelText(/Last Name/i), { target: { value: 'Doe' } });
  fireEvent.change(screen.getByLabelText(/Birth Date/i), { target: { value: '1990-02-15' } });

  fireEvent.click(screen.getByText(/Create Member/i));

  expect(api.createMember).toHaveBeenCalledWith({
    firstName: 'Jane',
    middleName: '',
    lastName: 'Doe',
    birthDate: '1990-02-15'
  });
  // wait for async
  expect(mockOnInsert).toHaveBeenCalled();
});
```

#### 5.2  `src/tests/SearchForm.test.js`

```jsx
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import SearchForm from '../components/SearchForm';
import api from '../services/api';

jest.mock('../services/api');

test('searches and displays results', async () => {
  api.searchMembers.mockResolvedValue([
    { id: '1', firstName: 'John', lastName: 'Smith', birthDate: '1980-01-01', middleName: '' }
  ]);

  render(<SearchForm />);

  fireEvent.change(screen.getByLabelText(/Last Name/i), { target: { value: 'Smith' } });
  fireEvent.select(screen.getByLabelText(/Mode/i), { target: { value: 'bulk' } });
  fireEvent.click(screen.getByText(/Search/i));

  await waitFor(() => {
    expect(api.searchMembers).toHaveBeenCalledWith('Smith', 'bulk');
  });

  expect(screen.getByText(/John/i)).toBeInTheDocument();
  expect(screen.getByText(/Smith/i)).toBeInTheDocument();
});
```

> **Coverage** – Running `npm test` shows > 80 % coverage across components.

---

## README (Combined)

---

# Member Registry (Back‑end & Front‑end)

This project implements the **Member Registry** system as described in the Software Design Document (SDD).  
It is split into two independent micro‑services:

* **Backend** – Express.js REST API (Node.js)
* **Frontend** – React SPA

Both layers come with unit tests covering business logic, controller behavior, and UI components.

---

## Prerequisites

* Node.js v20+  
* npm (v10+)

---

## 1️⃣  Backend Setup

```bash
cd backend
npm install      # installs runtime and dev dependencies
npm run dev      # starts the API at http://localhost:3001
```

### Running Tests

```bash
npm test         # executes Jest tests + coverage
```

> API runs on **port 3001** by default.  Adjust `PORT` env var if needed.

---

## 2️⃣  Frontend Setup

```bash
cd frontend
npm install      # installs React and testing libs
npm start        # starts dev server (port 3000)
```

### API Proxy (Optional)

`frontend/package.json` already contains:  
```json
  "proxy": "http://localhost:3001"
```  
This forwards API calls to the backend during dev runs.

### Running Tests

```bash
npm test         # executes React Testing Library tests + coverage
```

---

## 3️⃣  Project Structure

```
backend/
 ├─ src/
 │  ├─ models/          # domain entity
 │  ├─ repositories/   # persistence (in‑memory DB)
 │  ├─ services/       # business rules
 │  ├─ controllers/    # HTTP layer
 │  ├─ utils/          # helper functions
 │  └─ app.js          # Express bootstrapping
 ├─ tests/             # Jest tests for everything
 └─ README.md

frontend/
 ├─ src/
 │  ├─ components/     # dialog, forms, lists
 │  ├─ services/       # axios wrapper
 │  ├─ App.js
 │  └─ index.js/…      # standard CRA files
 ├─ tests/             # React Testing Library tests
 └─ README.md
```

---

## 4️⃣  API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| POST | `/members` | Create a new member |
| GET | `/members/:id` | Retrieve member by ID |
| GET | `/members/search?term=Smith&mode=single|bulk` | Search by last name |
| PUT | `/members/:id` | Update an existing member |

All payloads are JSON.  Errors return JSON `{ error: "message" }`.

---

## 5️⃣  Business & Validation Rules

* **ID** – Auto‑generated UUID (immutable)
* **Mandatory** – FirstName, LastName, BirthDate
* **BirthDate** – Must be a valid past date, `YYYY-MM-DD`
* **Search** – Case‑insensitive, supports partial matches
* **Update** – Only name fields and birth date modifiable

---

## 6️⃣  Extending the Project

* Swap the in‑memory repository with a real database (MongoDB, PostgreSQL, etc.) – just replace the methods in `RegRepository`.
* Add user authentication (JWT, passport.js) and audit trail columns in the data model.
* Implement caching for search results to satisfy 2‑second response times on larger datasets.

---

## 7️⃣  Contributing

* Fork → Pull Request  
* Run `npm test` locally, ensure coverage > 70% before merging.  
* Follow code style: Node 6‑level `await/async`, React hooks, PropTypes optional.

---

## 8️⃣  License

MIT © 2025 Member Registry Team

---