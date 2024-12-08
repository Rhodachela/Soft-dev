from rest_framework.permissions import BasePermission

class CustomPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
       print(f"request if {request.user}")
       print(f"Obj is {obj}")
       print(f"view is {view}")
       return True