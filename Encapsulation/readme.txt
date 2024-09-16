Use encapsulation to hide certain attributes that shouldn't be able to be set directly. Instead, define 
getters and setters as properties and interact with those. This also gives us the ability to validate 
inputs to ensure we don't set an invalid attribute value under the hood (such as radius = -5).