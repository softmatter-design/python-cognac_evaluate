from setuptools import setup

setup(
    name='project name',
    version='0.2.1',
    # install_requres=['PyYAML'], 依存するライブラリ（必要な場合）
    packages=["modules"],
    entry_points={
        'console_scripts': [
            "oreore = modules.main:main"
        ]
    }
)