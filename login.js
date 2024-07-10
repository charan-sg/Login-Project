angular.module('Login',[])
.controller('loginController',  ['$scope','$window', 'loginService',function($scope, $window,  loginService){
    
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
            msg = response.data
            if(msg["Login Successful"]){
                alert("Login Succesfull")
                $window.location.href = 'homepage.html'
            }
            else{
                $scope.loginmsg = "Invalid USER ID or PASSWORD";
                $scope.userid = '';
                $scope.password = '';   
            }
        })
    }

    $scope.Cancel = function(){
        console.log("Cancelled")
    }

}
])





