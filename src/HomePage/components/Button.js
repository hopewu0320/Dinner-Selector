import { type } from "@testing-library/user-event/dist/type"

var jsonData = {
    "dinner": [
        "炒飯",
        "便當",
        "滷肉飯",
        "魯肉飯",
        "鍋燒意麵",
        "肉羹麵",
        "牛肉麵",
        "鴨肉飯",
        "雞肉飯"
    ]
  }

const button = ({ReceivedKeyword}) =>{
    
    const onClick = () => {
        fetch('http://localhost:8000/dinner-option/',{ //記得加上斜線
            method:'GET',
            headers:{
                'Content-type': 'application/json',
            },
            //body:JSON.stringify(jsonData)
        })
        .then(response => response.json())
        .then(data => {
            console.log("回傳data:",data) //從後端處理過回傳的Data
            ReceivedKeyword(data.data)
        })
        .catch(error =>{
            console.error('Error:',error);
        })
        console.log("點擊晚餐button")
    }
    return <div>
        <button onClick={onClick} style={{width:"100px" ,height:"30px"}} >
            選擇晚餐
        </button>
    </div>
}

export default button