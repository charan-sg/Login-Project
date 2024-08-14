angular.module('SearchStudent', [])
    .controller('searchController', ['$scope', 'SearchStudentService', function($scope, SearchStudentService) {
        $scope.searchelement = '';
        $scope.searchvalue = '';

        $scope.Search = function() {
            const searchitems = {
                searchelement: $scope.searchelement,
                searchvalue: $scope.searchvalue    
            };

            SearchStudentService.search(searchitems)
                .then(function(response) {
                    if (response.data.student === "Details not found") {
                        window.alert("Details Not Found");
                        $scope.searchelement = '';
                        $scope.searchvalue = '';

                    } else {
                        $scope.student = response.data.student;
                    }
                })
                .catch(function(error) {
                    console.error('Search error:', error);
                });
        };
    }]);
