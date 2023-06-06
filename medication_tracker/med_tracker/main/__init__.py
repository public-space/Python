from flask import Blueprint

bp = Blueprint('main', __name__)

from med_tracker.main import views









#? the app/main/\_\_init\_\_.py script is the blueprint package.

#? We are dividing the app into blueprints. Each blueprint is a collection of views, templates, static files, and other elements that can be registered with the application. The registration is done in the app/\_\_init\_\_.py script, which runs the first time a request is received. The end result of this structure is that the application has two Flask blueprints: auth and main. The auth blueprint handles the authentication functions, and the main blueprint handles everything else.

#? The routes are the different URLs that the application implements. In Flask, handlers for the application routes are written as Python functions, called view functions. View functions are mapped to one or more route URLs so that Flask knows what logic to execute when a client requests a given URL.

#? The templates folder in the main directory is where Flask will look for Jinja2 templates that are used to render the pages. The static folder in the main directory is where Flask will look for the CSS and JavaScript files.

#? The app/\_\_init\_\_.py script is the application package, and the app/main/\_\_init\_\_.py script is the blueprint package. The templates and static folders are inside the blueprint package because they are associated with the blueprint.

#? The app/\_\_init\_\_.py script is the application factory, as explained earlier. The current_app and db objects are created here. The app/\_\_init\_\_.py script imports the routes module, which defines the view functions themselves. The bottom of the script imports the authentication blueprint. These imports are at the bottom to avoid circular dependencies, since views.py and errors.py need to import the main blueprint object.

#? The app/main/\_\_init\_\_.py script defines the blueprint. The script is similar to the app/\_\_init\_\_.py script, except there is no need to import the Blueprint class. Instead, the blueprint is created directly at the top of the script and passed to the constructor of the Blueprint class as a parameter. The routes are imported at the bottom and registered with the blueprint.