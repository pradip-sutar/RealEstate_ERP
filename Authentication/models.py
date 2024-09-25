from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission

# class UserManager(BaseUserManager):
#     def create_user(self, username, password=None, **extra_fields):
#         if not username:
#             raise ValueError('Users must have a username')
#         user = self.model(username=username, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(username, password, **extra_fields)

# class User(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(max_length=255, unique=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     groups = models.ManyToManyField(
#         Group,
#         related_name='custom_user_set',  # Unique related_name
#         blank=True,
#     )
#     user_permissions = models.ManyToManyField(
#         Permission,
#         related_name='custom_user_set',  # Unique related_name
#         blank=True,
#     )

#     objects = UserManager()

#     USERNAME_FIELD = 'username'

#     def __str__(self):
#         return self.username


