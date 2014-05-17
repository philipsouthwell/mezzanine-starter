mezzanine-starter
=================

A basic Python 3.3 mezzanine-cartridge project starter template. Includes a fresh template.

**Under Development**

![Screenshot of this Mezzanine theme](/fresh_theme/static/fresh-theme/example.jpg "Screenshot of mezzanine-starter home page")

## Installation
This is a basic starter project for Mezzanine/Cartridge project. As such it requires all the libraries needed by
Mezzanine and Cartridge. It also uses the library ![mezzanine-blocks](https://github.com/renyi/mezzanine-blocks)
which needs to be installed from github. All these dependencies can be satisfied by following these instructions

1. Clone this project into your local directory
2. Create and activate a Python 3.3 virtual environment:
   ```bash
       virtualenv -p Python3.3 /path/to/environment
       source /path/to/environment/bin/activate
   ```
   For windows users the last line should read:
   ```bash
       /path/to/environment/scripts/activate
   ```

3. Within the virtual environment install mezzanine_blocks via pip:
   ```bash
       pip install git+git://github.com/renyi/mezzanine-blocks.git
   ```
4. Still in the virtual environment navigate to your project folder and install the other libraries
   ```bash
       pip install -r requirements.txt
   ```
5. Create a local_settings.py file and fill in your database details
   ```python
   DEBUG = True

   # Make these unique, and don't share it with anybody.
   SECRET_KEY = "make-a-unique-key"
   NEVERCACHE_KEY = "make-another-unique-key"

   DATABASES = {
       "default": {
           # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
           "ENGINE": "django.db.backends.sqlite3",
           # DB name or path to database file if using sqlite3.
           "NAME": "database_name",
           # Not used with sqlite3.
           "USER": "",
           # Not used with sqlite3.
           "PASSWORD": "",
           # Set to empty string for localhost. Not used with sqlite3.
           "HOST": "localhost",
           # Set to empty string for default. Not used with sqlite3.
           "PORT": "3308",
       }
   }

   ALLOWED_HOSTS = ['27.0.0.1:8000',]
   ```
6. Now initialise your database
   ```bash
       python manage.py syncdb
   ```
   and also because Mezzanine uses South
   ```bash
       python manage.py migrate
   ```
7. We should now we able to run our django development server
   ```bash
       python manage.py runserver
   ```
8. Navigate in your browser to http://127.0.0.1:8000/ and view your new Mezzanine/Cartridge site!




## Configuration of Blocks and Home Page Feed
This theme has blocks which can be edited from the admin panel.

#### Home page
In the admin panel create "Rich Blocks" with the exact following names:
* home page image
* footer one
* footer two
* footer three
* footer four

In the admin panel also create a regular "Block" and give it the name:
* home page well

The content of these blocks will appear in the set positions on the home page.
For optimal display images placed in the footer blocks should be no wider than 250px, and images placed in the "home
page image" block should be no wider than 800px.

#### Other pages
In the admin panel also create "Rich Blocks" with the exact following names:
* side one
* side two

The content of these blocks will appear in the side bar on all other pages. For optimal display images placed in these
blocks should be no wider than 263px.

Features in development
-----------------------
* Make news feed tag used on home page inline editable



