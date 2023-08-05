import pluggy

hookspec = pluggy.HookspecMarker("gliese_plugin")

@hookspec
def gliese_plugin_name():
    """
    返回插件名称
    :param:
    :return: name
    """

@hookspec
def gliese_plugin_version():
    """
    返回插件版本
    :param:
    :return: version
    """

@hookspec
def gliese_plugin_description():
    """
    返回插件描述
    :param:
    :return: description
    """

@hookspec
def gliese_plugin_config(**kwargs):
    """
    插件配置
    :param:
    :return:
    """

@hookspec
def gliese_plugin_enable():
    """
    插件激活
    :param:
    :return:
    """

@hookspec
def gliese_plugin_disable():
    """
    插件禁用
    :param:
    :return:
    """

@hookspec
def gliese_device_id():
    """
    返回设备ID
    :param:
    :return: device_id
    """

@hookspec
def gliese_device_name():
    """
    返回设备名称
    :param:
    :return: device_name
    """

@hookspec
def gliese_device_properties():
    """
    返回设备属性
    :param:
    :return: device_properties
    """

@hookspec
def gliese_device_properties_setter(setter):
    """
    更新设备属性
    :param:
    :return:
    """

@hookspec
def gliese_device_on_connection():
    """
    设备连接
    :param:
    :return:
    """

@hookspec
def gliese_device_on_disconnection():
    """
    设备断开连接
    :param:
    :return:
    """

@hookspec
def gliese_device_on_cmd():
    """
    设备执行命令
    :param:
    :return:
    """
