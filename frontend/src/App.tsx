import React, { useState } from 'react'
import Student from './pages/Student'
import Tutor from './pages/Tutor'
import Staff from './pages/Staff'

type View = 'student' | 'tutor' | 'staff'

export default function App(){
  const [view, setView] = useState<View>('student')
  return (
    <div style={{fontFamily:'system-ui, sans-serif', padding:16}}>
      <h1>Study Group App (MVP Scaffold)</h1>
      <p>
        Switch role view:
        <button onClick={()=>setView('student')}>Student</button>{' '}
        <button onClick={()=>setView('tutor')}>Tutor</button>{' '}
        <button onClick={()=>setView('staff')}>Staff</button>
      </p>
      {view==='student' && <Student />}
      {view==='tutor' && <Tutor />}
      {view==='staff' && <Staff />}
      <footer style={{marginTop:32, opacity:0.7}}>
        API: {import.meta.env.VITE_API_BASE}
      </footer>
    </div>
  )
}
