import { Link } from 'react-router-dom'

const Home = () => {
  return (
    <>
      <h1>Home</h1>
      <div>
        <button type="button">
          <Link to={'/users'}>Users</Link>
        </button>
        <button type="button">
          <Link to={'/tasks'}>Tasks</Link>
        </button>
      </div>
    </>
  )
}

export default Home