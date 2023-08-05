import pluggy
from gliese_plugin import hookspecs, lib


def main():
    plugin_manager = get_plugin_manager()
    device_name = plugin_manager.hook.gliese_plugin_name()
    print(device_name)


# 获取资源
# class GlieseResouce():
#
#     def __init__(self, hook):
#         self.hook = hook
#         self.plugin_name = self.hook.gliese_plugin_name()
#         # self.device_name = self.hook.gliese_device_name()
#         # self.device_id = self.hook.gliese_device_id()
#         # self.device_properties = self.hook.gliese_device_properties()
#
#     def get_device_info(self):
#         return self.device_name, self.device_id
#
#     def get_device_properties(self):
#         return self.device_properties
#
#     def device_connect(self):
#         client, client_id = self.hook.gliese_device_on_connection()
#         return client
#
#     def device_disconnect(self):
#         self.hook.gliese_device_on_disconnection()
#
#     def device_properties_setter(self):
#         self.hook.gliese_device_properties_setter()


# 插件管理
def get_plugin_manager():
    plugin_manager = pluggy.PluginManager("gliese_plugin")
    plugin_manager.add_hookspecs(hookspecs)
    # plugin_manager.register(lib)
    plugin_manager.load_setuptools_entrypoints("gliese_plugin")
    plugins = plugin_manager.get_plugins()
    print(plugins)
    return plugin_manager



if __name__ == "__main__":
    main()