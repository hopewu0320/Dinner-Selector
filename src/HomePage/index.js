import { useMemo } from "react";
import { GoogleMap, useLoadScript, Marker } from "@react-google-maps/api";
import MapContainer from "./components/map";
import Button from "./components/Button";
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
    const [keyword,setKeyword] = useState(null);
    
    
    const fetchData =  ()=>{
        //console.log("FetchData url:",url)
        fetch(url)
        .then(response => {
            //console.log(response)
            if (response.ok)  return response.json();
            throw response;
        })
        .then(json => {
            setData(json);
            const places = json.results
            console.log(places);
            var idx = choose_shop(places.length)
            //不能寫places[5]
            if (places && places.length > idx) {
                console.log("End:",places[idx].geometry.location);
                setEnd(places[idx].geometry.location)
            }
            // places.forEach((place,i) => {
            //     // 每個 'place' 對象應該有一個 'geometry' 屬性
            //     const geometry = place.geometry.location;
            //     // 現在你可以使用這些經緯度值
            //     console.log(geometry,i);
            // });
            // var idx = choose_shop(places.length)
            // setEnd(places[idx].geometry.location)
        })
    }
    const choose_shop = (len) =>{
        var idx = Math.floor((Math.random()*len)+1)
        return idx;
    }
    const GetUrl = () => {navigator.geolocation.getCurrentPosition(function(position) {
        //console.log("Latitude is :", position.coords.latitude);
        //console.log("Longitude is :", position.coords.longitude);
        location = position.coords.latitude + ',' + position.coords.longitude
        const url  = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+ location +'&radius=5000&keyword='+keyword+'&language=zh-TW&key=' + API_KEY
        setUrl(url);
        //console.log(url)
        console.log("Start",{lat:position.coords.latitude,lng:position.coords.longitude})
        setStart({lat:position.coords.latitude,lng:position.coords.longitude}); //現在住家的位置
        
    });
    }
    
    const GetKeyword = (data) => {
        setKeyword(data)
        console.log("Selected dinner:",data)
    }
    
    //Fix FetchData和GetUrl的url不同步的問題
    //因為keyword改變 所以url改變，url改變 所以所搜尋的店家改變
    useEffect(()=>{ 
        GetUrl()
    },[location,keyword])
    useEffect(()=>{ 
        fetchData()
    },[location,url])
    
    return <div className="container" >
        
        <MapContainer start={start}  end={end} />
        <Button ReceivedKeyword = {GetKeyword}/>
    </div>
}

export default HomePage;
