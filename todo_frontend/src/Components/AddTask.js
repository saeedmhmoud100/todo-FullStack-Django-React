import React from 'react';
import {Button, Form} from "react-bootstrap";

function AddTask() {
    return (
        <div style={{width:'calc(100%-20px)',height:"40px",margin: '10px'}} className={'d-flex'}>
            <Form.Control style={{width:"80%",height:"100%",borderRadius:"10px 0 0",border:' 2px solid #282c34',borderRight: 'none'}} type={'text'} placeholder={'Add a new task'}/>
            <Button variant={"dark"} style={{width:"20%",height:"100%",borderRadius:"0 10px 0 0"}}>Add</Button>
        </div>
    );
}

export default AddTask;