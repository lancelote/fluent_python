import doctest
import os


def load_tests(_loader, tests, _ignore):
    test_files = []
    for root, dirs, files in os.walk('tests'):
        for file in files:
            if file.endswith('.doctest'):
                test_files.append(os.path.join(root, file))
    for test_file in test_files:
        tests.addTests(doctest.DocFileSuite(test_file))
    return tests
