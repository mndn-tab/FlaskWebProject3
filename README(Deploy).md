

# Docker
### 1.create .Dockerfile
### 2. to build image
``` docker build -f .Dockerfile -t flaskwebproject3 . ```

check with

``` docker images```
### 3. to run the container 
``` docker run -d --name  flask-container -p 5000:5000 flaskwebproject3 ```

check with

``` docker ps ```

``` docker logs flask-container```

# GitHub Docker Registry
### connect to registery
``` docker login ghcr.io ```

enter username and password (token)

### build image
``` docker build -f .Dockerfile  -t ghcr.io/mndn-tab/flaskwebproject3  . ```

### push it on registry
``` docker push  ghcr.io/mndn-tab/flaskwebproject3  ```

this will publish it on github registry. you can check it here: https://github.com/mndn-tab?tab=packages

# Publish on Render.com

### 1.  new -> web service
### 2. Image URL  -> copy-paste from github registry (docker pull ghcr.io/mndn-tab/flaskwebproject3:latest) -> connect 
### 3. fill in settings (Region, Instance Type, Environment Variables, etc) -> Create Web Service 
### 4. your app is deployed now, and you are given a url (see below pic)
### 5. to delete go to settings (see below pic) -> scroll to the bottom of the page and click "Delete Web Service" 

<img width="1558" height="294" alt="image" src="https://github.com/user-attachments/assets/fd04974f-0a9b-49a3-b856-094de7f3e869" />

# Diff Production vs Local

### 1. separate services connected by diff ports (microservices)
### 2. env variables (secrets)
