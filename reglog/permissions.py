from rest_framework.permissions import BasePermission
class GetOnly(BasePermission):
    def has_permission(self, request, view):

        lis=["GET","DELETE"]
        if request.method in lis:
            return True
        else:
            return False

class GetOrPost(BasePermission):
    def has_permission(self, request, view):
        lis=["GET","POST","PUT"]
        if request.method in lis:


            return True
        else:
            return False