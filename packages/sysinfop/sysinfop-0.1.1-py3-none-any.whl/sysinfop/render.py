from rich.panel import Panel
from rich import box
from .sysinfo import getSystemInfo

data = getSystemInfo()
box = box.MINIMAL

banner = f"[bold]{data['hostname']}[/bold]"

def render_item(label,data):
  return f"[bold]{label}[/bold]: {data}"

def render_string(data):
  str = ""
  
  # Loop over list of tuples and pass each tuple to
  # the render_item() function. Join the results together
  # and return the resulting string.
  for d in data:
    s = str + f"* {render_item(d[0], d[1])}\n"
    str = s
  return s

format_template = render_string([
  ("IP", data["ip-address"]),
  ("OS", data["platform"]),
  ("CPU", data["processor"]),
  ("RAM", data["ram"]),
  ("MAC", data["mac-address"]),
  ("ARCH", data["architecture"]),
])

layout = Panel(format_template,
               expand=False,
               height=8,
               box=box)
