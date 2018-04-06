from rest_framework import serializers
from BasicApi.models import User, Profile

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', 'first_name', 'last_name', 'email')


class ProfileSerializer(serializers.ModelSerializer):
	user = UserSerializer(required=True)

	class Meta:
		model = Profile
		fields = ('user', 'gender', 'address', 'mobile')
		# read_only_fields = ('user',)


	def update(self, instance, validated_data):
		user_data = validated_data.pop('user')

		user = instance.user
		instance.gender = validated_data.get('gender', instance.gender)
		instance.address = validated_data.get('address', instance.address)
		instance.mobile = validated_data.get('mobile', instance.mobile)

		instance.save()
		user.save()

		return instance