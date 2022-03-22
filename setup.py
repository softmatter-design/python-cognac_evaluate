from setuptools import setup

setup(
    name='project name',
    version='0.1.0',
    # install_requres=['PyYAML'], 依存するライブラリ（必要な場合）
    packages=["module"],
    entry_points={
        'console_scripts': [
            "command_name=module.main:main"
        ]
    }
)