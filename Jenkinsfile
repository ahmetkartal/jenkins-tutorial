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

    sh 'python test_basic_math.py'

    }
    }

        stage("Deploy") {

    steps{

    echo 'deploying the application'

    }
    }
}


}