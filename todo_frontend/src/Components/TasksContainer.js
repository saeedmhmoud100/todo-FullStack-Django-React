import React, {useEffect, useState} from 'react';
import AddTask from "./AddTask";
import TaskItem from "./TaskItem";
import axios from "axios";

const TasksContainer = () => {
    const [Data,setData] = useState([])

    useEffect(_=>{
        axios.get('http://localhost:8000/tasks/').then(
            (res) => {
                // console.log(res)
                setData(res.data)
            }
        )
    },[])

    return (
        <div style={{width:"30%" ,margin:"auto",marginTop:"30vh",backgroundColor:"#EEE",height:"400px",maxheight:"400px",borderRadius:'15px',overflowY:"hidden"}}>
            <AddTask setData={setData}/>

            <div className={'d-flex justify-content-start align-items-center flex-column gap-2'} style={{maxHeight:'320px',overflowY:"auto"}}>

                {
                        Data && Data.length>0 ? Data.map(item => <TaskItem key={item.id} item={item}/>)
                        :<h6 style={{color:"black"}} className={' mt-3'}>there are no tasks yet</h6>
                }
            </div>
        </div>
    );
};

export default TasksContainer;