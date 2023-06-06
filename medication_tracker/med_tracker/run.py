from med_tracker import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

#? Routes: These are URL patterns that the application can respond to. The routes of a Flask application are defined using Python decorators on view functions, which return responses to the requests.

#? Templates: These are HTML files which can include placeholders for variable content. They can be filled with data dynamically and rendered by the application.

#? Databases: This is where your application's data is stored. Flask can work with a variety of databases, but you'll use SQLite in this case.