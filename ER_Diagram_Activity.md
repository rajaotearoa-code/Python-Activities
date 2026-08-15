# Database Design: ER Diagram Analysis

## 1. System Scenario
This database system manages academic course delivery and student enrollment for an educational institution. Students, identified by their national ID (`NID`), can enroll in scheduled lectures, which automatically generates an official enrollment record capturing the course name and enrollment date.

Simultaneously, the system organizes faculty teaching assignments. Lecturers are linked directly to academic subjects and scheduled lecture sessions, establishing a clear record of which faculty member teaches a specific subject on any given date and time.

---

## 2. Additional Proposed Attributes

* **`Lecture` Entity:**
  * `Room_number` / `Location`: Specifies the physical classroom or online meeting link for the lecture session.
  * `Duration_minutes`: Records the duration/length of the lecture session.
* **`Student` Entity:**
  * `Email_address`: Stores the student's email for official institutional communications.
* **`Subjects` Entity:**
  * `Credit_points`: Specifies the academic credits or units earned upon completing the subject.

---

## 3. Relationship Types & Descriptions

* **`Enrolls` (Ternary Relationship):**
  * **Connected Entities:** `Student`, `Enrollment`, `Lecture`
  * **Description:** Represents a 3-way relationship linking a student to a specific lecture session while generating an associated enrollment record. It maps student attendance and course registration in one unified transaction.

* **`Lectures` (Ternary Relationship):**
  * **Connected Entities:** `Lecturer`, `Subjects`, `Lecture`
  * **Description:** Represents a 3-way relationship connecting a faculty instructor, a subject curriculum, and an individual scheduled lecture event. It defines which lecturer teaches a specific subject during a designated lecture slot.