sudo rm -r consumers/migrations
sudo rm -r consumers/__pycache__
sudo rm -r facegate/__pycache__
sudo mkdir consumers/migrations
sudo touch consumers/migrations/__init__.py
python3 manage.py shell <<EOF
from consumers.models import MyUser as User

# Crear el superusuario con tus credenciales
User.objects.create_superuser('admin', 'admin')


EOF