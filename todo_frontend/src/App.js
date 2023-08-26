import './App.css';
import axios from "axios";

function App() {

    const data = axios.get('http://localhost:8000/list/').then(res =>{

        console.log(res)
    }).catch(error => {
        console.error('Error:', error.message);
    });

  return (
    <div className="App">
      <header className="App-header">

      </header>
    </div>
  );
}

export default App;
