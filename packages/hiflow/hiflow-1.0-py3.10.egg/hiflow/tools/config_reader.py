#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File        : global_config.py
@Description : 用于项目的全局配置读取
@Date        : 2020/10/29 11:37:51
@Author      : merlinbao
@Version     : 1.0
"""


import imp
import json

from pathlib import Path

from .. import HF_MODEL_PATH, HF_PROJ_PATH, utils


class ConfigReader:

    def __init__(self, config_file):
        """ConfigReader负责配置文件的读取，并将用户写好的Stage类载入环境中

        Args:
            config_file (str): 配置文件的路径
        """

        assert config_file is not None and config_file.endswith('.py'), "Config file is invalid."

        self.load_config(config_file)
        self.register_stages()

    def load_config(self, config_file):
        config_file = ConfigReader.fix_references(config_file)
        cfgs = imp.load_source("cfgs", config_file)

        for k, v in cfgs.__dict__.items():
            if not k.startswith('__'):
                setattr(self, k, v)

    def register_stages(self):
        stages_dir_path = Path(HF_PROJ_PATH) / 'project' / 'stages'
        assert stages_dir_path.exists(), "Stages are not defined!"

        for stage_path in stages_dir_path.glob('*.py'):
            if 'stage' in str(stage_path):
                _ = imp.load_source("", str(stage_path))

    @staticmethod
    def fix_references(config_file):
        """修复配置文件中的路径指代为真实路径

        Args:
            config_file (str): 配置文件路径
        """

        # 修复文件
        content = None
        with open(config_file, 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                lines[i] = line.replace('$HF_PROJ_PATH', HF_PROJ_PATH).replace('$HF_MODEL_PATH', HF_MODEL_PATH)
            content = ''.join(lines)

        # 创建临时文件夹，存放修复后的配置文件
        tmp_dir_path = Path(HF_PROJ_PATH) / '.tmp' / 'config.py'
        if not tmp_dir_path.parent.exists():
            tmp_dir_path.parent.mkdir(parents=True)
        with tmp_dir_path.open('w') as f:
            f.write(content)

        return str(tmp_dir_path)

    def __str__(self):
        main_str = ''
        main_str += utils.wrap_title("Flow configuration:") + '\n'
        dump_str = json.dumps(self.flow_config, indent=4)
        dump_str = utils.make_list_flat(dump_str, ['classes'])
        return main_str + dump_str
