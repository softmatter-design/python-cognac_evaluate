from setuptools import setup


setup(
    name='chain_evaluate',
    version='0.1.0',
    # install_requres=['PyYAML'], 依存するライブラリ（必要な場合）
    packages=["chain_evaluation"],
    entry_points={
        'console_scripts': [
            "ore = chain_evaluation.main:egg"
        ]
    }
)