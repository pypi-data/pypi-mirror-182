# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['keras2trt']

package_data = \
{'': ['*']}

install_requires = \
['onnx==1.10.2',
 'protobuf>=3.9.2,<3.20',
 'tensorflow>=2.8.0',
 'tf2onnx==1.12.1',
 'tomlkit>=0.11.4,<0.12.0',
 'typer==0.6.1']

entry_points = \
{'console_scripts': ['keras2trt = keras2trt.cli:app']}

setup_kwargs = {
    'name': 'keras2trt',
    'version': '0.5.0',
    'description': 'CLI to convert TensorFlow models to TensorRT engines',
    'long_description': '# keras2trt\n\nKeras2TRT is a cli tool that is capable of converting keras saved_models to TensorRT engine. Currently supported conversions are:\n\n- Keras to ONNX\n- ONNX to TensorRT\n- Keras to TensorRT\n\n**_NOTE:_** The CLI is tested converting image segmentation, classification and detection models.\n\n## Requirements\n\nThe following packages need to be installed to use the cli.\n\n```bash\npip install nvidia-pyindex==1.0.9 \\\n&& pip install nvidia-tensorrt==8.4.2.4\n```\n\n**_NOTE:_** nvidia-tensorrt==8.4.2.4 is compatible with nvcr.io/nvidia/tritonserver:22.08-py3 docker image.\n\n## Installation\n\n```\npip install keras2trt\n```\n\n## Usage\n\n```\nUsage: keras2trt [OPTIONS] COMMAND [ARGS]...\n\nOptions:\n  --install-completion [bash|zsh|fish|powershell|pwsh]\n                                  Install completion for the specified shell.\n  --show-completion [bash|zsh|fish|powershell|pwsh]\n                                  Show completion for the specified shell, to\n                                  copy it or customize the installation.\n  --help                          Show this message and exit.\n\nCommands:\n  keras2onnx\n  keras2trt\n  onnx2trt\n  version\n```\n\n### keras2onnx\n\n```\nUsage: keras2trt keras2onnx [OPTIONS]\n\n  Convert Keras model to ONNX model.\n\n  - if --save-path does not have a suffix, ".onnx" suffix will be added to the\n  saved ONNX model.\n\nOptions:\n  --opset INTEGER     ONNX model opset.  [default: 15]\n  --keras-model PATH  Path to the Keras model.  [required]\n  --save-path PATH    Path to save the TensorRT engine.  [required]\n  --help              Show this message and exit.\n```\n\n#### Example\n\n```\nkeras2trt keras2onnx --keras-model models/inceptionv3 --opset 13 --save-path models/tf2onnx\n```\n\nModel path is a keras saved_model directory.\n\n```\nmodels/inceptionv3\n├── assets\n├── keras_metadata.pb\n├── saved_model.pb\n└── variables\n    ├── variables.data-00000-of-00001\n    └── variables.index\n```\n\n### keras2trt\n\n```\nUsage: keras2trt keras2trt [OPTIONS]\n\n  Convert Keras model to tensorrt engine.\n\n  - If --save-path does not have a suffix, ".engine" suffix will be added to\n  the saved TensorRT engine.\n\n  - All min_shape, opt_shape, and max_shape need to be set for dynamic batch\n  size.\n\n  - If none of the shape arguments is set, the batch size will be set as 1.\n\nOptions:\n  --opset INTEGER     ONNX model opset.  [default: 15]\n  --in-shape TEXT     Model input shape.\n  --min-shape TEXT    Minimum input shape for dynamic batch.\n  --opt-shape TEXT    Optimal input shape for dynamic batch.\n  --max-shape TEXT    Maximum input shape for dynamic batch.\n  --keras-model PATH  Path to the Keras model.  [required]\n  --save-path PATH    Path to save the TensorRT engine.  [required]\n  --help              Show this message and exit.\n```\n\n#### Example\n\n```\nkeras2trt keras2trt --opset 17 --in-shape "(1,256,256,3)" --keras-model models/inceptionv3 --save-path models/keras2trt.trt\n\nkeras2trt keras2trt --opset 15 --min-shape "(5,256,256,3)" --opt-shape "(15,256,256,3)" --max-shape "(30,256,256,3)" --keras-model models/inceptionv3 --save-path models/keras2trt\n```\n\nModel path is a keras saved_model directory.\n\n```\nmodels/inceptionv3\n├── assets\n├── keras_metadata.pb\n├── saved_model.pb\n└── variables\n    ├── variables.data-00000-of-00001\n    └── variables.index\n```\n\n### onnx2trt\n\n```\nUsage: keras2trt onnx2trt [OPTIONS]\n\n  Convert ONNX model to tensorrt engine.\n\n  - If --save-path does not have a suffix, ".engine" suffix will be added to\n  the saved TensorRT engine.\n\n  - All min_shape, opt_shape, and max_shape need to be set for dynamic batch\n  size.\n\n  - If none of the shape arguments is set, the batch size will be set as 1.\n\nOptions:\n  --in-shape TEXT    Model input shape.\n  --min-shape TEXT   Minimum input shape for dynamic batch.\n  --opt-shape TEXT   Optimal input shape for dynamic batch.\n  --max-shape TEXT   Maximum input shape for dynamic batch.\n  --onnx-model PATH  Path to the ONNX model.  [required]\n  --save-path PATH   Path to save the TensorRT engine.  [required]\n  --help             Show this message and exit.\n```\n\n#### Example\n\n```\nkeras2trt onnx2trt --in-shape "(1,256,256,3)" --onnx-model models/tf2onnx.onnx --save-path models/onnx2trt\n\nkeras2trt onnx2trt --min-shape "(5,256,256,3)" --opt-shape "(15,256,256,3)" --max-shape "(30,256,256,3)" --onnx-model models/tf2onnx.onnx --save-path models/onnx2trt\n```\n',
    'author': 'Emrecan Altinsoy',
    'author_email': 'emrecanaltinsoy@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://pypi.org/project/keras2trt/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
