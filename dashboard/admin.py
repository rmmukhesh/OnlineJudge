from django.contrib import admin
from .models import Problem, TestCase, Submission

# Register your models here.

@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'created_at')
    readonly_fields = ('created_by', 'created_at')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

@admin.register(TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    list_display = ('problem', 'id', 'is_public')
    list_filter = ('problem', 'is_public')

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('user', 'problem', 'status', 'submitted_at')
    list_filter = ('status', 'problem')
    readonly_fields = ('verdict_details',)