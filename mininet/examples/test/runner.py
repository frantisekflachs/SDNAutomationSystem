#!/usr/bin/env python

"""
Run all mininet.examples topology_tests
 -v : verbose output
 -quick : skip topology_tests that take more than ~30 seconds
"""

import unittest
import os
import sys
from mininet.util import ensureRoot
from mininet.clean import cleanup

class MininetTestResult( unittest.TextTestResult ):
    def addFailure( self, test, err ):
        super( MininetTestResult, self ).addFailure( test, err )
        cleanup()
    def addError( self,test, err ):
        super( MininetTestResult, self ).addError( test, err )
        cleanup()

class MininetTestRunner( unittest.TextTestRunner ):
    def _makeResult( self ):
        return MininetTestResult( self.stream, self.descriptions, self.verbosity )

def runTests( testDir, verbosity=1 ):
    "discover and run all topology_tests in testDir"
    # ensure root and cleanup before starting topology_tests
    ensureRoot()
    cleanup()
    # discover all topology_tests in testDir
    testSuite = unittest.defaultTestLoader.discover( testDir )
    # run topology_tests
    success = MininetTestRunner( verbosity=verbosity ).run( testSuite ).wasSuccessful()
    sys.exit( 0 if success else 1 )

if __name__ == '__main__':
    # get the directory containing example topology_tests
    testDir = os.path.dirname( os.path.realpath( __file__ ) )
    verbosity = 2 if '-v' in sys.argv else 1
    runTests( testDir, verbosity )
