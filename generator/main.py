from jinja2 import Environment, PackageLoader
import os


env = Environment(
    loader=PackageLoader("generator", "template")
)
