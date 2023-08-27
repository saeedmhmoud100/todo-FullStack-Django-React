import React, {useState} from 'react';
import deleteIcon from "../delete.png"
import axios from "axios";

const TaskItem = ({item}) => {
    const [itemData,setItemData] = useState(item)
    const handleChange = e =>{
        axios.put(`http://localhost:8000/tasks/${itemData.id}`,{...itemData ,'isDone':e.target.checked}).then(res => setItemData(res.data))
    }

    const handleDelete = e =>{
        axios.delete(`http://localhost:8000/tasks/${itemData.id}`).then(res => {
            setItemData(res.data)
            // console.log(res)
        })
    }

    return (
        <>
            {
                itemData && itemData.id ?
                    <div style={{width:'calc(100% - 20px',backgroundColor:"white",borderRadius:"5px",height:"45px",flexShrink:"0"}} className={'d-flex justify-content-between px-2 align-items-center'}>
                        <div>
                            <input type={'checkbox'} id={itemData.id} checked={itemData.isDone} onChange={handleChange}/>
                            <label style={{color:"black",fontSize:"75%",textDecoration:`${itemData.isDone ? 'line-through' : 'none'}`}} className={'px-2 py-0 my-0'} htmlFor={itemData.id}>{itemData.title}</label>
                        </div>
                        <img style={{cursor:"pointer"}} width={'20px'} src={deleteIcon} onClick={handleDelete}/>
                    </div>
                :null
            }
        </>
    );
};

export default TaskItem;