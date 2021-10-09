from rest_framework import serializers
from myapp.models import User,PowerPosition


class UserSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d', input_formats=['iso-8601'],required=False)

    class Meta:
        model = User
        fields = '__all__'


class PowerPositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = PowerPosition
        fields = ['position', 'id']

    def get_fields(self):
        fields = super(PowerPositionSerializer, self).get_fields()
        fields['children'] = PowerPositionSerializer(many=True, required=False)
        return fields
