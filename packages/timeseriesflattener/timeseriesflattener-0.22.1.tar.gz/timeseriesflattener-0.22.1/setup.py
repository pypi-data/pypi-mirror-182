# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['timeseriesflattener',
 'timeseriesflattener.feature_cache',
 'timeseriesflattener.testing']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy>=1.4.41,<1.5.42',
 'catalogue>=2.0.0,<2.1.0',
 'coloredlogs>14.0.0,<15.1.0',
 'dask>=2022.9.0,<2022.13.0',
 'deepchecks>=0.8.0,<0.11.0',
 'dill>=0.3.0,<0.3.6',
 'frozendict>=2.3.4,<2.4.0',
 'jupyter>=1.0.0,<1.1.0',
 'numpy>=1.23.3,<1.23.6',
 'pandas>=1.4.0,<1.6.0',
 'protobuf<=3.20.3',
 'psutil>=5.9.1,<6.0.0',
 'psycopmlutils>=0.2.4,<0.3.0',
 'pyarrow>=9.0.0,<10.1.0',
 'pydantic>=1.9.0,<1.10.0',
 'pyodbc>=4.0.34,<4.0.36',
 'scikit-learn>=1.1.2,<1.1.3',
 'scipy>=1.8.0,<1.9.4',
 'skimpy>=0.0.7,<0.1.0',
 'srsly>=2.4.4,<2.4.6',
 'wandb>=0.12.0,<0.13.5',
 'wasabi>=0.9.1,<0.10.2']

