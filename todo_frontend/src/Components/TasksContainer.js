import React from 'react';
import AddTask from "./AddTask";
import TaksItem from "./TaksItem";

const TasksContainer = () => {
    return (
        <div style={{width:"30%" ,margin:"auto",marginTop:"30vh",backgroundColor:"#EEE",height:"400px",maxheight:"400px",borderRadius:'15px',overflowY:"hidden"}}>
            <AddTask />

                <div className={'d-flex justify-content-start align-items-center flex-column gap-2'} style={{maxHeight:'320px',overflowY:"auto"}}>

                    <TaksItem/>
                    <TaksItem/>
                    <TaksItem/>
                    <TaksItem/>
                    <TaksItem/>
                    <TaksItem/>
                    <TaksItem/>
                    <TaksItem/>
                    <TaksItem/>
                    <TaksItem/>
                    <TaksItem/>
                    <TaksItem/>
                    <TaksItem/>

            </div>
        </div>
    );
};

export default TasksContainer;