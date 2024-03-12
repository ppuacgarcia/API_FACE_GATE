python3 manage.py shell <<EOF
from users.models import MyUser as User

# Crear el superusuario con tus credenciales
User.objects.create_superuser('admin', 'admin')


EOF