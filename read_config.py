import yaml,os

def read_config():
    '''读取yaml配置'''
    configpath = os.path.join(os.path.dirname(os.path.realpath(__file__)),'config.yaml')
    with open(configpath,'r',encoding='utf-8') as f:
        config = f.read()
    config = yaml.load(config,Loader=yaml.FullLoader)
    return config