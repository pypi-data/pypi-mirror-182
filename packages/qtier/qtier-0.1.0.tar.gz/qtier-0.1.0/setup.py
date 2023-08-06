# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['qtier', 'qtier.ext', 'qtier.gql', 'qtier.itemsystem']

package_data = \
{'': ['*']}

install_requires = \
['PySide6>=6.4.1,<7.0.0', 'QtPy>=2.3.0,<3.0.0', 'attrs>=22.1.0,<23.0.0']

setup_kwargs = {
    'name': 'qtier',
    'version': '0.1.0',
    'description': 'Cuter approuch to Qt-for-python, with focus on type hints.',
    'long_description': '# qtier\n## Cuter approach to Qt-for-python, with focus on type hints, JSON APIs and QML.\n\n### Example Usage:\nThe following example shows how qtier can be used to query a graphql service.\n*models.py*\n```python\nfrom qtier.itemsystem import role, define_roles\n\n\n@define_roles\nclass Worm:\n    name: str = role()\n    family: str = role()\n    size: int = role()\n\n\n@define_roles\nclass Apple:\n    size: int = role()\n    owner: str = role()\n    color: str = role()\n    # nested models are also supported!\n    worms: Worm = role(default=None)\n```\nqtier will create for you `QAbstractListModel` to be used in QML you only need to\ndefine your models with `define_roles`.\nqtier initializes the data with a dict, in this case coming from graphql service.\n\n*main.py*\n```python\nimport glob\nimport os\nimport sys\nfrom pathlib import Path\n\nfrom qtpy.QtQml import QQmlApplicationEngine\nfrom qtpy.QtCore import QObject, Signal\nfrom qtpy import QtCore, QtGui, QtQml, QtQuick\n\nfrom qtier import slot\nfrom qtier.gql.client import HandlerProto, GqlClientMessage, GqlWsTransportClient\nfrom qtier.itemsystem import GenericModel\nfrom tests.test_sample_ui.models import Apple\n\n\nclass EntryPoint(QObject):\n    class AppleHandler(HandlerProto):\n        message = GqlClientMessage.from_query(\n            """\n            query MyQuery {\n              apples {\n                color\n                owner\n                size\n                worms {\n                  family\n                  name\n                  size\n                }\n              }\n            }\n            """\n        )\n        def __init__(self, app: \'EntryPoint\'):\n            self.app = app\n\n\n        def on_data(self, message: dict) -> None:\n            self.app.apple_model.initialize_data(message[\'apples\'])\n\n        def on_error(self, message: dict) -> None:\n            print(message)\n\n        def on_completed(self, message: dict) -> None:\n            print(message)\n\n    def __init__(self, parent=None):\n        super().__init__(parent)\n        main_qml = Path(__file__).parent / \'qml\' / \'main.qml\'\n        QtGui.QFontDatabase.addApplicationFont(str(main_qml.parent / \'materialdesignicons-webfont.ttf\'))\n        self.qml_engine = QQmlApplicationEngine()\n        self.gql_client = GqlWsTransportClient(url=\'ws://localhost:8080/graphql\')\n        self.apple_query_handler = self.AppleHandler(self)\n        self.gql_client.query(self.apple_query_handler)\n        self.apple_model: GenericModel[Apple] = Apple.Model()\n        QtQml.qmlRegisterSingletonInstance(EntryPoint, "com.props", 1, 0, "EntryPoint", self)  # type: ignore\n        # for some reason the app won\'t initialize without this event processing here.\n        QtCore.QEventLoop().processEvents(QtCore.QEventLoop.ProcessEventsFlag.AllEvents, 1000)\n        self.qml_engine.load(str(main_qml.resolve()))\n\n\n    @QtCore.Property(QtCore.QObject, constant=True)\n    def appleModel(self) -> GenericModel[Apple]:\n        return self.apple_model\n\n\ndef main():\n    app = QtGui.QGuiApplication(sys.argv)\n    ep = EntryPoint()  # noqa: F841, this collected by the gc otherwise.\n    ret = app.exec()\n    sys.exit(ret)\n\n\nif __name__ == "__main__":\n    main()\n```\n\n![Example](assets/qtier.gif)\n',
    'author': 'Nir',
    'author_email': '88795475+nrbnlulu@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<3.12',
}


setup(**setup_kwargs)
