angular.module('Login',[])
.controller('loginController',  ['$scope','loginService', function($scope, loginService){
    $scope.userid = '';
    $scope.password = '';

    $scope.Submit = function(){
        var logincredentials = {
            userid : $scope.userid,
            password : $scope.password
        };
        console.log(logincredentials);
    
    loginService.login(logincredentials)
        .then(function(response){
            // console.log(response.data)
        })
    

    }

}
])





