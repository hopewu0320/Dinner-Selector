import React, { useRef, useEffect } from 'react';

const MapContainer = () => {
  const googleMapRef = useRef(null);
  let googleMap = null;

  // 初始化地图
  useEffect(() => {
    if (window.google) {
      const initializeMap = () => {
        const mapOptions = {
          zoom: 8,
          center: { lat: 25.0196468, lng: 121.4134637 }, // 示例中心点，根据需要替换
        };
        googleMap = new window.google.maps.Map(googleMapRef.current, mapOptions);
      };

      initializeMap();
    } else {
      console.error("Google Maps API is not loaded.");
    }
  }, []);

  return <div ref={googleMapRef} style={{ width: '400px', height: '300px' }} />;
};

export default MapContainer;