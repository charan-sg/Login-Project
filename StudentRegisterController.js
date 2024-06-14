angular.module('StudentRegister', [])
.controller('registerController', ['$scope', 'StudentService',  function($scope, StudentService) {
    $scope.firstname = '';
    $scope.middlename = '';  
    $scope.lastname = '';
    $scope.emailid = '';
    $scope.phonenumber = '';
    $scope.dob = '';
    $scope.branch = '';
    $scope.admision_date = '';
    $scope.bloodgroup = '';
    $scope.city = '';
    $scope.state = '';
    $scope.addr1 = '';
    $scope.addr2 = '';
    $scope.zipcode = '';
    $scope.gender = '';

    $scope.submitForm = function() {
        const formData = {
            firstname: $scope.firstname,
            middlename: $scope.middlename,
            lastname: $scope.lastname,
            emailid: $scope.emailid,
            phonenumber: $scope.phonenumber,
            dob: $scope.dob,
            branch: $scope.branch,
            admision_date: $scope.admision_date,
            bloodgroup: $scope.bloodgroup,
            city: $scope.city,
            state: $scope.state,
            addr1: $scope.addr1,
            addr2: $scope.addr2,
            zipcode: $scope.zipcode,
            gender: $scope.gender
        };
        console.log("Form Submitted Successfully");
        console.log("Form Data:", formData);
    
    StudentService.submitForm(formData)
        .then(function(response) {
            console.log("Data successfully sent to the server:", response.data);
        })
        .catch(function(error) {
            console.error("Error sending data to the server:", error);
        });
    };
    function cancel(){
        console.log("Cancelled")
    }
}]);
