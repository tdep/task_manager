import './App.css'
import Home from './Home'
import Users from './Users'
import Tasks from './Tasks'
import { BrowserRouter, Routes, Route } from "react-router-dom"

function App() {

  return (
    <div className = "App">
      <BrowserRouter>
        <Routes>
          <Route path={'/'} element={<Home />}/>
          <Route path={'users'} element={<Users />}/>
          <Route path={'tasks'} element={<Tasks />} />
        </Routes>
      </BrowserRouter>
    </div>
  )
}

export default App
