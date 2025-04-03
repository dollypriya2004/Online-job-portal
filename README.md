# Online Job Portal

##  Overview
The **Online Job Portal** is a web-based platform that connects **job seekers** with **employers**, making job applications and recruitment more efficient. It allows users to post jobs, search for opportunities, apply for jobs, and manage applications.

##  Features
###  **Admin Module**
- Manages user accounts, job postings, and overall platform activities.
- Verifies and approves recruiter profiles.
- Generates reports and maintains the database.

###  **Recruiter Module**
- **General Recruiters**: Can post up to 30 jobs per month and view applications.
- **Super Recruiters**: Have unlimited job postings and can directly contact super users.

###  **Job Seeker Module**
- **General Users**: Can apply for up to 15 jobs per month and track applications.
- **Super Users**: Can apply for up to 30 jobs per month and update profiles.
- Upload resumes and edit personal details.

###  **Job Search & Filters**
- Search jobs based on keywords, location, company, and salary.
- Apply filters for better job matching.

###  **Application Management**
- Users can view application status and recruiters can track applicants.
- Recruiters can shortlist, accept, or reject candidates.

##  Tech Stack
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Backend**: Django (Python)
- **Database**: SQLite / PostgreSQL

##  Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/online-job-portal.git
   ```
2. Navigate to the project folder:
   ```bash
   cd online-job-portal
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```
6. Open your browser and visit:
   ```
   http://127.0.0.1:8000/
   ```


