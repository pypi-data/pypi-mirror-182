# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pulsar_data_collection',
 'pulsar_data_collection.data_capture',
 'pulsar_data_collection.db_connectors.influxdb']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy>=1.4.39,<2.0.0',
 'influxdb-client[ciso]>=1.31.0,<2.0.0',
 'influxdb==5.3.1',
 'pandas>=1.4.2,<2.0.0',
 'pydantic>=1.6.2,<2.0.0',
 'pysqlite3>=0.4.7,<0.5.0']

setup_kwargs = {
    'name': 'pulsar-data-collection',
    'version': '0.1.1',
    'description': 'sdk enabling data collection from model serving code for our MPM solution',
    'long_description': '# pulsar_data_collection\n\nPulsar data collection SDK is an open-source Python library for\npushing/processing/collecting features, predictions and metadata. Works with different\ndata storages, at this point InfluxDB is implemented.\n\n## Getting started\n\nInstall Pulsar Data Collection with pip:\n\n```bash\npython3 -m pip install --upgrade pip\npython3 -m pip install --upgrade pulsar-data-collection\n```\n\n### Components\n\nThere are two core components in data collection SDK: storage engine and data capture.\nRight now storage engine implemented only for InfluxDb, it helps to make ingestion and digestion operations\nto the database.\n\n#### Data Capture\n\n`DataCapture` class helps to ingest dataset to database with needed parameters and needed format for future\ndigestion and metrics calculation without any significant changes of data.\n\nIt requires `storage_engine` (available only influxdb right now), `operation_type` (`DATABASE_OPERATION_TYPE_INSERT_PREDICTION`,\n`DATABASE_OPERATION_TYPE_METRICS`),  `login_url` (object of DatabaseLogin class) as input parameters.\n\nOperation type `DATABASE_OPERATION_TYPE_INSERT_PREDICTION` uses for any ingestion operations to the database.\nIt requires additional parameters: `model_id`, `model_version`, `data_id`", `y_name`, `pred_name` what describes\nan input dataset.\nFor operation type `DATABASE_OPERATION_TYPE_METRICS` what commonly uses for retrieving dataset ready for metrics\ncalculation these parameters aren\'t required.\n\nThe last and probably one the most important class to work with is `DataWithPrediction`.\nIt requires two parameters as input: `prediction`, `data_points`. Where `prediction` is prediction value of the model,\nand `data_points` is features dataset. `Push` method of the `DataCapture` takes object of `DataWithPrediction` as\nrequired parameter, and after that makes ingestion operation to database with data transforming, like adding timestamp,\nchanging name of prediction column in dataset, combining features with prediction into single dataset, creating\ninfluxdb unique cache, etc.\n\nList of methods of `DataCapture` class:\n\n- push(data: DataWithPrediction)\n- ingests data to the db after preprocessing it;\n- collect(filters: dict) - retrieves data from db;\n- collect_eval_timestamp - retrieves the newest timestamp in the database;\n- push_eval_timestamp(eval_df: df) - ingesting new one timestamp into db;\n- push_metrics(metrics_df: df) - ingesting metrics dataframe to the database after calculations\n\n### Example usage\n\nInitialize Database credentials:\n\n```python\nfrom pulsar_data_collection.data_capture import DatabaseLogin\ndatabase_login = DatabaseLogin(db_host=<db_host>), db_port=<db_port>, db_user=<db_user>, db_password=<db_password>, protocol=<db_protocol>)\n```\n\nInitialize DataCapture class, depends on operation type use appropriate constant.\nFor inserting data into the database:\n\n```python\nfrom pulsar_data_collection.data_capture import DataCapture, DATABASE_OPERATION_TYPE_INSERT_PREDICTION\n\ndat_predict = DataWithPrediction(prediction=prediction, data_points=to_predict)\n\ndat_capture = DataCapture(\n    storage_engine="influxdb",\n    model_id=<model_id>,\n    model_version=<model_verstion>,\n    data_id=<data_id>,\n    y_name=<y_name>,\n    pred_name=<pred_name>,\n    operation_type=<operation_type>,\n    login_url=<database_login>,\n)\n\ndat_capture.push(dat_predict)\n```\n\nFor collecting data from the database:\n\n```python\nfrom pulsar_data_collection.data_capture import DataCapture, DATABASE_OPERATION_TYPE_METRICS\n\ndat_capture = DataCapture(\n    storage_engine="influxdb",\n    operation_type=DATABASE_OPERATION_TYPE_METRICS,\n    login_url=database_login\n)\n\ndat_capture.collect()\n```\n\nCollection the newest prediction data what wasn\'t precessed\n\n```python\n# receiving the last period of data\n\nlast_eval_timestamp = dat_capture.collect_eval_timestamp()\n\n# if last period exists, collecting only data what wasn\'t collected previously\nif last_eval_timestamp:\n    last_eval_timestamp_str = last_eval_timestamp.strftime(\'%Y-%m-%d %H:%M:%S\')\n    db_df = pd.DataFrame(dat_capture.collect({"time": f">= \'{last_eval_timestamp_str}\'"}).get("prediction"))\nelse:\n    db_df = pd.DataFrame(dat_capture.collect().get("prediction"))\n```\n\nExample of pushing calculated metrics:\n\n```python\ndat_capture.push_metrics(df_result_drift)\n```\n\nExample of pushing the timestamp when metrics were calculated:\n\n```python\ndat_capture.push_eval_timestamp(eval_timestamp_df)\n```\nTODO: add use cases of input dataframes: metrics, prediction, datapoint\n\n## About [PulsarML](https://pulsar.ml/)\n\nPulsarML is a project helping with monitoring your models and gain powerful insights into its performance.\n\nWe released two Open Source packages :\n\n- [pulsar-data-collection](https://github.com/Rocket-Science-Development/pulsar_data_collection) :  lightweight python SDK enabling data collection of features, predictions and metadata from an ML model serving code/micro-service\n- [pulsar-metrics](https://github.com/Rocket-Science-Development/pulsar_metrics) : library for evaluating and monitoring data and concept drift with an extensive set of metrics. It also offers the possibility to use custom metrics defined by the user.\n\nWe also created [pulsar demo](https://github.com/Rocket-Science-Development/pulsar_demo) to display an example use-case showing how to leverage both packages to implement model monitoring and performance management.\n\nWant to interact with the community? join our [slack channel](https://pulsarml.slack.com)\n\nPowered by [Rocket Science Development](https://rocketscience.one/)\n\n## Contributing\n\n1. Fork this repository, develop, and test your changes\n2. open an issue\n3. Submit a pull request with a reference to the issue\n\nTODO: add use cases of input dataframes: metrics, prediction, datapoint\n\n',
    'author': 'Pulsar team',
    'author_email': 'pulsar@data-rs.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Rocket-Science-Development/pulsar_data_collection',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
