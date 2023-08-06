from abc import ABC, abstractmethod

from configparser import ConfigParser
from pathlib import Path

from .. import HF_PROJ_PATH
from .flow import Flow
from ..tools import ConfigReader


class Interface(ABC):

    def __init__(self, config_file=None, **kwargs):
        # 如果config_file为None，则读取默认配置
        if config_file is None:
            config_file = self.get_default_setting_file()
        self.cfgr = ConfigReader(config_file)

        # show config
        if kwargs.get('show_config', True):
            print(self.cfgr)

        self.flow = Flow.from_config(flow_config=self.cfgr.flow_config, **kwargs)
    
    def get_default_setting_file(self):
        setting_file_path = Path(HF_PROJ_PATH) / 'project' / 'interface' / 'setting.ini'
        assert setting_file_path.exists(), "Default setting file is not provided!"

        setting = ConfigParser()
        setting.read(str(setting_file_path))
        config_file_path = Path(HF_PROJ_PATH) / 'project' / setting['DEFAULT']['config']
        return str(config_file_path)

    def run_flow(self, feed_dict):
        self.flow(feed_dict)

    @abstractmethod
    def respond(self, req):
        """这个方法用于和底层服务进行对接

        Args:
            req (dict): 输入的服务调用字典

        Returns:
            dict: 输出的返回结果字典
        """

        raise NotImplementedError()
