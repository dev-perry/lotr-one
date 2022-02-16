Author:
 Perry Asibey-Bonsu

## Description
The aim of this project was to assemble an SDK that gave developers access to the Lord of the Rings API available at https://the-one-api.dev/

## Context
Before undertaking the project it was important to understand how the API was structured, its routes, and the kind of data it returned. Some preliminary testing was done with Postman to understand the data and how the API handled URL parameters.

## Targets
The SDK needed to be able to communicate with the API successfully and output the response data. This data should be assignable to a variable to allow for easy manipulation by the end-user. Using the SDK should be straightforward and simple.

## Design Thinking
The user should be able to create a single client object that gives them access to the necessary functions they need to interact with the API. Since there is a route available on the API that doesn't require credentials, users should be able to use the SDK without an API key. Any function that requires an API key should be decorated with a function that ensures a credential has been provided to the instance.

## Alternatives Considered
Initially a strategy where each API route had its own data model was pursued. However, this strategy produced a lot of redundant code. More "work" was given to the requester functions to dynamically configure each API call based on the pattern presented in the API documentation.

## Next Steps
This SDK would be more functional if it included support for options such as pagination, filtering, and sorting. Additionally, the error responses from the API due to invalid parameters or throttling need to be listened for and presented to the user in such a way that they understand what is going on.