import git

from cqh_util import invoke_util
from invoke import task
import os
proj_dir = os.path.dirname(
    os.path.abspath(__file__)
)
proj_name = 'cqh_util'
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


@task
def upload(c):
    c.run("twine upload dist/*")


@task
def deploy(c):
    c.run("rm -rf ${proj_dir}/docs/_build/html")
    with c.cd(f"{proj_dir}/docs"):
        c.run("/home/vagrant/envs/default/bin/sphinx-build -M html . _build")
    cmd = f"ansible-playbook  {proj_dir}/playbooks/deploy.yaml -e proj_name={proj_name} -e proj_dir={proj_dir}"
    c.run(cmd)


@task
def build_and_install(c):
    generate(c)
    dist_dir = os.path.join(
        proj_dir, 'dist'
    )
    if os.path.exists(dist_dir):
        for file in os.listdir(dist_dir):
            abs_path = os.path.join(dist_dir, file)
            os.remove(abs_path)
            print("remove {}".format(abs_path))

    c.run("python3 setup.py sdist bdist_wheel")
    whl_path = None
    for file in os.listdir(dist_dir):
        if file.endswith(".whl"):
            abs_path = os.path.join(dist_dir,
                                    file)
            whl_path = abs_path
            break

    assert whl_path
    c.run("pip install -U {}".format(whl_path))


@task
def gpush(c):
    repo = git.Repo(proj_dir)
    active_branch = repo.active_branch
    repo.remote().push(active_branch)


@task
def copy_files(c):
    c.run(f"ansible-playbook {proj_dir}/playbooks/copy_files.yaml -e proj_name={proj_name} -e proj_dir={proj_dir}")


@task
def generate(c):

    readme_path = os.path.join(proj_dir, 'readme.rst')
    target_conf_path = os.path.join(proj_dir, proj_name, 'conf.py')
    with open(readme_path, 'r') as read_f, open(target_conf_path, 'w') as write_f:
        write_f.write('''doc = """
                      {}
                      """\n'''.format(read_f.read()))
