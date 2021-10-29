from app import createSchema, create_app

app=create_app()
app.app_context().push()

createSchema()