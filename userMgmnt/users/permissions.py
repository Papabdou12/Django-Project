# yourapp/permissions.py

from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == 'admin'

class IsTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == 'teacher'

class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == 'student'
