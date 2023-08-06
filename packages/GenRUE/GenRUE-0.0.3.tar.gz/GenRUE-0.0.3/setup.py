from setuptools import setup, find_packages

with open("README", "r", encoding="utf-8") as fh:   # 读取文件中介绍包的详细内容
    long_description = fh.read()
# long_description为读取README.md的内容，encoding="utf-8"设置是为了README.md的内容支持中文

setup(
    name="GenRUE",  # 包名
    version="0.0.3",  # 版本
    description="",  # 包简介
    include_package_data=True,  # 是否允许上传资源文件
    author="Qianlian Wang",  # 作者
    author_email="wangqianlian@foxmail.com",  # 作者邮件
    maintainer="Qianlian Wang",  # 维护者
    maintainer_email="wangqianlian@foxmail.com",  # 维护者邮件
    license="MIT License",  # 协议
    url="https://github.com/WangQianlian/GenRUE",  # github或者自己的网站地址
    packages=find_packages(),  # 包的目录
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',  # 设置编写时的python版本
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',  # 设置python版本要求
    install_requires=["numpy", "pandas", "openpyxl"],  # 安装所需要的库

)
