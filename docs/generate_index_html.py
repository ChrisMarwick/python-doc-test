import jinja2
import os


os.chdir(os.path.dirname(os.path.realpath(__file__)))
REPO_NAME = 'python-doc-test'


def is_local_build():
    return False


def get_redirect_url():
    doc_versions = os.listdir('./build/release')
    version = max(doc_versions)
    # When running non-locally we need to include the repo name explicitly as this is part of the url.
    # However when running locally the redirect only uses the folder structure so we shouldn't include the repo name
    prefix = '' if is_local_build() else REPO_NAME
    return f'./release/{version}/index.html'


environment = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath='./'))
template = environment.get_template('./index.html')
with open('./build/index.html', 'w') as f:
    f.write(template.render(redirect_url=get_redirect_url()))
