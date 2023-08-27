import './App.css';
import TasksContainer from "./Components/TasksContainer";
import {
    QueryClient,
    QueryClientProvider,
} from '@tanstack/react-query'

const queryClient = new QueryClient()

function App() {
    return (
    <QueryClientProvider client={queryClient}>
        <div className="App">
            <header className="App-header">
                <TasksContainer />
            </header>
        </div>
    </QueryClientProvider>



  );
}

export default App;
