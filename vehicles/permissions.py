from rest_framework import permissions

class IsPartDealhersip(permissions.BasePermission):
    def has_object_permission(self, request, view, obj, method):
        # for item in obj:
        #     return item.dealership == request.user.dealership
        if method == "create":
            for item in obj:
                return item.dealership == request.user.dealership
        else:   
            return obj.dealership == request.user.dealership
    
    def has_permission(self, request, view):
        return super().has_permission(request, view)
    
