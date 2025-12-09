<Code>
**1. System Architecture**

*Overall Design*  
- **JSP files:**  
  - `Navigation.jsp`: Provides navigation interface.  
  - `DeptInfo.jsp` & `DeptTable.jsp`: Departments form and table view.  
  - `AddDept.jsp` & `EditDept.jsp`: Forms for adding/editing departments.  
  - `EditEmp.jsp` & `EmpInfo.jsp`: Employee form and individual view.  
  - `SalGradeInfo.jsp` & `SalGradeTable.jsp`: Salary grades form and table view.  
  - Action pages: `AddDeptAction`, `EditDeptAction`, `RemoveDeptAction`, `AddEmpAction`, `EditEmpAction`, `FindEmpSubmit`, `RemoveEmp`, `FindDeptSubmit`, `SortDepts`, `ViewSalGradeAction`, `AddSalGradeAction`, `SalGradeInfoAction`.  
  - Data retrieval: Fetch departments, employees, salary grades via DAO methods.  
  - Sorting: `SortDepts` action sorts departments based on selected criteria.  

*Key Components*  
- **DAO Factory (`DAOFactory.java`)**: Creates instances for department, employee, and salary grade DAOs.  
- **Exception Handling (`ModelException.java`)**: Catches and processes exceptions from DAO operations.  
- **HTTP Request Handling (`SRequest.java`)**: Retrieves parameters from parsed HTTP requests.  

**2. Functional Requirements**

- **Input Handling:** User inputs data to create/delete departments, employees, and salary grades via forms in `Navigation.jsp`, `DeptInfo.jsp`, `DeptTable.jsp`, `AddDept.jsp`, `EditDept.jsp`, `EditEmp.jsp`, `EmpInfo.jsp`, `SalGradeInfo.jsp`, `SalGradeTable.jsp`. Search using `FindDept`, `FindEmp`, `FindSalGrade`.  
- **Data Processing:** JSP pages validate inputs and forward them to corresponding action classes (`AddDeptAction`, `EditDeptAction`, `RemoveDeptAction`, `AddEmpAction`, `EditEmpAction`, `FindEmpSubmit`, `RemoveEmp`, `FindDeptSubmit`, `SortDepts`, `ViewSalGradeAction`). Action classes interact with DAOs to perform CRUD operations on respective models.  
- **Output Generation:** Results (e.g., department, employee, salary grade details; search result lists) are displayed back via JSP pages using respective servlets (`AddSalGradeAction`, `EditSalGradeAction`) and filters (`SortDepts`, `ViewSalGradeAction`).  

**3. Business Requirements**

- **Authorized Actions:** Business rules enforce CRUD, search, sorting, and viewing of departments, employees, and salary grades.  
- **Success Criteria:** All CRUD operations, searches, and sorting complete without errors; results displayed correctly in UI forms.

</Code>
</Code>
This is the expected criteria for your final answer: The code for a complete Backend NodeJS implementation and frontend React  application, with test suites and a README for setup instructions. All code should align with the requirements and technical specifications provided in the spec.
You MUST return the actual complete content as the final answer, not a summary.
Your final answer MUST be formatted in Markdown syntax.
Follow these guidelines:
- Use `#` for headers
- Use `**` for bold text
- Use `*` for italic text
- Use `-` or `*` for bullet points
- Use `` `code` `` for inline code
- Use ```language for code blocks`