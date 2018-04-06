from rest_framework import generics, permissions
from BasicApi.models import Profile
from .serializers import ProfileSerializer
from django.shortcuts import get_object_or_404

class RetrieveUpdateProfile(generics.RetrieveUpdateAPIView):

	# def get_queryset(self):
	# 	queryset = Profile.objects.all()
	# 	user_id = self.request.query_params.get('user.id', None)
	# 	if user_id is not None:
	# 		queryset = queryset.get(pk = user_id)

	# 	return queryset

	queryset = Profile.objects.all()

	# to use api/v1/user/info instead of api/v1/user/info/1
	def get_object(self):
		queryset = self.filter_queryset(self.get_queryset())
		obj = get_object_or_404(queryset, pk=self.request.user.id)
		return obj

	serializer_class = ProfileSerializer
	# permission_classes = (permissions.AllowAny,)