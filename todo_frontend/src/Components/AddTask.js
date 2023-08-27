import React, {useState} from 'react';
import {Button, Form} from "react-bootstrap";
import axios from "axios";

function AddTask({setData}) {
    const [title,setTitle] = useState('')

    const handleAdd = _=>{
        if(title)
            axios.post('http://localhost:8000/tasks/',{title}).then(res => {
                if(res.status===201){
                    setData(res.data)
                    setTitle('');
                }

            })
    }

    return (
        <div style={{width:'calc(100%-20px)',height:"40px",margin: '10px'}} className={'d-flex'}>
            <Form.Control value={title} onChange={e => setTitle(e.target.value)} style={{width:"80%",height:"100%",borderRadius:"10px 0 0",border:' 2px solid #282c34',borderRight: 'none'}} type={'text'} placeholder={'Add a new task'}/>
            <Button onClick={handleAdd} variant={"dark"} style={{width:"20%",height:"100%",borderRadius:"0 10px 0 0"}}>Add</Button>
        </div>
    );
}

export default AddTask;