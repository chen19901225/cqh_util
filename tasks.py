
from cqh_util import invoke_util
from invoke import task
import os
proj_dir = os.path.dirname(
    os.path.abspath(__file__)
)

venv_dir = os.path.join(proj_dir,
                        'venv')


@task
def lint_new(c):
    file_list = invoke_util.git_unstaged_and_untracked_file_list(
        proj_dir=proj_dir
    )
    file_list = [e for e in file_list if e.endswith(".py")]
    cmd = "{}/bin/flake8 {}".format(venv_dir,
                                    " ".join(file_list)
                                    )
    c.run(cmd)
