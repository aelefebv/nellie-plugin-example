# Developing plugins for Nellie
[Nellie]([url](https://github.com/aelefebv/nellie)) is a Napari plugin designed for automated organelle segmentation, tracking, and hierarchical feature extraction in 2D/3D live-cell microscopy. To extend its capabilities and foster a collaborative ecosystem, Nellie supports additional plugins that integrate seamlessly with its core functionality. 

This guide provides a step-by-step workflow for developers to create, package, and distribute their own Nellie plugins, making them easily installable via pip and accessible through the Napari interface under the Plugins -> Nellie plugins submenu.

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
