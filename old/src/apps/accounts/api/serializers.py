from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from apps.accounts.email import send_confirmation_email

# Auth user model class
User = get_user_model()


class SelfUserSerializer(serializers.ModelSerializer):
    """
    User itself control
    Serializer class needed for serializing user own data and make CRUD operations with that.
    """

    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    phone_number = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])
    birth_at = serializers.DateField(required=False)

    class Meta:
        model = User
        fields = ('first_name',
                  'last_name',
                  'email',
                  'phone_number',
                  'sex',
                  'birth_at',
                  'password',
                  'created_at',
                  'updated_at',
                  'uuid',
                  'is_email_verified',
                  )
        read_only_fields = ('created_at',
                            'updated_at',
                            'uuid',
                            'is_email_verified',
                            )

    def create(self, validated_data):
        """ Method which creates user object """

        user = super(SelfUserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        send_confirmation_email(self.context['request'], user)
        return user

    def update(self, instance, validated_data):
        """ Method which updates user object """

        # Get email and password from validated data if exists
        password = validated_data.pop('password', None)
        email = validated_data.pop('email', None)

        instance.last_name = validated_data.get('last_name', None)
        instance.first_name = validated_data.get('first_name', None)
        instance.phone_number = validated_data.get('phone_number', None)
        instance.sex = validated_data.get('sex', None)
        instance.birth_at = validated_data.get('birth_at', None)

        if password is not None:
            instance.set_password(password)

        if email is not None and email != instance.email:
            instance.email = email
            send_confirmation_email(self.context['request'], instance)

        instance.save()

        return instance


class FullUserSerializer(serializers.ModelSerializer):
    """
    Full control
    Serializer class needed for serializing user full data and make CRUD operations with that.
    """

    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    phone_number = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])
    birth_at = serializers.DateField(required=False)

    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('created_at',
                            'updated_at',
                            'uuid',
                            )

    def create(self, validated_data):
        """ Method which creates user object """

        user = super(FullUserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        send_confirmation_email(self.context['request'], user)
        return user

    def update(self, instance, validated_data):
        """ Method which updates user object """

        # Get email and password from validated data if exists
        password = validated_data.pop('password', None)
        email = validated_data.pop('email', None)

        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        if email is not None and email != instance.email:
            instance.email = email
            send_confirmation_email(self.context['request'], instance)

        instance.save()

        return instance


class OtherUserSerializer(serializers.ModelSerializer):
    """
    Other users control
    Serializer class needed for serializing user own data and make CRUD operations with that.
    """

    class Meta:
        model = User
        fields = ('first_name',
                  'last_name',
                  'email',
                  'phone_number',
                  'birth_at',
                  'sex',
                  'uuid',
                  )
        read_only_fields = ('first_name',
                            'last_name',
                            'email',
                            'phone_number',
                            'birth_at',
                            'sex',
                            'uuid',
                            )
