pipeline {
    agent any

    triggers {
        pollSCM('*/5 * * * 1-5')
    }

    options {
        skipDefaultCheckout(true)
        // Keep the 10 most recent builds
        buildDiscarder(logRotator(numToKeepStr: '10'))
        timestamps()
    }

    environment {
      PATH="$PATH"
    }

    stages {

        stage ("Code pull"){
            steps{
                checkout scm
            }
        }

        stage('Create environment') {
            steps {
                withPythonEnv('python3') {
                	echo "Building virtualenv"
                    sh  ''' python3 -m venv venv
                            . ./venv/bin/activate
                            pip install pytest
                            pip install radon
                            pip install coverage
                            pip install pylint
                        '''
                    }
            }
        }

        stage('Static code metrics') {
            steps {
                withPythonEnv('python3') {
	                echo "Raw metrics"
        	        sh  ''' . ./venv/bin/activate
                	        radon raw --json calculator > raw_report.json
                        	radon cc --json calculator > cc_report.json
	                        radon mi --json calculator > mi_report.json

                	    '''
	                echo "Test coverage"
        	        sh  ''' . ./venv/bin/activate
                	        coverage run calculator/Calculator.py 1 1 2 3
                        	python -m coverage xml -o reports/coverage.xml
	                    '''
        	        echo "Style check"
                	sh  ''' . ./venv/bin/activate
                            python -m pylint --output-format=parseable --exit-zero calculator > pylint.log
	                    '''
                }
            }
            post{
                always{
                    step([$class: 'CoberturaPublisher',
                                   autoUpdateHealth: false,
                                   autoUpdateStability: false,
                                   coberturaReportFile: 'reports/coverage.xml',
                                   failNoReports: false,
                                   failUnhealthy: false,
                                   failUnstable: false,
                                   maxNumberOfBuilds: 10,
                                   onlyStable: false,
                                   sourceEncoding: 'ASCII',
                                   zoomCoverageChart: false
                    ])

                    step([$class: 'WarningsPublisher',
                                   parserConfigurations : [[
                                        parserName : 'PYLint',
                                        pattern : 'pylint.log'
                                   ]],
                                   unstableTotalAll : '0',
                                   usePreviousBuildAsReference: true
                    ])
                }
            }
        }


        stage('Unit tests') {
            steps {
                withPythonEnv('python3') {
                    sh ''' . ./venv/bin/activate
                            python -m pytest --verbose --junit-xml reports/unit_tests.xml
                       '''
                }
            }
            post {
                always {
                    // Archive unit tests for the future
                    junit allowEmptyResults: true, testResults: 'reports/unit_tests.xml'
                }
            }
        }
    }
}
