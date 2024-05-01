import logo from './logo.svg';
import './App.css';

function App() {
    const handleSubmit = (event) => {
      event.preventDefault();
    }


  return (
    <div className="App">
      <form onSubmit={handleSubmit}>  
      <label htmlFor="description">Description:</label>
        <input type="text" id="description" name="description" />

        <label htmlFor="interval">Interval:</label>
        <select id="interval" name="interval">
           <option value="daily">Daily</option>
           {/* ...other options ...*/}
        </select>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}


export default App;
