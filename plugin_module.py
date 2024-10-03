from napari.utils.notifications import show_info


def nellie_plugin_function(napari_viewer):
    show_info("Hello from my plugin!")
    print("Hello from my plugin!")
