import React, {useEffect, useState} from 'react';
import AddTask from "./AddTask";
import TaskItem from "./TaskItem";
import {
    useQuery,
} from '@tanstack/react-query'
import axios from "axios";
import {Spinner} from "react-bootstrap";

const TasksContainer = () => {

    const { isLoading, isError, data,isFetched } = useQuery({
        queryKey: ['repoData'],
        queryFn: () =>
            axios.get('http://localhost:8000/tasks/').then(
                (res) => res.data
            ),
    })
    const [Data,setData] = useState([])

    useEffect(_=>{
        if(isFetched && ! isError)
            setData(data)
    },[data])

    return (
        <div style={{width:"30%" ,margin:"auto",marginTop:"30vh",backgroundColor:"#EEE",height:"400px",maxheight:"400px",borderRadius:'15px',overflowY:"hidden"}}>
            <AddTask />

            <div className={'d-flex justify-content-start align-items-center flex-column gap-2'} style={{maxHeight:'320px',overflowY:"auto"}}>

                {
                    isLoading ? <Spinner variant={'primary'} animation={"border"} className={'mt-4'}/>
                        : Data.map(item => <TaskItem key={item.id} item={item}/>)
                }
            </div>
        </div>
    );
};

export default TasksContainer;