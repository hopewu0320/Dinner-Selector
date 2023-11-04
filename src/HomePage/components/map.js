import React, { useRef, useEffect } from 'react';

const MapContainer = () => {
  const googleMapRef = useRef(null);
  let googleMap = null;

  useEffect(() => {
    if (window.google) {
      const initializeMap = () => {
        const mapOptions = {
          zoom: 8,
          center: { lat: -34.397, lng: 150.644 },
        };

        googleMap = new window.google.maps.Map(googleMapRef.current, mapOptions);

        // 创建DirectionsService和DirectionsRenderer实例
        const directionsService = new window.google.maps.DirectionsService();
        const directionsRenderer = new window.google.maps.DirectionsRenderer();
        directionsRenderer.setMap(googleMap);

        calculateAndDisplayRoute(directionsService, directionsRenderer);
      };

      initializeMap();
    } else {
      console.error("Google Maps API is not loaded.");
    }
  }, []);

  // 计算和显示路线
  const calculateAndDisplayRoute = (directionsService, directionsRenderer) => {
    const start = { lat: 25.0196468, lng: 121.4134637 }; // 起点坐标
    const end = { lat: 25.026144, lng: 121.419915 }; // 终点坐标
    directionsService.route(
      {
        origin: start,
        destination: end,
        travelMode: window.google.maps.TravelMode.DRIVING, // 可以更改为WALKING, BICYCLING, 或TRANSIT
      },
      (response, status) => {
        if (status === window.google.maps.DirectionsStatus.OK) {
          // 显示路线
          directionsRenderer.setDirections(response);
        } else {
          window.alert('Directions request failed due to ' + status);
        }
      }
    );
  };

  return <div ref={googleMapRef} style={{ width: '100%', height: '400px' }} />;
};

export default MapContainer;
