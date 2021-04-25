from django.urls import path
from .views import GoalView, WorkView, PostGoalView, WeekGoalView, MonthGoalView, DayWorkView, After_SchoolWorkView, PostWorkView, SpecficDayWorkView, SpecficAfter_SchooWorkView

urlpatterns = [
    path('goal/', GoalView.as_view()),
    path('goal/weekly/', WeekGoalView.as_view()),
    path('goal/monthly/', MonthGoalView.as_view()),
    path('goal/post/', PostGoalView.as_view()),
    path('work/', WorkView.as_view()),
    path('work/daily/', DayWorkView.as_view()),
    path('work/daily/<int:dotw>/', SpecficDayWorkView.as_view()),
    path('work/after_school/', After_SchoolWorkView.as_view()),
    path('work/after_school/<int:dotw>/', SpecficAfter_SchooWorkView.as_view()),
    path('work/post/', PostWorkView.as_view())
]