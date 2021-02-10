from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core.mail import send_mail
from random import choice
from string import ascii_letters, digits, punctuation

# Create your models here.
class UserManager(BaseUserManager):
    def generate_password():
        possible_characters = ascii_letters + digits + punctuation
        random_list = [choice(possible_characters) for i in range(10)]
        password = "".join(random_list)
        return password

    def send_activation_link(email, password):
        send_mail(
            'Your School App Activation Link!',
            f'You can now log in to School Web App! Use following data: {email} and password: {password}',
            'school.maintaining.app@gmail.com',
            [email],
            fail_silently=False,
            )

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            password = self.generate_password()
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        self.send_activation_link(email,password)
        return user

    def create_student_and_parents(self, email, email_parent1, email_parent2):
    	pass

    def create_teacheruser(self, email):
        user = self.create_user(email)
        user.is_teacher = True
        user.save(using=self._db)
        return user

    def create_principaluser(self, email, password):
        user = self.create_user(email)
        user.is_principal = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        UserManager.send_activation_link(email,password)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='Email address', max_length=255, unique=True)
    first_name = models.CharField(verbose_name='First name', max_length=50, null=True, blank=True)
    last_name = models.CharField(verbose_name='Last name', max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)
    is_principal = models.BooleanField(default=False)

    student_index= models.CharField(
        verbose_name='Student index number', 
        max_length=6, 
        unique=True, 
        null=True, 
        blank=True
        )
    parent1 = models.OneToOneField(
        'User',
        on_delete=models.DO_NOTHING, 
        verbose_name='Parent 1', 
        related_name='parent_1', 
        null=True,
        blank=True
        )
    parent2 = models.OneToOneField(
        'User',
        on_delete=models.DO_NOTHING, 
        verbose_name='Parent 2', 
        related_name='parent_2', 
        null=True,
        blank=True
        )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    list_filter = ('is_admin','is_staff','is_parent','is_active','is_student','is_principal','is_teacher')
    objects = UserManager()

    def get_full_name(self):
        return self.first_name, self.last_name

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def staff(self):
        "Is the user a member of principal?"
        return self.is_staff

    @property
    def admin(self):
        "Is the user a admin member?"
        return self.is_admin

    @property
    def active(self):
        "Is the user active?"
        return self.is_active

    @property
    def student(self):
        "Is the user a student?"
        return self.is_student
    
    @property
    def parent(self):
        "Is the user a parent?"
        return self.is_parent

    @property
    def teacher(self):
        "Is the user a teacher?"
        return self.is_teacher

    @property
    def principal(self):
        "Is the user a member of principal?"
        return self.is_principal

