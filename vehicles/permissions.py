from rest_framework import permissions

class IsPartDealhersip(permissions.BasePermission):
    def has_object_permission(self, request, view, obj, method):
        # for item in obj:
        #     return item.dealership == request.user.dealership
        return obj.dealership == request.user.dealership
    
    def has_permission(self, request, view):
        if view.action == 'create':
            if not request.user.is_authenticated:
                return False
        dealership = request.user.dealership
        vehicle = request.data

        if dealership != vehicle.get('dealership'):
            return False
        return True
    
# class IsPublishDealership(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if view.action == 'create':
#             if not request.user.is_authenticated:
#                 return False
#             dealership = request.user.dealership
#             vehicle = request.data

#             if dealership != vehicle.get('dealership'):
#                 return False
#             return True
#         return super().has_permission(request, view)