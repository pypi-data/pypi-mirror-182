import os
import json
import uuid
import yaml
import shutil
import hashlib
import requests
import pandas as pd
import huggingface_hub as hh
from .settings import config
def get_():
    server_file = os.path.join(config['axiom_path'], 'server')
    if os.path.exists(server_file):
        server = open(server_file).read()
        stage = open(os.path.join(config['axiom_path'], 'stage')).read()
        project = open(os.path.join(config['axiom_path'], 'project')).read()
        return server, stage, project
    return None

def create_project(server=None, stage=None, project=None):
    if server is None:
        server, stage, project = get_()
    if server == 'huggingface':
        create_project_huggingface(stage, project)

def set_(server, stage, project):
    '''
    simple: to start over at any time, nothing will be lost when deleted
    test: testing some functions of axiom or to see how it works, suggesting delete time: daily
    develop: developing a project
    stable: the development is stable
    publish: publishing as a jounal paper, not deleting
    axiom_test: testing axiom itself
    '''
    assert stage in ['simple', 'test', 'dev', 'stable', 'public', 'axiom_test']
    open(os.path.join(config['axiom_path'], 'server'), 'w').write(server)
    open(os.path.join(config['axiom_path'], 'stage'), 'w').write(stage)
    open(os.path.join(config['axiom_path'], 'project'), 'w').write(project)
    create_project(server, stage, project)


