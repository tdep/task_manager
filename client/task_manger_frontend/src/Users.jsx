import { useState, useEffect } from "react"
import { Link } from 'react-router-dom'
const Users = () => {
  const [allUsers, setAllUsers] = useState([])

  useEffect(() => {
    const request = async () => {
      let req = await fetch('http://127.0.0.1:3000/users')
      let res = await req.json()
      if (req.ok) {
        setAllUsers(res)
      }
    }
    request()
  }, [])

  return (
    <>
      <h1>Users</h1>
      <div>
        {allUsers.map((user, i) => {
          return (
            <div key={i}>
              <p>{user.username}</p>
              <p>{user.email}</p>
              <p>{user.id}</p>
            </div>
          )
        })}
      </div>
      <div>
        <button type="button">
          <Link to={'/'}>Home</Link>
        </button>
        <button type="button">
          <Link to={'/tasks'}>Tasks</Link>
        </button>
      </div>
    </>
  )
}

export default Users