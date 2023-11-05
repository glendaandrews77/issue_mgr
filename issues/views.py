from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Issue, Status
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

class IssueListView(ListView):
    template_name="issues/list.html"
    model= Issue

class IssueDetailView(DetailView):
    template_name="issues/detail.html"
    model= Issue

class IssueDeleteView(DeleteView):
    template_name="issues/delete.html"
    model= Issue
    success_url= reverse_lazy('to_do_list')

class InProgressView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    template_name = "issues/list.html"
    model = Issue
    context_object_name = "issue_list"

    def get_queryset(self):
        in_progress_status = Status.objects.get(name="in_progress")
        return Issue.objects.filter(status=in_progress_status, assignee=self.request.user).order_by("-created_on")


class DoneView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    template_name = "doneIssues/list.html"
    model = Issue
    context_object_name = "issue_list"

class IssueCreateView(LoginRequiredMixin, CreateView):
    model=Issue
    template_name="issues/new.html"
    fields= "__all__"

class IssueEditView(LoginRequiredMixin, UpdateView):
    model=Issue
    template_name="issues/new.html"
    fields= "__all__"