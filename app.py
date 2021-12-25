from src import app, context_initializer

context_initializer.Initializer()
if __name__ == '__main__':
    app.run(debug=True)
