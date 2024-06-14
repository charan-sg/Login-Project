angular.module('Login')
.service('loginService', ['$http', function($http){
    this.login = function(logincredentials){
        const login_details = 'http://localhost:5000/api/login';
        return $http.post(login_details, logincredentials)
    }
}])