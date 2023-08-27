import './App.css';
import axios from "axios";
import TasksContainer from "./Components/TasksContainer";

function App() {

    const data = axios.get('http://localhost:8000/tasks/').then(res =>{

        console.log(res)
    }).catch(error => {
        console.error('Error:', error.message);
    });

  return (
    <div className="App">
      <header className="App-header">
            <TasksContainer />
      </header>
    </div>
  );
}

export default App;
