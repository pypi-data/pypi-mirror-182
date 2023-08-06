from setuptools import setup

setup(
    packages = [
        "campfire",
        "campfire.components",
        "campfire.components.tools",
        "campfire.components.firebase",
        "campfire.components.firebase.proto"
    ],
    package_data = {"campfire": [
        "./*.py",
        "./config.json",
        "./components/*.py",
        "./components/firebase/*.py",
        "./components/firebase/proto/*.py",
        "./components/tools/*.py",
        "./components/cert.pem"
    ]}
)