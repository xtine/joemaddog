# joemaddog
- Python 3.6.4
- django 2.1.2
- Sass 1.14.1

## Front End Compilation
```
cd scss
sass --watch style.scss ../static/css/style.css --no-source-map --style compressed
```
## Local Development
Create a `local_settings.py` in `maddog` folder that has `DEBUG = True`
