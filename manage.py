from app import create_app
from flask_script import manager,Server

app = create_app('developement')

manager = Manager (app)
manager.add_command('server', Server)
if __name__ == '__main__':
    manager.run()