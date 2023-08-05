import gliese_plugin


@gliese_plugin.hookimpl
def gliese_plugin_name():
    """
    返回插件名称
    :param:
    :return: name
    """

@gliese_plugin.hookimpl
def gliese_plugin_version():
    """
    返回插件版本
    :param:
    :return: version
    """

@gliese_plugin.hookimpl
def gliese_plugin_description():
    """
    返回插件描述
    :param:
    :return: description
    """

@gliese_plugin.hookimpl
def gliese_plugin_config(**kwargs):
    """
    插件配置
    :param:
    :return:
    """

@gliese_plugin.hookimpl
def gliese_plugin_enable():
    """
    插件激活
    :param:
    :return:
    """

@gliese_plugin.hookimpl
def gliese_plugin_disable():
    """
    插件禁用
    :param:
    :return:
    """

@gliese_plugin.hookimpl
def gliese_device_id():
    """
    返回设备ID
    :param:
    :return: device_id
    """

@gliese_plugin.hookimpl
def gliese_device_name():
    """
    返回设备名称
    :param:
    :return: device_name
    """

@gliese_plugin.hookimpl
def gliese_device_properties():
    """
    返回设备属性
    :param:
    :return: location of device
    """

@gliese_plugin.hookimpl
def gliese_device_properties_setter(setter):
    """
    更新设备属性
    :param:
    :return:
    """
    # error: hook calling supports only keyword arguments

@gliese_plugin.hookimpl
def gliese_device_on_connection():
    """
    设备连接
    :param:
    :return:
    """

@gliese_plugin.hookimpl
def gliese_device_on_disconnection():
    """
    设备断开连接
    :param:
    :return:
    """


@gliese_plugin.hookimpl
def gliese_device_on_cmd():
    """
    设备执行命令
    :param:
    :return:
    """