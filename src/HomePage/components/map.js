import React, { useRef, useEffect,useState } from 'react';

const MapContainer = ({start}) => {
  const googleMapRef = useRef(null);
  const [distance, setDistance] = useState('');
  const [duration, setDuration] = useState('');
  let googleMap = null;
  
  // 计算和显示路线
  const calculateAndDisplayRoute = (directionsService, directionsRenderer) => {
    //const start = { lat: 25.0196468, lng: 121.4134637 }; // 起点坐标
    const end = { lat: 25.026144, lng: 121.419915 }; // 终点坐标

    directionsService.route(
      {
        //傳入request
        origin: {lat:start.lat,lng:start.lng},
        destination: end,
        travelMode: window.google.maps.TravelMode.DRIVING, // 可以更改为WALKING, BICYCLING, 或TRANSIT

      },
      (response, status) => {
        //回應response
        if (status === window.google.maps.DirectionsStatus.OK) {
          // 显示路线
          directionsRenderer.setDirections(response);
          
          console.log(response)
        } else {
          window.alert('Directions request failed due to ' + status);
        }
      }
    );
  };

  const Show_Distance = ()=>{
    const end = { lat: 25.026144, lng: 121.419915 }; // 终点坐标
    const distanceMatrixService = new window.google.maps.DistanceMatrixService();
        distanceMatrixService.getDistanceMatrix({
          origins: [start],
          destinations: [end],
          travelMode: window.google.maps.TravelMode.DRIVING,
        }, (response, status) => {
          if (status === window.google.maps.DistanceMatrixStatus.OK) {
            const origins = response.originAddresses;
            const destinations = response.destinationAddresses;
            

            for (let i = 0; i < origins.length; i++) {
              const results = response.rows[i].elements;
              for (let j = 0; j < results.length; j++) {
                const element = results[j];
                if (element.status === "OK") {
                  setDistance(element.distance.text);
                  setDuration(element.duration.text);
                  // Display the distance and duration on the map
                  const infoWindow = new window.google.maps.InfoWindow({
                    content: `Distance: ${element.distance.text} - Duration: ${element.duration.text}`,
                    position: end, // You can choose where to anchor this infoWindow
                  });
                  infoWindow.open(googleMap);
                }
              }
            }
          } else {
            console.error(`Error fetching distance matrix: ${status}`);
          }
        });
  }

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
        const distanceMatrixService = new window.google.maps.DistanceMatrixService();
        directionsRenderer.setMap(googleMap);

        calculateAndDisplayRoute(directionsService, directionsRenderer);
        Show_Distance()
      };

      initializeMap();
    } else {
      console.error("Google Maps API is not loaded.");
    }
  }, [start]);



  return <div ref={googleMapRef} style={{ width: '100%', height: '400px' }} />;
};

export default MapContainer;
