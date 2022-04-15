
This Dockerfile is for a development web server. It includes Apache2 core and active CGI.

In it we adopted a base Ubuntu image in version 16.04 because we do not need to set a region and a timezone for Apache2.

===========================================================================

Docker infos:

To run our Dockerfile, just run the command:
docker build -t REPOSITORY_NAME .

After build the image, you can run the command to create our container:
docker run -dit --name CONTAINER_NAME -p LOCAL_PORT:CONTAINER_PORT REPOSITORY_NAME

Now you have your container running! That's were easy!

If you open your browser and type localhost:LOCAL_PORT, you will see your Apache2 server page.

If you want enter the container, you can run the command:
docker exec -it CONTAINER_NAME bash

===========================================================================

CGI infos:

Address:
-localhost:LOCAL_PORT/cgi-bin/FILE_NAME.cgi

CGI Files Directory:
-/usr/lib/cgi-bin/ 

** For a CGI to be recognized we need to give execution permission to the file we create, for example the file example.cgi that is in the directory /usr/lib/cgi-bin/ or if you want you can see it in the repository where the Dockerfile is. **

** PERMISSION INFOS https://www.vivaolinux.com.br/dica/Entendendo-as-permissoes-de-arquivos-no-Linux **

===========================================================================

Apache2 infos:

Apache2 Configuration Directory:
-/etc/apache2/

Apache2 Files Directory:
-/var/www/html/

===========================================================================

Any questions or suggestions, contact me at:

EMAIL: victorhugo290498@gmail.com
LINKEDIN: https://www.linkedin.com/in/victor-hugo-4b67591b0/



