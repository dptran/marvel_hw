from app import cli, create_app, db
from app.blueprints.auth.models import User
from app.blueprints.main.models import Post
from app.blueprints.api.models import Collection

app = create_app()
cli.register(app)

@app.shell_context_processor
def make_context():
    return {
        'db': db,
        'User': User,
        'Post': Post,
        'Collection' : Collection,
    }