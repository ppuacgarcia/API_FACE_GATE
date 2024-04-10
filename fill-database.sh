python3 manage.py shell <<EOF
from consumers.models import MyUser as User

# Crear el superusuario con tus credenciales
User.objects.create_superuser('admin', 'admin')


EOF
python3 manage.py runserver