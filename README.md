# VirtualPlannerBackend
Backend for Virtual Planner


How to use
Clone this respository or something idk

Run manage.py in virtual_planner


Endpoints:

/goal/ Shows all goals
/goal/weekly/ Shows all goals with goal_type="weekly"
/goal/monthly/ Shows all goals with goal_type="monthly"

/work/ Shows all work objects
/work/daily/ shows all work objects with work_type = "daily"
/work/after_school/ Shows all work objects with work_type = "after_school"

/work/daily/<int>/ Shows all work objects with work_type = "daily" AND due_date corresponds to the day of the week of <int> (0-6, Sun-Sat)
/work/after_school/<int>/ Same as ^^ but with work_type="after_school"
  
Posting:

/goal/post/ Takes in the parameters "text", "due_date", and "goal_type". goal_type should be "weekly" or "monthly"
/work/post/ Takes in the parameters "text", "due_date", and "work_type". work_type should be "daily" or "after_school"

due_date is a Date object
They also have the attribute "completed" which is a Boolean