def get_folder_sha256(folder):
    md5 = hashlib.sha256()
    size_ = 0
    for subdir, _, files in os.walk(folder):
        for f in files:
            full_name = os.path.join(subdir, f)
            size_ += os.stat(full_name).st_size
            with open(full_name, 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    md5.update(chunk)
    return md5.hexdigest(), size_

def axiom_directory_request(func, d):
    axiom_directory_server = open(os.path.join(config['home'], '.huggingface', 'axiom_directory_server')).read()
    key = open(os.path.join(config['home'], '.huggingface', 'key')).read()
    url = f'{axiom_directory_server}/{func}'
    d['key'] = key
    return requests.post(url, json=d).text

def sha256_exists_huggingface(sha256):
    return axiom_directory_request('sha256', {'sha256': sha256})

def sha256_exists(sha256, server=None): # shared among different stages and projects
    if server is None:
        server, _, _ = get_()
    if server == 'huggingface':
        return sha256_exists_huggingface(sha256)


def get_repo_id(stage=None, project=None): # what in ['info', 'obj', 'sha256_info']
    if stage is None:
        _, stage, project = get_()
    user_name = open(os.path.join(config['home'], '.huggingface', 'user_name')).read()
    repo_id = user_name+'/'+stage+'_'+project.replace('/', '_')
    return repo_id




def put_axiom_directory(info_yaml, stage=None, project=None):
    if stage is None:
        _, stage, project = get_()
    d = {'stage': stage, 'project': project, 'info': info_yaml}
    return axiom_directory_request('put', d)


def create_project_huggingface(stage, project):
    repo_id = get_repo_id(stage, project)
    try:
        hh.create_repo(repo_id, repo_type='dataset', token=True, private=True)
    except Exception as e:
        print(e)



def put_node_huggingface(compressed_obj_file, info_yaml, stage=None, project=None): # node means obj + info
    if stage is None:
        _, stage, project = get_()
    repo_id = get_repo_id(stage, project)
    sha256 = info_yaml['sha256']
    hh.upload_file(path_or_fileobj=compressed_obj_file,path_in_repo=sha256,repo_id=repo_id,repo_type="dataset",token=True)


def put_node(compressed_obj_file, info_yaml, server=None, stage=None, project=None):
    if server is None:
        server, stage, project = get_()
    if server == 'huggingface':
        put_node_huggingface(compressed_obj_file, info_yaml, stage, project)

def add_obj(folder, server=None, stage=None, project=None):
    if server is None:
        server, stage, project = get_()
    sha256, folder_size = get_folder_sha256(folder)
    uuid_folder = os.path.split(folder)[0]
    info_file = os.path.join(uuid_folder, 'info.yaml')
    if not os.path.exists(info_file):
        if info_file == 'info.yaml':
            info_file = os.path.join('.', info_file)
        print("make sure %s exists" % info_file)
        return None
    info_yaml = yaml.safe_load(open(info_file))
    obj_folder = os.path.split(folder)[-1]
    cmd = 'cd '+folder+'&& tar zfc ../'+obj_folder+'.tar.gz ./'
    print(cmd)
    os.system(cmd)
    gz_size = os.stat(folder+'.tar.gz').st_size
    info_yaml['original_size'] = folder_size
    info_yaml['compressed_size'] = gz_size
    info_yaml['sha256'] = sha256
    compressed_obj_file = folder+'.tar.gz'
    yaml.safe_dump(info_yaml, open(info_file, 'w'))
    put_node(compressed_obj_file, info_yaml, server, stage, project)

    if os.path.exists(compressed_obj_file):# when server is local, just move, this might not exist
        os.remove(compressed_obj_file)
    print(sha256, 'added')

def add_obj_server(folder, server=None, stage=None, project=None): # folder with all data but not info.yaml
    sha256, folder_size = get_folder_sha256(folder)
    print('sha256', sha256)
    sha256_txt = sha256_exists(sha256)
    info_from_server = None
    uuid_folder = os.path.split(folder)[0]
    info_file = os.path.join(uuid_folder, 'info.yaml')
    if not os.path.exists(info_file):
        if info_file == 'info.yaml':
            info_file = os.path.join('.', info_file)
        print("make sure %s exists" % info_file)
        return None
    info_yaml = yaml.safe_load(open(info_file))
    info_yaml['sha256'] = sha256

    if not sha256_txt == "N":
        info_from_server = yaml.safe_load(sha256_txt)
        print(f'obj {sha256} exists, skip the obj')
        info_from_server['given_name']
        info_yaml['original_size'] = info_from_server['original_size']
        info_yaml['compressed_size'] = info_from_server['compressed_size']

    else:
        obj_folder = os.path.split(folder)[-1]
        cmd = 'cd '+folder+'&& tar zfc ../'+obj_folder+'.tar.gz ./'
        print(cmd)
        os.system(cmd)
        gz_size = os.stat(folder+'.tar.gz').st_size
        info_yaml['original_size'] = folder_size
        info_yaml['compressed_size'] = gz_size
        compressed_obj_file = folder+'.tar.gz'
        yaml.safe_dump(info_yaml, open(info_file, 'w'))
        print(sha256, 'added to axiom obj server')
        put_node(compressed_obj_file, info_yaml, server, stage, project)
        if os.path.exists(compressed_obj_file):# when server is local, just move, this might not exist
            os.remove(compressed_obj_file)

    if server is None:
        server, stage, project = get_()

    put_axiom_directory(info_yaml, stage, project)
    cache_sha256_folder = os.path.join(config['axiom_cache'], sha256)

    if os.path.isdir(cache_sha256_folder):
        print(f'{cache_sha256_folder} exists, skip')
    else:
        shutil.copytree(folder, cache_sha256_folder)

def add_data_int(value, given_name, server=None, stage=None, project=None):
    assert isinstance(value, int)
    if server is None:
        server, stage, project = get_()
    tmp_folder = str(uuid.uuid4())
    obj_folder = os.path.join(tmp_folder, 'obj')
    os.makedirs(obj_folder)
    value_file = os.path.join(obj_folder, 'value')
    open(value_file, 'w').write(str(value))
    info_file = os.path.join(tmp_folder, 'info.yaml')
    info = {
        'axiom_name': '__AXIOM__',
        'description': 'int %d' % value,
        'given_name': given_name,
        'type': 'data.int'
    }
    yaml.safe_dump(info, open(info_file, 'w'))
    add_obj_server(obj_folder, server, stage, project)
    shutil.rmtree(tmp_folder)


def get_yamls_huggingface(stage=None, project=None):
    if stage is None:
        _, stage, project = get_()


def get_yamls_huggingface(stage=None, project=None):
    if stage is None:
        _, stage, project = get_()
    func = 'listall'
    d = {'path': f'{stage}/{project}'}
    return json.loads(axiom_directory_request(func, d))

def get_yamls(server=None, stage=None, project=None):
    if server is None and stage is None:
        server, stage, project = get_()
    if server == 'huggingface':
        return get_yamls_huggingface(stage, project)

def yamls_to_df(ys):
    columns = ['sha256', 'given_name', 'type', 'size']
    d = {}
    for c in columns:
        d[c] = []
    for y in ys:
        sha256 = y['sha256']
        sha256 = f'<a href="./obj/{sha256}/index.html" target="_blank">{sha256}</a>'
        d['sha256'].append(sha256)
        d['given_name'].append(y['given_name'])
        d['type'].append(y['type'])
        d['size'].append(y['compressed_size'])
    df = pd.DataFrame.from_dict(d)
    df = df.sort_values('given_name')
    return df

folder_me = os.path.split(__file__)[0]

mermaid_str = '''```mermaid
graph TD
__ITEMS__

```
'''

def mermaind_item(y, style, shape_left, shape_right):
    return f'    %s{shape_left}%s{shape_right}\n    style %s %s' % (y['sha256'], y['given_name'].split('/')[-1], y['sha256'], style)

def mermaid_items(ys, style, shape_left, shape_right):
    return [mermaind_item(y, style, shape_left, shape_right) for y in ys]

def get_sha256_by_given_name_huggingface(given_name, stage=None, project=None):
    if stage is None:
        _, stage, project = get_()
    func = 'get'
    d = {'stage': stage, 'project': project, 'given_name': given_name}
    print('d', d)
    txt = axiom_directory_request(func, d)
    if not txt.startswith('__err'):
        info = yaml.safe_load(txt)
        return info['sha256']
    else:
        return None

def get_sha256_by_given_name(given_name, server=None, stage=None, project=None):
    if server is None:
        server, stage, project = get_()
    if server == 'huggingface':
        return get_sha256_by_given_name_huggingface(given_name, stage, project)


def download_node_from_server_huggingface(sha256, stage=None, project=None):
    if stage is None:
        _, stage, project = get_()
    cache_dir = config['huggingface_cache']
    repo_id = get_repo_id(stage, project)
    hh.hf_hub_download(repo_id=repo_id, filename=sha256, repo_type="dataset", cache_dir=cache_dir, token=True)
    sha = hh.dataset_info(repo_id).sha
    obj_folder = os.path.join(config['huggingface_cache'], 'datasets--'+repo_id.replace('/','--'), 'snapshots', sha)
    extract_folder = os.path.join(config['axiom_cache'], sha256)
    if not os.path.isdir(extract_folder):
        os.makedirs(extract_folder)
        md5_full_path = os.path.join(obj_folder, sha256)
        cmd = 'tar zxf %s -C %s' % (md5_full_path, extract_folder)
        print(cmd)
        os.system(cmd)
    return extract_folder

def download_node_from_server(sha256, server=None, stage=None, project=None):
    if server is None:
        server, stage, project = get_()
    if server == 'huggingface':
        return download_node_from_server_huggingface(sha256, stage, project)

def get_folder_by_given_name(given_name, server=None, stage=None, project=None):
    sha256 = get_sha256_by_given_name(given_name, server, stage, project)
    if sha256 is None:
        return None
    cache_folder = os.path.join(config['axiom_cache'], sha256)
    if os.path.isdir(cache_folder):
        return cache_folder
    return download_node_from_server(sha256)


def documentation(out_folder, func_map):
    server, stage, project = get_()
    cmd = f"cd {out_folder} && mkdocs new main"
    os.system(cmd)

    yamls = get_yamls()

    df = yamls_to_df(yamls)

    index_md_file = os.path.join(folder_me, 'documentation', 'index.py')
    template = open(index_md_file).read()
    print('template', template)
    template = template.replace('__TITLE__', project)
    template = template.replace('__DATA__', df.to_markdown())
    target_file = os.path.join(out_folder, 'main', 'docs', 'index.md')
    open(target_file, 'w').write(template)
    cmd = f"cd {out_folder}/main/ && mkdocs build"
    os.system(cmd)

    obj_folder = os.path.join(out_folder, 'main', 'site', 'obj')
    if not os.path.isdir(obj_folder):
        os.makedirs(obj_folder)

    for y in yamls:
        func = func_map[y['type']]
        data_folder = get_folder_by_given_name(y['given_name'], server, stage, project)
        index_folder = os.path.join(obj_folder, y['sha256'])
        if not os.path.exists(index_folder):
            os.makedirs(index_folder)
        func(y, data_folder, index_folder)


def reset():
    pass

