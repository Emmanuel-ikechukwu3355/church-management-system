from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
    
#     Created 13 todos

# Checking repository status and 

# Added 2 todos

# root contents so I can give accurate GitHub push guidance.

# Read [](file:///c%3A/Users/USER/Desktop/church_project)

# ## What you can add to the project

# ### 1. Core features
# - Authentication
#   - login / logout
#   - staff/admin accounts
#   - role-based access control for members, attendance, and events
# - Member profile pages
#   - full member details
#   - edit profile
#   - membership status / join date
# - Event registration
#   - let members sign up for events
#   - track attendance by event and member
# - Attendance reporting
#   - daily/weekly/monthly attendance reports
#   - attendance percentages
#   - graphs for attendance trends

# ### 2. UX and UI improvements
# - Responsive templates with Bootstrap / Tailwind
# - better navigation and dashboard layout
# - flash messages for success/error actions
# - search, filtering, and pagination on lists

# ### 3. Data features
# - CSV / Excel export for members, events, attendance
# - PDF reports for attendance summaries
# - email notifications for events or reminders

# ### 4. Code quality and structure
# - add `app_name = 'members'` to each app urls.py
# - use `ForeignKey('members.Member')` string references to avoid circular imports
# - move cross-app imports into functions if needed
# - add unit tests for models, views, and forms
# - clean up templates and shared base layout

# ### 5. Deployment and production readiness
# - static files management
# - environment settings for DEBUG vs production
# - deploy to Heroku, Render, or PythonAnywhere

# ---

# ## How to push this project to GitHub

# ### If this repo is not yet initialized
# Run these in church_project:

# ```bash
# cd C:\Users\USER\Desktop\church_project
# git init
# ```

# ### Add a `.gitignore`
# Create a `.gitignore` with at least:

# ```
# venv/
# __pycache__/
# *.pyc
# db.sqlite3
# *.log
# .DS_Store
# ```

# ### Commit
# ```bash
# git add .
# git commit -m "Initial church system project"
# ```

# ### Create GitHub repo
# Either:
# - create a new repo on GitHub via the website,
# or
# - use GitHub CLI if installed:
#   ```bash
#   gh repo create my-church-system --public --source=. --remote=origin
#   ```

# ### Add remote and push
# ```bash
# git remote add origin https://github.com/<your-username>/<repo-name>.git
# git branch -M main
# git push -u origin main
# ```

# ---

# ## If you want, I can help next with:
# - fixing the remaining migration/URL import error
# - creating a proper `.gitignore`
# - adding login/auth and role management
# - preparing the app for GitHub deployment

# Updated todo list
