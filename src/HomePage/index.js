import { useMemo } from "react";
import { GoogleMap, useLoadScript, Marker } from "@react-google-maps/api";
import {useEffect,useState} from "react"

const API_KEY = "AIzaSyCUVdzk_i0PG4VBLwFQFxn8S3xMd-1xu70"
const url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=25.019961231608928,121.45529784290277&radius=1000&keyword=鴨肉飯&language=zh-TW&key=' + API_KEY

const HomePage = () =>{
    const [data,setData] = useState({});
    const [selectedItem, setSelectedItem] = useState([]);

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
    const fetchCoor =  ()=>{
        fetch("https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyCUVdzk_i0PG4VBLwFQFxn8S3xMd-1xu70")
        .then(response => {
            
            if (response.ok)  return response.json();
            throw response;
        })
        .then(json => {
            
            console.log(json)
        })
        
    }
    
    useEffect(()=>{
        
        fetchData()
    },[])
    
    return <div className="container" >
        
    </div>
}
export default HomePage;

