from jinja2 import Environment, PackageLoader
import os


env = Environment(
    loader=PackageLoader("gen", "template")
)


build_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "gen/build")
if not os.path.exists(build_dir):
    os.mkdir(build_dir)
index_path = os.path.join(build_dir, "index.html")

site_html = env.get_template("site/pages/index.html").render()

with open(index_path, mode="w") as html_file:
    html_file.write(site_html)


print("index.html file generated successfully!\n" +
      "You can find it at gen/build/index.html")
