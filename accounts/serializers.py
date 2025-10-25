from rest_framework import serializers

from accounts.models import User


class ProfileMeSerializer(serializers.ModelSerializer):
    permissions = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'is_superuser',
            'is_staff',
            'is_active',
            'date_joined',
            'permissions',
        ]

    def get_permissions(self, obj):

        def sort_key(perm_txt):
            app, perm = perm_txt.split('.')
            action, mdl = perm.split('_')
            return app, mdl, action

        return sorted(
            list(obj.get_user_permissions() | obj.get_group_permissions() | obj.get_role_permissions()),
            key=sort_key,
        )
