import { useMemo } from "react";
import { GoogleMap, useLoadScript, Marker } from "@react-google-maps/api";
import MapContainer from "./components/map";

import {useEffect,useState,useRef} from "react"


const API_KEY = "AIzaSyCUVdzk_i0PG4VBLwFQFxn8S3xMd-1xu70"
const origin = {lat:25.0196468 , lng : 121.4134637}
const destination = {lat: 25.026144, lng: 121.419915}
const google = window.google;

var location;

const HomePage = () =>{
    const [data,setData] = useState({});
    const [selectedItem, setSelectedItem] = useState([]);
    const [url,setUrl] = useState({});
    const [position,setPosition] = useState({});
    const [start,setStart] = useState({});
    const [end,setEnd] = useState({});
    
    
    
    const fetchData =  ()=>{
        fetch(url)
        .then(response => {
            console.log(response)
            if (response.ok)  return response.json();
            throw response;
        })
        .then(json => {
            setData(json);
            const places = json.results
            console.log(places);
            
        })
        
    }
    const GetUrl = () => {navigator.geolocation.getCurrentPosition(function(position) {
        console.log("Latitude is :", position.coords.latitude);
        console.log("Longitude is :", position.coords.longitude);
        location = position.coords.latitude + ',' + position.coords.longitude
        const url  = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+ location +'&radius=1000&keyword=牛排&language=zh-TW&key=' + API_KEY
        setUrl(url);
        setStart({lat:position.coords.latitude,lng:position.coords.longitude});
    });
    }
   
    useEffect(()=>{ 
        
        fetchData()
        GetUrl()
        
    
    },[location])
    
    return <div className="container" >
        
        <MapContainer start={start} />
        
    </div>
}

export default HomePage;
