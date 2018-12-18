import multiprocessing
import os
import threading
import time
from datetime import datetime

from test_junkie.decorators import DecoratorType
from test_junkie.constants import SuiteCategory, TestCategory


class ClassMetrics:

    def __init__(self):

        self.__stats = {"status": None, "retry": 0, "runtime": 0, "start": None, "end": None,
                        DecoratorType.BEFORE_CLASS: {"performance": [], "exceptions": []},
                        DecoratorType.BEFORE_TEST: {"performance": [], "exceptions": []},
                        DecoratorType.AFTER_TEST: {"performance": [], "exceptions": []},
                        DecoratorType.AFTER_CLASS: {"performance": [], "exceptions": []}}

    def update_decorator_metrics(self, decorator, start_time, exception=None):

        self.__stats[decorator]["performance"].append(time.time() - start_time)
        self.__stats[decorator]["exceptions"].append(exception)

    def update_suite_metrics(self, status, start_time):

        self.__stats["status"] = status
        if status not in [SuiteCategory.CANCEL, SuiteCategory.SKIP, SuiteCategory.IGNORE]:
            self.__stats["retry"] += 1
        self.__stats["start"] = start_time
        self.__stats["end"] = time.time()
        self.__stats["runtime"] = self.__stats["end"] - self.__stats["start"]

    def get_metrics(self):

        return self.__stats


class TestMetrics:

    def __init__(self):

        self.__stats = {}

    def update_metrics(self, status, start_time, param=None, class_param=None, exception=None):

        def __get_template():

            return {"status": None,
                    "retry": 0,
                    "performance": [],
                    "exceptions": []}

        string_param = str(param)
        string_class_param = str(class_param)
        if string_class_param not in self.__stats:
            self.__stats.update({string_class_param: {string_param: __get_template()}})
        elif string_param not in self.__stats[string_class_param]:
            self.__stats[string_class_param].update({string_param: __get_template()})
        self.__stats[string_class_param][string_param]["performance"].append(time.time() - start_time)
        self.__stats[string_class_param][string_param]["exceptions"].append(exception)
        self.__stats[string_class_param][string_param]["retry"] += 1
        self.__stats[string_class_param][string_param]["status"] = status
        self.__stats[string_class_param][string_param]["param"] = param
        self.__stats[string_class_param][string_param]["class_param"] = class_param

    def get_metrics(self):

        return self.__stats


