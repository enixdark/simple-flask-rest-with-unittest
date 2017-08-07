node {
    stage('Checkout'){
        checkout scm
    }
    stage('Build image with docker') {
        app = docker.build("enixdark/simple-flask-rest-with-unittest")
    }
     
    stage("Install and test unit with container") {
        app.inside {
            sh "apt-get update -qy"
            sh "apt-get install -y python-dev python-pip" 
            sh "pip install virtualenv"
            sh "virtualenv venv"
            sh "./venv/bin/pip install -r requirements.txt"
            sh "./venv/bin/python manage.py test"
        }
        
    }
    
    stage("deploy app"){
       sh "ansible-playbook deployment/playbook.yml"
    }
}


