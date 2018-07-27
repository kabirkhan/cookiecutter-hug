"""Routes for {{cookiecutter.project_name}}"""
import hug
from services.echo import EchoService


@hug.get('/echo', examples="text=hello world")
def echo(text):
    """
    Return passed text back to caller as an example.
    """
    return EchoService.echo(text)