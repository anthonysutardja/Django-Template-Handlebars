Django Template Handlebars
======
Django's templating syntax and Handlebars.js's expressions have overlapping syntax, i.e. `{{ stuff }}` , that makes it very difficult to create templates that utilize both frameworks.

**TODOS:** Enable `{% block %}` tags to be rendered within the handlebars designated fragments.

This **templatetag** application allows you to use both in a seamless manner.

##Installation
- Place the _handlebars_ app folder along with your apps.
- Add the app to `INSTALLED_APPS` in _settings.py_

##Templating
Django will automatically look for a folder called _templatetags_ in each installed app.
In a template, you must load the handlebars template tags at the beginning of the template.

		{% load handlebars %}
		<!DOCTYPE HTML>
		<html lang='en'>
			etc...
					
To use the handlebars template tag, simply surround your code that you wish to be templated by **Handlebars.js** rather than Django.

		{% load handlebars %}
		<!DOCTYPE HTML>
		<html lang='en'>
		    <head>
		        <title>{{title}}</title>
		    </head>
		    <body>
		
		    {% handlebars %}
		    <!-- This code is not contexted by Django -->
		        <h1>Hello, {{name}}</h1>
		        <p>This ia bunch of text.</p>
		        <div id="wrap">
		            {{#list books}} {{title}} {{/list}}
		        </div>
		        <p>{{books_avail}}</p>
		    {% endhandlebars %}
		
		    <h2>{{ some_var_in_django }}</h2>
		    </body>
		</html>

**Note:** If there is a naming conflict (e.g. another tag already has the name 'handlebars'), resolve it by renaming the file _templatetags/handlebars.py_ to _templatetags/somethingelse.py_.

Feel free to fork and toy with it!