import os
import sys
import pprint
import getpass
from .settings import config
from .common import get_



def main(sys_argv):
    if len(sys_argv) == 1:
        lines = open(__file__).read().split('\n')
        lines = [line for line in lines if line.find('if sys_argv[1]') > 0][1:]
        cmds = [line.split("'")[1].split("'")[0] for line in lines]
        comments = [line.split("#")[-1] for line in lines]
        usages = [cmds[i]+': '+comments[i] for i in range(len(cmds))]
        print('\n'.join(usages))
        return

    if sys_argv[1] == 'info': # show basic info of the project
        print('my file name', __file__)
        print('config', config)
        server, stage, project = get_()
        print(server, stage, project)


    if sys_argv[1] == 'huggingface': # settup the huggingface token and username
        token = getpass.getpass('huggingface token:')
        user_name = input('huggingface private db user:')
        axiom_directory_server = input('axiom_directory_server:')
        key = getpass.getpass('axiom_directory_server key:')

        huggingface_path = os.path.join(config['home'], '.huggingface')
        if not os.path.isdir(huggingface_path):
            os.mkdir(huggingface_path)
        
        open(os.path.join(huggingface_path, 'token'), 'w').write(token)
        open(os.path.join(huggingface_path, 'user_name'), 'w').write(user_name)
        open(os.path.join(huggingface_path, 'axiom_directory_server'), 'w').write(axiom_directory_server)
        open(os.path.join(huggingface_path, 'key'), 'w').write(key)


        

if __name__ == '__main__':
    main(sys.argv)
