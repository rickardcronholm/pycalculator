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
                        '''
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
        }
    }
}
