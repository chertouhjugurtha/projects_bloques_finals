from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
   def has_permission(self, request, view):
      return request.user.is_admin

class IsEditor(BasePermission):
   def has_permission(self, request, view):
      return request.user.is_editor

class IsUser(BasePermission):
   def has_permission(self, request, view):
      return request.user.is_user

# class BlocklistPermission(BasePermission):
#     """
#     Global permission check for blocked IPs.
#     """

#     def has_permission(self, request, view):
#         ip_addr = request.META['REMOTE_ADDR']
#         blocked = Blocklist.objects.filter(ip_addr=ip_addr).exists()
#         return not blocked