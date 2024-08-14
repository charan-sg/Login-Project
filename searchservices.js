angular.module('SearchStudent')
    .service('SearchStudentService', ['$http', function($http) {
        this.search = function(searchitems) {
            const searchdetails = 'http://localhost:5000/api/search';
            console.log(searchdetails)
            return $http.post(searchdetails, searchitems);
        };
        
    }]);
