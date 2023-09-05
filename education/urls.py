from django.urls import path
from rest_framework.routers import DefaultRouter
from education.apps import EducationConfig
from education.views import CourseViewSet, LessonListView, LessonDetailView, LessonCreateView, LessonUpdateView, \
    LessonDeleteView, PaymentListView, PaymentDetailView, PaymentUpdateView, PaymentCreateView, PaymentDeleteView

app_name = EducationConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
                  path('lesson/', LessonListView.as_view()),
                  path('lesson/<int:pk>/', LessonDetailView.as_view()),
                  path('lesson/update/<int:pk>/', LessonUpdateView.as_view()),
                  path('lesson/create/', LessonCreateView.as_view()),
                  path('lesson/delete/<int:pk>/', LessonDeleteView.as_view()),
                  path('payment/', PaymentListView.as_view()),
                  path('payment/<int:pk>/', PaymentDetailView.as_view()),
                  path('payment/update/<int:pk>/', PaymentUpdateView.as_view()),
                  path('payment/create/', PaymentCreateView.as_view()),
                  path('payment/delete/<int:pk>/', PaymentDeleteView.as_view()),

              ] + router.urls
