import subprocess
import sys

pip_list = [
    "flake8",
    "pydocstyle",
    "bandit",
    "mypy",
    "black",
    "isort",
    "prettier",
]
html_list = [
    "stylelint",
    "htmlhint",
]
for i in pip_list:
    subprocess.check_call([sys.executable, "-m", "pip", "install", i])


for i in html_list:
    subprocess.check_call([sys.executable, "-m", "npm", "install", i])
