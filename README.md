##Introduction

This repository contains LiveTemplates for [AngularJS](http://angularjs.org/) and [Jasmine](https://github.com/pivotal/jasmine) to be used in WebStorm (or other JetBrains products).

Check the [blog post](http://pkozlowskios.wordpress.com/2012/07/15/live-templates-for-angular-js-in-webstorm/) for more!

##Installation

AFAIK WebStorm doesn't have any particular installation (or import) procedure for LiveTemplates. 
Instead just drop `*.xml` files from this repository into WebStorm's folder where it stores LiveTemplates.
Usually this is the `[your home directory]/.WebIde40/config/templates`.

##Live Templates
###AngularJS
`ngm` - A new angular module without a config function

```JavaScript
var $moduleName$ = angular.module('$moduleName$',[]);
$END$
```
`ngc` - A global (outside of a module) controller function

```JavaScript
var $controllerName$ = function($scope) {
    $END$
} 
```
`ngf` - A function in angular's controller

```JavaScript
$scope.$functionName$ = function() {
    $END$
}
```
`ngdl` - A directive with a link function only

```JavaScript
.directive('$directiveName$', function($directiveDeps$) {

    return function(scope, element, attrs) {
        $END$
    }
});
```
`sem` - scope, element, attrs inside a linking function

```JavaScript
scope, element, attrs$END$
```
`lf` - A link function

```JavaScript
function (scope, element, attrs$ctrl$) {
$END$    
}
```
`ngdc` - A directive with a compile function

```JavaScript
directive('$directiveName$', function factory($injectables$) {
  var directiveDefinitionObject = {   
    $directiveAttrs$
    compile: function compile(tElement, tAttrs, transclude) {    
      $END$
      return function (scope, element, attrs) {                    
      }
    }
  };
  return directiveDefinitionObject;
})
```
`cf` - A compile function

```JavaScript
function compile(tElement, tAttrs, transclude) {    
      $END$
      return function (scope, element, attrs) {                    
      }
}
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

