import os
import nose
import shutil
import yaml
from fundamentals import utKit, cl_utils
from fundamentals.utKit import utKit

from dryxPython.projectsetup import setup_main_clutil

su = setup_main_clutil(
    arguments={},
    docString=__doc__,
    logLevel="DEBUG",
    options_first=False,
    projectName="fundamentals",
    tunnel=False
)
arguments, settings, log, dbConn = su.setup()

# load settings
stream = file(
    "/Users/Dave/.config/fundamentals/fundamentals.yaml", 'r')
settings = yaml.load(stream)
stream.close()

# SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE
moduleDirectory = os.path.dirname(__file__)
utKit = utKit(moduleDirectory)
log, dbConn, pathToInputDir, pathToOutputDir = utKit.setupModule()
utKit.tearDownModule()


class test_utKit():

    def test_utKit_function(self):
        kwargs = {}
        kwargs["log"] = log
        kwargs["settings"] = settings
        # xt-kwarg_key_and_value

        testObject = utKit(**kwargs)
        testObject.get()

        # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
