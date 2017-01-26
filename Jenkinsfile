node { // <1>
    stage('Build') { // <2>
        sh 'echo build' // <3>
    }

    stage('Test') {
        sh 'python test_random.py'
    }

    stage('Deploy') {
        sh 'echo delpoy'
    }
}
