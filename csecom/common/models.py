from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserManager(BaseUserManager):
    def create_user(self, student_id, name, password=None):
        if not student_id:
            raise ValueError('학번을 정확히 입력해주세요.')

        user = self.model(student_id=student_id, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, student_id, name, password):
        user = self.create_user(student_id=student_id, name=name, password=password,)
        user.is_admin = True
        user.save(using=self._db)

        return user
    
class User(AbstractBaseUser):
    student_id = models.CharField(verbose_name='학번', max_length=10, unique=True)
    name = models.CharField(verbose_name='이름', max_length=20)
    password = models.CharField(verbose_name='비밀번호', max_length=128)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_student_pay = models.BooleanField(default=False)
    locker_id = models.IntegerField(verbose_name='사물함 번호', default=0)

    objects = UserManager()

    USERNAME_FIELD = 'student_id'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return f'{self.student_id}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    
    @property
    def is_check(self):
        return self.is_student_pay

    @property
    def locker_used(self):
        return self.locker_id
