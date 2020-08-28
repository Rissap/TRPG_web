from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager


# user managar & model for registration

class PlayerAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class PlayerAccount(AbstractBaseUser):
	email = models.EmailField(verbose_name="email", max_length=60, unique=True)
	username = models.CharField(max_length=30, unique=True)
	last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	notifications = models.BooleanField(default=False)


	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	objects = PlayerAccountManager()

	def __str__(self):
		return self.email

	# For checking permissions. to keep it simple all admin have ALL permissons
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
	def has_module_perms(self, app_label):
		return True


# game entities




"""
class Post(models.Model):
	title = models.CharField(max_length=255) 

	def __str__(self):
		return '{}'.format(self.title, )


class Employee(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, )
	post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return '{} {}'.format(self.post, self.user.username)


class Product(models.Model):
	title = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=13, decimal_places=2)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '{} {}'.format(self.title, self.price)

class Sales(models.Model):
	types = models.CharField(max_length=20, unique=True)
	coef = models.DecimalField(max_digits=3, decimal_places=2)
	priority = models.IntegerField(unique=True, null=True)

	def __str__(self):
		return '{}'.format(self.coef)


class Order(models.Model):
	customer = models.CharField(max_length=255)
	consultant = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	sale = models.ForeignKey(Sales, on_delete=models.SET_NULL, blank=True, null=True, default=None)
	total = models.DecimalField(max_digits=13, decimal_places=2)
	confirmed = models.BooleanField(default=False)
	paid = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '{} {} with {}'.format(self.customer, self.product, self.sale)
"""