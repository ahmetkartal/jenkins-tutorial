pipeline{
agent any

stages {
    stage("Build") {

    steps{

    echo 'building the application'
    }
    }

        stage("Test") {

    steps{

    sh 'python3 tests/test_basic_math.py'

    }
    }
            stage("Tox Test") {

    steps{

    sh 'tox'

    }
    }

        stage("Deploy") {

    steps{

    echo env.BRANCH_NAME + " is being deployed"
    echo 'deploying the application'
    echo 'deploying test application'

    }
    }
}


}