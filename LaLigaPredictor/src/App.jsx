import { useState } from 'react'
import heroImg from './assets/hero.png'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import './App.css'
import ModelForm from './Components/ModelForm.jsx'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="App">
      <ModelForm />
    </div>
  )
}

export default App
