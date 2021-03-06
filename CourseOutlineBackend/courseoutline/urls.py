from django.urls import path
from django.views import debug

from . import views

urlpatterns = [
    path('', debug.default_urlconf),
    # coordinator
    path('coordinator/', views.CoordinatorPostGetView.as_view()),
    path('coordinator/<str:CourseID>/', views.CoordinatorPostGetView.as_view()),
    path('coordinator/v2/<str:ModelID>/', views.CoordinatorPutDelView.as_view()),

    # info
    path('info/', views.InfoPostGetView.as_view()),
    path('info/<str:CourseID>/', views.InfoPostGetView.as_view()),
    path('info/v2/<str:ModelID>/', views.InfoPutDelView.as_view()),

    # grade determination
    path('gradedetermination/', views.GradeDeterminationPostGetView.as_view()),
    path('gradedetermination/<str:CourseID>/', views.GradeDeterminationPostGetView.as_view()),
    path('gradedetermination/v2/<str:ModelID>/', views.GradeDeterminationPutDelView.as_view()),

    # outcome
    path('outcome/', views.OutcomePostGetView.as_view()),
    path('outcome/<str:CourseID>/', views.OutcomePostGetView.as_view()),
    path('outcome/v2/<str:ModelID>/', views.OutcomePutDelView.as_view()),

    # timetable
    path('timetable/', views.TimetablePostGetView.as_view()),
    path('timetable/<str:CourseID>/', views.TimetablePostGetView.as_view()),
    path('timetable/v2/<str:ModelID>/', views.TimetablePutDelView.as_view()),

    # grade distribution
    path('gradedistribution/', views.GradeDistributionPostGetView.as_view()),
    path('gradedistribution/<str:CourseID>/', views.GradeDistributionPostGetView.as_view()),
    path('gradedistribution/v2/<str:ModelID>/', views.GradeDistributionPutDelView.as_view()),

    # lecture
    path('lecture/', views.LecturePostGetView.as_view()),
    path('lecture/<str:CourseID>/', views.LecturePostGetView.as_view()),
    path('lecture/v2/<str:ModelID>/', views.LecturePutDelView.as_view()),

    # tutorial
    path('tutorial/', views.TutorialPostGetView.as_view()),
    path('tutorial/<str:CourseID>/', views.TutorialPostGetView.as_view()),
    path('tutorial/v2/<str:ModelID>/', views.TutorialPutDelView.as_view()),

    # course
    path('course/', views.CoursePostGetView.as_view()),
    path('course/<str:CourseID>/', views.CoursePostGetView.as_view()),
    path('course/v2/<str:ModelID>/', views.CoursePutDelView.as_view()),

    # textbook
    path('textbook/', views.TextbookPostGetView.as_view()),
    path('textbook/<str:CourseID>/', views.TextbookPostGetView.as_view()),
    path('textbook/v2/<str:ModelID>/', views.TextbookPutDelView.as_view()),

    # auweight
    path('auweight/', views.AuWeightPostGetView.as_view()),
    path('auweight/<str:CourseID>/', views.AuWeightPostGetView.as_view()),
    path('auweight/v2/<str:ModelID>/', views.AuWeightPutDelView.as_view()),

    # contentcategory
    path('contentcategory/', views.ContentCategoryPostGetView.as_view()),
    path('contentcategory/<str:CourseID>/', views.ContentCategoryPostGetView.as_view()),
    path('contentcategory/v2/<str:ModelID>/', views.ContentCategoryPutDelView.as_view()),

    # lab
    path('lab/', views.LabPostGetView.as_view()),
    path('lab/<str:CourseID>/', views.LabPostGetView.as_view()),
    path('lab/v2/<str:ModelID>/', views.LabPutDelView.as_view()),

    # section
    path('section/', views.SectionPostGetView.as_view()),
    path('section/<str:CourseID>/', views.SectionPostGetView.as_view()),
    path('section/v2/<str:ModelID>/', views.SectionPutDelView.as_view()),
]
