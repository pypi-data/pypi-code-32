import pprint
import sys

sys.path.insert(1, __file__.split("playground")[0])
from test_junkie.reporter.reporter import Reporter
from test_junkie.debugger import LogJunkie
LogJunkie.enable_logging(10)

from playground.suiteA import TestSuiteA
# from playground.suiteB import TestSuiteB
# from playground.suiteC import TestSuiteC
from playground.suiteD import TestSuiteD
from test_junkie.runner import Runner

runner = Runner([TestSuiteA], monitor_resources=True,
                html_report="E:\Development\\test_junkie\\playground\\report.html")

aggregator = runner.run(test_multithreading_limit=10)
suite_objects = runner.get_executed_suites()

for suite in suite_objects:
    print(suite.get_class_name())
    tests = suite.get_test_objects()
    print(suite.metrics.get_metrics())
    print(suite.get_data_by_tags())
    for test in tests:
        print(test.metrics.get_metrics())

# tags = aggregator.get_report_by_tags()
# features = aggregator.get_report_by_features()
# totals = aggregator.get_basic_report()
# owners = aggregator.get_report_by_owner()
# reporter = Reporter("E:\Development\\test_junkie\\test_junkie\.resources", features, totals)
# pprint.pprint(reporter.get_dataset_per_feature())
# pprint.pprint(reporter.get_absolute_results())
# pprint.pprint(aggregator.get_report_by_owner())
