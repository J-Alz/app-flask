from app import create_app

app = create_app()

if __name__ == '__main__':
    app.config.from_object('config.DevConfig')
    app.run()