import React from 'react';
import deleteIcon from "../delete.png"

const TaskItem = () => {
    return (
        <div style={{width:'calc(100% - 20px',backgroundColor:"white",borderRadius:"5px",height:"45px",flexShrink:"0"}} className={'d-flex justify-content-between px-2 align-items-center'}>
            <div>
                <input type={'checkbox'} style={{    marginTop: "1px"}}/>
                <label style={{color:"black"}} className={'px-2 py-0 my-0'}>text for a test</label>
            </div>
            <img style={{cursor:"pointer"}} width={'20px'} src={deleteIcon} />
        </div>
    );
};

export default TaskItem;