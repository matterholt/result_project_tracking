# results tracker

## Roadmap

0. User
   ->

1. Fea Models
   -> add models
   -> update models with values
   -> do we need to know the Owner??

2. Model stiffness Results
   -> add results associated with model
   -> select model to compare
   -> need to have Target | Base Model | CM models
   -> Store the punch file
   -> Process results and add to database

3. Model Judgement
   -> If model NG,OK or can be improved

## Django Rest API

list a collection of models
create new objects in the database

## TODO's

- [ ] 1.0 Create a route for user to login, User needs to have permissions to access

## Todo 1.0

### Need to figure out

how does react keep track of the login state of user? - sessions ?? - cookies ??

### Requirements:

The User is invited to the the platform, and should not have to register,

- User can request to join the platform
- User is requested to join the platform

### Routes

     Sign in to the platform
     ''
     request to join platform

### Resources

https://wsvincent.com/django-rest-framework-authentication-tutorial/

- [x] Model structure for database
- [x] Test Models for fea results
- [x] Install django djangorestframework django-cors-headers
- [x] Serialization of the model data, converting to python classes to json to allowing web to consume data.(json to class as well)
- [x] Setting up generic API views -> restframework (also class, and function)
- [x] set up the URLs, or another name routes
- [x] Apply to installed apps

https://blog.logrocket.com/creating-an-app-with-react-and-django/