class Aggregator:

    def __init__(self, executed_suites):

        self.__executed_suites = executed_suites

    def get_basic_report(self):

        report = {"total": 0,
                  TestCategory.SUCCESS: 0,
                  TestCategory.FAIL: 0,
                  TestCategory.ERROR: 0,
                  TestCategory.IGNORE: 0,
                  TestCategory.SKIP: 0,
                  TestCategory.CANCEL: 0}

        for suite in self.__executed_suites:
            for test in suite.get_test_objects():
                test_metrics = test.metrics.get_metrics()
                for class_param, class_param_data in test_metrics.items():
                    for param, param_data in class_param_data.items():
                        report["total"] += 1
                        report[param_data["status"]] += 1
        return report

    def get_report_by_features(self):

        report = {}
        for suite in self.__executed_suites:
            feature = suite.get_feature()
            if feature not in report:
                report.update({feature: {"_totals_": Aggregator.get_template()}})
            for test in suite.get_test_objects():
                component = test.get_component()
                if component not in report[feature]:
                    report[feature].update({component: Aggregator.get_template()})
                test_metrics = test.metrics.get_metrics()
                Aggregator._update_report(report, test_metrics, feature, component)
        return report

    def get_report_by_tags(self):

        report = {}
        for suite in self.__executed_suites:
            tag_metrics = suite.get_data_by_tags()
            for metric, metric_data in tag_metrics.items():
                if metric == "_totals_":
                    continue
                metric = metric if metric is not None else "Not Defined"
                if metric not in report:
                    report.update({metric: Aggregator.get_template()})
                for entry in metric_data["performance"]:
                    report[metric]["performance"].append(entry)
                for entry in metric_data["exceptions"]:
                    if entry is not None:
                        report[metric]["exceptions"].append(entry)
                for retry in metric_data["retries"]:
                    report[metric]["retries"].append(retry)
                report[metric]["total"] += metric_data["total"]
                for status in TestCategory.ALL:
                    report[metric][status] += metric_data[status]
        return report

    def get_report_by_owner(self):

        report = {"_totals_": Aggregator.get_template()}
        for suite in self.__executed_suites:
            for test in suite.get_test_objects():
                owner = test.get_owner()
                if owner not in report:
                    report.update({owner: Aggregator.get_template()})
                test_metrics = test.metrics.get_metrics()
                Aggregator._update_report(report, test_metrics, owner)
        return report

    @staticmethod
    def _update_report(report, metrics, category, subcategory=0):

        for class_param, class_param_data in metrics.items():
            for param, data in class_param_data.items():
                for entry in data["performance"]:
                    if subcategory == 0:
                        report[category]["performance"].append(entry)
                        report["_totals_"]["performance"].append(entry)
                    else:
                        report[category][subcategory]["performance"].append(entry)
                        report[category]["_totals_"]["performance"].append(entry)
                for entry in data["exceptions"]:
                    if entry is not None:
                        if subcategory == 0:
                            report[category]["exceptions"].append(entry)
                            report["_totals_"]["exceptions"].append(entry)
                        else:
                            report[category][subcategory]["exceptions"].append(entry)
                            report[category]["_totals_"]["exceptions"].append(entry)
                if subcategory == 0:
                    report[category]["retries"].append(data["retry"])
                    report["_totals_"]["retries"].append(data["retry"])
                    report[category]["total"] += 1
                    report["_totals_"]["total"] += 1
                    report[category][data["status"]] += 1
                    report["_totals_"][data["status"]] += 1
                else:
                    report[category][subcategory]["retries"].append(data["retry"])
                    report[category]["_totals_"]["retries"].append(data["retry"])
                    report[category][subcategory]["total"] += 1
                    report[category]["_totals_"]["total"] += 1
                    report[category][subcategory][data["status"]] += 1
                    report[category]["_totals_"][data["status"]] += 1

        return report

    @staticmethod
    def get_template():

        return {"performance": [],
                "exceptions": [],
                "retries": [],
                "total": 0,
                TestCategory.SUCCESS: 0,
                TestCategory.SKIP: 0,
                TestCategory.FAIL: 0,
                TestCategory.CANCEL: 0,
                TestCategory.IGNORE: 0,
                TestCategory.ERROR: 0}

    def get_average_test_runtime(self):

        from statistics import mean
        samples = []
        for suite in self.__executed_suites:
            for test in suite.get_test_objects():
                test_metrics = test.metrics.get_metrics()
                for class_param, class_param_data in test_metrics.items():
                    for param, param_data in class_param_data.items():
                        samples.append(mean(param_data["performance"]))
        return mean(samples) if samples else None


class ResourceMonitor(threading.Thread):

    def __init__(self, file_path=None,):

        self.file_path = "{dir}{sep}.resources".format(dir=os.path.dirname(os.path.abspath(__file__)),
                                                       sep=os.sep) if file_path is None else file_path

        threading.Thread.__init__(self)
        self.exit = multiprocessing.Event()

    def get_file_path(self):

        return self.file_path

    def run(self):
        import psutil
        with open(self.file_path, "w+") as records:
            records.write("")
        while not self.exit.is_set():
            time.sleep(1)
            data = "{timestamp}, {cpu}, {memory}\n".format(timestamp=datetime.now(),
                                                           cpu=psutil.cpu_percent(),
                                                           memory=psutil.virtual_memory().percent)
            with open(self.file_path, "a+") as records:
                records.write(data)

    def shutdown(self):
        self.exit.set()
