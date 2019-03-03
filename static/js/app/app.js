var app = angular.module('HomeworkApp', [
    'ngRoute',
]);

app.config(function ($routeProvider, $httpProvider) {
    'use strict';
    // csrf token
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

    $routeProvider
        .when('/', {
            url: '/',
            templateUrl: 'static/client/templates/code/code.html',
            controller: 'codeController',
            authenticate: true
        })
        .otherwise({
            template: "<h1>Page not found</h1>"
        });
});
