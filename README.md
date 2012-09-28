##Introduction

This repository contains LiveTemplates for [AngularJS](http://angularjs.org/) and [Jasmine](https://github.com/pivotal/jasmine) to be used with [JetBrains](http://www.jetbrains.com/) products such as [IntelliJ](http://www.jetbrains.com/idea/) or [WebStorm](http://www.jetbrains.com/webstorm/). Live Templates are a set of abbreviations that expand in to 'code snippets' for common tasks such as creating variables and functions. These abbreviations significantly speed up development and reduce coding errors.

These Live Templates are incomplete, but compatible with Angular JS version 1.0.1.

Check out the [blog post](http://pkozlowskios.wordpress.com/2012/07/15/live-templates-for-angular-js-in-webstorm/) for more!

##Installation

### IntelliJ
Copy the Live Template xml files into your user's IntelliJ folder. This is typically in `[home directory]/.IntelliJIdea<version>/config/templates`. If IntelliJ is currently open, you will need to restart the IDE.

Note: The default Live Template expansion character is TAB. To use a Live Template abbreviation, type the abbreviation and press the expansion character. The Live Template definitions can be found in the Settings Menu (CTRL+ALT+S), IDE Settings, Live Templates, angular.js.

### WebStorm
AFAIK WebStorm doesn't have any particular installation (or import) procedure for LiveTemplates. 
Instead just drop `*.xml` files from this repository into WebStorm's folder where it stores LiveTemplates.
Usually this is the `[your home directory]/.WebIde40/config/templates`.

##How to use the Live Templates
The Live Templates abbreviations have been organized into two lists: frequently used (such as defining scoped variables) and infrequently used (such as defining filters).

###AngularJS

####Frequently Used
Frequently used abbreviations are those that are commonly used after the structure of the Angular JS application has been created (modules, services, factories, etc). These are your day-to-day shortcuts.

The following show the available abbrivations and their default implementations. $CURSOR-POINT$ indicates where the cursor will be placed upon template completion.

`ngc` - Define a new Angular Controller. You can change the controller name and parameters.
```JavaScript
function MyController($scope) {
    $CURSOR-POINT$
};
```

`ngf` - Define a new $scope'd function inside an Angular Controller. You can change the function name and parameters. This includes a simple JavaDoc header.
```JavaScript
/**
 * TODO: Document scoped function myFunction
 */
$scope.myFunction = function() {
    $CURSOR-POINT$
};
```

`ngv` - Define a new $scope'd variable inside an Angular Controller. You can change the variable name and an enumeration window will appear for the value. You can choose: null, {}, [], and "".
```JavaScript
$scope.myVariable = {};
```

`ngw` - Define a $watch for a variable inside an Angular Controller. You can change the variable to be watched.
```JavaScript
$scope.$watch('myVariable', function(newValue, oldValue, scope) {
    if (oldValue != null && newValue != null) {
       $CURSOR-POINT$
    }
});
```

`ngon` - Define a $on for a $broadcast/$emit on the $scope inside an Angular Controller. You can change the event to watch.
```JavaScript
$scope.$on("myEvent", function(event, args) {
    $CURSOR-POINT$
});
```

`nge` - Define an $emit for a $scope inside an Angular Controller / Angular Controller Function. You can change the event name and optional event arguments
```JavaScript
$scope.$emit("eventName", eventArgs);$CURSOR-POINT$
```

`ngb` - Define a $broadcast for a $scope inside an Angular Controller / Angular Controller Function. You can change the event name and optional event arguments
```JavaScript
$scope.$broadcast("eventName", eventArgs);
```

####Infrequently Used
Infrequently used abbreviations are those that are used to create the structure of the Angular JS application. These define modules, services and other declarations to setup and create your application. These abbreviations are full words.

`module` - Define an Angular module without a config function. You can change the module name and set optional dependencies.
```JavaScript
/**
 * TODO: Document module myModule
 */
angular.module('myModule', [dependencies]);$CURSOR-POINT$
```

`factory` - Define an Angular Module Factory to be attached to a previously defined module. You can change the factory name and factory injectables.
```JavaScript
.factory('myService', function($rootScope, $http, $location) {
    var myService = {
        $CURSOR-POINT$
    };
    return myService;
})
```

`service` - Define an Angular Module Service to be attached to a previously defined module. You can change the service name and service injectables.
```JavaScript
.service('myService', function($rootScope, $http, $location) {
    this.myServiceFunction = function() {
        return null;$CURSOR-POINT$
    };
})
```

`filter` - Define an Angular Module Filter to be attached to a previously defined module. You can change the filter name.
```JavaScript
.filter('myFilter', function() {
    return function(input, value) {
        return null$CURSOR-POINT$;
    };
})
```

`router` - Define a skeleton definition of an Angular Router. You can change the following:
* Application variable 
* First route URL
* First route template url (a partial)
* First route controller
* Default route URL (the otherwise)
* HTML5 Mode (true or false)
* Route prefix. Default is #

```JavaScript
/**
 * Define Application routing table
 */
myApplication.config(['$routeProvider', '$locationProvider', function($routeProvider) {

    $routeProvider
        .when('/myUrl', {
            templateUrl: '/partial/partial.html', 
            controller: myController
        })
        .otherwise({redirectTo: '/home'})
    ;
    
    // Set HTML5 Mode - http://docs.angularjs.org/api/ng.$locationProvider
    $locationProvider.html5Mode(true);
    
    // Prefix all route provider when cases with the following
    $locationProvider.hashPrefix("#");
}]);
```

`when` - Define a when condition of an Angular Router. You can change the following:
* Route URL
* Route template partial URL
* Route controller

```JavaScript
.when('/myUrl', {
	templateUrl: '/partials/myPartial.html', 
	controller: myController
})
```

###Jasmine
`jasd` - Jasmine describe template

```JavaScript
describe('$describe$', function() {

    $END$
})
```
`jasi` - Jasmine it template

```JavaScript
it('$should$', function($dependencies$) {
    $END$
});
```

##Credits
* [Pawel Kozlowski](https://github.com/pkozlowski-opensource) for initial creation of the Angular JS Live Template
* [Jaymes Bearden](https://github.com/jaymes-bearden) expansion, testing and documentation

##TODO
* Add Live Template directive abbreviations back