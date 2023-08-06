# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['qucuQuantum']

package_data = \
{'': ['*']}

install_requires = \
['cupy-cuda11x>=11.4.0,<12.0.0',
 'cuquantum-python>=22.11.0,<23.0.0',
 'cuquantum>=22.11.0,<23.0.0',
 'cutensornet-cu11>=2.0.0,<3.0.0',
 'numpy>=1.23.5,<2.0.0']

setup_kwargs = {
    'name': 'quqcs',
    'version': '0.1.0',
    'description': 'quqcs is an open source library for quantum compute simulating on NVIDIA GPU',
    'long_description': '## qucuQUantum\n\n[![Documentation Status](https://img.shields.io/badge/docs-latest-brightgreen.svg)](http://developer.queco.cn)\n[![License](https://img.shields.io/badge/license-Apache%202-blue.svg)](LICENSE)\n[![Download Code](https://img.shields.io/badge/download-zip-green.svg)](https://github.com/xxx)\n\n### **概述**\n---\n* qucuQuantum 是基于 NVIDIA cuQuantum 开发的量子线路模拟器，可与启科量子编程框架QuTrunk集成，实现基于本地GPU服务器的量子线路模拟计算加速。\n* qucuQuantum 目前只支持 State Vector 的量子线路模拟\n* qucuQuantum 基于 Python 语言，提供门级别的 API， 包括H, CH, P, CP, R, CR, Rx, Ry, Rz, Rxx, Ryy, Rzz, X, Y, Z, S, T, Sdg, Tdg, SqrtX, CSqrtX, SqrtSwap, Swap, CSwap, CNot, MCX, CY, MCZ, U1, U2, U3, U, CU, ISwap, SqrtXdg, PH等量子门\n* qucuQuantum 目前只支持与QuTrunk本地集成，需要与QuTrunk部署在同一台 NVIDIA GPU 服务器上。\n\n### **下载和安装**\n---\n* qucuQuantum 作为独立的库，与 runtime 集成，由 runtime 完成部署安装。\n\n### **使用方法**\n1. qucuQuantum 库引入QuTrunk代码中\n```import\nfrom qucuQuantum.cuQuantum import BackendcuQuantum\n```\n\n2. 在QuTrunk代码中，构造QCircuit对象时，指定backend为BackendcuQuantum, \n```initialize\ncircuit = QCircuit(backend=BackendcuQuantum())\n```\n### **示例代码**\n\n以下示例展示了利用 QuTrunk 运行 bell-pair 量子算法：\n\n  ```python\n  # import package\n  from qutrunk.circuit import QCircuit\n  from qutrunk.circuit.gates import H, CNOT, Measure, All\n  from qucuQuantum.cuQuantum import BackendcuQuantum\n\n  # allocate resource\n  qc = QCircuit(backend=BackendcuQuantum())\n  qr = qc.allocate(2) \n\n  # apply quantum gates\n  H * qr[0]   \n  CNOT * (qr[0], qr[1])\n  All(Measure) * qr\n\n  # print circuit\n  qc.print()   \n  # run circuit\n  res = qc.run(shots=1024) \n  # print result\n  print(res.get_counts()) \n  # draw circuit\n  qc.draw()\n  ```\n运行结果：\n<div>\n<img src="http://developer.queco.cn/media/images/bell_pairYunXingJieGuo.original.png"/>\n</div>\n\n### **许可证**\n---\nqucuQuantum 是自由和开源的，在Apache 2.0许可证版本下发布。\n\n\n### ** 依赖 **\n| 内容                            | 要求                                 |\n|-------------------------------|------------------------------------|\n| GPU 架构                        | Volta, Turing, Ampere, Ada, Hopper |\n| NVIDIA GPU Compute Capability | 7.0+                               |\n| CUDA                          | 11.x                               |\n| CPU 架构                        | x86_64, ppc64Ie, ARM64             |\n| 操作系统                          | Linux                              |\n| GPU 驱动                        |   450.80.02+ (Linux)                |\n\n',
    'author': 'sunhaiyang',
    'author_email': 'sunhaiyang@qudoor.cn',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'http://www.qudoor.com/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
