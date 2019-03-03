app.controller('codeController', function ($scope, $http) {

    'use strict';

    $scope.pageTitle = "Code Controller Page";

    // This method use code information render template
    $http.get('api/code/').then(function success(response) {
        $scope.codeList = [];
        for (var _code = 0; _code < response.data.length; _code++) {
            var addData = {};
            addData.id = response.data[_code].id;
            addData.code = response.data[_code].code;
            addData.created_date = response.data[_code].created_date;
            $scope.codeList.push(addData);
        }
    });

    $scope.addCodeBtn = function () {
        $scope.addTaskBtn = true;
        $scope.updateTaskBtn = false;
    };

    $scope.currentItem = function (code) {

        $scope.id = code;
        $scope.edit = code;

        $scope.addTaskBtn = false;
        $scope.updateTaskBtn = true;
    };

    $scope.addCode = function () {
        $http({
            method: "post",
            url: "api/code/",
            data: {code: $scope.code}
        }).then(function success(response) {
            $scope.codeList.push(response.data);
            console.log("data insert successfully");
            console.log(response.data);
        });
    };


});
