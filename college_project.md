# College Management System — UML Design Documentation

## 1. Project Overview & Scope
A lightweight academic system designed to model core interactions among **Students**, **Lecturers**, and **Courses**. The system enforces prerequisite validation during enrollment, tracks course capacity, and enables lecturers to record grades and manage course outlines.

---

## 2. Use Case Diagram & Specification

### Diagram Layout
```text
+---------------------------------------------------------------------------------+
|                            College Management System                            |
|                                                                                 |
|   [Student] -----------> (Browse Courses)                                       |
|         |                                                                       |
|         +--------------> (Enroll in Course)                                     |
|         |                       |                                               |
|         |                       +---<<include>>---> (Verify Prerequisites)      |
|         |                       |                                               |
|         |                       +---<<extend>>----> (Apply Late Enrollment Fee) |
|         |                                                                       |
|         +--------------> (View Academic Results) <------------------+           |
|                                                                     |           |
|   [Lecturer] ----------> (Manage Course Outline)                    |           |
|         |                                                           |           |
|         +--------------> (Record / Update Grades) ------------------+           |
|         |                                                                       |
|         +--------------> (Generate Class Attendance List)                       |
+---------------------------------------------------------------------------------+
```

### Actors
* **Student (Primary Actor):** Browses course offerings, submits enrollment requests, and checks academic transcripts.
* **Lecturer (Primary Actor):** Updates syllabus outlines, records course marks, and exports attendance rosters.

### Key Relationships
* **`<<include>>` (Verify Prerequisites):** Mandatory verification step executed unconditionally whenever a student attempts to enroll in a course.
* **`<<extend>>` (Apply Late Enrollment Fee):** Conditional branch executed only if the enrollment attempt occurs after the standard registration deadline.

### Formal Use Case Specification

| Field | Description |
| :--- | :--- |
| **Use Case Name** | `Enroll in Course` |
| **Primary Actor** | Student |
| **Preconditions** | Student is authenticated; course catalog for the active semester is published. |
| **Postconditions** | Student record appended to course roster; available seat count decremented. |

**Main Flow of Activities:**
1. Student searches catalog and selects a course.
2. System triggers `Verify Prerequisites` (`<<include>>`) against student academic history.
3. System checks registration date and evaluates `Apply Late Enrollment Fee` (`<<extend>>`).
4. System verifies seat availability.
5. System registers the student, updates course capacity, and returns an enrollment confirmation.

**Exception Handling:**
* **Prerequisites Missing:** System halts enrollment and displays required prerequisite courses.
* **Course Capacity Full:** System notifies student and offers placement on the course waitlist.

---

## 3. Activity Diagram: Course Enrollment Workflow

### Diagram Layout
```text
Student Swimlane                        College System Swimlane
================                        =======================
    (● Start)
        |
        v
 [Select Course from
  Available Catalog] -----------------> [Fetch Course Data &
                                         Check Prerequisites]
                                                 |
                                                 v
                                        <Prerequisites Met?>
                                         /                \
                                   [No] /                  \[Yes]
                                       v                    v
                               [Display Error]     [Check Seat Capacity]
                                       |                    |
                                    (◉ End)                 v
                                                    <Seats Available?>
                                                     /              \
                                               [No] /                \[Yes]
                                                   v                  v
                                           [Prompt Waitlist]   ================== (Fork)
                                                   |              |          |
                                                (◉ End)           v          v
                                                            [Add to   [Decrement
                                                             Roster]   Capacity]
                                                                  |          |
                                                               ================== (Join)
                                                                      |
                                                                      v
                                                               [Generate Enrollment
                                                                Confirmation]
                                                                      |
                                                                      v
                                                                   (◉ End)
```

### Workflow Steps
1. **Initiation:** Student selects a target course from the available catalog.
2. **Prerequisite Check (Decision Node):** If prerequisites are not satisfied, an error is returned and the workflow terminates.
3. **Capacity Check (Decision Node):** If no seats remain, the system routes the student to the waitlist prompt and ends the execution.
4. **Concurrency (Fork / Join):** When validation succeeds, the system runs two database updates simultaneously:
   * Adds the student ID to the active course roster.
   * Decrements the remaining course capacity counter.
5. **Confirmation:** Both updates synchronize at the Join bar before issuing the final registration receipt.

---

## 4. Class Diagram & OOP Structure

### Diagram Layout
```text
+----------------------------------------------------+
|                      Person                        |
+----------------------------------------------------+
| - id: String                                       |
| - name: String                                     |
| - email: String                                    |
+----------------------------------------------------+
| + login(): Boolean                                 |
| + getProfile(): String                             |
+----------------------------------------------------+
                         ^
                         | (Generalisation)
           +-------------+-------------+
           |                           |
+--------------------------+  +--------------------------------+
|         Student          |  |            Lecturer            |
+--------------------------+  +--------------------------------+
| - studentId: String      |  | - staffId: String              |
| - major: String          |  | - department: String           |
| - academicStatus: String |  | - officeNumber: String         |
+--------------------------+  +--------------------------------+
| + enroll(c: Course)      |  | + assignGrade(s: Student,      |
| + viewGrades(): Map      |  |               c: Course, g: Str|
+--------------------------+  | + viewRoster(c: Course): List  |
                              +--------------------------------+
           | 0..*                             | 1
           |                                  |
           | (enrolls in)                     | (teaches)
           |                                  |
           | 1..*                             | 0..*
+----------------------------------------------------+
|                      Course                        |
+----------------------------------------------------+
| - courseCode: String                               |
| - title: String                                    |
| - credits: Integer                                 |
| - maxCapacity: Integer                             |
+----------------------------------------------------+
| + hasPrerequisites(s: Student): Boolean            |
| + isFull(): Boolean                                |
| + addStudent(s: Student): Boolean                  |
+----------------------------------------------------+
```

### Structural Relationships & Multiplicities

| Relationship | Type | Multiplicity | Description |
| :--- | :--- | :--- | :--- |
| **`Person` $\rightarrow$ `Student` / `Lecturer`** | Generalisation | N/A | Inheritance hierarchy; `Student` and `Lecturer` inherit base identity fields and authentication methods from `Person`. |
| **`Lecturer` $\rightarrow$ `Course`** | Association | `1` to `0..*` | Exactly one lecturer is assigned to deliver a course; a lecturer may instruct zero, one, or multiple courses. |
| **`Student` $\rightarrow$ `Course`** | Association | `0..*` to `1..*` | A student may register for one or many courses; each active course contains zero to many enrolled students. |