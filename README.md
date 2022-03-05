# slash/idk

`slash/idk` *(Slash, I don't know)* is a [Django](https://www.djangoproject.com/)-based web app that lets you run a simple local web server, where you can shorten long URLs with the name of your choice.

By providing the desired name as a subdirectory to the server's domain name, the app redirects you to the original page mapped to this name.

## Requirements

To run the web app, you primarily need the following installed on your system:
- [Python 3.7+](https://www.python.org/)

## Install

To install the web app, clone the repository in the directory of your choice and enter the project's root directory:

```sh
git clone https://github.com/mhmdkanj/slash-idk.git
cd slash-idk
```

It is highly recommended to deal with the app within a virtual environment.
For more info regarding virtual environments, please refer to the [Python docs](https://docs.python.org/3/tutorial/venv.html).
To create one, execute the following:

```sh
python3 -m venv ./venv
source ./venv/bin/activate  # for Unix/MacOS systems
# OR
venv\Scripts\activate.bat  # for Windows systems
```

Now, you can safely install the dependencies of the web app using [pip](https://pypi.org/project/pip/):

```sh
pip install -r requirements.txt
```

Just for the first time, it is required to set up the database used by the web app (or at least make sure it's okay) by just running the following Django commands:

```sh
cd src
python src/manage.py makemigrations
python src/manage.py migrate
```

## Usage

To run the server, use the following Django command:

```sh
python src/manage.py runserver
```

Most probably, the web server will use port `8000` (otherwise, check the output of the previous command).
If that's the case, then you can open the app by inputting the following URL in your web browser: [http://localhost:8000/](http://localhost:8000/)

To add a mapping:
1. Paste your URL in the first field
2. Enter a short name in the second field
3. Just click `Save`!

For instance, if typing out `http://google.com` tires you, and you would rather use something short like `ggl`, you can input this info as such and then click save:

![Usage](img/usage.png)

The next time you want to visit this site, you can then enter in your browser:
`http://localhost:8000/ggl`, which redirects you to `http://google.com`.

You can also press `"Suggest Name"` to suggest a randomly generated shortened name for the URL.

To quit the server, press `Ctrl`+`C` within the terminal the server was launched from.
