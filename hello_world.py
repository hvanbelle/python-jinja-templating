import jinja2
environment = jinja2.Environment()
template = environment.from_string("Hello, {{ name }}!")
message = template.render(name="World")
print(message)