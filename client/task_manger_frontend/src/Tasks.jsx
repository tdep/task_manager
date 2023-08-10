import { useEffect, useState } from "react"
import { Link } from 'react-router-dom'

const Tasks = () => {
  const [allTasks, setAllTasks] = useState([])

  useEffect(() => {
    const request = async () => {
      let req = await fetch("http://127.0.0.1:3000/tasks")
      let res = await req.json()

      if (req.ok) {
        setAllTasks(res)
      }
    }
    request()
  }, [])
  return (
    <div>
      <h1>Tasks</h1>
      <div>
        {allTasks.map((task, i) => {
          return (
            <>
              <div key={i} style={{border:"1px solid black", display:"flex", flexDirection:"column"}}>
                <h3>{task.title}</h3>
                <p>
                  <span><b>Description:</b> {task.description}</span><br/>
                  <span><b>Due Date:</b> {task.due_date}</span>
                </p>
              </div>
            </>
          )
        })}
      </div>
      <div>
        <button type="button">
          <Link to={"/"}>Home</Link>
        </button>
        <button type="button">
          <Link to={"/users"}>Users</Link>
        </button>
      </div>
    </div>
  )
}

export default Tasks