setup_kwargs = {
    'name': 'timeseriesflattener',
    'version': '0.22.1',
    'description': 'A package for converting time series data from e.g. electronic health records into wide format data.',
    'long_description': '<a href="https://github.com/Aarhus-Psychiatry-Research/timeseriesflattener"><img src="https://github.com/Aarhus-Psychiatry-Research/timeseriesflattener/blob/main/docs/_static/icon.png?raw=true" width="200" align="right"/></a>\n\n# Timeseriesflattener\n\n[![github actions docs](https://github.com/Aarhus-Psychiatry-Research/timeseriesflattener/actions/workflows/documentation.yml/badge.svg)](https://aarhus-psychiatry-research.github.io/timeseriesflattener/)\n[![github actions pytest](https://github.com/Aarhus-Psychiatry-Research/timeseriesflattener/actions/workflows/main_test_and_release.yml/badge.svg)](https://github.com/Aarhus-Psychiatry-Research/timeseriesflattener/actions)\n![python versions](https://img.shields.io/badge/Python-%3E=3.9-blue)\n[![Code style: black](https://img.shields.io/badge/Code%20Style-Black-black)](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html)\n\n[![PyPI version](https://badge.fury.io/py/timeseriesflattener.svg)](https://pypi.org/project/timeseriesflattener/)\n\nTime series from e.g. electronic health records often have a large number of variables, are sampled at irregular intervals and tend to have a large number of missing values. Before this type of data can be used for prediction modelling with machine learning methods such as logistic regression or XGBoost, the data needs to be reshaped. \n\nIn essence, the time series need to be *flattened* so that each prediction time is represented by a set of predictor values and an outcome value. These predictor values can be constructed by aggregating the preceding values in the time series within a certain time window. \n\n`timeseriesflattener` aims to simplify this process by providing an easy-to-use and fully-specified pipeline for flattening complex time series. \n\n## 🔧 Installation\nTo get started using timeseriesflattener simply install it using pip by running the following line in your terminal:\n\n```\npip install timeseriesflattener\n```\n\n## ⚡ Quick start\n\n```py\nimport numpy as np\nimport pandas as pd\n\nif __name__ == "__main__":\n\n    # Load a dataframe with times you wish to make a prediction\n    prediction_times_df = pd.DataFrame(\n        {\n            "id": [1, 1, 2],\n            "date": ["2020-01-01", "2020-02-01", "2020-02-01"],\n        },\n    )\n    # Load a dataframe with raw values you wish to aggregate as predictors\n    predictor_df = pd.DataFrame(\n        {\n            "id": [1, 1, 1, 2],\n            "date": [\n                "2020-01-15",\n                "2019-12-10",\n                "2019-12-15",\n                "2020-01-02",\n            ],\n            "value": [1, 2, 3, 4],\n        },\n    )\n    # Load a dataframe specifying when the outcome occurs\n    outcome_df = pd.DataFrame({"id": [1], "date": ["2020-03-01"], "value": [1]})\n\n    # Specify how to aggregate the predictors and define the outcome\n    from timeseriesflattener.feature_spec_objects import OutcomeSpec, PredictorSpec\n    from timeseriesflattener.resolve_multiple_functions import maximum, mean\n\n    predictor_spec = PredictorSpec(\n        values_df=predictor_df,\n        lookbehind_days=30,\n        fallback=np.nan,\n        entity_id_col_name="id",\n        resolve_multiple_fn=mean,\n        feature_name="test_feature",\n    )\n    outcome_spec = OutcomeSpec(\n        values_df=outcome_df,\n        lookahead_days=31,\n        fallback=0,\n        entity_id_col_name="id",\n        resolve_multiple_fn=maximum,\n        feature_name="test_outcome",\n        incident=False,\n    )\n\n    # Instantiate TimeseriesFlattener and add the specifications\n    from timeseriesflattener import TimeseriesFlattener\n\n    ts_flattener = TimeseriesFlattener(\n        prediction_times_df=prediction_times_df,\n        entity_id_col_name="id",\n        timestamp_col_name="date",\n        n_workers=1,\n        drop_pred_times_with_insufficient_look_distance=False,\n    )\n    ts_flattener.add_spec([predictor_spec, outcome_spec])\n    df = ts_flattener.get_df()\n    df\n```\nOutput:\n\n|      |   id | date                | prediction_time_uuid  | pred_test_feature_within_30_days_mean_fallback_nan | outc_test_outcome_within_31_days_maximum_fallback_0_dichotomous |\n| ---: | ---: | :------------------ | :-------------------- | -------------------------------------------------: | --------------------------------------------------------------: |\n|    0 |    1 | 2020-01-01 00:00:00 | 1-2020-01-01-00-00-00 |                                                2.5 |                                                               0 |\n|    1 |    1 | 2020-02-01 00:00:00 | 1-2020-02-01-00-00-00 |                                                  1 |                                                               1 |\n|    2 |    2 | 2020-02-01 00:00:00 | 2-2020-02-01-00-00-00 |                                                  4 |                                                               0 |\n\n\n## 📖 Documentation\n\n| Documentation          |                                                                                        |\n| ---------------------- | -------------------------------------------------------------------------------------- |\n| 🎓 **[Tutorial]**       | Simple and advanced tutorials to get you started using `timeseriesflattener`           |\n| 🎛 **[API References]** | The detailed reference for timeseriesflattener\'s API. Including function documentation |\n| 🙋 **[FAQ]**            | Frequently asked question                                                              |\n| 🗺️ **[Roadmap]**        | Kanban board for the roadmap for the project                                           |\n\n[Tutorial]: https://aarhus-psychiatry-research.github.io/timeseriesflattener/tutorials.html\n[api references]: https://Aarhus-Psychiatry-Research.github.io/timeseriesflattener/\n[FAQ]: https://Aarhus-Psychiatry-Research.github.io/timeseriesflattener/faq.html\n[Roadmap]: https://github.com/orgs/Aarhus-Psychiatry-Research/projects/11/views/1\n\n## 💬 Where to ask questions\n\n| Type                           |                        |\n| ------------------------------ | ---------------------- |\n| 🚨 **Bug Reports**              | [GitHub Issue Tracker] |\n| 🎁 **Feature Requests & Ideas** | [GitHub Issue Tracker] |\n| 👩\u200d💻 **Usage Questions**          | [GitHub Discussions]   |\n| 🗯 **General Discussion**       | [GitHub Discussions]   |\n\n[github issue tracker]: https://github.com/Aarhus-Psychiatry-Research/timeseriesflattener/issues\n[github discussions]: https://github.com/Aarhus-Psychiatry-Research/timeseriesflattener/discussions\n\n\n## 🎓 Projects\nPSYCOP projects which use `timeseriesflattener`. Note that some of these projects have yet to be published and are thus private.\n\n| Project                 | Publications |                                                                                                                                                                                                                                       |\n| ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |\n| **[Type 2 Diabetes]**   |              | Prediction of type 2 diabetes among patients with visits to psychiatric hospital departments                                                                                                                                          |\n| **[Cancer]**            |              | Prediction of Cancer among patients with visits to psychiatric hospital departments                                                                                                                                                   |\n| **[COPD]**              |              | Prediction of Chronic obstructive pulmonary disease (COPD) among patients with visits to psychiatric hospital departments                                                                                                             |\n| **[Forced admissions]** |              | Prediction of forced admissions of patients to the psychiatric hospital departments. Encompasses two seperate projects: 1. Prediciting at time of discharge for inpatient admissions. 2. Predicting day before outpatient admissions. |\n| **[Coercion]**          |              | Prediction of coercion among patients admittied to the hospital psychiatric department. Encompasses predicting mechanical restraint, sedative medication and manual restraint 48 hours before coercion occurs.                        |\n\n\n[Type 2 diabetes]: https://github.com/Aarhus-Psychiatry-Research/psycop-t2d\n[Cancer]: https://github.com/Aarhus-Psychiatry-Research/psycop-cancer\n[COPD]: https://github.com/Aarhus-Psychiatry-Research/psycop-copd\n[Forced admissions]: https://github.com/Aarhus-Psychiatry-Research/psycop-forced-admissions\n[Coercion]: https://github.com/Aarhus-Psychiatry-Research/pyscop-coercion\n',
    'author': 'Martin Bernstorff',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
