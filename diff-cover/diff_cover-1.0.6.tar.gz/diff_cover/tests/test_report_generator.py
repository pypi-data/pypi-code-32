from __future__ import unicode_literals

from io import BytesIO
from textwrap import dedent

import mock

from diff_cover.diff_reporter import BaseDiffReporter
from diff_cover.report_generator import (
    BaseReportGenerator, HtmlReportGenerator,
    StringReportGenerator, TemplateReportGenerator
)
from diff_cover.tests.helpers import (
    load_fixture, assert_long_str_equal
)
import unittest
from diff_cover.violationsreporters.violations_reporter import BaseViolationReporter, Violation


class SimpleReportGenerator(BaseReportGenerator):
    """
    Bare-bones concrete implementation of a report generator.
    """

    def __init__(self, cover, diff):
        super(SimpleReportGenerator, self).__init__(cover, diff)

    def generate_report(self, output_file):
        pass


class BaseReportGeneratorTest(unittest.TestCase):
    """
    Base class for constructing test cases of report generators.
    """

    # Test data, returned by default from the mocks
    SRC_PATHS = {'file1.py', 'subdir/file2.py'}
    LINES = [2, 3, 4, 5, 10, 11, 12, 13, 14, 15]
    VIOLATIONS = [Violation(n, None) for n in (10, 11, 20)]
    MEASURED = [1, 2, 3, 4, 7, 10, 11, 15, 20, 30]

    XML_REPORT_NAME = ["reports/coverage.xml"]
    DIFF_REPORT_NAME = "master"

    # Subclasses override this to provide the class under test
    REPORT_GENERATOR_CLASS = None

    # Snippet returned by the mock
    SNIPPET = "<div>Snippet with \u1235 \u8292 unicode</div>"
    SNIPPET_STYLE = '.css { color:red }'

    def setUp(self):

        # Create mocks of the dependencies
        self.coverage = mock.MagicMock(BaseViolationReporter)
        self.diff = mock.MagicMock(BaseDiffReporter)

        self.addCleanup(mock.patch.stopall)

        # Patch snippet loading to always return the same string
        self._load_snippets_html = mock.patch(
            'diff_cover.snippets.Snippet.load_snippets_html'
        ).start()

        self.set_num_snippets(0)

        # Patch snippet style
        style_defs = mock.patch(
            'diff_cover.snippets.Snippet.style_defs'
        ).start()

        style_defs.return_value = self.SNIPPET_STYLE

        # Set the names of the XML and diff reports
        self.coverage.name.return_value = self.XML_REPORT_NAME
        self.diff.name.return_value = self.DIFF_REPORT_NAME

        # Configure the mocks
        self.set_src_paths_changed([])

        self._lines_dict = dict()
        self.diff.lines_changed.side_effect = self._lines_dict.get

        self._violations_dict = dict()
        self.coverage.violations.side_effect = self._violations_dict.get

        self._measured_dict = dict()
        self.coverage.measured_lines.side_effect = self._measured_dict.get

        # Create a concrete instance of a report generator
        self.report = self.REPORT_GENERATOR_CLASS(self.coverage, self.diff)

    def set_src_paths_changed(self, src_paths):
        """
        Patch the dependency `src_paths_changed()` return value
        """
        self.diff.src_paths_changed.return_value = src_paths

    def set_lines_changed(self, src_path, lines):
        """
        Patch the dependency `lines_changed()` to return
        `lines` when called with argument `src_path`.
        """
        self._lines_dict.update({src_path: lines})

    def set_violations(self, src_path, violations):
        """
        Patch the dependency `violations()` to return
        `violations` when called with argument `src_path`.
        """
        self._violations_dict.update({src_path: violations})

    def set_measured(self, src_path, measured):
        """
        Patch the dependency `measured_lines()` return
        `measured` when called with argument `src_path`.
        """
        self._measured_dict.update({src_path: measured})

    def set_num_snippets(self, num_snippets):
        """
        Patch the depdenency `Snippet.load_snippets_html()`
        to return `num_snippets` of the fake snippet HTML.
        """
        self._load_snippets_html.return_value = \
            num_snippets * [self.SNIPPET]

    def use_default_values(self):
        """
        Configure the mocks to use default values
        provided by class constants.

        All source files are given the same line, violation,
        and measured information.
        """
        self.set_src_paths_changed(self.SRC_PATHS)

        for src in self.SRC_PATHS:
            self.set_lines_changed(src, self.LINES)
            self.set_violations(src, self.VIOLATIONS)
            self.set_measured(src, self.MEASURED)
            self.set_num_snippets(0)

    def assert_report(self, expected):
        """
        Generate a report and assert that it matches
        the string `expected`.
        """
        # Create a buffer for the output
        output = BytesIO()

        # Generate the report
        self.report.generate_report(output)

        # Get the output
        output_str = output.getvalue()
        output.close()

        # Verify that we got the expected string
        assert_long_str_equal(expected, output_str, strip=True)


