from django.urls import path
from .views import (
    IssueListView, 
    InProgressView, 
    DoneView, 
    IssueCreateView,
    IssueDetailView,
    IssueDeleteView,
    IssueEditView,

)

urlpatterns = [
    path("", IssueListView.as_view(), name="to_do_list"), 
    path("in-progress/", InProgressView.as_view(), name="in_progress"), 
    path("done/", DoneView.as_view(), name="done"),
    path("new/", IssueCreateView.as_view(), name="new"),
    path("detail/<int:pk>", IssueDetailView.as_view(), name="detail"),
    path("delete/<int:pk>", IssueDeleteView.as_view(), name="delete"),
    path("edit/<int:pk>", IssueEditView.as_view(), name="edit"),

]
