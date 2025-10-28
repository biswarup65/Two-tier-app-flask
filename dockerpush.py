def call(String CredentialsID,String Imagename,String Tag){
  withCredentials([usernamePassword(credentialsId: CredentialsID,usernameVariable: "docker_user",passwordVariable: "docker_pass")]){
    sh "docker login -u ${env.docker_user} -p ${env.docker_pass}"
    sh " docker tag two-tier-flask:v3 ${env.docker_user}/${Imagename}:${Tag}"
    sh " docker push ${env.docker_user}/${Imagename}:${Tag} "
    echo " Docker Image Pushed Successfully on DockerHub"
  }
}