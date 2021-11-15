from jinja2 import Environment, PackageLoader
import os


env = Environment(
    loader=PackageLoader("generator", "template")
)


build_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "build")
if not os.path.exists(build_dir):
    os.mkdir(build_dir)
index_path = os.path.join(build_dir, "index.html")


site_html = env.get_template("site/pages/index.html").render()

with open(index_path, mode="w") as html_file:
    html_file.write(site_html)
