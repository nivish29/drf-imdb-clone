from rest_framework import permissions

class AdminorReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        admin_permission = bool(request.user and request.user.is_staff)
        return request.method == "GET" or admin_permission

class ReviewUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: #this means that the request is a GET request
            return True
            
        else:
            return obj.review_user == request.user #is the user who made the review is the same as current logged in user that is a admin