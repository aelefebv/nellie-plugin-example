# Developing plugins for Nellie
[Nellie]([url](https://github.com/aelefebv/nellie)) is a Napari plugin designed for automated organelle segmentation, tracking, and hierarchical feature extraction in 2D/3D live-cell microscopy. To extend its capabilities and foster a collaborative ecosystem, Nellie supports additional plugins that integrate seamlessly with its core functionality. 

This guide provides a step-by-step workflow for developers to create, package, and distribute their own Nellie plugins, making them easily installable via pip and accessible through the Napari interface under the Plugins -> Nellie plugins submenu.

# Understanding the Nellie Plugin System

## How the Plugin System Works

### 1. Entry Points Mechanism

Nellie leverages Python’s entry_points mechanism to discover and load plugins dynamically. Entry points are a way for Python packages to advertise components (like functions or classes) that can be used by other packages at runtime.

- Entry Point Group: Nellie defines a specific entry point group called nellie.plugins. Plugins register their functions under this group.
- Registration: When a plugin is installed (typically via pip), the entry points declared in its setup.py or pyproject.toml are registered in the Python environment.
- Discovery: Nellie scans the nellie.plugins entry point group to find all registered plugins.

### 2. Plugin Discovery and Loading in Nellie

When Nellie is loaded within Napari:

- Scanning for Plugins: Nellie uses the importlib.metadata.entry_points (or pkg_resources.iter_entry_points for older Python versions) to retrieve all entry points under the nellie.plugins group.
- Loading Plugin Functions: Each discovered entry point is loaded, obtaining a reference to the plugin function.
- Building the Menu: Nellie adds each plugin to the Napari menu under Plugins -> Nellie, allowing users to easily access the additional functionality.

### 3. Integration with Napari

- Napari Plugin Architecture: While Napari has its own plugin system, Nellie’s plugin system operates within its own namespace to maintain a cohesive user experience.
- Menu Hierarchy: Plugins registered under Nellie’s system appear in a dedicated submenu, ensuring they are easily distinguishable from other Napari plugins.
- User Interaction: When a user selects a Nellie plugin from the menu, the corresponding function is invoked, allowing the plugin to interact with the napari_viewer and Nellie’s data.

# Example Workflow for Plugin Developers:

1.	Write the Plugin Function:
 ```python
# plugin_module.py
def nellie_plugin_function(napari_viewer):
    # Access Nellie's outputs and perform custom processing
    pass
```
2.	Set Up setup.py:
```python
from setuptools import setup

setup(
    name='my-nellie-plugin',
    version='0.1.0',
    py_modules=['plugin_module'],
    entry_points={
        'nellie.plugins': [
            'Custom Plugin Name = plugin_module:nellie_plugin_function',
        ],
    },
)
```
3.	Distribute the Plugin:
Publish the plugin to PyPI or share it so users can install it via
```bash
pip install my-nellie-plugin.
```

## Distributing the plugin

### 1.	Install Build Tools:
Make sure you have the latest versions of setuptools and wheel:
```bash
pip install --upgrade setuptools wheel
```

### 2.	Build the Package:
From the root directory of your project (where setup.py is located), run:
```bash
python setup.py sdist bdist_wheel
```
This will create a dist/ directory containing:
- A source distribution (.tar.gz)
- A built distribution wheel (.whl)

### 3. Upload Your Package to PyPI
To upload your package to PyPI, you’ll use the twine tool.
a.	Create a PyPI Account:
- Go to PyPI and create an account if you don’t have one.
- Verify your email address.

b.	Install Twine:
```bash
pip install --upgrade twine
```

c.	Test Your Package with TestPyPI (Optional but Recommended):
Upload to TestPyPI:
- TestPyPI is a separate instance of PyPI for testing.
- Create an account on TestPyPI.
```bash
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```
Test Installation from TestPyPI:
```bash
pip install --index-url https://test.pypi.org/simple/ my-nellie-plugin
```

d.	Upload to PyPI:
When you’re ready to release your Nellie plugin publicly:
```bash
twine upload dist/*
```

### 4. Verify Installation
After uploading to PyPI, verify that your package can be installed and works as expected.

a.	Install Your Plugin:
```bash
pip install my-nellie-plugin
```

b.	Test the Plugin in Napari with Nellie:
- Open Napari.
- Load Nellie, then ensure your plugin appears under Plugins -> Nellie plugins -> Custom Plugin Name.
- Test the functionality to confirm everything works as intended.

# Summary of the Plugin Workflow
1. Plugin Function Definition: Create a function that accepts napari_viewer and implements your desired functionality.
2. Entry Point Registration: Register your plugin function under the nellie.plugins entry point group in your setup.py.
3. Packaging and Distribution: Package your plugin using standard Python packaging tools and distribute it via PyPI or other means.
4. Installation by Users: Users install your plugin via pip, which registers the entry points.
5. Plugin Discovery by Nellie: When Nellie initializes, it discovers all installed plugins registered under nellie.plugins.
6. Integration into Napari: Plugins are added to the Napari menu under Plugins -> Nellie, providing easy access for users.
7. Execution: When a user selects your plugin from the menu, your function is called with the napari_viewer, allowing you to interact with both Nellie and Napari.

# Additional Resources
- Python Entry Points Documentation: [Python Packaging User Guide - Entry Points]([url](https://packaging.python.org/en/latest/specifications/entry-points/))
- Napari Plugin Development: [Napari Plugin Developer Guide]([url](https://napari.org/stable/plugins/index.html))
- Nellie Source Code: [Refer to Nellie’s source code for examples of how plugins are discovered and loaded.]([url](https://github.com/aelefebv/nellie))

# Frequently Asked Questions

Q: How does Nellie discover plugins at runtime?

A: Nellie uses the Python entry_points mechanism to discover plugins. When Nellie initializes, it queries the nellie.plugins entry point group to find all registered plugin functions. These functions are then loaded and integrated into the Napari interface.

Q: Do I need to modify Nellie’s source code to add my plugin?

A: No, you don’t need to modify Nellie’s source code. By registering your plugin via entry points and ensuring it’s installed in the Python environment, Nellie can automatically discover and integrate your plugin.

Q: Can my plugin have its own dependencies?

A: Yes, you can specify any dependencies your plugin requires in the install_requires section of your setup.py. These dependencies will be installed automatically when users install your plugin via pip.

Q: What versions of Python are supported?

A: Ensure that your plugin is compatible with the Python versions supported by Nellie and Napari. Typically, supporting Python 3.9 and above is recommended.

Q: Can I contribute my plugin back to the Nellie project?

A: Absolutely! If you believe your plugin adds valuable functionality that would benefit the broader user base, consider contributing it back to the Nellie project. You can submit a pull request or contact the maintainers (aka me, Austin) for more information.
