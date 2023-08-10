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
              <div key={i}>
                <p>{task.title}</p>
                <p>{task.description}</p>
                <p>{task.user_id}</p>
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