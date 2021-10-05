
from django.db.models.deletion import CASCADE
#from net.views import upload
import uuid
from datetime import date
from django.db import models
from stdimage import StdImageField, JPEGField
from django.contrib.auth.models import BaseUserManager, AbstractUser

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

#Customização da model Admin
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user_manager(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Informe o email")
        
        email = self.normalize_email(email)
        user = self.model(email=email, password=password, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user_manager(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError("O super usuario precisa ter o atributo is_superuser = True")

        if extra_fields.get('is_staff') is not True:
            raise ValueError("O super usuario precisa ter o atributo is_staff = True")
        
        return self._create_user_manager(email, password, **extra_fields)

class MyUserAdmin(AbstractUser):
    email = models.EmailField(verbose_name='email adress', max_length=255, unique=True)
    dt_expiracao = models.DateTimeField('Data de Expiracao', default=date(year=1900, month=1, day=1))
    is_staff = models.BooleanField('Membro da equipe', default=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'dt_expiracao']

    def __str__(self):
        return self.email
    
    objects = UserManager()


