angular.module('StudentRegister')
.service('StudentService', ['$http', function($http) {
    this.submitForm = function(formData) {
        const registerdetails = 'http://localhost:5000/api/submitForm';
        return $http.post(registerdetails, formData);
    };
}]);