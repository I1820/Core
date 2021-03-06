'use strict';

/**
 * @ngdoc directive
 * @name i1820UiApp.directive:i1820DiscoveryPanel
 * @description
 * # i1820DiscoveryPanel
 */
angular.module('i1820UiApp')
  .directive('i1820DiscoveryPanel', function ($location, DiscoveryService) {
    return {
      templateUrl: 'views/templates/discovery-panel.html',
      restrict: 'E',
      scope: {},
      link: function ($scope) {
        $scope.agents = DiscoveryService.query();

        $scope.refresh = function () {
          DiscoveryService.refresh();
          $scope.agents = DiscoveryService.query();
        };

        $scope.toAgent = function (agentId) {
          $location.path('/agent/' + agentId);
        };

        $scope.$watch(function () {
          return DiscoveryService.query();
        }, function (agents) {
          $scope.agents = agents;
        });
      }
    };
  });
