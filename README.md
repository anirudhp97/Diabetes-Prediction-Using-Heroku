# Diabetes-Prediction-Using-Heroku

This repository consists of end-to-end Machine Learning project where the model is deployed on Heroku platform. </br>
Heroku is a free, cloud platform, which provides Platform as a Service (PaaS) to the developers, which means a developer can build, run and deploy an application at scale. </br>

Webapp:
![Heroku_Output](https://user-images.githubusercontent.com/30742445/149907084-eadfb085-c7af-40e8-9e4e-c7a74201124d.png)

Steps to deploy Machine Learning model in Heroku (via linking github repository with heroku): </br>
Step 1: Build a Machine Learning and save the model in .pkl format. </br>
Step 2: Create a Web App using Flask. </br>
Step 3: Commit the code in github. </br>
Step 4: Create an account in Heroku. </br>
Step 5: Link the github to Heroku. </br>
Step 6: Deploy the model. </br>

Two important points to keep in mind before deploying the model: </br>
(1) Creation of Procfile: This configuration file lets Heroku understand which is the first file it has to execute. Without this file even though the model can be built and deployed, it throws an 'Application error' while loading the web application in the browser. Thus creating this file is of upmost importance. It is also important to keep in mind that there is no extension to this file. </br>
(2) Creation of Requirements.txt file: This file consists of all the libraries and other dependencies which are used to build the project. Heroku goes through this file and installs all the dependencies while building the application for deployment. It is important to list down all the libraries along with the version which was used to build the model.</br>

Link to the web application: https://diabetes-prediction-heroku.herokuapp.com </br>
Tutorial on how to deploy the model on Heroku: https://www.youtube.com/watch?v=mrExsjcvF4o&list=PLZoTAELRMXVOAvUbePX1lTdxQR8EY35Z1&index=2
