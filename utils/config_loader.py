import os
import yaml


def load_config(path: str = None) -> dict:
    if path is None:
        path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.yaml')
    with open(os.path.abspath(path), 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


# 模块级单例，直接 from utils.config_loader import config 即可使用
config = load_config()