class SimpleReportGeneratorTest(BaseReportGeneratorTest):

    REPORT_GENERATOR_CLASS = SimpleReportGenerator

    def setUp(self):
        super(SimpleReportGeneratorTest, self).setUp()
        self.use_default_values()

    def test_src_paths(self):
        self.assertEqual(self.report.src_paths(), self.SRC_PATHS)

    def test_coverage_name(self):
        self.assertEqual(self.report.coverage_report_name(),
                         self.XML_REPORT_NAME)

    def test_diff_name(self):
        self.assertEqual(self.report.diff_report_name(),
                         self.DIFF_REPORT_NAME)

    def test_percent_covered(self):

        # Check that we get the expected coverage percentages
        # By construction, both files have the same diff line
        # and coverage information

        # There are 6 lines that are both in the diff and measured,
        # and 4 of those are covered.
        for src_path in self.SRC_PATHS:
            self.assertAlmostEqual(
                self.report.percent_covered(src_path),
                4.0 / 6 * 100)

    def test_violation_lines(self):

        # By construction, each file has the same coverage information
        expected = [10, 11]
        for src_path in self.SRC_PATHS:
            self.assertEqual(self.report.violation_lines(src_path), expected)

    def test_src_with_no_info(self):

        self.assertNotIn('unknown.py', self.report.src_paths())
        self.assertIs(self.report.percent_covered('unknown.py'), None)
        self.assertEqual(self.report.violation_lines('unknown.py'), [])

    def test_src_paths_not_measured(self):

        # Configure one of the source files to have no coverage info
        self.set_measured('file1.py', [])
        self.set_violations('file1.py', [])

        # Expect that we treat the file like it doesn't exist
        self.assertNotIn('file1.py', self.report.src_paths())
        self.assertIs(self.report.percent_covered('file1.py'), None)
        self.assertEqual(self.report.violation_lines('file1.py'), [])

    def test_total_num_lines(self):

        # By construction, each source file has the same coverage info
        num_lines_in_file = len(set(self.MEASURED).intersection(self.LINES))
        expected = len(self.SRC_PATHS) * num_lines_in_file
        self.assertEqual(self.report.total_num_lines(), expected)

    def test_total_num_missing(self):

        # By construction, each source file has the same coverage info,
        # in which 3 lines are uncovered, 2 of which are changed
        expected = len(self.SRC_PATHS) * 2
        self.assertEqual(self.report.total_num_violations(), expected)

    def test_total_percent_covered(self):

        # Since each file has the same coverage info,
        # the total percent covered is the same as each file
        # individually.
        self.assertEqual(self.report.total_percent_covered(), 66)


class TemplateReportGeneratorTest(BaseReportGeneratorTest):
    REPORT_GENERATOR_CLASS = TemplateReportGenerator

    def _test_input_expected_output(self, input_with_expected_output):
        for test_input, expected_output in input_with_expected_output:
            self.assertEqual(expected_output,
                             TemplateReportGenerator.combine_adjacent_lines(test_input))

    def test_combine_adjacent_lines_no_adjacent(self):
        in_out = [([1, 3], ["1", "3"]),
                  ([1, 5, 7, 10], ["1", "5", "7", "10"])]
        self._test_input_expected_output(in_out)

    def test_combine_adjacent_lines(self):
        in_out = [([1, 2, 3, 4, 5, 8, 10, 12, 13, 14, 15], ["1-5", "8", "10", "12-15"]),
                  ([1, 4, 5, 6, 10], ["1", "4-6", "10"]),
                  ([402, 403], ["402-403"])]
        self._test_input_expected_output(in_out)

    def test_empty_list(self):
        self.assertEqual([], TemplateReportGenerator.combine_adjacent_lines([]))

    def test_one_number(self):
        self.assertEqual(["1"], TemplateReportGenerator.combine_adjacent_lines([1]))


class StringReportGeneratorTest(BaseReportGeneratorTest):

    REPORT_GENERATOR_CLASS = StringReportGenerator

    def test_generate_report(self):

        # Generate a default report
        self.use_default_values()

        # Verify that we got the expected string
        expected = dedent("""
        -------------
        Diff Coverage
        Diff: master
        -------------
        file1.py (66.7%): Missing lines 10-11
        subdir/file2.py (66.7%): Missing lines 10-11
        -------------
        Total:   12 lines
        Missing: 4 lines
        Coverage: 66%
        -------------
        """).strip()

        self.assert_report(expected)

    def test_hundred_percent(self):

        # Have the dependencies return an empty report
        self.set_src_paths_changed(['file.py'])
        self.set_lines_changed('file.py', [line for line in range(0, 100)])
        self.set_violations('file.py', [])
        self.set_measured('file.py', [2])

        expected = dedent("""
        -------------
        Diff Coverage
        Diff: master
        -------------
        file.py (100%)
        -------------
        Total:   1 line
        Missing: 0 lines
        Coverage: 100%
        -------------
        """).strip()

        self.assert_report(expected)

    def test_empty_report(self):

        # Have the dependencies return an empty report
        # (this is the default)

        expected = dedent("""
        -------------
        Diff Coverage
        Diff: master
        -------------
        No lines with coverage information in this diff.
        -------------
        """).strip()

        self.assert_report(expected)


class HtmlReportGeneratorTest(BaseReportGeneratorTest):

    REPORT_GENERATOR_CLASS = HtmlReportGenerator

    def test_generate_report(self):
        self.use_default_values()
        expected = load_fixture('html_report.html')
        self.assert_report(expected)

    def test_empty_report(self):

        # Have the dependencies return an empty report
        # (this is the default)

        # Verify that we got the expected string
        expected = load_fixture('html_report_empty.html')
        self.assert_report(expected)

    def test_one_snippet(self):

        self.use_default_values()

        # Have the snippet loader always report
        # provide one snippet (for every source file)
        self.set_num_snippets(1)

        # Verify that we got the expected string
        expected = load_fixture('html_report_one_snippet.html').strip()
        self.assert_report(expected)

    def test_multiple_snippets(self):

        self.use_default_values()

        # Have the snippet loader always report
        # multiple snippets for each source file
        self.set_num_snippets(2)

        # Verify that we got the expected string
        expected = load_fixture('html_report_two_snippets.html').strip()
        self.assert_report(expected)
